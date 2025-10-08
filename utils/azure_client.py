
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential

def get_chat_client():
    return AzureOpenAIChatClient(credential=AzureCliCredential())
