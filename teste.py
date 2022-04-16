#Crie um algoritmo que conte de 1-100 aonde
#Multiplos de 15 devem ser substituídos por FizzBuzz
#Multiplos de 5 devem ser substituídos por Fizz
#Multiplos de 3 devem ser substituídos por Buzz

def fizzbuzz():
    for n in range (1,101): 
        if (n %15==0):
            print('FizzBuzz')
        elif (n %3==0):
            print('Buzz')
        elif (n %5==0):
            print('Fizz')
        else:
            print(n)
fizzbuzz()