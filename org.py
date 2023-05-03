import os
import glob
lst = []
ruta = "/Users/Einar/Downloads/"
files = glob.glob("" + ruta + "*.*")
print(files)


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
    u = cadena.split("\\")
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
                #print("ya existe")
                if z == "INI":
                    print()
                else:
                    try:
                        os.rename((ruta+splitear2(x)), (ruta+z+"/"+splitear2(x)))
                    except:
                        print("owo")
            else:
                
                os.makedirs((ruta +z), exist_ok=True)
                lst.append(z)
                for y in files:
                    if splitear(splitear2(y)).upper() == z:
                        os.rename((ruta+splitear2(y)), (ruta+z+"/"+splitear2(y)))
                        #print("que onda")
                    else:
                        print()
dirs()

