def funcao(num):
    result = (1/2.718**num) - (2*num**2) + 4
    return result

def valores ():
    while True:
        F_de_A = int(input("Digite o primeiro numero real: "))
        F_de_B = int(input("Digite o segundo numero real: "))

        totalA = funcao(F_de_A)
        totalB = funcao(F_de_B)

        multiplicaçãoDosTotais = totalA * totalB

        
        print("Equação utilizada: e(-x) - 2x² + 4 = 0\n")
        print(f"f(A) = {totalA:.2f}")
        print(f"f(B) = {totalB:.2f}\n")

        if multiplicaçãoDosTotais > 0:
            print("-- não é possível afirmar que existe solução neste intervalo, tente outros dois números --")
        
        elif multiplicaçãoDosTotais < 0:
            while True:
                soma = (F_de_A + F_de_B)/2
                if funcao(F_de_A) * funcao(soma) < 0:
                    F_de_B = soma
                    if F_de_B - F_de_A <= 0.1:
                        print(f"intervalo: [{F_de_A},{F_de_B}]")
                        break

                elif funcao(F_de_B) * funcao(soma) < 0:
                    F_de_A = soma
                    if F_de_A * F_de_B <= 0.1:
                        print(f"intervalo: [{F_de_A},{F_de_B}]")
                        break
            break
valores()