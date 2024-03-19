

# Uma empresa de serviços te contratou para desenvolver um programa
# com a seguinte lógica:

# O operador irá digitar o salário de um cliente.

# Se o salário for maior ou igual que R$ 3.000,00, o programa irá escrever
# na tela “Oferecer Plano Alfa”
# Caso seja menor, o programa escreverá “Oferecer Plano Beta”.


salarioDoCliente = float(input("Digite o salário do cliente: R$"))

if salarioDoCliente >= 3000.0:
    print(f'''
        ===================================== 
        salario do cliente: {salarioDoCliente} 
        Plano a ser ofertado [Plano Alfa]
        =====================================
    ''')
else:
      print(f'''
     ==========================================
        salario do cliente: {salarioDoCliente} 
        Plano a ser ofertado [Plano Beta]
     ==========================================
    ''')
