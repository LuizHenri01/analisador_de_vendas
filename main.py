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

# Extrai o dia da semana da coluna de data
df["dia_semana"] = df["data"].dt.day_name()


# =========================
# RESUMO GERAL
# =========================

faturamento = calcular_faturamento(df)
quantidade_vendas = len(df)
quantidade_unidades = df["quantidade"].sum()
ticket_medio = calcular_ticket_medio(df)

produto_maior, valor_maior = encontrar_maior_venda(df)
produto_menor, valor_menor = encontrar_menor_venda(df)


# =========================
# TOP 3 VENDAS
# =========================

vendas_ordenadas = df.sort_values(
    "faturamento",
    ascending=False
)

top_3_vendas = vendas_ordenadas.head(3)


# =========================
# RESUMO POR PRODUTO
# =========================

resumo_produtos = df.groupby("produto").agg(
    quantidade_vendas=("id", "size"),
    unidades_vendidas=("quantidade", "sum"),
    faturamento=("faturamento", "sum")
)


# =========================
# RESUMO POR CATEGORIA
# =========================

resumo_categorias = df.groupby("categoria").agg(
    quantidade_vendas=("id", "size"),
    unidades_vendidas=("quantidade", "sum"),
    faturamento=("faturamento", "sum")
)


# =========================
# RESUMO POR VENDEDOR
# =========================

resumo_vendedores = df.groupby("vendedor").agg(
    quantidade_vendas=("id", "size"),
    unidades_vendidas=("quantidade", "sum"),
    faturamento=("faturamento", "sum")
)

indice_maior_vendedor = resumo_vendedores["faturamento"].idxmax()

vendedor_maior_faturamento = indice_maior_vendedor

valor_maior_faturamento_vendedor = resumo_vendedores.loc[
    indice_maior_vendedor,
    "faturamento"
]


# =========================
# RESUMO POR PAGAMENTO
# =========================

resumo_pagamentos = df.groupby("forma_pagamento").agg(
    quantidade_vendas=("id", "size"),
    faturamento=("faturamento", "sum")
)


# =========================
# FATURAMENTO POR DATA
# =========================

faturamento_por_data = df.groupby("data")["faturamento"].sum()


# =========================
# FATURAMENTO POR DIA DA SEMANA
# =========================

faturamento_por_dia_semana = df.groupby(
    "dia_semana"
)["faturamento"].sum()


# =========================
# EXIBIÇÃO DOS RESULTADOS
# =========================

print("\n=== RESUMO GERAL ===")

print(f"Faturamento total: R$ {faturamento:.2f}")
print(f"Quantidade de vendas: {quantidade_vendas}")
print(f"Quantidade de unidades vendidas: {quantidade_unidades}")
print(f"Ticket médio: R$ {ticket_medio:.2f}")
print(f"Maior venda: {produto_maior} - R$ {valor_maior:.2f}")
print(f"Menor venda: {produto_menor} - R$ {valor_menor:.2f}")
print(f"Registros inválidos: {erros}")


print("\n=== TOP 3 VENDAS ===")

print(
    top_3_vendas[
        ["id", "produto", "quantidade", "valor", "faturamento"]
    ]
)


print("\n=== RESUMO POR PRODUTO ===")

print(resumo_produtos)


print("\n=== RESUMO POR CATEGORIA ===")

print(resumo_categorias)


print("\n=== RESUMO POR VENDEDOR ===")

print(resumo_vendedores)


print("\n=== VENDEDOR COM MAIOR FATURAMENTO ===")

print(
    f"{vendedor_maior_faturamento} - "
    f"R$ {valor_maior_faturamento_vendedor:.2f}"
)


print("\n=== RESUMO POR FORMA DE PAGAMENTO ===")

print(resumo_pagamentos)


print("\n=== FATURAMENTO POR DATA ===")

print(faturamento_por_data)


print("\n=== FATURAMENTO POR DIA DA SEMANA ===")

print(faturamento_por_dia_semana)