from calculadora import soma

# Calculadora Simples

while True:
    # Apresentação
    print('\n\t\t\t -- Calculadora Simples --\n')

    # Menu
    print('1. Soma')
    print('2. Subtração')
    print('3. Sair')

    # Escolha do usuário
    op = int(input('\n\t\t\tOpção: '))

    # Processamento
    if op == 1:
        print('\n\t\t\t Soma \n')

        #Entrada
        num1 = int(input('Informe n1: '))
        num2 = int(input('Informe n2: '))

        # Processamento
        total = soma(num1, num2)

        #Saída
        print(f'\n\n\t{num1} + {num2} = {total}\n')
    elif op == 2:
        print('\n\t\t\t Subtração \n')

        #Entrada

        #Processamento

        #Saída

    elif op == 3:
        # Termina a aplicação
        print('\n\tForte abraço!\n')
        break

    else:
        # Opção incorreta
        print(f'\nA opção {op} é incorreta!\n')
