import random
import hashlib
import sys
from datetime import datetime
bytes = int(sys.argv[1])
seed = 0
if len(sys.argv) == 2:
    hash = hashlib.sha512(random.randbytes(bytes)).hexdigest()
elif len(sys.argv) == 3:
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