fb = int(input("Digite o numero: "))


for i in range(1,(fb+1)):
    if i == 15:
        print(i, "fizz2buzz2!")
    elif i == 1987:
        print(i, "ITS THAT THE BITE OF 87?!?!?!?!?")
    elif i % 3 == 0 and  i % 5 == 0 and i % 7 == 0:
        print(i,"FizzBuzzPop!") 
    elif i % 5 == 0 and i % 3 == 0:
        print(i, "fizzbuzz!")
    elif i % 3 == 0 and i % 7 == 0:
        print (i, "fizzpop!")
    elif i % 5 == 0 and i % 7 == 0:
        print(i,"Buzzpop!")
    elif i % 3 == 0:
        print (i, "fizz!")
    elif i % 5 == 0:
        print (i, "buzz!")
    elif i % 7 == 0:
        print(i, "pop!")
    else:
        print(i)