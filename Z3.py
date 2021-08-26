import re


regex = "^A[a-z]*[0-5]+ g$"

while 1:
    tekst= input("Unesi tekst: ")
    rezultat = re.findall(regex,tekst)
    if rezultat:
        break
print("Doslo je do podudaranja.")
    
