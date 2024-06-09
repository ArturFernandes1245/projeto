def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# IA de Perda de Gordura
def calcular_peso_ideal_min(altura):
    imc_ideal_min = 18.5
    peso_ideal_min = imc_ideal_min * (altura ** 2)
    return peso_ideal_min

def calcular_peso_ideal_max(altura):
    imc_ideal_max = 24.9
    peso_ideal_max = imc_ideal_max * (altura ** 2)
    return peso_ideal_max

def sugestao_refeicoes_perda_peso():
    sugestoes = [
        "Café da manhã: Aveia com frutas e iogurte natural",
        "Almoço: Salada de quinoa com legumes e peito de frango grelhado",
        "Lanche: Cenouras baby com homus",
        "Jantar: Peixe grelhado com vegetais no vapor",
        "Sobremesa: Frutas frescas"
    ]
    return "\n".join(sugestoes)

def sugestao_exercicios_casa():
    sugestoes = [
        "Exercício 1: Polichinelos - 3 séries de 30 segundos",
        "Exercício 2: Agachamentos - 3 séries de 15 repetições",
        "Exercício 3: Flexões - 3 séries de 10 repetições",
        "Exercício 4: Abdominais - 3 séries de 20 repetições",
        "Exercício 5: Prancha - 3 séries de 30 segundos"
    ]
    return "\n".join(sugestoes)

def aconselhamento_perda_gordura(peso, altura):
    if peso <= 0 or altura <= 0:
        return "Peso e altura devem ser valores positivos e maiores que zero."

    imc_atual = calcular_imc(peso, altura)
    peso_ideal_min = calcular_peso_ideal_min(altura)
    peso_ideal_max = calcular_peso_ideal_max(altura)
    
    if imc_atual < 18.5:
        peso_a_ganhar = peso_ideal_min - peso
        return f"Você está abaixo do peso. Para alcançar um IMC saudável, você precisa ganhar aproximadamente {peso_a_ganhar:.2f} kg. Consulte um profissional de saúde."
    elif 18.5 <= imc_atual <= 24.9:
        return "Seu peso está normal. Mantenha um estilo de vida saudável."
    else:
        peso_a_perder = peso - peso_ideal_max
        semanas_necessarias = peso_a_perder / 0.5  # Supondo perda de 0.5 kg por semana
        sugestoes_refeicoes = sugestao_refeicoes_perda_peso()
        sugestoes_exercicios = sugestao_exercicios_casa()
        return (f"Para alcançar um IMC saudável, você precisa perder aproximadamente {peso_a_perder:.2f} kg. "
                f"Recomenda-se perder peso gradualmente, cerca de 0.5 kg por semana, o que levaria aproximadamente "
                f"{semanas_necessarias:.1f} semanas. Consulte um profissional de saúde para um plano personalizado.\n\n"
                f"Sugestão de refeições saudáveis para ajudar na perda de peso:\n{sugestoes_refeicoes}\n\n"
                f"Sugestão de exercícios para fazer em casa:\n{sugestoes_exercicios}")

def main():
    try:
        peso = float(input("Digite o seu peso (kg): "))
        altura = float(input("Digite a sua altura (m): "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        print(aconselhamento_perda_gordura(peso, altura))
    except ValueError:
        print("Por favor, insira valores numéricos válidos para peso e altura.")

if __name__ == "__main__":
    main()
