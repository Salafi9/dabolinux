def countvowels():
    vowels=['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    username = input('Please Enter Your Name>  ')
    name = sorted(username)
    c = 0
    j = ' '
    for alphabet in name:
        if alphabet == j:
            name.remove(j)
            continue
        if alphabet in vowels:
            c += 1
    l = len(name)

    print('Your name have vowels', c)
    print('And it countain %s Number of words' % l)

    if c == l:
        print('Therefore Your Name contain only vowels no consonant, ')
        print("Congratulations!!! You're special")
    else:
        if c != l and c > 0:
            print('You have Normal Name')
            print("Therefore their're %d Consonant in Your name" % (l - c))

        else:
            c == 0
            print("Your Name contain no Vowels, You're special")
countvowels()