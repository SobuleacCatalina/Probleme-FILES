with open("input.txt","r") as f:
    sir=f.readline()
nrma=0
nrmi=0
nr=0
ns=0
for i in sir:
    if ord(i) in range(65,91):
        nrma+=1
with open("litereA.txt","w") as f:
    f.write(str(nrma))
for i in sir:
    if ord(i) in range(97,123):
        nrmi+=1
with open("litereB.txt","w") as f:
    f.write(str(nrmi))
for i in sir:
    if ord(i) in range(49,58):
        nr+=1
with open("cifre.txt","w") as f:
    f.write(str(nr))
for i in sir:
    if ord(i) in range(33,42):
        ns+=1
with open("caractere.txt","w") as f:
    f.write(str(ns))