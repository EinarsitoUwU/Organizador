import os
import glob
import sqlite3
#W
j="\\"
#W
with open("./ruta.txt") as archivo:
    v = archivo.readlines()
with open("./ignore.txt") as archivo:
        p = archivo.readlines()
def connection():
    con = sqlite3.connect("ficheros.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE files(folder string)")
    
def ignore(lista):
    cf=0
    for x in lista:
        a = x.upper().strip()
        lista[cf]=a
        cf=cf+1
    return lista
def compro(str):
    kl = ignore(p)
    lista = kl
    c = str
    alfa = False
    for x in lista:
        if x == c:
            print("si hay")
            alfa = True
        else:
            print("no hay")
            print(x)
    return alfa

def splitear(cadena):
    u = cadena.split(".")
    a = u[1]
    if a == None:
        return cadena
    else:
        return a
def extensions():
    for x in files:
        extension = splitear(x)
        print(extension)
        return extension
def splitear2(cadena):
    #W
    u = cadena.split(j)
    #W
    a = u[1]
    if a == None:
        return cadena
    else:
        return a
def dirs():

    for x in files:
            
            global z
            u = splitear(x)
            z = u.upper()
            print(z)
            test = os.path.exists(ruta+z)
            
            if  test == True or z == "INI":
                
                if compro(z) == True or z == "INI":
                    print("Cancel")
                else:
                    print("move")
                    try:
                        os.rename((ruta+splitear2(x)), (ruta+z+"/"+splitear2(x)))
                    except:
                        print("owo")
            else:

                os.makedirs((ruta +z), exist_ok=True)
                for y in files:
                    if splitear(splitear2(y)).upper() == z:
                        os.rename((ruta+splitear2(y)), (ruta+z+"/"+splitear2(y)))
                        #print("que onda")
                    else:
                        print()
count=0

for k in v:
    ruta = k.strip()
    #W
    ruta=ruta.replace(j, '/')
    #W
    print(ruta)
    files = glob.glob("" + ruta + "*.*")
    print(files)

    dirs()
connection()
exit()
