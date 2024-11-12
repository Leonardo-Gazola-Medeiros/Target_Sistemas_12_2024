def fibo(n):
    lista_fibo = [0,1,1]

    if n == 0:
        print(f'O valor {n} faz parte da sequência de fibonacci')
        return None
    while lista_fibo[-1] <= n:
        if lista_fibo[-1] == n:
            print(f"O valor {n} faz parte da sequência de fibonacci")
            break
        lista_fibo.append(lista_fibo[-1]+lista_fibo[-2])

        print(lista_fibo[-1])

    if lista_fibo[-1] != n:
        print(f'O numero {n} não faz parte da sequencia de fibonacci')

fibo(1000)