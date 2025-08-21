# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def definicao_prioridade(paciente):
    nome, idade, status = paciente

    if status == "urgente":
        return (0,-idade)
    elif idade >= 60:
        return (1,-idade)
    else:
        return (2,-idade)

pacientes_ordenados = sorted(pacientes, key=definicao_prioridade)

# TODO: Exiba a ordem de atendimento com título e vírgulas:
print("Ordem de Atendimento: ",", ".join([p[0] for p in pacientes_ordenados])) 
