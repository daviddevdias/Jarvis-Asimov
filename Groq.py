import os
import sys
import speech_recognition as sr
from gtts import gTTS
import pygame
from langchain_groq import ChatGroq 
from elevenlabs import ElevenLabs





# ===============================
# CONFIG INICIAL
# ===============================

api_key = "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"
os.environ["GROQ_API_KEY"] = api_key

client = ElevenLabs(api_key="fccce4e1cb194268dfa6ddacfdfcebd94b49c54860330c9317bca985cacedc66")
AGENT_ID="5301kb3x3eszeeztar588y9t5hq5"

chat = ChatGroq(model="llama-3.1-8b-instant")

os.makedirs("audios", exist_ok=True)

nome = input("Qual é seu nome? ").strip().title()
print(f"Bem-vindo senhor Verificado >>> {nome} <<<")

recognizer = sr.Recognizer()  


# ===============================
# FUNÇÃO PARA GERAR ÁUDIO
# ===============================
def cria_audio(texto):
    caminho = "audios/fala.mp3"

    if os.path.exists(caminho):
        try:
            os.remove(caminho)
        except PermissionError:
            pygame.mixer.quit()
            os.remove(caminho)

    # gerar áudio com ElevenLabs
    audio_bytes = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", 
        text=texto,
        model_id="eleven_multilingual_v2"
    )

    with open(caminho, "wb") as f:
        for chunk in audio_bytes:
            f.write(chunk)


    pygame.mixer.init()
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

    pygame.mixer.quit()


# ===============================
# OUVIR MICROFONE 
# ===============================
def ouvir_microfone():
    with sr.Microphone(device_index=0, sample_rate=48000) as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=1)

        recognizer.energy_threshold = 25
        recognizer.dynamic_energy_threshold = True
        recognizer.pause_threshold = 1.5
        recognizer.non_speaking_duration = 0.6

        print(f"Ouvindo, {nome}...")

        try:
            audio = recognizer.listen(
                mic,
                timeout=15,          # 
                phrase_time_limit=20  
            )
        except sr.WaitTimeoutError:
            print("Não ouvi nada...")
            return ""

    try:
        frase = recognizer.recognize_google(audio, language="pt-BR")
        return frase
    except:
        print("Não entendi.")
        return ""


# ===============================
# INPUT VIA VOZ
# ===============================
def input_voz(prompt=""):
    print(prompt)
    frase = ouvir_microfone()
    print(f"[entrada por voz]: {frase}")
    return frase


# ===============================
# AÇÕES DE SISTEMA
# ===============================
def verificar_acao(frase):
    f = frase.lower()

    if "sair" in f or "encerrar" in f or "fechar" in f:
        print("Desligando...")
        cria_audio("Fechando o sistema. Até mais!")
        sys.exit(0)


# ===============================
# BEM-VINDO (fala inicial)
# ===============================
cria_audio(f"Olá senhor {nome}, Versão de teste IA")


# ===============================
# LOOP PRINCIPAL
# ===============================
historico = []

while True:

    pergunta = input_voz(f"{nome}: O que posso ajudar você? (ou diga Encerrar)")

    if not pergunta:
        continue

    verificar_acao(pergunta)

    mensagem = (
        f"Usuário: {nome}\n"
        f"Histórico:\n" + "\n".join(historico[-10:]) + "\n"
        f"Pergunta atual: {pergunta}"
    )

    resposta = chat.invoke(mensagem).content

    print("\nChatGroq:", resposta)
    cria_audio(resposta)

    historico.append(f"{nome}: {pergunta}")

