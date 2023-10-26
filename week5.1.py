from sys import platform

if platform == "win32":
    print("This is windows")
elif platform == "linux":
    print("This is linux")
else:
    print("This is neither windows or linux")