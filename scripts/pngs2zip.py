import os
from zipfile import ZipFile


# Zip several png files
def png2zip(fileName: str, zipPath: str):

    # files = list(filter(lambda x: x[-4:] == '.png', os.listdir(path)))
    files = os.listdir(zipPath)

    with ZipFile(zipPath + ".zip", 'w') as zp:
        for fpng in files:
            zp.write(zipPath + "/" + fpng, fileName + "/" + fpng)