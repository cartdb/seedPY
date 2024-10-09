import os
import sys
if len(sys.argv) != 1 and len(sys.argv) != 2:
    raise Exception("Too many or too little arguments!")
if len(sys.argv) == 2:
    output = sys.argv[1]
    output = open(output, "w")
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
        print(item + " Mapper: " + str(mapper))
        if len(sys.argv) == 2:
            if linesWritten == 0:
                output.write(item + " Mapper: " + str(mapper))
                linesWritten += 1
            else:
                output.write("\n" + item + " Mapper: " + str(mapper))
