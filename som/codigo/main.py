from pydub import AudioSegment
from fones import fones
import pathlib

CURTO = 250
LONGO = 500
FADE = 0.01
CROSSFADE = 0.3
INTERVALO = 50
GAP = 7

outPut = pathlib.Path("som") / "output"

def silabaToAudio(silaba):
    audio = AudioSegment.empty()
    for letra in silaba.split("/"):
        novo = AudioSegment.empty()
        if (len(letra) == 3):
            novo += fones[letra[1:]][:LONGO]
        else:            
            novo += fones[letra][:CURTO]
        
        if (letra[0] != "a"):
            novo = novo - GAP
        
        if (letra[0] == "a" and len(letra) != 3):
            novo = novo + GAP

        if (audio.duration_seconds > 0):
            audio = audio.append(novo, crossfade=LONGO * CROSSFADE)
        else:
            audio = novo

    return audio

def main():
    nome = input()
    fraseInicial = input().split(" ")
    fraseFinal = AudioSegment.empty()
    
    for palavra in fraseInicial:
        audioPalavra = AudioSegment.empty()
        for silaba in palavra.split("."):
            audioPalavra += silabaToAudio(silaba)
        fraseFinal += audioPalavra.fade_in(LONGO * FADE).fade_out(LONGO * FADE)
        fraseFinal += AudioSegment.silent(duration=INTERVALO)
    
    fraseFinal.export(outPut / f"{nome}.mp3", format="mp3")

if __name__ == "__main__":
    main()

