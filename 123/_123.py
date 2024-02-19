from string import *  
from random import *
  #3
#while True:
#    sym=input("Mis simbol kasutame?")
#    if sym in punctuation: 
#        break
#    else:
#        print("Saab kasutada ainult: !#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ")
#while True:
#    try:
#        N=int(input("Ridade arv: "))
#        break
#    except TypeError:
#        print("Ainult täisarvud")
#for i in range(N):
#    print(randint(1,50)*sym)
#    #print(sym.ljust(randint(1,50),sym))

 #4
Indeksid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]

while True:
    indeks=input("Indeks: ")
    if len(indeks)==5 and indeks.isdigit():
        break
    else:
        print("Ainult 5 numbriline arv saab konytollida!")

print(indeks,"kasutatakse",Indeksid[int(indeks[0])-1],"piirkonnas")
if int(indeks[0])-1 in [1,2,3]:
    pass
else:
    pass