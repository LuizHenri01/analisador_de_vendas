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

    produto = df.loc[indice, "produto"]
    valor = df.loc[indice, "valor"]

    return produto, valor


def encontrar_menor_venda(df):
    indice = df["valor"].idxmin()

    produto = df.loc[indice, "produto"]
    valor = df.loc[indice, "valor"]

    return produto, valor


# Carregamento dos dados
vendas, erros = carregar_vendas()

# Criação do DataFrame
df = pd.DataFrame(vendas)

# ANÁLISES GERAIS

faturamento = calcular_faturamento(df)
quantidade_vendas = len(df)
ticket_medio = calcular_ticket_medio(df)

produto_maior, valor_maior = encontrar_maior_venda(df)
produto_menor, valor_menor = encontrar_menor_venda(df)

# ANÁLISES COM PANDAS

# Vendas ordenadas da maior para a menor
vendas_ordenadas = df.sort_values("valor", ascending=False)

# 3 maiores vendas
top_3_vendas = vendas_ordenadas.head(3)

# Resumo por produto
resumo_produtos = df.groupby("produto").agg(
    quantidade_vendas=("valor", "size"),
    faturamento=("valor", "sum")
)

# Print dos Resultados

print("\n RESUMO GERAL ")
print(f"Faturamento total: R$ {faturamento:.2f}")
print(f"Quantidade de vendas: {quantidade_vendas}")
print(f"Ticket médio: R$ {ticket_medio:.2f}")
print(f"Maior venda: {produto_maior} - R$ {valor_maior:.2f}")
print(f"Menor venda: {produto_menor} - R$ {valor_menor:.2f}")
print(f"Registros inválidos: {erros}")


print("\n TOP 3 VENDAS ")
print(top_3_vendas)


print("\n RESUMO POR PRODUTO ")
print(resumo_produtos)