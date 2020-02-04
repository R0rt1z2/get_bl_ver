import sys

global compare
VER_STRING = b'LK_VER:'

def main():
  if compare:
    print("I: Comparing two bootloaders...")
    data1 = bl1.read()
    data2 = bl2.read()
    offset1 = data1.find(VER_STRING)
    offset2 = data2.find(VER_STRING)
    bl1.seek(offset1 + 7)
    bl2.seek(offset2 + 7)
    ver1 = bl1.read(2)
    ver2 = bl2.read(2)
    int_ver1 = int.from_bytes(ver1, "little")
    int_ver2 = int.from_bytes(ver2, "little")
    ver1 = ver1.hex()
    ver2 = ver2.hex()
    if ver1 != ver2:
      print("W: Bootloaders have different version! {} ({}) vs {} ({})".format(ver1, int_ver1, ver2, int_ver2))
    else:
      print("I: Bootloaders have the same version: {} ({})".format(ver1, int_ver1))
  else:
    data = bl.read()
    offset = data.find(VER_STRING)
    bl.seek(offset + 7)
    ver = bl.read(2) # 2 bytes determine ver
    int_ver = int.from_bytes(ver, "little")
    ver = ver.hex()
    print("I: BL Version: {} ({})".format(ver, int_ver))
  
if __name__ == "__main__":
  if sys.argv[1] == "-c":
     compare = True
     bl1 = open(sys.argv[2], "rb")
     bl2 = open(sys.argv[3], "rb")
  else:
     compare = False
     bl = open(sys.argv[1], "rb")
  main()
