
prevnum=1
num=1
tsum=0
while num < 4000000:
  if num%2 == 0:
    tsum += num
  tmp = prevnum
  num = num + prevnum
  prevnum = tmp
print tsum
