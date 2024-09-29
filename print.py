import hashlib
import sys
import os
if len(sys.argv) != 2 and len(sys.argv) != 3:
    raise Exception("Too many or too little arguments!")
if len(sys.argv) == 3:
    write = open(sys.argv[2], "w")
linesWritten = 0
for x in os.listdir():
    if x.endswith(sys.argv[1]):
        file = open(x, "rb")
        file = file.read()
        print(x + " SHA512: " + hashlib.sha512(file).hexdigest())
        if len(sys.argv) == 3:
            if linesWritten == 0:
                write.write(x + " SHA512: " + hashlib.sha512(file).hexdigest())
                linesWritten += 1
            else:
                write.write("\n" + x + " SHA512: " + hashlib.sha512(file).hexdigest())