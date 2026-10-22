from pydub import AudioSegment
from fones import fones
import pathlib
import random

CURTO = 125
LONGO = 250
SURDO = 62
FADE = 0.3
CROSSFADE = 0.2
INTERVALO = 25
GAP = 5
VAZIO = 100

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
            novo += somAleatorio((int(LONGO*1.8)if letra[0] == 'r' else LONGO), fones[letra[1:]])
        else:            
            novo += somAleatorio(int(CURTO*1.8) if letra[0] == 'r' else CURTO, fones[letra])
        
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
        if (palavra == ""):
            fraseFinal += AudioSegment.silent(duration=VAZIO)
            continue
        audioPalavra = AudioSegment.empty()
        for silaba in palavra.split("."):
            audioPalavra += silabaToAudio(silaba)
        fraseFinal += audioPalavra.fade_in(CURTO * FADE).fade_out(CURTO * FADE)
        fraseFinal += AudioSegment.silent(duration=INTERVALO)
    
    return fraseFinal

def criarArquivo(nome, fraseInicial):
    fraseFinal = fraseToAudio(fraseInicial)
    fraseFinal.export(outPut / f"{nome}.mp3", format="mp3")