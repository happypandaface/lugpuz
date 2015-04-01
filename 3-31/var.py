import sys

if len(sys.argv) < 2:
  print "give me an amount"
  exit(0)

ls = list(sys.argv[1])
words=[]
seed = 0
num=len(ls)
word=[]
cls = ls[:]
while True:
  if seed > len(ls)**len(ls):
    break
  if len(cls) == 0:
    wstr = "".join(word)
    if wstr not in words:
      words.append(wstr)
    word = []
    cls = ls[:]
    seed = seed + 1
    continue
  n = seed%len(cls)
  word.append(cls[n])
  del cls[n]

for wstr in words:
  print wstr
