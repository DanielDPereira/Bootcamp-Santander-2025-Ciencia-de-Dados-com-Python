peso = float(input())
preco_por_tonelada = float(input())
tipo_cliente = input()

valor_total = peso * preco_por_tonelada

if tipo_cliente == "Novo cliente":
    desconto = 0
elif tipo_cliente == "Cliente fidelizado":
    desconto = 0.05
elif tipo_cliente == "Cliente premium":
    desconto = 0.10
else:
    desconto = 0

valor_final = valor_total * (1 - desconto)

print(f"{valor_final:.2f}")