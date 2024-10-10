import os
import sys
import hashlib
import pathlib
workdir = os.getcwd()
if len(sys.argv) != 2:
    raise Exception("disassembler.exe [file]")
file = sys.argv[1]
if os.path.isfile(file) == False:
    raise Exception(file + " not found!")
bytesArr = []
headerBytes = []
count = 0
input = open(file, "rb")
fileread = input.read()
bytefour = fileread[4:5]
bytefour = int.from_bytes(bytefour)
print("PRG ROM Banks: " + bytefour)
bytefive = fileread[5:6]
bytefive = int.from_bytes(bytefive)
print("CHR ROM Banks: " + bytefive)
bytesix = fileread[6:7]
bytesix = int.from_bytes(bytesix)
if bytesix&2**0 != 0:
    print("Mirroring: Vertically Mirrored")
else:
    print("Mirroring: Horizontally Mirrored")
if bytesix&2**1 != 0:
    if file.endswith(".nes"):
        os.remove(file)
    raise Exception("This disassembler does not support ROMs that have battery-backed PRG RAM!")
if bytesix&2**2 != 0:
    if file.endswith(".nes"):
        os.remove(file)
    raise Exception("This disassembler does not support ROMs that have 512-byte trainers!")
if bytesix&2**3 != 0:
    if file.endswith(".nes"):
        os.remove(file)
    raise Exception("This disassembler does not support ROMs that have alternate nametable layouts!")
if bytesix&2**4 != 0 or bytesix&2**5 != 0 or bytesix&2**6 != 0 or bytesix&2**7 != 0:
    if file.endswith(".nes"):
        os.remove(file)
    raise Exception("This disassembler does not support ROMs that use mappers!")
byteseven = fileread[7:8]
byteseven = int.from_bytes(byteseven)
if byteseven&2**0 != 0:
    if file.endswith(".nes"):
        os.remove(file)
    raise Exception("This disassembler does not support VS System ROMs!")
if byteseven&2**1 != 0:
    if file.endswith(".nes"):
        os.remove(file)
    raise Exception("This disassembler does not support Playchoice-10 ROMs!")
if byteseven&2**2 != 0 and byteseven&2**3 != 0:
    if file.endswith(".nes"):
        os.remove(file)
    raise Exception("This disassembler does not support NES 2.0 ROMs!")
if byteseven&2**4 != 0 or byteseven&2**5 != 0 or byteseven&2**6 != 0 or byteseven&2**7 != 0:
    if file.endswith(".nes"):
        os.remove(file)
    raise Exception("This disassembler does not support ROMs that use mappers!")
for byte in pathlib.Path(file).read_bytes():
    bytesArr.append(byte)
    if count < 7:
        headerBytes.append(byte)
    count += 1
del bytesArr[:16]
if os.path.isfile("asm6f.exe") == False:
    raise Exception("asm6f.exe is not installed! Download asm6f at https://github.com/freem/asm6f and extract the files to " + workdir)
byteCount = 0
if fileread[0:4] != b'\x4e\x45\x53\x1a' or os.path.getsize(file) != (bytefour * 16384) + (bytefive * 8192):
    print(fileread[0:4])
    raise Exception("Not a valid INES ROM file! A valid INES ROM file will have the characters [4E 45 53 1A] followed by [Number of PRG Banks] [Number of CHR Banks] and then followed by zeroes [00 00 00 00 00 00 00 00 00]! Edit the ROM in a hex editor if required.")
input = open(file, "wb")
if fileread[7:15] != b'\x00\x00\x00\x00\x00\x00\x00\x00\x00':
    input.write(bytearray(headerBytes))
    input.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    input.write(bytearray(bytesArr))
input = open(file, "rb")
fileread = input.read()
hash = hashlib.sha512(fileread).hexdigest()
prgbanks = fileread[4:5]
chrbanks = fileread[5:6]
fileoutputname = file.split(".nes")
fileoutputname = fileoutputname[0]
fileoutputname = fileoutputname + ".asm"
fileoutput = open(fileoutputname, "w")
linesWritten = 0
for byte in pathlib.Path(file).read_bytes():
    if byte >= 16:
        hexVersion = hex(byte)
    else:
        hexVersion = "0" + hex(byte)
    hexVersion = hexVersion.replace("0x", "")
    instruction = ".DB $" + hexVersion
    if linesWritten == 0:
        fileoutput.write(instruction)
    else:
        fileoutput.write("\n" + instruction)
    linesWritten += 1
fileoutput.close()
os.system('asm6f.exe "' + fileoutputname + '" "' + file + '"')
filehash = open(file, "rb")
filehash = filehash.read()
filehash = hashlib.sha512(filehash).hexdigest()
if hash == filehash:
    print("Disassembling complete.")
else:
    print("Disassembling failed.")
