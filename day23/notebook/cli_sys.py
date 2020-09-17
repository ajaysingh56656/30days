import sys
from getpass import getpass

if __name__ == "__main__":
    try:
        name = sys.argv[1]
    except:
        name = input("What's your name?\n")
    pw = getpass("What's Your passsword\n")
    print(name, pw)
    
