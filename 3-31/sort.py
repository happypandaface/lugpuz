import random

unsort=[]
for i in range(0,20):
  unsort.append(random.randint(0,40))
print unsort
print sorted(unsort)
