matriculas_logica = []
matriculas_linguagem = []

for i in range(10):
    num_matricula = int(input("Digite o número da matrícula do aluno em Lógica: "))
    matriculas_logica.append(num_matricula)

for i in range(8):
    num_matricula = int(input("Digite o número da matrícula do aluno em Linguagem de Programação: "))
    matriculas_linguagem.append(num_matricula)

for matricula in matriculas_linguagem:
    if matriculas_logica.count(matricula) != 0:
        print(matricula)