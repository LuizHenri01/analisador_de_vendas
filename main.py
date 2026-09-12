vendas = [
    {"produto": "Notebook", "valor": 3500},
    {"produto": "Mouse", "valor": 120},
    {"produto": "Teclado", "valor": 250},
    {"produto": "Monitor", "valor": 1200},
    {"produto": "Headset", "valor": 300}
]


# Calcula o faturamento total
def calcular_faturamento(vendas):

    total = 0

    for venda in vendas:
        total += venda["valor"]

    return total


# Encontra a maior venda
def encontrar_maior_venda(vendas):

    maior_venda = vendas[0]["valor"]

    for venda in vendas:
        if venda["valor"] > maior_venda:
            maior_venda = venda["valor"]

    return maior_venda


# Encontra a menor venda
def encontrar_menor_venda(vendas):

    menor_venda = vendas[0]["valor"]

    for venda in vendas:
        if venda["valor"] < menor_venda:
            menor_venda = venda["valor"]

    return menor_venda


# Encontra o produto com a maior venda
def encontrar_produto_maior_venda(vendas):

    maior_venda = vendas[0]["valor"]
    produto_maior_venda = vendas[0]["produto"]

    for venda in vendas:
        if venda["valor"] > maior_venda:
            maior_venda = venda["valor"]
            produto_maior_venda = venda["produto"]

    return produto_maior_venda, maior_venda


# Encontra o produto com a menor venda
def encontrar_produto_menor_venda(vendas):

    menor_venda = vendas[0]["valor"]
    produto_menor_venda = vendas[0]["produto"]

    for venda in vendas:
        if venda["valor"] < menor_venda:
            menor_venda = venda["valor"]
            produto_menor_venda = venda["produto"]

    return produto_menor_venda, menor_venda


# Calcula o faturamento
total = calcular_faturamento(vendas)

# Calcula a quantidade de vendas
qntd_vendas = len(vendas)

# Calcula o ticket médio
ticket_medio = total / qntd_vendas

# Encontra a maior venda
maior_venda = encontrar_maior_venda(vendas)

# Encontra a menor venda
menor_venda = encontrar_menor_venda(vendas)

# Encontra produto e valor da maior venda
produto_maior_venda, valor_maior_venda = encontrar_produto_maior_venda(vendas)

# Encontra produto e valor da menor venda
produto_menor_venda, valor_menor_venda = encontrar_produto_menor_venda(vendas)


# Exibe os resultados
print(f"Faturamento total: R$ {total}")
print(f"Quantidade de vendas: {qntd_vendas}")
print(f"Ticket médio: R$ {ticket_medio:.2f}")
print(f"Maior venda: R$ {maior_venda}")
print(f"Menor venda: R$ {menor_venda}")
print(f"Produto com maior venda: {produto_maior_venda} - R$ {valor_maior_venda}")
print(f"Produto com menor venda: {produto_menor_venda} - R$ {valor_menor_venda}")