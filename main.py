import math
def is_palindrome(n):
    '''
    Determina daca un numar este palindrom(numar care scris invers este egal cu el insusi) sau nu
    Input: 
    n, numar intreg, n >= 0
    Output:
    True, n palindrom
    False, n nepalindrom
    '''

    copie=n
    oglindit=0
    while(n!=0):
        oglindit=oglindit*10 + n%10
        n=n//10
    if(copie==oglindit):
        return True
    return False

def test_is_palindrome():
    assert is_palindrome(202)==True
    assert is_palindrome(23)==False
    assert is_palindrome(100)==False
    assert is_palindrome(7637)==False
    assert is_palindrome(1)==True

def get_n_choose_k(n,k):
    '''
    Calculeaza combinari de n luate cate k
    Input: 
    n, k numere naturale, 0 <= k <= n
    Output:
    O lista de patrate perfecte care satisfac relatia: a <= pp si pp <= b
    '''

    i=1
    nfact=1
    while i<=n:
        nfact=nfact*i
        i=i+1
    i=1
    kfact=1
    while i<=k:
        kfact=kfact*i
        i=i+1
    i=1
    nkfact=1
    while i<=n-k:
        nkfact=nkfact*i
        i=i+1
    return nfact//(kfact*nkfact)

def test_get_n_choose_k():
    assert get_n_choose_k(6,4)==15
    assert get_n_choose_k(10,8)==45
    assert get_n_choose_k(10,0)==1

def get_perfect_squares(start, end):
    """
    Determina patratele perfecte din intervalul inchis dat
    Input:
    start, end - numere intregi, start,end >=0 (capetele intervalului inchis)
    Output:
    Lista patratele perfecte care satisfac relatia: start <= pp <= end
    """
    lst=[]
    for x in range(start, end+1):
        if(math.sqrt(x)==int(math.sqrt(x))):
            lst.append(x)
    return lst

def test_get_perfect_squares():
    assert get_perfect_squares(1,10)==[1,4,9]
    assert get_perfect_squares(10,25)==[16,25]
    assert get_perfect_squares(1,100)==[1,4,9,16,25,36,49,64,81,100]
    assert get_perfect_squares(2,3)==[]

def main():
    while True:
        print("Alege o problema: ")
        print("1.Determină dacă un număr dat este palindrom")
        print("2.Combinari de n luate cate k")
        print("3.Afiseaza toate patratele perfecte dintr-un interval inchis dat")
        print("x.Exit")
        nr=input()
        if nr=='1':
            n=int(input("Introdu numarul n: "))
            if(is_palindrome(n)):
                print(f"Numarul {n} este palindrom")
            else:
                print(f"Numarul {n} nu este palindrom")
        elif nr=='2':
            n=int(input("Introdu valoarea n: "))
            k=int(input("Introdu valoarea k: "))
            print(f"Sunt {get_n_choose_k(n,k)} combinari de n luate cate k")
        elif nr=='3':
            start=int(input("Introdu capatul stang: "))
            end=int(input("Introduce capatul drept: "))
            pp=get_perfect_squares(start,end)
            if len(pp)!=0:
                print(f"Patratele perfecte din intervalul [{start},{end}] sunt: {pp}")
            else:
                print(f"Nu exista patrate perfecte in intervalul [{start},{end}]")
        elif nr=='x':
            break
        else:
            print("Optiune invalida")

test_is_palindrome()
test_get_n_choose_k()
test_get_perfect_squares()
main()