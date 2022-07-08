#Tamanho = 271 # tamanho da peça total em cm
#GrossuraDivisorias = 1.5 # em cm
#Divisoes = 11 # numero de VÃOS

Tamanho = float(input("Tamanho total da peça (em cm): "))
GrossuraDivisorias = float(input("Grossura das divisórias (em cm): "))
Divisoes = float(input("numero de VÃOS: "))

x = 0
for i in range(int(Divisoes-1)):
    x = x + ((Tamanho-GrossuraDivisorias*(Divisoes-1))/Divisoes)
    print('%.1f cm' % x)
    x = x + GrossuraDivisorias
    print('%.1f cm' % x)
    print('\n')
x = x + ((Tamanho-GrossuraDivisorias*(Divisoes-1))/Divisoes)
print('%.1f cm' % x)
input("Enter para Fechar")
