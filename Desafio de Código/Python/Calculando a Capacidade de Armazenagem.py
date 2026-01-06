import math

total_caixas = input().strip()
capacidade_palete = input().strip()

total_caixas = int(total_caixas)
capacidade_palete = int(capacidade_palete)

paletes_necessarios = math.ceil(total_caixas / capacidade_palete)

print(str(paletes_necessarios))