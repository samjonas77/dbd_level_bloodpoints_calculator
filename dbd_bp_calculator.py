import math
#overview:
#f(x) = (230.57*(x+42.34)^2-416152.34)-(230.57*(p+42.34)^2-416152.34)
#       (            c               )-(               f            )
#       (    a          )              (    d          )
#       (       b          )           (          e       )


#input:

level1 = int(input("Level you are at: "))
level2 = int(input("Level you want to aquire: "))
print()

leveldif = str(level2 - level1)
print("You need: " + leveldif + " levels")
print()
wait = input("Press Enter to continue program.")
print()


#calculation:

level42_2 =  float(level2+42.34)
a = float(math.pow(level42_2, 2))
b = float(230.57 * a)
c = float(b - 416152.34)


level42_1 =  float(level1+42.34)
d = float(math.pow(level42_1, 2))
e = float(230.57 * d)
f = float(e - 416152.34)

result = float(c-f)
result2 = float(result / 1000)

bp_needed1= int(result2)
bp_needed2= str(bp_needed1 * 1000)

print()
print("You need ca. " + bp_needed2 + " Bloodpoints")
print()
print()
print()




wait = input("Press Enter to close program.")