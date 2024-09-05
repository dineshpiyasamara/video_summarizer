import getpass
import os
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.documents import Document
from transformers import pipeline
import openai

load_dotenv()

def get_summary(docs):
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    openai.api_key = os.getenv('OPENAI_API_KEY')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a text summarizer. summary needs to content multiple short sentences"},
            {"role": "user", "content": docs}
        ],
        max_tokens=100,
        n=1,
        temperature=0
    )

    # docs = [Document(docs)]

    # llm = ChatOpenAI(
    # model="gpt-3.5-turbo",
    # temperature=0
    # )
    # prompt = ChatPromptTemplate.from_messages(
    #     [("system", "Write a concise summary of the following:\\n\\n{context}")]
    # )
    # chain = create_stuff_documents_chain(llm, prompt)
    # result = chain.invoke({"context": docs})

    # summarizer = pipeline("summarization", "google/pegasus-xsum")
    # tokenizer_kwargs = {'truncation':True,'max_length':512}
    # result = summarizer(docs, min_length=30, do_sample=False,**tokenizer_kwargs)

    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": "Write a concise summary of the following:\\n\\n{docs}"}],
    #     max_tokens=100,
    #     n=1,
    #     temperature=0
    # )

    # print(response)

    # result = ""
    # for choice in response.choices:
    #     result = result + " " + choice.message.content

    result = response.choices[0].message['content']

    return result