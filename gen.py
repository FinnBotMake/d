import string
import random
import os
x=100

#SYRUM#3961


while not (x == 0) :
            
  tokens = (''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(27)))
  x -= 1
  a_file = open("Promocode.txt", "a" )
  a_file.write('https://discord.com/billing/promotions/'+tokens + '\n')
  a_file.close()