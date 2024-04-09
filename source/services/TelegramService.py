from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler

from services.OpenAIService import OpenAIService


    

class TelegramService:
    def __init__(self, api_key: str, openAiService: OpenAIService):
        self._api_key = api_key
        self._application = None
        self._job_queue = None
        self._openAiService = openAiService
        
    async def _common_message_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        message = update.message.text
        
        response = self._openAiService.get_response(user_id, message)
        
        await context.bot.send_message(chat_id=user_id, text=response)
        
    def initialize(self):
        self._application = ApplicationBuilder().token(self._api_key).build()
        self._application.add_handler(MessageHandler(None, self._common_message_handler))
        self._job_queue = self._application.job_queue
        
    async def _send_message_handler(self, context: ContextTypes.DEFAULT_TYPE):
        chat_id = context.job.chat_id
        message = context.job.data
        
        await context.bot.send_message(chat_id=chat_id, text=message)
        
    def send_message(self, user_id: str, message: str):
        self._job_queue.run_once(self._send_message_handler, 5, data=message, chat_id=user_id)
        
    def run(self):
        self._application.run_polling()