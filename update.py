import os
import sys
import random
if len(sys.argv) != 3:
    raise Exception("Too many or too little arguments!")
if os.path.isfile(sys.argv[1]) and sys.argv[1].endswith(".zip"):
    os.system("python zipextract.py")
else:
    raise Exception("Zip file not found!")
os.system("python print.py " + sys.argv[2] + " " + sys.argv[2] + ".txt")
file = open(sys.argv[2] + ".txt", "r")
hashes = []
while True:
    line = file.readline()
    if not line:
        break
    line = line.split(" SHA512: ")[0]
    line = line.replace("\\n", "")
    hashes.append(line)
rom = random.choice(hashes)
os.system("python run.py " + str(os.path.getsize(rom)) + " " + rom)
