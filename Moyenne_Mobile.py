def y():
    print("Entrer le nombre de variable dans la serie")
    ini = int(input())
    y = [0]*ini
    
    for i in range(0,ini,1):
        print("Valeur de y"+str(i+1)+" :")
        y[i] = float(input())
    return y

def ordre():
    print("Entrer la moyenne d'ordre")
    ordre = int(input())
    return ordre

def moyenne_mobile(y,ordre):
    m = [0]*(len(y)-(2*ordre))
    for i in range(0,len(m),1):
        for j in range(0,((2*ordre)+1),1):
            m[i] += y[i+j]
    for k in range(0,len(m),1):
        m[k] = (m[k]/((2*ordre)+1))
        print ("M"+str(k+1)+" = " + str(m[k]))
    return m

def residus(m,y,ordre):
    print("Voulez-vous afficher les Residus de la moyenne mobile ? Oui (1) / Non (0)")
    ini = int(input())
    res = [0]*len(m)
    if(ini == 1):
        for i in range(0,len(m),1):
            res[i] = y[i+ordre] - m[i]
            print("e"+str(i+1)+" = " +str(res[i]))
        return res
    else: return

def quantile(r):
    print("Voulez-vous afficher les quantiles des Residus ? Oui (1) / Non (0)")
    ini = int(input())
    if(ini == 1):
            print("Quantile Inf 5% = "+str((len(r)*(5/100)))+"  Quantile Sup 95% = "+str((len(r)*(95/100))))
    else: return

def MSE(r):
    print("Voulez-vous afficher la moyenne des carrés des erreurs (MSE) ? Oui (1) / Non (0)")
    ini = int(input())
    summ = 0
    if(ini == 1):
        for i in range(0,len(r),1):
            summ += r[i]**2
        print( "La moyenne des carrés des erreurs est egale a "+str(summ/len(r)))
    else: 
        print("Fin du Programme")
        return
y=y()
ordre=ordre()
residu = residus(moyenne_mobile(y,ordre),y,ordre)
quantile(residu)
MSE(residu)