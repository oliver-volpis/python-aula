nome = str(input('Qual o seu nome? '))
idade = int(input('Qual a sua idade? '))

if (idade<16)
    voto = 'Nao precisa votar'

elif (idade == 16 or idade > 65)
    voto = 'Voto não obrigatorio'

else:
    voto = 'Voto obrigatorio'


print(f'De acordo com a sua idade, {nome} você {voto}.')
