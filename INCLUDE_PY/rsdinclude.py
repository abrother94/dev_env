import os

MP="/home/nick_huang/Intel_RSD_Test/ORG_B/2.1.3/rsd/PSME/"
pinclude=[]
for subdir, dirs, files in os.walk(MP):
    for dir in dirs:
        fullpath = os.path.join(subdir, dir)
        if fullpath.endswith('include'):
            pinclude.append("-isystem")
            pinclude.append(fullpath)

def get_rsd_include():
    return  pinclude
