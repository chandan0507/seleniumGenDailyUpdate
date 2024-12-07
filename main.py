from getUrl import getUrlFromUser
from singleElements import getSingleElement

while True:
    fileName = input("Please enter the filename : ")
    fileName.strip()
    fileNamepy = fileName+".py"
    # instead of none, not is used to check empty or not
    if not fileName:
        continue 
    print(f"Given fileName is {fileNamepy}")
    getUrlFromUser(fileNamepy)
    getSingleElement(fileNamepy)