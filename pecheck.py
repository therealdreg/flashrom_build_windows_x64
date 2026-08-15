#!/usr/bin/python3

import pefile
import sys

pe = pefile.PE(sys.argv[1])
if pe.verify_checksum():
    print("PE checksum verified")
else:
    print("PE checksum invalid")