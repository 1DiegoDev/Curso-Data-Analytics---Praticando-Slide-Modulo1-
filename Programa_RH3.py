vendasDoVendedor = float(input("Digite as vendas do vendedor: R$ "))

comissaoMaior = vendasDoVendedor * 0.04
comissaoMenor = vendasDoVendedor * 0.02

if vendasDoVendedor >= 10000.0:
    print(f'''
        ===================================== 
            VENDAS DO VENDEDOR: R$ {vendasDoVendedor} 
            COMISSÃO E VENDAS: R$ {comissaoMaior}
        =====================================
    ''')
else:
    print(f'''
        ===================================== 
            VENDAS DO VENDEDOR: R$ {vendasDoVendedor} 
            COMISSÃO E VENDAS: R$ {comissaoMenor}
        =====================================
    ''')