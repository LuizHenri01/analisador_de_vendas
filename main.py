import csv

def processar_linha(linha):
    if linha["produto"] == "":
        print("Erro: produto vazio")
        return None # sem venda valida a partir desse registro

    try:
        linha["valor"] = int(linha["valor"])
        return linha

    except ValueError:
        print(
            f"Erro ao processar produto: {linha['produto']} "
            f"| Valor recebido: {linha['valor']}"
        )
        return None


def carregar_vendas():
    vendas = []
    erros = 0

    with open("vendas.csv", mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            venda = processar_linha(linha)

            if venda is None:
                erros += 1
                continue

            vendas.append(venda)

    return vendas, erros


def calcular_faturamento(vendas):
    total = 0

    for venda in vendas:
        total += venda["valor"]

    return total


def encontrar_maior_venda(vendas):
    maior_venda = vendas[0]["valor"]

    for venda in vendas:
        if venda["valor"] > maior_venda:
            maior_venda = venda["valor"]

    return maior_venda


def encontrar_menor_venda(vendas):
    menor_venda = vendas[0]["valor"]

    for venda in vendas:
        if venda["valor"] < menor_venda:
            menor_venda = venda["valor"]

    return menor_venda


def encontrar_produto_maior_venda(vendas):
    maior_venda = vendas[0]["valor"]
    produto_maior_venda = vendas[0]["produto"]

    for venda in vendas:
        if venda["valor"] > maior_venda:
            maior_venda = venda["valor"]
            produto_maior_venda = venda["produto"]

    return produto_maior_venda, maior_venda


def encontrar_produto_menor_venda(vendas):
    menor_venda = vendas[0]["valor"]
    produto_menor_venda = vendas[0]["produto"]

    for venda in vendas:
        if venda["valor"] < menor_venda:
            menor_venda = venda["valor"]
            produto_menor_venda = venda["produto"]

    return produto_menor_venda, menor_venda


def calcular_ticket_medio(vendas):
    total = calcular_faturamento(vendas)
    quantidade_vendas = len(vendas)

    return total / quantidade_vendas


# Carregamento dos dados
vendas, erros = carregar_vendas()

# Análises
faturamento = calcular_faturamento(vendas)
quantidade_vendas = len(vendas)
ticket_medio = calcular_ticket_medio(vendas)

maior_venda = encontrar_maior_venda(vendas)
menor_venda = encontrar_menor_venda(vendas)

produto_maior, valor_maior = encontrar_produto_maior_venda(vendas)
produto_menor, valor_menor = encontrar_produto_menor_venda(vendas)


# Resultados
print(f"Faturamento total: R$ {faturamento}")
print(f"Quantidade de vendas: {quantidade_vendas}")
print(f"Ticket médio: R$ {ticket_medio:.2f}")
print(f"Maior venda: R$ {maior_venda}")
print(f"Menor venda: R$ {menor_venda}")
print(f"Produto com maior venda: {produto_maior} - R$ {valor_maior}")
print(f"Produto com menor venda: {produto_menor} - R$ {valor_menor}")
print(f"Registros inválidos: {erros}")