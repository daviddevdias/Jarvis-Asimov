


def resposta_do_bot(mensagens):
    return 'resposta_do_bot'

mensagens = []

while True:
    pergunta = input('Digite a pergunta para o bot ou digite X para sair: ')
    
    if pergunta.lower() == 'x':
        break
    
    mensagens.append({'role': 'user', 'content': pergunta})

    resposta = resposta_do_bot(mensagens)

    mensagens.append({'role': 'assistant', 'content': resposta})

    print(f'Bot: {resposta}')
