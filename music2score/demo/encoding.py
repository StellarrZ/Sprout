import os
from base64 import b64encode

files = os.listdir(os.getcwd())
pngs = list(filter(lambda x: x[-4:] == ".png", files))
print(len(pngs))

for png in pngs:
    with open(png, 'rb') as fh:
        enc = b64encode(fh.read())
    with open(png[:-4] + ".txt", 'wb') as fh:
        fh.write(enc)