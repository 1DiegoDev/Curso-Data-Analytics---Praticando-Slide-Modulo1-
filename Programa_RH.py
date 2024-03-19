# ctrl + ; = colocar tudo selecionado como cmentario
# #Amanda está participando de um processo seletivo para a empresa JWC.
# #Ela chegou na etapa de entrevista técnica e foi informada que deverá
# #desenvolver um pequeno programa de RH.

# Para o programa, utilize os seguintes valores:
# Desconto do INSS - 8%.
# Desconto do VT - 6%.


nomeDoFuncionario = input("Digite o nome do funcinaro:")
salarioBrutoFuncionario = float(input("Digite o salario do funcionario:"))

#
taxaValeTransporte = 0.08
taxaInss = 0.06

descontoValeTransporte = taxaValeTransporte * salarioBrutoFuncionario
descontoInss = salarioBrutoFuncionario * taxaInss
#Quando uma conta etá em () será a primeira conta cm prioridade a ser feita primeiro
salarioLiquidoFuncionaro = salarioBrutoFuncionario - (salarioBrutoFuncionario - descontoInss)


#(F'''''') QUEBRA A LINHA. Ex:
print(f'''
============================== H O L E R I T E ==============================
|            - DADOS DO FUNCIONÁRIO: {nomeDoFuncionario}                    |
|            - SALARIO BRUTO: R${salarioBrutoFuncionario}                   |
|            - DESCONTO VALE TRANSPORTE: R${descontoValeTransporte}         |
|            - DESCONTO INSS: {descontoInss}                                |
|            - SALÁRIO LÍQUIDO A RECEBER: R${salarioLiquidoFuncionaro}      |
=============================================================================     
''')


# Desconto do INSS - 8%.
# Desconto do VT - 6%.