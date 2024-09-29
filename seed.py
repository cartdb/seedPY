import random
import sys
if len(sys.argv) != 4:
    raise Exception("Too many or too little arguments!")
seedSize = int(sys.argv[1])
seedStart = int(sys.argv[2])
seedEnd = int(sys.argv[3])
while True:
    file = open("file" + str(seedSize) + "(" + str(seedStart) + ").bin", "wb")
    random.seed(seedStart)
    file.write(random.randbytes(seedSize))
    seedStart += 1
    if seedStart > seedEnd:
        break