# calculadora_saude.py

def calcular_imc(peso, altura):
    # Correção Bug 1: potenciação (altura ** 2), não multiplicação por 2
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    # Correção Bug 2: faixas contínuas com >= / <=, sem sobreposição nem "buracos"
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidade"

def calcular_agua_diaria(peso):
    # Correção Bug 3: 35ml por kg de peso -> multiplicar, não dividir
    litros = peso * 0.035
    return litros

def calcular_frequencia_cardiaca_maxima(idade):
    # Correção Bug 4: fórmula é 220 - idade, não soma
    fc_max = 220 - idade
    return fc_max

def menu():
    print("\n" + "="*30)
    print(" SISTEMA DE SAÚDE E BEM-ESTAR ")
    print("="*30)
    print("1. Calcular IMC")
    print("2. Calcular Recomendação de Água")
    print("3. Calcular Frequência Cardíaca Máxima")
    print("4. Sair")
    # Correção Bug 5: converte a entrada para int direto no menu,
    # com tratamento de erro caso o usuário digite algo não numérico
    entrada = input("Escolha uma opção (1-4): ")
    try:
        opcao = int(entrada)
    except ValueError:
        opcao = -1  # valor inválido garante que caia no "else" do main()
    return opcao

def main():
    while True:
        opcao = menu()

        # Correção Bug 6: agora funciona porque 'opcao' já é int
        if opcao == 1:
            peso = float(input("Digite seu peso (kg): "))
            altura = float(input("Digite sua altura (m): "))
            imc = calcular_imc(peso, altura)
            print(f"Seu IMC é: {imc:.2f}")
            print(f"Classificação: {classificar_imc(imc)}")
        elif opcao == 2:
            peso = float(input("Digite seu peso (kg): "))
            qtd_agua = calcular_agua_diaria(peso)
            print(f"Sua meta diária de água é: {qtd_agua:.2f} Litros")
        elif opcao == 3:
            idade = int(input("Digite sua idade: "))
            fc = calcular_frequencia_cardiaca_maxima(idade)
            print(f"Sua Frequência Cardíaca Máxima estimada é: {fc} bpm")
        elif opcao == 4:
            print("Encerrando o sistema...")
            print("Obrigado por usar nosso sistema!")
            break  # Correção Bug 7: sai do loop infinito
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
