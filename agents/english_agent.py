
def create_english_agent(chat_client):
    return chat_client.create_agent(
        instructions="Translate the input text from Spanish to English."
    )
