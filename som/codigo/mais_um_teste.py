from gerarAudio import fraseToAudio
fraseInicial = input().split(" ")
audio = fraseToAudio(fraseInicial)
audio += 20
audio.export("eudesisto.mp3")