[1mdiff --git a/main.py b/main.py[m
[1mindex b8fcd4f..b866e29 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -1,9 +1,11 @@[m
 import csv[m
[32m+[m[32mimport pandas as pd[m
[32m+[m
 [m
 def processar_linha(linha):[m
     if linha["produto"] == "":[m
         print("Erro: produto vazio")[m
[31m-        return None # sem venda valida a partir desse registro[m
[32m+[m[32m        return None[m
 [m
     try:[m
         linha["valor"] = int(linha["valor"])[m
[36m@@ -36,33 +38,27 @@[m [mdef carregar_vendas():[m
     return vendas, erros[m
 [m
 [m
[31m-def calcular_faturamento(vendas):[m
[31m-    total = 0[m
[32m+[m[32mdef calcular_faturamento(df):[m
[32m+[m[32m    return df["valor"].sum()[m
 [m
[31m-    for venda in vendas:[m
[31m-        total += venda["valor"][m
 [m
[31m-    return total[m
[32m+[m[32mdef calcular_ticket_medio(df):[m
[32m+[m[32m    total = calcular_faturamento(df)[m
[32m+[m[32m    quantidade_vendas = len(df)[m
 [m
[32m+[m[32m    return total / quantidade_vendas[m
 [m
[31m-def encontrar_maior_venda(vendas):[m
[31m-    maior_venda = vendas[0]["valor"][m
[31m-[m
[31m-    for venda in vendas:[m
[31m-        if venda["valor"] > maior_venda:[m
[31m-            maior_venda = venda["valor"][m
 [m
[31m-    return maior_venda[m
[32m+[m[32mdef encontrar_maior_venda(df):[m
[32m+[m[32m    indice = df["valor"].idxmax()[m
 [m
[32m+[m[32m    return df.loc[indice, "valor"][m
 [m
[31m-def encontrar_menor_venda(vendas):[m
[31m-    menor_venda = vendas[0]["valor"][m
 [m
[31m-    for venda in vendas:[m
[31m-        if venda["valor"] < menor_venda:[m
[31m-            menor_venda = venda["valor"][m
[32m+[m[32mdef encontrar_menor_venda(df):[m
[32m+[m[32m    indice = df["valor"].idxmin()[m
 [m
[31m-    return menor_venda[m
[32m+[m[32m    return df.loc[indice, "valor"][m
 [m
 [m
 def encontrar_produto_maior_venda(vendas):[m
[36m@@ -89,23 +85,19 @@[m [mdef encontrar_produto_menor_venda(vendas):[m
     return produto_menor_venda, menor_venda[m
 [m
 [m
[31m-def calcular_ticket_medio(vendas):[m
[31m-    total = calcular_faturamento(vendas)[m
[31m-    quantidade_vendas = len(vendas)[m
[31m-[m
[31m-    return total / quantidade_vendas[m
[31m-[m
[31m-[m
 # Carregamento dos dados[m
 vendas, erros = carregar_vendas()[m
 [m
[32m+[m[32m# Criação do DataFrame[m
[32m+[m[32mdf = pd.DataFrame(vendas)[m
[32m+[m
 # Análises[m
[31m-faturamento = calcular_faturamento(vendas)[m
[31m-quantidade_vendas = len(vendas)[m
[31m-ticket_medio = calcular_ticket_medio(vendas)[m
[32m+[m[32mfaturamento = calcular_faturamento(df)[m
[32m+[m[32mquantidade_vendas = len(df)[m
[32m+[m[32mticket_medio = calcular_ticket_medio(df)[m
 [m
[31m-maior_venda = encontrar_maior_venda(vendas)[m
[31m-menor_venda = encontrar_menor_venda(vendas)[m
[32m+[m[32mmaior_venda = encontrar_maior_venda(df)[m
[32m+[m[32mmenor_venda = encontrar_menor_venda(df)[m
 [m
 produto_maior, valor_maior = encontrar_produto_maior_venda(vendas)[m
 produto_menor, valor_menor = encontrar_produto_menor_venda(vendas)[m
