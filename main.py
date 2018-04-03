#!/usr/bin/python
import RSD_PY 
from RSD_PY import rsdinclude 

#sys.path.insert(0, "~/RSD_PY/")

def main():
    S=rsdinclude.get_rsd_include()
    str1 = ''.join(S)
    print str1

if __name__ == "__main__":
    main()
