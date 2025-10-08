
def create_spanish_agent(chat_client):
    return chat_client.create_agent(
        instructions="Translate the input text from French to Spanish."
    )
