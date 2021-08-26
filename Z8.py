ime = input("Unesite ime: ")

prvip = lambda ime: "Dobrodosli, " + ime
print(prvip(ime))

def pozdrav(ime):
    return "Lijep pozdrav, " + ime

def pime(pozdrav):
    return pozdrav(ime)

print(pime(pozdrav))
