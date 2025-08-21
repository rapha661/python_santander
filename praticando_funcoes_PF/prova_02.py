def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # TODO: Crie o processamento das reservas:
    confirmadas = []
    recusadas = []
    for solicitacao in reservas_solicitadas:
        if solicitacao in quartos_disponiveis:
            confirmadas.append(solicitacao)
            quartos_disponiveis.remove(solicitacao)
        else:
            recusadas.append(solicitacao)
            
    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()