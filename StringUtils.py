 # Checks if a String is None
def isNone(str):
    if str == None:
        return True
    else:
        return False

 # Checks if a String is Empty
def isEmpty(str):
    if str == "":
        return True
    else:
        return False

 # Checks if a String is whitespace or Empty
def isBlank(str):
    if str == None or str == "":
        if str == None:
            return False
        return True
    else:
        if str.strip() == "":
            return True
        return False

# Checks if a String is empty ("") or None
def isNoneOrEmpty(str):
    if str == None or str == "":
        return True
    else:
        return False

# Checks if a String is whitespace, empty ("") or None.
def isNoneOrBlank(str):
    if str == None or str == "" or str.strip() == "":
        return True
    else:
        return False

if __name__ == '__main__':
    myteststring = " "
    print(isNone(myteststring))
    print(isEmpty(myteststring))
    print(isBlank(myteststring))
    print(isNoneOrEmpty(myteststring))
    print(isNoneOrBlank(myteststring))
