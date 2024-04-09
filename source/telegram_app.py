import os
from services.OpenAIService import OpenAIService
from services.TelegramService import TelegramService


def main():
    openAi_api_key = os.getenv("OPENAI_API_KEY")
    telegram_api_key = os.getenv("TELEGRAM_API_KEY")
    
    openAiService = OpenAIService(api_key=openAi_api_key)
    telegramService = TelegramService(api_key=telegram_api_key, openAiService=openAiService)
    
    telegramService.initialize()
    
    telegramService.run()
    
if __name__ == "__main__":
    main()