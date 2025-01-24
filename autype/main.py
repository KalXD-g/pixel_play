from getch import getch
import time
from pathlib import Path
from playsound import playsound
import random

sound_files_path = Path("sound_files")

sound_files = [file for file in sound_files_path.iterdir() if file.is_file() and file.suffix in ['.mp3', '.wav']]

total_played = 0
correct_played = 0

reaction_times = []

def call_random_sound():
    global total_played
    global correct_played

    i = 0
    esc_char = "\x1b"

    while i == 0:
        file = sound_files[random.randint(0, len(sound_files)-1)]
        playsound(str(file))
        start = time.time()
        answer = getch()

        if answer == file.name[0]:
            end = time.time()
            playsound('short_beep.mp3')
            reaction_times.append(end-start)
            print(f"RT = {round(end-start,5)}s")
            print(f"A = {file.name[0]}\n")
            total_played+=1
            correct_played+=1
            
        elif answer == esc_char:
            playsound('power_down.mp3')
            print(f"Average Reaction Time->{sum(reaction_times)/len(reaction_times):.5f} seconds")
            print(f"Accuracy->{(correct_played/total_played)*100:.2f}%")
            i = 1

        else:
            end = time.time()
            reaction_times.append(end-start)
            playsound('wrong_beep.mp3')
            print(f"RT = {round(end-start,5)}s")
            print(f"A = {file.name[0]}\n")
            total_played+=1

call_random_sound()
