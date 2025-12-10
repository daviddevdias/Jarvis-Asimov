import os 

from langchain_core.prompts import ChatGroq


api_key = "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"

os.environ("GROQ_API_KET") = api_key

chat = ChatGroq(model="llama-3.3-70b-versatile")


nome = input('Seu nome é ')


print(f"Olá {nome}! Digite 'sair' para encerrar.")


historico = []

historico


