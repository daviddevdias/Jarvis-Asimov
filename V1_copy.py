import os 
from config import api_key

from langchain_core.prompts import ChatGroq




os.environ("GROQ_API_KET") = api_key

chat = ChatGroq(model="llama-3.3-70b-versatile")


nome = input('Seu nome é ')


print(f"Olá {nome}! Digite 'sair' para encerrar.")


historico = []

historico


