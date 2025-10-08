
import asyncio
from utils.azure_client import get_chat_client
from agents.french_agent import create_french_agent
from agents.spanish_agent import create_spanish_agent
from agents.english_agent import create_english_agent
from workflow.translation_workflow import build_translation_workflow

async def main():
    chat_client = get_chat_client()
    french = create_french_agent(chat_client)
    spanish = create_spanish_agent(chat_client)
    english = create_english_agent(chat_client)

    workflow = build_translation_workflow(french, spanish, english)

    async for event in workflow.run("Translate: Hello, how are you?"):
        print(event)

if __name__ == "__main__":
    asyncio.run(main())
