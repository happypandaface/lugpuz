n1=999
n2=999
hn = 0
while n1 > 0:
  s = n1*n2
  if s > hn:
    w = str(s)
    isp = True
    for i in range(len(w)//2):
      if w[i] != w[len(w)-1-i]:
        isp = False
    if isp:
      hn = s
  n2 -= 1
  if n2 == 0:
    n1 -= 1
    n2 = 999
print str(hn)
