
def create_french_agent(chat_client):
    return chat_client.create_agent(
        instructions="Translate the input text from English to French."
    )
