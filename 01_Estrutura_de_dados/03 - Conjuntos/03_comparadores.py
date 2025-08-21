conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado_uniao = conjunto_a.union(conjunto_b)
print(resultado_uniao)

resultado_interseccao = conjunto_a.intersection(conjunto_b)
print(resultado_interseccao)

resultado_diferenca_a = conjunto_a.difference(conjunto_b)
print(resultado_diferenca_a)

resultado_diferenca_b = conjunto_b.difference(conjunto_a)
print(resultado_diferenca_b)

resultado_diferenca_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(resultado_diferenca_simetrica)