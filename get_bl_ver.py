import sys

STR_VER = b'LK_VER:'
AMZN_MAGIC = b'AMZN'

def check_amzn(data, bl):
  if not data:
      print("E: Cannot open bootloader data! Abort...") 
      exit(1)
  if AMZN_MAGIC in data:
      pass
  else:
      print("E: Cannot find amzn magic in {}! Abort...".format(bl))
      exit(1)

def main():
  if sys.argv[1] == "-c":
    print("I: Comparing two bootloaders...")

    # 1) Open bootloader
    bl1 = open(sys.argv[2], "rb")
    bl2 = open(sys.argv[3], "rb")

    # 2) Check bootloaders
    if sys.argv[2] == sys.argv[3]:
        print("E: You cannot compare same bootloader! Abort...")
        exit(1)

    # 3) Read bl data
    data1 = bl1.read()
    data2 = bl2.read()

    # 4) Check amzn magic
    check_amzn(data1, sys.argv[2])
    check_amzn(data2, sys.argv[)

    # 5) Find offsets
    offset1 = data1.find(STR_VER)
    offset2 = data2.find(STR_VER)
    bl1.seek(offset1 + 7)
    bl2.seek(offset2 + 7)

    # 6) Read version data
    ver1 = bl1.read(2)
    ver2 = bl2.read(2)
    int_ver1 = int.from_bytes(ver1, "little")
    int_ver2 = int.from_bytes(ver2, "little")
    ver1 = ver1.hex()
    ver2 = ver2.hex()

    # 7) Compare bootloaders
    if ver1 != ver2:
      print("W: Bootloaders have different version! {} ({}) vs {} ({})".format(ver1, int_ver1, ver2, int_ver2))
      exit(1)
    else:
      print("I: Bootloaders have the same version: {} ({})".format(ver1, int_ver1))
      exit(1)

  # 1) Open bootloader
  bl = open(sys.argv[1], "rb")

  # 2) Read Bl data
  data = bl.read()

  # 3) Check amzn magic
  check_amzn(data, sys.argv[1])

  # 4) Find offset
  offset = data.find(STR_VER)
  bl.seek(offset + 7)

  # 5) Read version data
  ver = bl.read(2) # 2 bytes determine ver
  int_ver = int.from_bytes(ver, "little")
  ver = ver.hex()
  print("I: BL Version: {} ({})".format(ver, int_ver))


if __name__ == "__main__":
   main()
