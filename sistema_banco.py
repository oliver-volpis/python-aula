#print("**********Menu**********")
#print("Criar Usuário")
#print("Depositar")
#print("Sacar")

saldo = 0
limite = 500
numero_saques = 0
limites_saques = 3
usuarios =[]#criei uma lista vazia , pois serão adicionados valores posteriormente
contas = []
agencia='0001'


def menu():
    print('''
        **********Menu**********
        (1) Criar Usuário
        (2) Criar Conta
        (3) Listar Contas
        (d) Depositar
        (s) Sacar
        (e) Extrato
        (q) Sair
    ''')
    return input('Qual opção deseja')

def deposito(valor,saldo):
    #  vou receber o valor do depósito e somar ao saldo
    if valor > 0 :
        saldo += valor
        #print mostrando o valor depositado
        print(f'Você depositou R${valor}')      
    else:
        print('Valor do deposito Ínválido.Verifique a quantia digitada.')
    
    return saldo

def saque(saque,saldo):
   global  numero_saques,limites,limites_saques
    #De acordo com a documentação Python , váriaveis globais não ficam presas ao limite do escopo da função.
   if numero_saques >= limites_saques:
    print('Você atingiu o limite de saques de sua conta.Tente novamente no proximo dia útil')
   else:
        if saque <= 0:
            print('Saque Inválido.Verifique o valor e tente novamente.')
        elif saque > limite :
            print('Valor limite excedido.Verifique o valor e tente novamente.')
        elif saque > saldo :
            print('Saldo insuficiênte.Verifique o valor e tente novamente.')
        else:
            saldo -= saque
            numero_saques += 1
            
        return saldo        