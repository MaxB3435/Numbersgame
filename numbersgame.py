import random
ng = 1
g = 0

number = random.randint(1,100)
print (number)
while True:
    g = int(input("Jag datorn tänker på ett heltal mellan 1 och 100. Vad gissar du?"))
    if g != number:
        ng = ng +1
        
        print(g)
        if g > number:
            print('Nix, lägre')
        else:
            print('Nix, högre')
    else:
        print('RÄTT! Du klarade spelet på', ng,'gissningar')
        exit()
    