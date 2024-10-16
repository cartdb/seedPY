import os
delimiters = ["(", ")"]
supportedRegions = []
file = open("region.txt", "r")
while True:
    line = file.readline()
    if not line:
        break
    line = line.replace("\\n", "")
    line = line.replace("\n", "")
    line = line.split(" ")
    for lines in range(len(line)):
        supportedRegions.append(line[lines])
for item in os.listdir(os.getcwd()):
    if item.endswith(".nes"):
        rom = item
        flag = False
        for delimiter in delimiters:
            item = " ".join(item.split(delimiter))
        item = item.split()
        for entries in range(len(item)):
            for regions in range(len(supportedRegions)):
                if item[entries] == supportedRegions[regions]:
                    item = item[entries]
                    region = item
                    flag = True
                if flag == True:
                    break
            if flag == True:
                break
        if flag == False:
            raise Exception("Region not found for " + rom)
        else:
            if region == 'United':
                region = "United Kingdom"
            elif region == 'Europe,':
                region = "Europe, Hong Kong"
            elif region == 'USA,':
                region = "USA, Europe"
            print(region)