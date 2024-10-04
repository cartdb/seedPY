import os
folder = os.getcwd()
for item in os.listdir(folder):
    if item.endswith(".nes"):
        os.system('nessplitter.exe "' + item + '"')
        os.system('chrtopng.exe "' + item.replace(".nes", ".chr") + '" "' + item.replace(".nes", ".png") + '"')
        os.remove(item)
        os.system('nesasm "' + item.replace(".nes", ".asm") + '"')
        if os.path.isfile(item) == False:
            print(item)
            try:
                os.remove(item.replace(".nes", ".asm"))
            except:
                continue
            try:
                os.remove(item.replace(".nes", ".png"))
            except:
                continue
            try:
                os.remove(item.replace(".nes", ".chr"))
            except:
                continue
os.system("mkdir asm")
os.system("mkdir chr")
os.system("mkdir png")
os.system("mkdir nes")
os.system("move *.asm asm")
os.system("move *.chr chr")
os.system("move *.png png")
os.system("move *.nes nes")