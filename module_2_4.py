numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = 0
for i in numbers: # перебор элементов входящих в список numbers
    if i == 1:
        continue
    if i > 1:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break # остановка перебора range, если число непростое
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('Primes: ', primes) # Вывод списка просытых чисел
print('Not Primes: ', not_primes) # Вывод списка непросытых чисел
