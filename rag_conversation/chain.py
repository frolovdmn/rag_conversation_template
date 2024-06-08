from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings

model = Ollama(model = 'qwen2')
embeddings = HuggingFaceEmbeddings()

