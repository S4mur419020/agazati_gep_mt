import random

lista = []
i = 0
print("\n 2. feladat")
while i<15:
    rszam:int = int(random.randint(-90,500))
    lista.append(rszam)
    i+=1



def masodik_feladat():
    print("II/A, B, C: ")
    index = 0
    while index < len(lista):
        if index < 14:
            print(f"\t{lista[index]}",end="*")
        else:
            print(f"{lista[index]}",end=" ")
        index += 1




def oszthatoak_szama():
    print("\nII/D,E")
    index = 0
    eredmeny = 0
    while index < len(lista):
        if lista[index] % 10==0:
            eredmeny += 1
        index += 1
    return eredmeny





def fajlba_kiir():
    f = open("kimutatas.txt","w",encoding="utf-8")
    f.write("II/F\n")
    f.write(f"\t Tízzel osztható számok száma:  : {oszthatoak_szama()} ")
    f.close()



def konzolra_kiir():
    print("\n II/F:\n\t",oszthatoak_szama())
    