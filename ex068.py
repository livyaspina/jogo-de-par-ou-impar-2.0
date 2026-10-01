import random
import time
vit = 0
print('-='*20)
print("VAMOS JOGAR PAR OU IMPAR?")
print('-='*20)

while True:
    num = int(input('Diga um valor: '))
    qual = input('PAR OU IMPAR?[P/I]: ').upper().strip()
    computador = random.randint(0,100)
    total = num + computador
    time.sleep(2)
    print('-='*20)
    print(f'Você jogou {num} e o computador {computador}. O total foi {total}')
    print('-='*20)
    time.sleep(2)
    if total % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'

    if qual == resultado:
        vit +=1
        print(f'Deu {'PAR'if resultado == 'P' else 'ÍMPAR'}')
        time.sleep(2)
        print('''VOCÊ VENCEU!
        Vamos novamente...''')
        print('-='*20)
    else: 
        print(f'Deu {'PAR'if resultado == 'P' else 'ÍMPAR'}')
        time.sleep(2)
        print('VOCÊ PERDEU!!!!!!')
        print('-='*20)
        break

print(f'''FIM DE JOGO
Vitórias: {vit}''')