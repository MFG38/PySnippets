# To become a folder packager. Unfinished.

import os
import zipfile

# Create ZIP with all files and subfolders within the source folder.
def pack_folder(src,dest):
    relroot = os.path.abspath(os.path.join(src,os.pardir))
    
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(src):
            zip.write(root,os.path.relpath(relroot))
            for file in files:
                filename = os.path.join(root,file)
                if os.path.isfile(filename):
                    arcname = os.path.join(os.path.relpath(root,relroot),file)
                    zip.write(arcname,filename)
    zip.close()
