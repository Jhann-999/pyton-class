def mcd(a,b):
    print(f"Trabajamos con {a} y {b}")
    if b == 0:
        print(f"b=0, MCD es {a}")
        return a
    else:
        resto = a % b
        print(f"{a}%{b}={resto} ... Llamamos MCD({b},{resto})")
        return mcd(b,resto)
r = mcd(8,12)
print(f"El MCD es: {r}")