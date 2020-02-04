import sys

global compare
STR_VER = b'LK_VER:'

def main():
  if compare:
    print("I: Comparing two bootloaders...")
    if sys.argv[2] == sys.argv[3]:
        print("E: You cannot compare same bootloader! Abort...")
        exit(1)
    data1 = bl1.read()
    data2 = bl2.read()
    if b'AMZN' not in data1:
       print("E: Bootloader 1 is not from Amazon! Abort...")
       exit(1)
    elif b'AMZN' not in data2:
       print("E: Bootloader 2 is not from Amazon! Abort...")
       exit(1)
    offset1 = data1.find(STR_VER)
    offset2 = data2.find(STR_VER)
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
    if b'AMZN' not in data:
        print("E: Bootloader is not from Amazon! Abort...")
        exit(1)
    offset = data.find(STR_VER)
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
