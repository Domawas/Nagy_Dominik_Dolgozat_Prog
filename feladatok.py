import random
def elso_feladat():
    szam1 = int(input("Kérek egy páros számot: "))
    
    while szam1 % 2 != 0: 
        print(f"Ez nem páros! PÁROS számot kérek! {szam1}")
        szam1 = int(input("Kérek egy páros számot: "))  
    
    print(szam1)

def masodik():
    szamok=[]
    i=0
    igen=0
    oszthato=0
    while (i < 13):
        szam=int(random.random()*140)+10
        szamok.append(szam)
        i+=1
    
    print(szamok)
    while igen<13:
        if szamok[igen]%3==0:
            oszthato+=1
        igen+=1
    print(f"{oszthato}db 3-mal osztható")


def harmadik(text,n):
    text=text.upper()
    if (len(text))<n:
        print(f"Nincs {n}. karakter")
    print(text[{n}]*3)



def negyedik():
    i = 0
    nevek=[]
    print("Kérem, adjon meg neveket! (A kilépéshez írjon '@' jelet)")
    nev = input("Adj meg egy nevet (vagy @ a kilépéshez): ")
    while nev != '@':
        nev = input("Adj meg egy nevet (vagy @ a kilépéshez): ")
        if nev=='@':
            print(f"A felhasználó {i} nevet adott meg.")
            return nevek

        i += 1
        nevek.append(nev)
        











