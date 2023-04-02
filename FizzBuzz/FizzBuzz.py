
rangeX = 101
text = ["Fizzbuzz","Fizz","Buzz"]
def FizzBuzz(Fizz = int, Buzz = int):
    for cunt in range (1, rangeX):
        if 0 == cunt%Fizz and 0 == cunt%Buzz:
          print(text[0])
        elif cunt % Fizz == 0:
            print(text[1])
        
        elif cunt % Buzz == 0:
            print(text[2])
         
        
        else:
          print(cunt)


    






FizzBuzz(Fizz = 3, Buzz = 5)
FizzBuzz(Fizz = 7, Buzz = 9)