import pydub
import pathlib

fones = {}
caminho = pathlib.Path("som") / "audios" / "notas.mp3"

audio = pydub.AudioSegment.from_file(caminho)

for i in range(1, 9):
    fones[f"m{i}"] = audio[2000 * (i-1) : 2000 * (i-1) + 1000]
    #print(f"m{i} = {2000 * (i-1)} : {2000 * (i-1) + 1000}")

for i in range(1, 9):
    fones[f"v{i}"] = audio[16000 + 2000 * (i-1) : 16000 + 2000 * (i-1) + 1000] 
    #print(f"v{i} = {16000 + 2000 * (i-1)} : {16000 + 2000 * (i-1) + 1000}")

fones[f"f"] = audio[32000 : 32500] - 10
fones[f"p"] = audio[48000 : 48500] + 10

for i in range(1, 9):
    fones[f"r{i}"] = audio[64000 + 2000 * (i-1) : 64000 + 2000 * (i-1) + 1000] 
    #print(f"a{i} = {64000 + 2000 * (i-1)} : {64000 + 2000 * (i-1) + 1000}")

for i in range(1, 9):
    fones[f"a{i}"] = audio[80000 + 2000 * (i-1) : 80000 + 2000 * (i-1) + 1000] 
    #print(f"c{i} = {80000 + 2000 * (i-1)} : {80000 + 2000 * (i-1) + 1000}")
