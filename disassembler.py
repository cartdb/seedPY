import os
import sys
import hashlib
import pathlib
workdir = os.getcwd()
if len(sys.argv) != 2:
    raise Exception("disassembler.exe [file]")
if os.path.isfile("nesasm.exe") == False:
    raise Exception("nesasm.exe is not installed! Download at https://github.com/ClusterM/nesasm and copy the 2 DLL files and nesasm.exe to " + workdir)
else:
    if os.path.isfile(file):
        file = sys.argv[1]
    else:
        raise Exception(file + " not found!")
byteCount = 0
fileread = file.read()
if fileread[0:3] != b'\x4e\x45\x53\x1a' or fileread[7:15] != b'\x00\x00\x00\x00\x00\x00\x00\x00\x00':
    raise Exception("Not a valid INES ROM file! A valid INES ROM file will have the characters [4E 45 53 1A] followed by [Number of PRG Banks] [Number of CHR Banks] and then followed by zeroes [00 00 00 00 00 00 00 00 00]! Edit the ROM in a hex editor if required.")
prgbanks = fileread[4:5]
chrbanks = fileread[5:6]
bytesix = fileread[6:7]
mirroring = 0
mapper = 0
bytesix = int.from_bytes(bytesix)
if bytesix&2**0 != 0:
    mirroring += 2**0
if bytesix&2**1 != 0:
    raise Exception("This disassembler does not support ROMs that have battery-backed PRG RAM!")
if bytesix&2**2 != 0:
    raise Exception("This disassembler does not support ROMs that have 512-byte trainers!")
if bytesix&2**3 != 0:
    raise Exception("This disassembler does not support ROMs that have alternate nametable layouts!")
if bytesix&2**4 != 0 or bytesix&2**5 != 0 or bytesix&2**6 != 0 or bytesix&2**7 != 0:
    raise Exception("This disassembler does not support ROMs that use mappers!")
fileoutput = file.split(".")
fileoutput = fileoutput[0]
fileoutput = fileoutput + ".asm"
fileoutput = open(fileoutput, "w")
bank = 0
addrdec = 32768
addr = hex(addrdec)
for byte in pathlib.Path(file).read_bytes():
    if byteCount == 0 and byte >= 16:
        if linesWritten == 0:
            fileoutput.write(".bank " + str(bank))
            fileoutput.write(".org " + str(addr))
            linesWritten += 1
        else:
            fileoutput.write("\n" + ".bank " + str(bank))
            fileoutput.write("\n" + ".org " + str(addr))
            linesWritten += 1
    elif byteCount == 8000:
        byteCount = 0
        bank += 1
        if linesWritten == 0:
            fileoutput.write(".bank " + str(bank))
            fileoutput.write(".org " + str(addr))
            linesWritten += 1
        else:
            fileoutput.write("\n" + ".bank " + str(bank))
            fileoutput.write("\n" + ".org " + str(addr))
            linesWritten += 1
    if byte >= 16:
        hexVersion = hex(byte)
    else:
        hexVersion = "0" + hex(byte)
    hexVersion = hexVersion.replace("0x", "")
    instruction = ".DB $" + hexVersion
    if linesWritten == 0:
        fileoutput.write(instruction)
        linesWritten += 1
    else:
        fileoutput.write("\n" + instruction)
        linesWritten += 1
    if byte >= 16:
        byteCount += 1
