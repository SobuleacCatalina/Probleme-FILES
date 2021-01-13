"""
Se dau două numere. Să se înmulţească cel mai mare cu doi şi cel mai mic cu trei şi să se afişeze rezultatele. 
Exemplu : date de intrare « numere.txt »: 3  7  date de ieşire « produs.txt »: 9  14
"""
with open("numere.txt","r") as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    p1=int(a)*2
    p2=int(b)*3
elif int(b)>int(a):
    p2=int(a)*2
    p1=int(b)*3
else:
    p1=p2="Sunt numere egale"
with open("produs.txt","w") as f: 
    f.write(str(p1)+" "+str(p2))   