"""
Informe o número da turma: 
Turma - 93313

Nome completo dos componentes.
1 - Heloisa Lima de Oliveira
2 - júlia Vitória dos Santos Azevedo Jesus
3 - Fábio De Carvalho Neves
"""
#adicionando variaveis
idade = []
salario = []
sexo = []
pessoas = []

while True:
    print("Menu:")
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados e sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        idade = int(input("Informe a idade: "))
        sexo = input("Informe o sexo (M/F): ").upper()
        salario = float(input("Informe o salário: "))
        pessoas.append((idade, sexo, salario))

    elif opcao == "2":
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
            break

        total_salario = sum(s for _, _, s in pessoas)
        media_salario = total_salario / len(pessoas)

        idades = [i for i in pessoas]
        maior_idade = max(idades)
        menor_idade = min(idades)

        mulheres_alto_salario = sum(1 for _, s, _ in pessoas if s == 'F' and _ >= 5000)

        print(f"Média de salário: R$ {media_salario:.2f}")
        print(f"Maior idade: {maior_idade} anos")
        print(f"Menor idade: {menor_idade} anos")
        print(f"Mulheres com salário ≥ R$ 5.000: {mulheres_alto_salario}")

        break
    else:
        print("Opção inválida. Tente novamente.")
