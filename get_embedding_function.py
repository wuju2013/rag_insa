#from langchain_community.embeddings.ollama import OllamaEmbeddings
#from langchain_community.embeddings.bedrock import BedrockEmbeddings
from ollama import Client

client = Client(host='http://10.167.35.241:18083')
#localClient = Client(host='http://localhost:11434')

def get_embedding_function():
    # embeddings = BedrockEmbeddings(
    #     credentials_profile_name="default", region_name="us-east-1"
    # )
    #embeddings = OllamaEmbeddings(model="nomic-embed-text")
    embeddings = client.embeddings(model="EEVE-Korean-10.8B:latest")
    #embeddings = localClient.embeddings(model="nomic-embed-text")
    return embeddings
