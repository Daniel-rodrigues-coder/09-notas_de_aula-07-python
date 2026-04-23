contador = int(input('Digite um número: '))
n = 1
if contador  == 0:
        print ('programa encerrado')
elif contador >  10:
        print ('número inválido')
else:
    for n in range(1, contador+1 , 1) : 
        print (n)