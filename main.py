def menu():
    print("1.citire lista")
    print("2.Afisare nr prime")
    print("3.Iesire")
def citirelista():
    l=[]
    n=int(input("Dati nr de elemente: "))
    for i in range(n):
        l.append(int(input("l["+ str(i)+"]=")))
    return l
def is_prime(n):
    if n<2:
      return False
    if n==2:
      return True
    for i in range(2,n//2+1):
      if n%i==0:
        return False
    return True
def test_is_prime():
    assert is_prime(2)==True
    assert is_prime(3)==True
    assert is_prime(4)==False
def ToatenrPrime(l):
    '''
    determina toate nr prime dintr o lista
    :param l: lista de numere intregi
    :return: o lista continanand elementele prime din l
    '''
    rezultat=[]
    for x in l:
        if is_prime(x):
            rezultat.append(x)
    return rezultat
def testToatenrPrime():
    assert ToatenrPrime([1,2,3])==[2,3]
    assert ToatenrPrime([])==[]

def main():
    test_is_prime()
    testToatenrPrime()
    l=[]
    while True:
        menu()
        optiune=input("Dati optiunea de la utilizator: ")
        if optiune=="1":
            l=citirelista()
        elif optiune=="2":
            print(ToatenrPrime(l))
        elif optiune=="3":
            break
        else:
            print("Optiune gresita.")

main()