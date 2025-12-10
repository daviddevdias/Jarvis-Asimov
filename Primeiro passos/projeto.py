from langchain_core.prompts import ChatPromptTemplate


Templete = ChatPromptTemplate.from_messages(
    [("user", "Traduza {expressao} para a lingua {lingua}")]
)

print(Templete)

Templete.invoke({"expressao": "Beleza?", "lingua": "inglês"})
