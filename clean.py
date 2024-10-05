import os
folder = os.getcwd()
for item in os.listdir(folder):
    if item.endswith(".nes"):
        if os.path.getsize(item) == 40976 or os.path.getsize(item) == 24592:
            os.system('nessplitter.exe "' + item + '"')
            os.system('chrtopng.exe "' + item.replace(".nes", ".chr") + '" "' + item.replace(".nes", ".png") + '"')
            os.remove(item)
            os.system('nesasm "' + item.replace(".nes", ".asm") + '"')
            if os.path.isfile(item) == False:
                print(item)
                if os.path.isfile(item.replace(".nes", ".asm")):
                    os.remove(item.replace(".nes", ".asm"))
                if os.path.isfile(item.replace(".nes", ".chr")):
                    os.remove(item.replace(".nes", ".chr"))
                if os.path.isfile(item.replace(".nes", ".png")):
                    os.remove(item.replace(".nes", ".png"))
        else:
            os.remove(item)
            print(item)
os.system("mkdir asm")
os.system("mkdir chr")
os.system("mkdir png")
os.system("mkdir nes")
os.system("move *.asm asm")
os.system("move *.chr chr")
os.system("move *.png png")
os.system("move *.nes nes")