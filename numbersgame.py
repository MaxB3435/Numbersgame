import random
ng = 1
g = 0

number = random.randint(1,100)
print ('Jag datorn tänker på ett heltal mellan 1 och 100. Vad gissar du?')
while True:
    g = int(input())
    if g != number:
        ng = ng +1
        if g > number:
            print('Nix, lägre')
        else:
            print('Nix, högre')
    else:
        print('RÄTT! Du klarade spelet på', ng,'gissningar')
        exit()
    