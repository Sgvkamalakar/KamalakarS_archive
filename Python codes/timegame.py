import time
import random

def main():
   target=random.randint(0,10)
   print('\nYour target time is {} seconds\n'.format(target))
   input(" \n:::::Press Enter to Begin:::::\n")
   start=time.perf_counter()
   input("\n....Press Enter again after {} seconds....\n".format(target))
   elapsed=time.perf_counter()-start
   print("\nElapsed time: {0:.1f} seconds".format(elapsed))
   if elapsed==target:
       print("Perfect timing!!")
   elif elapsed<target:
       print("({0:.1} seconds too fast)".format(target-elapsed))
   else:
        print("({0:.1} seconds too slow)".format(elapsed-target))

if __name__=="__main__":
   main()
