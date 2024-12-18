def AB():
    print("I/A:")
    nev:str=str(input("Múzeum neve: "))
    latogato:str=str(input("Látogató neve: "))
    ertek:int=int(input("Értékrlés (1-20): "))
    
    print("I/B:")    
    if ertek<0:
        print("Az értékelés nem lehet negatív vagy 0!")
    elif ertek==0:
        print("Az értékelés nem lehet negatív vagy 0!")
    elif ertek>20:
        print("20 pont feletti értékelés nem elfogadható!") 
    else:
        print("Köszönjük az értékelést!")