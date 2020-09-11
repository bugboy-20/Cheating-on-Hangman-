# TODO: la prima e ultima lettera sono date

def contieneLeVocali(parola):
    vocali=['a','e','i','o','u'];
    for x in range(len(parola)):
        if schema_parola[x]==True:
            if parola[x] not in vocali:
                return False
    return True

def eliminaParoleCon(candidata):
    while True:
        riparti=False
        for parola in parole:
          if candidata in parola:
              parole.remove(parola)
              riparti=True
        if not riparti:
            break

def eliminaParoleCheNonRispettanoLoSchema(schema):
    while True:
        riparti=False
        for parola in parole:
            for x in range(len(schema)):
                if schema[x] != '§' and schema[x] != parola[x]:
                    parole.remove(parola)
                    riparti=True
                    break
        if not riparti:
            break
f=open("parole.txt","rt",encoding="utf8")

schema_parola=[];
parole=[];
lettere={'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
print("Inserisci il numero di lettere")
nLettere=int(input())#perchè dov'essere +1
nLettere+=1
print("Sai dove sono le vocali? [S/N]")
if input().lower() == 's': # OPTIMIZE:
    isVocali = True
    print("scrivi in che posizioni sono le vocali")
    sas=input().split()
    for x in range(nLettere):#è true dovge ci sono le vocali
        schema_parola.append(False)
    for x in sas:
        schema_parola[int(x)]=True


    for parola in f:
        if len(parola)==nLettere and contieneLeVocali(parola):
            parole.append(parola.strip('\n'))
    for x in range(len(schema_parola)):
        schema_parola[x]='§'
    #print(schema_parola)
else:
    for parola in f:
        if len(parola)==nLettere:
            parole.append(parola.strip('\n'))
print(str(len(parole)) + " parole caricate")



while len(parole)>1:
    for lettera in lettere:
        lettere[lettera]=0
    for parola in parole:
        for lettera in lettere:
            if lettera in parola:
                lettere[lettera]+=parola.count(lettera)
    candidata=max(lettere, key=lettere.get)
    print("Contine " + candidata + "? [S/N]")
    if input().lower() == 's':
        print("Dove?")
        sas=input().split()
        for x in sas:
            schema_parola[int(x)]=candidata
        eliminaParoleCheNonRispettanoLoSchema(schema_parola)

    else:
        eliminaParoleCon(candidata)
    print("sono rimaste " + str(len(parole)) + " parole")
    if len(parole) <= 25:
        for parola in parole:
            print(parola)
    lettere.pop(candidata)
#for x in parole:
#    print(x + "di lunghezza " + str(len(x)))
