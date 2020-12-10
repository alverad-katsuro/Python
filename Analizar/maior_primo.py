def maior_primo(x) -> object:
    for maior in reversed(range(1,x+1)):
     if all(maior%n!=0 for n in range(2,maior)):
        return maior
