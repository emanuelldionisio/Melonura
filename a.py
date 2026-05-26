from pydub import AudioSegment

# 1m 6aa 3m

audio = AudioSegment.from_file("todos_as_notas_dos_sapos.mp3")
a = audio[:250]
b = audio[90000:90500]
c = audio[4000:4250] 
novo_audio = a + b + c
novo_audio.export("novo_audio.mp3", format="mp3")