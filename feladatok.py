
def elso_feladat():
    szam1 = int(input("Kérek egy páros számot: "))
    
    while szam1 % 2 != 0: 
        print(f"Ez nem páros! PÁROS számot kérek! {szam1}")
        szam1 = int(input("Kérek egy páros számot: "))  
    
    print(szam1)

