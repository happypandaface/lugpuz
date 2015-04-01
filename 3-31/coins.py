import sys

if len(sys.argv) < 2:
  print "give me an amount"
  exit(0)

tot=float(sys.argv[1])
print tot
totc = tot*100
q = totc//25
totc -= q*25
d = totc//10
totc -= d*10
n = totc//5
totc -= n*5
p = totc
print "you can do this with %d quarters, %d dimes, %d nickels, and %d pennies"%(q,d,n,p)
