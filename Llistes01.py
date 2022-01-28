def capicua(paraula):

    j = len(paraula)-1
    r = True

    for i in paraula:
        if i != paraula[j]:
            r = False 
        j-= -1
    return r

def printCapicua(paraula):
    print("La paraula", paraula,end=" ")
    if (capicua(paraula)):
        print("Es capicua")
    else:
        print("No es capicua")
    return True
