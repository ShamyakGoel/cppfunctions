char1 = ""
import random
class LessArgsException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = args[0]
    def __str__(self) -> str:
        return self.message
"""
Many c/c++ functions are written in cppfunctions module. PLease install as "pip install cppfunctions"
"""
from sys import stdin
from typing import IO
EOF = -1
# String/Character IO. C/C++ Functions but in python !!
def fopen(filename:str , mode:str):
    return open(filename , mode)
def fgets(file : IO):
    """
    Fecths a string from a file. Identical to c/c++ fgets function
    Developed by : Shamyak Goel (28/10/2021)\n
    ARGUEMENTS:
        File : File to the line is readed
    Returns:
        A string read by readline() function
    """
    return file.readline()
def fputs(file : IO,string:str):
    """
    Writes a string from a file. Identical to c/c++ fputs function
    Developed by : Shamyak Goel (28/10/2021)
    ARGUEMENTS:
        File : To be written
        String : Content
    Does:
        Writes a string to file
    """
    file.write(string+"\n")
def fputc(file : IO , string:str):
    """
    Puts/Writes a character into a file. Identical to c/c++ fputc function
    Developed by : Shamyak Goel (26/10/2021)\n
    ARGUEMENTS:
        None
    Does:
        Writes character to a file
    """
    file.write(string[0])
def fgetc(file : IO):
    """
    Fecths a character from a file. Identical to c/c++ fgetc function
    Developed by : Shamyak Goel (26/10/2021)\n
    ARGUEMENTS:
        None
    Returns:
        A character read by read() function
    """
    return file.read(1)
def get(file:IO):
    """
    Gets a character from a file. Identical to c/c++ get function
    Developed by : Shamyak Goel (26/10/2021)\n
    ARGUEMENTS:
        None
    Returns:
        A character fetched by file
    """
    return file.read(1)
def put(file:IO , string : str):
    """
    Puts a character into a file. Identical to c/c++ put function
    Developed by : Shamyak Goel (26/10/2021)\n
    ARGUEMENTS:
        None
    Does:
        Writes character to a file
    """
    for i in string:
        file.write(i)
def puts(str):
    """
    Puts a string in stdout. Identical to c/c++ puts function
    Developed by : Shamyak Goel (26/10/2021)\n
    ARGUEMENTS:
        str : string to be put on stdout
    Does:
        Writes a string to stdout
    """
    print(str , end="")
def getchar():
    return stdin.read(1)
def scanf(__format:str , *msg):
    global char1
    count = 0
    arr = []
    for i in __format:
        if(i == '%'):
            char1 = i
        elif char1 == '%' and i == 'd':
            print(msg[count])
            data = int(input().split(" ")[0])
            arr.append(data)
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "i"):
            print(msg[count])
            data = int(input().split(" ")[0])
            arr.append(data)
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "s"):
            print(msg[count])
            data = input().split(" ")[0]
            arr.append(data)
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "f"):
            print(msg[count])
            data = float(input().split(" ")[0])
            arr.append(data)
            count+=1
            char1 = ""
    return arr
def getline(propmt):
    """
    Identical to gets function but you can pass a propmt
    Developed by : Shamyak Goel (26/10/2021)\n
    ARGUEMENTS:
        propmt : displaying before input
    Returns:
        A string fecthed by input() function.
    """
    return input(propmt+"\n")
def gets():
    """
    An alternative for c/c++ gets function.
    Developed by : Shamyak Goel (26/10/2021)\n
    ARGUEMENTS:
        None
    Returns:
        A string fecthed by input() function.
    """
    return input()
def sscanf(arr , __format: str):
    """
    An alternative for c/c++ sscanf function.
    Developed by : Shamyak Goel (26/10/2021)\n
    ARGUEMENTS:
        arr : to be variables are scanned
        __format : Formatted string with special characters %d or %i for an int , %s for a string , %f for a float , %b for a bolean value
    """
    global char1
    vars = list()
    count = 0
    for i in __format:
        if(i == '%'):
            char1 = i
        elif(char1 == "%" and i == "d"):
            vars.append(int(arr[count]))
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "i"):
            vars.append(int(arr[count]))
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "s"):
            vars.append(str(arr[count]))
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "f"):
            vars.append(float(arr[count]))
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "b"):
            vars.append(bool(arr[count]))
            count+=1
            char1 = ""
    return vars
def sprintf(__format:str , *vars):
    """
    An alternative for c/c++ sprintf function.
    Developed by : Shamyak Goel (27/10/2021)\n
    ARGUEMENTS:
        __format : str\n
        *vars : list of variables to be replaced by special characters : %d or %i for an int , %s for a string , %f for a float , %b for a bolean value
    """
    count= 0
    arr = list()
    global char1
    for i in __format:
        if(i == '%'):
            char1 = i
        elif(char1 == "%" and i == "d"):
            arr.append(int(vars[count]))
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "i"):
            arr.append(int(vars[count]))
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "s"):
            arr.append(str(vars[count]))
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "f"):
            arr.append(float(vars[count]))
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "b"):
            arr.append(bool(vars[count]))
            count+=1
            char1 = ""
    return arr
def printf(__format:str , *vars):
    """
    An alternative for c/c++ printf function.
    Developed by : Shamyak Goel (13/10/2021)\n
    ARGUEMENTS:
        __format : str\n
        *vars : list of variables to be replaced by special characters : %d or %i for an int , %s for a string , %f for a float , %b for a bolean value
    """
    global char1
    count = 0
    result = __format
    for i in __format:
        if(i == '%'):
            char1 = i
        elif(char1 == "%" and i == "d"):
            try:
             result = result.replace("%d" , str(int(vars[count])) , 1)
            except IndexError:
             raise(LessArgsException("Please provide arguements to printf()."))
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "i"):
            try:
             result = result.replace("%i" , str(int(vars[count])) , 1)
            except IndexError:
             raise(LessArgsException("Please provide arguements to printf()."))
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "s"):
            try:
             result = result.replace("%s" , str(vars[count]) , 1)
            except IndexError:
             raise(LessArgsException("Please provide arguements to printf()."))
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "f"):
            try:
                result = result.replace("%f" , str(float(vars[count])) , 1)
            except:
                raise(LessArgsException("Please provide arguements to printf()."))
            count+=1
            char1 = ""
        elif(char1 == "%" and i == "b"):
            try:
             result = result.replace("%b" , str(bool(vars[count])) , 1)
            except IndexError:
             raise(LessArgsException("Please provide arguements to printf()."))
            count+=1
            char1 = ""
    print(result , end="")
    return result
def isdigit(string):
    if str(string).isdigit():
        return True
    else:
        return False
# New functions with extraordinary features
def priint(*ints):
    ints = map(int , ints)
    for i in ints:
        print(i , end=" ")
    print()
def priflo(*floats):
    floats = map(float , floats)
    for i in floats:
        print(i , end=" ")
    print()
def pristr(*strs):
    strs = map(str , strs)
    for i in strs:
        print(i , end=" ")
    print()
def bopen(filename:str , mode:str):
    return open(filename , mode+"b")
def bwrite(file:IO,content:str):
    file.write(content.encode())
def bread(file:IO):
    content = ""
    i:bytes
    for i in file:
        content+=i.decode()
    return content