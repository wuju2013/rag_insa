import argparse
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
#from langchain_community.llms.ollama import Ollama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
#from langchain_openai import ChatOpenAI
from ollama import Client

from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.

{context}

---

Answer the question based on the above context: {question}
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)


def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=3)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    #model = Ollama(model="mistral")
    # model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=OPENAI_API_KEY)
    # response_text = model.invoke(prompt)

    client = Client(host='http://10.167.35.241:18083')
    #localClient = Client(host='http://localhost:11434')


    response_text = client.chat(model='EEVE-Korean-10.8B:latest', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    # response_text = localClient.chat(model='mistral:latest', messages=[
    #     {
    #         'role': 'user',
    #         'content': prompt,
    #     },
    # ])

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text
    
    formatted_prompt = f"Prompt: {prompt}\nSources: {sources}"
    #print(formatted_prompt)
    #return formatted_prompt


if __name__ == "__main__":
    main()
