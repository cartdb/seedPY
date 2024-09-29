import random
import hashlib
import sys
import os
from datetime import datetime
bytes = int(sys.argv[1])
seed = 0
if len(sys.argv) == 2:
    hash = hashlib.sha512(random.randbytes(bytes)).hexdigest()
elif len(sys.argv) == 3:
    if os.path.isfile(sys.argv[2]):
        if os.path.getsize(sys.argv[2]) == bytes:
            file = sys.argv[2]
            file = open(file, "rb")
            file = file.read()
            hash = hashlib.sha512(file).hexdigest()
        else:
            raise Exception("The size listed is not the same size as the file listed!")
    else:
        hash = sys.argv[2]
else:
    raise Exception("Exiting program now...")
start = datetime.now()
while True:
    file = open("file" + str(bytes) + ".bin", "wb")
    random.seed(seed)
    file.write(random.randbytes(bytes))
    file.close()
    file = open("file" + str(bytes) + ".bin", "rb")
    file = file.read()
    if hashlib.sha512(file).hexdigest() == hash:
        break
    else:
        seed += 1
        print("Seed: " + str(seed))
end = datetime.now()
print((end - start).total_seconds())