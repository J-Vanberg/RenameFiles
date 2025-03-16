import os
import random
import re
import string

# Rename files
def randomizeName(files):
    for name in files:
        prefix = "".join(random.choice(string.digits) for _ in range(length))
        os.rename(name, f"{prefix}-{name}")

def undoName(files):
    for name in files:
        os.rename(name, name[length + 1:])

# Variables
length = 5
nameBlacklist = []
nameWhitelist = []
extensionBlacklist = [".py"]
extensionWhitelist = []

# Fetch files, ignore self
files = [
    name
    for name in os.listdir(".")
    if os.path.isfile(name)
    and os.path.splitext(name)[0] not in nameBlacklist
    and os.path.splitext(name)[1] not in extensionBlacklist
    and (not nameWhitelist or os.path.splitext(name)[0] in nameWhitelist)
    and (not extensionWhitelist or os.path.splitext(name)[1] in extensionWhitelist)
]

# Check if renaming or undoing
randomized = all(re.search(fr"^\d{{{length}}}-", n) for n in files)
if randomized:
    print(f"{len(files)} file names are currently randomized, undo?")
    print("[Y] Continue")
    print("[N] Abort")
    print("\n")
    
    response = input("Enter Y/N:")
    if response.upper() == "Y":
        undoName(files)
        
        print("\n")
        print(f"Reset names of {len(files)} file(s).")

else:
    print(f"You are about to randomize {len(files)} file names.")
    print("[Y] Continue")
    print("[N] Abort")
    print("\n")
    
    response = input("Enter Y/N:")
    if response.upper() == "Y":
        randomizeName(files)
        
        print("\n")
        print(f"Randomized names of {len(files)} file(s).")