f=open('test_configuratie.txt')
n=int(f.readline()) # numarul de stari
m=int(f.readline()) # numarul de caractere din alfabet
l_litere=f.readline().split() # alfabetul
initiala=int(f.readline()) # stare initiala
k=int(f.readline()) # numarul de stari finale
l_finale=[int(element) for element in f.readline().split()] # lista starilor finale


dex=dict([])  # in dex[inceput] vom pune translatiile (litera, destinatie)
for i in range(n):
    dex[i]=[]

l=int(f.readline()) # numarul de translatatii
for linie in f:
    linie=linie.split()
    linie[0]=int(linie[0])
    linie[2]=int(linie[2])
    dex[linie[0]].append(tuple([linie[1],linie[2]]))
f.close()
# am terminat de citit datele

def parsare(cuvant,stare_curenta,verificare_parcurs):
    ok=0
    if len(cuvant)==0:
        if stare_curenta in l_finale:
            ok=1
        else: # Caz pentru '', dar mai avem translatatii lambda
            for i in dex[stare_curenta]:
                if i[0] == '$' and verificare_parcurs[i[1]] == 0:
                    verificare_parcurs[stare_curenta] = 1
                    stare_curenta = i[1]
                    ok = parsare(cuvant, stare_curenta, verificare_parcurs)
        return ok
    else:
        for i in dex[stare_curenta]:
            if ok == 1:
                break
            if i[0]=='$' and verificare_parcurs[i[1]]==0 :
                verificare_parcurs[stare_curenta]=1
                stare_curenta=i[1]
                ok=parsare(cuvant,stare_curenta,verificare_parcurs)
            else:
                if i[0]==cuvant[0]:
                    verificare_parcurs=[0 for i in range(n)]
                    stare_curenta=i[1]
                    ok=parsare(cuvant[1:],stare_curenta,verificare_parcurs)
    return ok

f=open("test_cuvinte.txt")
for linie in f:
    linie=linie.strip()
    v=[0 for i in range(n)]
    print(linie+' '+str(parsare(linie,initiala,v)))
f.close()