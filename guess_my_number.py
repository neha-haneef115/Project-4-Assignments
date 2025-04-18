import random
def main():
   
    randomnum= random.randint(0,100)
    guessnum=-1
    print(randomnum)
    while guessnum!=randomnum:
   
     guessnum=int(input("Guess your number:"))
     if(guessnum==randomnum):
        print("you guessed correctly")

     elif(randomnum<guessnum):
        print("your guess was too high")

     elif(randomnum>guessnum):
        print("your guess was too low")   


if __name__=="__main__":
   main()    
            

    