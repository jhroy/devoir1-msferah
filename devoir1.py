#2020 - Mayssa Ferah
# coding: utf-8

url="https://montrealcampus.ca?p="
#print(url)
l1=list(range(20000,30151))
#print(l1)
#20000 et 30150
#pr chaque film au sing. ds les films au pluriel
urlS= [] 
for nb in l1:
    #print(url+str(nb))
    urlS.append(url+str(nb))
#sortir boucle backspace
print(urlS)
print(len(urlS))