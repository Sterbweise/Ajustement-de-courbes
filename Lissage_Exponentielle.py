def y():
    print("Entrer le nombre de variable dans la serie")
    ini = int(input())
    y = [0]*ini
    
    for i in range(0,ini,1):
        print("Valeur de y"+str(i+1)+" :")
        y[i] = float(input())
    return y

def Gamma():
    print("Entrer la valeur de Gamma")
    e = float(input())
    if (e >= 0 and e <= 1):
        return e
    else:
        print("Gamma n'est pas compris entre 0 et 1")
        return Gamma()
    
def lissage_expo(y,e):
    z = [0]*len(y)
    z[0] = (1/3)*(y[0]+y[1]+y[2])
    for i in range(1,len(y),1):
        z[i] = e*y[i]+(1-e)*z[i-1]

    for j in range(0,len(z),1):
        print ("Z"+str(j+1)+" = " + str(z[j]))

lissage_expo(y(),Gamma())