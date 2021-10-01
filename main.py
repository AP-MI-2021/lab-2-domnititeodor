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
    Combinarile de n luate cate k, numar natural
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

def main():
    while True:
        print("Alege o problema: ")
        print("1.Determină dacă un număr dat este palindrom")
        print("2.Combinari de n luate cate k")
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
        elif nr=='x':
            break
        else:
            print("Optiune invalida")

test_is_palindrome()
test_get_n_choose_k()
main()