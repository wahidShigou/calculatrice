A = float(input("saisir la valeur de A :"))
op = (input("saisir l'operateur :"))
B = float(input("saisir la valeur de B :"))
if op =="+" :
    print("A + B =", A+B)
elif op =="-" :
    print("A - B =", A-B)
elif op =="/" :
    if B != 0 :
        print("A / B =", A/B)
    else:
        print("la division par 0 est impossible")
elif op =="*" :
    print("A * B =", A*B)
else :
    print("l'operateur est incorrect")