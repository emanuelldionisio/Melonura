from pydub import AudioSegment
from fones import fones
import pathlib
import random

CURTO = 250
LONGO = 500
SURDO = 100
FADE = 0.1
CROSSFADE = 0.3
INTERVALO = 50
GAP = 7

outPut = pathlib.Path("som") / "output" 
outPut.mkdir(exist_ok=True)

def somAleatorio(tamanho, audio):
    if (len(audio) <= tamanho):
        return audio
    inicioMax = len(audio) - tamanho
    inicio = random.randint(0, inicioMax)
    return audio[inicio : inicio + tamanho]

def silabaToAudio(silaba):
    audio = AudioSegment.empty()
    for letra in silaba.split("/"):
        novo = AudioSegment.empty()
        if (letra[0] in "pf"):
            novo += somAleatorio(SURDO, fones[letra])
        elif (len(letra) == 3):
            novo += somAleatorio(LONGO, fones[letra[1:]])
        else:            
            novo += somAleatorio(CURTO, fones[letra])
        
        if (letra[0] not in "apf"):
            novo = novo - GAP

        if (audio.duration_seconds > 0):
            audio = audio + novo if letra[0] in "pf" else audio.append(novo, crossfade=CURTO * CROSSFADE)
        else:
            audio = novo

    return audio

def fraseToAudio(fraseInicial: list[str]):
    fraseFinal = AudioSegment.empty()
    
    for palavra in fraseInicial:
        audioPalavra = AudioSegment.empty()
        for silaba in palavra.split("."):
            audioPalavra += silabaToAudio(silaba)
        fraseFinal += audioPalavra.fade_in(CURTO * FADE).fade_out(CURTO * FADE)
        fraseFinal += AudioSegment.silent(duration=INTERVALO)
    
    return fraseFinal

def criarArquivo(nome):
    fraseInicial = input().split(" ")
    fraseFinal = fraseToAudio(fraseInicial)
    fraseFinal.export(outPut / f"{nome}.mp3", format="mp3")