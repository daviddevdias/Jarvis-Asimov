from langchain_core.prompts import ChatPromptTemplate

templete = ChatPromptTemplate.from_messages(
    [('user', 'Traduzir {expressao} para a {lingua}')]
)

print(templete)