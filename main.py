import csv
from datetime import datetime

import pandas as pd


def processar_linha(linha):
    if linha["produto"] == "":
        print("Erro: produto vazio")
        return None

    try:
        linha["id"] = int(linha["id"])
        linha["quantidade"] = int(linha["quantidade"])
        linha["valor"] = int(linha["valor"])
        linha["data"] = datetime.strptime(linha["data"], "%Y-%m-%d")

        return linha

    except ValueError:
        print(
            f"Erro ao processar produto: {linha['produto']} "
            f"| Dados inválidos"
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
    return df["faturamento"].sum()


def calcular_ticket_medio(df):
    total = calcular_faturamento(df)
    quantidade_vendas = len(df)

    return total / quantidade_vendas


def encontrar_maior_venda(df):
    indice = df["faturamento"].idxmax()

    produto = df.loc[indice, "produto"]
    valor = df.loc[indice, "faturamento"]

    return produto, valor


def encontrar_menor_venda(df):
    indice = df["faturamento"].idxmin()

    produto = df.loc[indice, "produto"]
    valor = df.loc[indice, "faturamento"]

    return produto, valor


vendas, erros = carregar_vendas()

df = pd.DataFrame(vendas)

# Calcula o faturamento de cada venda
df["faturamento"] = df["quantidade"] * df["valor"]

# Extrai o dia da semana da data
df["dia_semana"] = df["data"].dt.day_name()

# Traduz os dias da semana para português
dias_semana = {
    "Monday": "segunda-feira",
    "Tuesday": "terça-feira",
    "Wednesday": "quarta-feira",
    "Thursday": "quinta-feira",
    "Friday": "sexta-feira",
    "Saturday": "sábado",
    "Sunday": "domingo"
}

df["dia_semana"] = df["dia_semana"].map(dias_semana)

# Define a ordem dos dias da semana
ordem_dias = [
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira",
    "sábado",
    "domingo"
]

df["dia_semana"] = pd.Categorical(
    df["dia_semana"],
    categories=ordem_dias,
    ordered=True
)

# Calcula o resumo geral
faturamento = calcular_faturamento(df)
quantidade_vendas = len(df)
quantidade_unidades = df["quantidade"].sum()
ticket_medio = calcular_ticket_medio(df)

produto_maior, valor_maior = encontrar_maior_venda(df)
produto_menor, valor_menor = encontrar_menor_venda(df)

# Ordena as vendas pelo maior faturamento
vendas_ordenadas = df.sort_values(
    "faturamento",
    ascending=False
)

top_3_vendas = vendas_ordenadas.head(3)

# Agrupa as vendas por produto
resumo_produtos = df.groupby("produto").agg(
    quantidade_vendas=("id", "size"),
    unidades_vendidas=("quantidade", "sum"),
    faturamento=("faturamento", "sum")
)

# Agrupa as vendas por categoria
resumo_categorias = df.groupby("categoria").agg(
    quantidade_vendas=("id", "size"),
    unidades_vendidas=("quantidade", "sum"),
    faturamento=("faturamento", "sum")
)

# Agrupa as vendas por vendedor
resumo_vendedores = df.groupby("vendedor").agg(
    quantidade_vendas=("id", "size"),
    unidades_vendidas=("quantidade", "sum"),
    faturamento=("faturamento", "sum")
)

# Encontra o vendedor com maior faturamento
indice_maior_vendedor = resumo_vendedores["faturamento"].idxmax()

vendedor_maior_faturamento = indice_maior_vendedor

valor_maior_faturamento_vendedor = resumo_vendedores.loc[
    indice_maior_vendedor,
    "faturamento"
]

# Agrupa as vendas por forma de pagamento
resumo_pagamentos = df.groupby("forma_pagamento").agg(
    quantidade_vendas=("id", "size"),
    faturamento=("faturamento", "sum")
)

# Calcula o faturamento por data
faturamento_por_data = df.groupby("data")["faturamento"].sum()

# Calcula o faturamento por dia da semana
faturamento_por_dia_semana = (
    df.groupby("dia_semana", observed=False)["faturamento"]
    .sum()
    .sort_index()
)

# Exibe o resumo geral
print("\nResumo geral")

print(f"Faturamento total: R$ {faturamento:.2f}")
print(f"Quantidade de vendas: {quantidade_vendas}")
print(f"Quantidade de unidades vendidas: {quantidade_unidades}")
print(f"Ticket médio: R$ {ticket_medio:.2f}")
print(f"Maior venda: {produto_maior} - R$ {valor_maior:.2f}")
print(f"Menor venda: {produto_menor} - R$ {valor_menor:.2f}")
print(f"Registros inválidos: {erros}")

# Exibe as três maiores vendas
print("\nTop 3 vendas")

print(
    top_3_vendas[
        ["id", "produto", "quantidade", "valor", "faturamento"]
    ]
)

# Exibe o resumo por produto
print("\nResumo por produto")

print(resumo_produtos)

# Exibe o resumo por categoria
print("\nResumo por categoria")

print(resumo_categorias)

# Exibe o resumo por vendedor
print("\nResumo por vendedor")

print(resumo_vendedores)

# Exibe o vendedor com maior faturamento
print("\nVendedor com maior faturamento")

print(
    f"{vendedor_maior_faturamento} - "
    f"R$ {valor_maior_faturamento_vendedor:.2f}"
)

# Exibe o resumo por forma de pagamento
print("\nResumo por forma de pagamento")

print(resumo_pagamentos)

# Exibe o faturamento por data
print("\nFaturamento por data")

print(faturamento_por_data)

# Exibe o faturamento por dia da semana
print("\nFaturamento por dia da semana")

print(faturamento_por_dia_semana)