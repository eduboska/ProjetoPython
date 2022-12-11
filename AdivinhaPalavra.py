import random
name = input("Qual seu nome? ")
print("Boa sorte ", name)
words = ['exceto', 'cínico', 'idoneo', 'indole', 'apogeu', 'utopia', 'merito', 'casual', 'idiota', 'pressa', 'hetero',
         'legado', 'nocivo', 'gentil', 'paixao', 'safado', 'otario', 'formal', 'sessao', 'julgar', 'tambem', 'presta',
         'sobrio', 'solene']
word = random.choice(words)
print("Adivinhe as letras!")
guesses = ''
turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("Você venceu!!!")

        print("A palavra é: ", word)
        break

    guess = input('Adivinhe a letra:')
    guesses += guess

    if guess not in word:
        turns -= 1
        print('Errou!!!')

        print('Você tem mais ', + turns, 'chances')
        if turns == 0:
            print('Você perdeu :(')

