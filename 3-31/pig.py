import sys
import re

if len(sys.argv) < 2:
  print "give me a word"
  exit(0)

w = sys.argv[1]
m = re.search("^[^aeiou]*", w)
pre=m.group(0)
suff=w[len(pre):]
if len(pre) == 0:
  pre = "w"

print suff+pre+"ay"
