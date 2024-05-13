def éPrimo(k):
    i = 2
    while i < k:
        if k % i == 0:
            return False
        i += 1
    return True

def maior_primo(n):
    i = n
    while i > 1:
        if éPrimo(i):
            return i
        i -= 1
    return 0

print(maior_primo(100))
print(maior_primo(7))