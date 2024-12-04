def CheckDuplicate(id):
    if id.isalpha():
        if id.islower():
            if len(id) <=50:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

id = input()
result = CheckDuplicate(id)
if result:
    print(id + "??!")