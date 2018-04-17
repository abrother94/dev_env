import os

MP="/home/nick_huang/Study_ONL/OpenNetworkLinux/packages/base/amd64/kernels/kernel-3.16-lts-x86-64-all/builds/linux-3.16.53"
pinclude=[]
for subdir, dirs, files in os.walk(MP):
    for dir in dirs:
        fullpath = os.path.join(subdir, dir)
        if fullpath.endswith('include'):
            pinclude.append("-isystem")
            pinclude.append(fullpath)

def get_include():
    return  pinclude
