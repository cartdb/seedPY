import os
import sys
if len(sys.argv) != 1 and len(sys.argv) != 2 or len(sys.argv) == 2 and sys.argv[1] != "--install":
    raise Exception("Too many or too little arguments!")
if len(sys.argv) == 2:
    os.system("go install github.com/retroenv/nesgodisasm@latest")
for item in os.listdir(os.getcwd()):
    if item.endswith(".nes"):
        file = item
        fileread = open(file, "rb")
        fileread = fileread.read()
        headerByteOne = fileread[6:7]
        headerByteOne = int.from_bytes(headerByteOne)
        headerByteTwo = fileread[7:8]
        headerByteTwo = int.from_bytes(headerByteTwo)
        if file.endswith(".nes") == False or headerByteOne >= 16 or headerByteTwo >= 16:
            if file.endswith(".nes"):
                os.remove(file)
                print(file)
        else:
            os.system('nesgodisasm.exe -nohexcomments -nooffsets -a nesasm "' + file + '"')
            os.system('nesasm.exe "' + file.replace(".nes", ".asm") + '"')
            filename = file.replace(".nes", ".asm")
            file = open(filename, "r")
            lineCount = 0
            byteCount = 0
            start = 0
            end = 0
            lineNum = 0
            lines = []
            while True:
                line = file.readline()
                if not line:
                    lineCount += 1
                else:
                    lineCount = 0
                    lineNum += 1
                    lines.append(line)
                if lineCount > 2:
                    break
                if ".byte" in line:
                    byteCount += 1
                else:
                    byteCount = 0
                if byteCount >= 512:
                    end = lineNum
                    start = lineNum - 512
            file.close()
            lineCount = 0
            file = open(filename, "r")
            lines = file.readlines()
            chrLines = []
            inc = 0 
            while start + inc < end and start != 0 and end != 0:
                line = lines[start + inc]
                line = line.replace(".byte $", "")
                line = line.split(", $")
                for entrys in range(len(line)):
                    if ".incbin" not in line[entrys]:
                        chrLines.append(int(line[entrys], 16))
                inc += 1
            if len(chrLines) == 8192:
                file = open(filename.replace(".asm", ".chr"), "wb")
                file.write(bytearray(chrLines))
            file = open(filename, "w")
            lineCount = 0
            for line in range(len(lines)):
                if lineCount < start:
                    file.write(lines[line])
                else:
                    file.write(' .incbin "' + filename.replace(".asm", ".chr") + '"')
                    os.system('chrtopng.exe "' + filename.replace(".asm", ".chr") + '"')
                    break
                lineCount += 1
            file.close()
