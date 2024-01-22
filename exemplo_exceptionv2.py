import logging

logging.basicConfig(filename="logApp.log", level=logging.DEBUG)

def calculoValores(num1, num2):
    try:
        resultado = num1/num2
    except ZeroDivisionError:
        logging.exception("Problema na divisão dos numeros por zero")
        print("erro de processamento, tente um divisor diferente de zero.")
    else:
        return resultado


x = int(input("Digite o primeiro numero"))

y = int(input("Digite o segundo numero"))

print(calculoValores(x, y))