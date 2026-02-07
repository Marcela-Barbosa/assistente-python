print ('===Assistente do Gabriel===')
n=int(input('Digite um número inteiro:'))
print('Antecessor:',n-1)
print('Sucessor:',n+1)

print('------------------------')

n=float(input('Digite um número:'))
print('Dobro:',n*2)
print('Triplo:',n*3)
print('Raiz:',n*1/2)

print('-------------------------')

nota1= float(input('Digite a primeira nota:'))
nota2=float(input('Digite a segunda nota:'))
media=(nota1+nota2)/2
print('Média do aluno:',media)

print('-------------------')

metros=float(input('Digite o valor em metros:'))
centimetros=metros*100
milimetros=metros*1000
print('Valor em centímetros:',centimetros)
print('Valor em milímetros:',milimetros)

print('-----------------------------')

numero=int(input('Digite um número inteiro para ver a tabuada:'))
print(f'Tabuada do {numero}:')
for i in range(1,11):
    print(f'{numero}*{i}={numero*i}')

print('---------------------------')

dinheiro=float(input('Quanto de dinheiro você tem na carteira?R$:'))
dolar=dinheiro/5.27
print(f'Com R$ {dinheiro:.2f} você pode comprar US$ {dolar:.2f}')

print('---------------------------------------------------')

largura=float(input('Digite a largura da parede (em metros):'))
altura=float(input('Digite a altura em metros):'))
area=largura*altura
tinta=area/2
print(f'A área da parede é {area:.2f}m²')
print(f'Você precisará de tinta {tinta:.2f}litros de tinta')

print('------------------------------------------------')

preco=float(input('Digite o preço do produto:R$'))
desconto=preco*0.05
novo_preco= preco-desconto
print(f'Preço original:R${preco:.2f}')
print(f'Desconto de 5%:R${desconto:.2f}')
print(f'Novo preço:R${novo_preco:.2f}')

print('===Fim do programa===')
