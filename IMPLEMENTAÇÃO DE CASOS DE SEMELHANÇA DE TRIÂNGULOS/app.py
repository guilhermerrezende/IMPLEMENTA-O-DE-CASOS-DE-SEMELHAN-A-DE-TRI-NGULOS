def verifica_LAL(lado1_triang1, angulo_triang1, lado2_triang1, lado1_triang2, angulo_triang2, lado2_triang2):
    if angulo_triang1 == angulo_triang2:
        proporcao1 = lado1_triang1 / lado1_triang2
        proporcao2 = lado2_triang1 / lado2_triang2
        return proporcao1 == proporcao2
    return False

def verifica_AA(angulo1_triang1, angulo2_triang1, angulo1_triang2, angulo2_triang2):
    return (angulo1_triang1 == angulo1_triang2 and angulo2_triang1 == angulo2_triang2) or \
           (angulo1_triang1 == angulo2_triang2 and angulo2_triang1 == angulo1_triang2)

def verifica_LLL(lado1_triang1, lado2_triang1, lado3_triang1, lado1_triang2, lado2_triang2, lado3_triang2):
    proporcao1 = lado1_triang1 / lado1_triang2
    proporcao2 = lado2_triang1 / lado2_triang2
    proporcao3 = lado3_triang1 / lado3_triang2
    return proporcao1 == proporcao2 == proporcao3

def verifica_semelhanca(triangulo1, triangulo2, tipo):
    if tipo == "LAL" and verifica_LAL(*triangulo1, *triangulo2):
        return "Triângulos semelhantes pelo critério LAL"
    elif tipo == "AA" and verifica_AA(*triangulo1, *triangulo2):
        return "Triângulos semelhantes pelo critério AA"
    elif tipo == "LLL" and verifica_LLL(*triangulo1, *triangulo2):
        return "Triângulos semelhantes pelo critério LLL"
    else:
        return "Triângulos não são semelhantes"

# Função para obter os dados de entrada do usuário
def obter_dados_triangulo(tipo):
    if tipo == "LAL":
        lado1 = float(input("Informe o primeiro lado do triângulo: "))
        angulo = float(input("Informe o ângulo entre os lados (em graus): "))
        lado2 = float(input("Informe o segundo lado do triângulo: "))
        return (lado1, angulo, lado2)
    
    elif tipo == "AA":
        angulo1 = float(input("Informe o primeiro ângulo do triângulo (em graus): "))
        angulo2 = float(input("Informe o segundo ângulo do triângulo (em graus): "))
        return (angulo1, angulo2)
    
    elif tipo == "LLL":
        lado1 = float(input("Informe o primeiro lado do triângulo: "))
        lado2 = float(input("Informe o segundo lado do triângulo: "))
        lado3 = float(input("Informe o terceiro lado do triângulo: "))
        return (lado1, lado2, lado3)
    
    else:
        print("Critério inválido. Tente novamente.")
        return obter_dados_triangulo(tipo)

# Obter o critério de semelhança do usuário
tipo = input("Escolha o critério de semelhança (LAL, AA, LLL): ").strip().upper()

# Obter dados dos dois triângulos com base no critério escolhido
print("\nInsira os dados do primeiro triângulo:")
triangulo1 = obter_dados_triangulo(tipo)

print("\nInsira os dados do segundo triângulo:")
triangulo2 = obter_dados_triangulo(tipo)

# Verificar semelhança
resultado = verifica_semelhanca(triangulo1, triangulo2, tipo)
print("\nResultado:", resultado)
