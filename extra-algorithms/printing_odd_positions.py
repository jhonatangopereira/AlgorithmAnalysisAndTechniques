numbers = [2, 4, 6, 8, 10, 12] # θ(1) - instrução simples
for i in range(len(numbers)):  # θ(n) - tudo que estiver dentro do for tem essa complexidade
    if numbers[i] % 2 == 0:    # θ(n) - está dentro do for, logo tem a mesma complexidade
        print(i)
