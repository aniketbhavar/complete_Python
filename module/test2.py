from app import x,add
print(x)
add(10,20)
product(29,30)
from app import *
print(x)
add(10,20)
product(10,20)

#member aliasing:
from app import x as y, add as sum
print(y)
sum(20,20)
 
from app import x as y
print(x)
print(y)
