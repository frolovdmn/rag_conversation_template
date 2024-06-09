from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

model = Ollama(model = 'qwen2')
embeddings = HuggingFaceEmbeddings()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            'system',
            'description'
        ),
        MessagesPlaceholder('chat_history'),
        (
            'human', 
            '{text}'
        )
    ]
)

chain = prompt | model