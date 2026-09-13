import csv
import pandas as pd


def processar_linha(linha):
    if linha["produto"] == "":
        print("Erro: produto vazio")
        return None

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


def calcular_faturamento(df):
    return df["valor"].sum()


def calcular_ticket_medio(df):
    total = calcular_faturamento(df)
    quantidade_vendas = len(df)

    return total / quantidade_vendas


def encontrar_maior_venda(df):
    indice = df["valor"].idxmax()

    return df.loc[indice, "valor"]


def encontrar_menor_venda(df):
    indice = df["valor"].idxmin()

    return df.loc[indice, "valor"]


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


# Carregamento dos dados
vendas, erros = carregar_vendas()

# Criação do DataFrame
df = pd.DataFrame(vendas)

# Análises
faturamento = calcular_faturamento(df)
quantidade_vendas = len(df)
ticket_medio = calcular_ticket_medio(df)

maior_venda = encontrar_maior_venda(df)
menor_venda = encontrar_menor_venda(df)

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