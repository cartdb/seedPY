import os
from datetime import datetime
roms = open("roms.txt", "r")
times = open("times.txt", "r")
rom = []
time = []
while True:
    line = roms.readline()
    if not line:
        break
    line = line.replace("\\n", "")
    line = line.replace("\n", "")
    rom.append(line)
while True:
    line = times.readline()
    if not line:
        break
    line = line.replace("\\n", "")
    line = line.replace("\n", "")
    time.append(int(line))
for item in os.listdir(os.getcwd()):
    for items in range(len(rom)):
        if rom[items] in item:
            start = datetime.now()
            os.system('fceux64.exe "' + item + '"')
            end = datetime.now()
            print((end - start).total_seconds())
            time.append((end - start).total_seconds())
            if (end - start).total_seconds() >= (time[items] / 60):
                if (end - start).total_seconds() < (time[items] / 60) * 1.5:
                    print("You win!")
                elif (end - start).total_seconds() == (time[items] / 60) * 1.5:
                    print("Tie!")
                elif (end - start).total_seconds() > (time[items] / 60) * 1.5:
                    print("You lose!")
            else:
                raise Exception("Invalid time!")