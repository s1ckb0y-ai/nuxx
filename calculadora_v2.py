saida = ""
def adicao(num1,num2):
    resultado = num1 + num2
    return resultado
def subtracao(num1,num2):
    resultado = num1 - num2
    return resultado
def divisao(num1,num2):
    resultado = num1/num2
    if num1 == 0:
        return 0
    elif num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return resultado
def mult(num1,num2):
    resultado = num1*num2
    return resultado
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao == 'mult':
        resultado = mult(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    
    return resultado

while saida.lower() != "nao":
    try:
         num1 = float(input("Digite o primeiro número: "))
         num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Insira apenas numeros.")

    operacao = input("Digite a operação desejada (+, -, *, / ou o nome da operação): ").lower()

    resultado = calculadora(num1, num2, operacao)

    print(f"Resultado da operação: {resultado}")

    saida = input("Deseja continuar? (sim/nao): ").lower()
    
    print("Encerrando programa")
