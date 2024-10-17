import os
supportedRegions = []
files = []
linesWritten = []
file = open("region.txt", "r")
while True:
    line = file.readline()
    if not line:
        break
    line = line.replace("\\n", "")
    line = line.replace("\n", "")
    supportedRegions.append(line)
for regions in range(len(supportedRegions)):
    files.append(open(supportedRegions[regions] + ".txt", "w"))
    linesWritten.append(0)
for item in os.listdir(os.getcwd()):
    if item.endswith(".nes"):
        rom = item
        flag = False
        for regions in range(len(supportedRegions)):
            if "(" + supportedRegions[regions] + ")" in item:
                flag = True
                if linesWritten[regions] == 0:
                    files[regions].write(item)
                    linesWritten[regions] += 1
                else:
                    files[regions].write("\n" + item)
                item = supportedRegions[regions]
                break
        if flag == False:
            raise Exception("Region not found for " + rom)
        else:
            print(rom + " Region: " + item)