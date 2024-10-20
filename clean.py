import os
roms = open("roms.txt", "w")
times = open("times.txt", "w")
linesWritten = 0
for item in os.listdir(os.getcwd()):
    if item.endswith(".nes"):
        file = item
        fileread = open(file, "rb")
        fileread = fileread.read()
        headerByteOne = fileread[6:7]
        headerByteOne = int.from_bytes(headerByteOne)
        headerByteTwo = fileread[7:8]
        headerByteTwo = int.from_bytes(headerByteTwo)
        mapper = 0
        if headerByteOne&2**4 != 0:
            mapper += 2**0
        if headerByteOne&2**5 != 0:
            mapper += 2**1
        if headerByteOne&2**6 != 0:
            mapper += 2**2
        if headerByteOne&2**7 != 0:
            mapper += 2**3
        if headerByteTwo&2**4 != 0:
            mapper += 2**4
        if headerByteTwo&2**5 != 0:
            mapper += 2**5
        if headerByteTwo&2**6 != 0:
            mapper += 2**6
        if headerByteTwo&2**7 != 0:
            mapper += 2**7
        if mapper != 0:
            os.remove(item)
        else:
            print(item)
            if os.path.isfile(item.replace(".nes", ".fm2")):
                if linesWritten == 0:
                    roms.write(item)
                    linesWritten += 1
                    fm2 = open(item.replace(".nes", ".fm2"), "r")
                    time = 0
                    while True:
                        line = fm2.readline()
                        if not line:
                            break
                        if "||" in line:
                            time += 1
                    print(str(time))
                    times.write(str(time))
                else:
                    roms.write("\n" + item)
                    fm2 = open(item.replace(".nes", ".fm2"), "r")
                    time = 0
                    while True:
                        line = fm2.readline()
                        if not line:
                            break
                        if "||" in line:
                            time += 1
                    print(str(time))
                    times.write("\n" + str(time))