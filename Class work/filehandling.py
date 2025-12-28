'''
try:
    file=open('filehandling.txt','r')
except FileNotFoundError:
    print("File is not present")
else:
    print(file.read())
    print(file.readline())
    print(file.readlines())
    file.close()
    file.seek
    '''
try:
    with open('filehandling.txt','r')as file:
        print(file.read())
        file.seek(0)
        print(file.readline())
        file.seek(0)
        print(file.readlines())
except FileNotFoundError:
    print("File is not present")
