import random

def apocal(n):
   bc = 0
   for i in xrange(n):
     a = random.random()
     while a < 0.5:
        bc += 1
        a = random.random()
   return bc * 1. / n
   
if __name__ == "__main__":
  print apocal(10000000)