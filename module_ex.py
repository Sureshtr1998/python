
# import functionsPrograms
# from functionsPrograms import add
from functionsPrograms import *

# res1, res2 = functionsPrograms.add(10,12)
res1, res2 = add(10,12)
# This gives the starting point, if we are executing this file it gives __main__ if it is import statment (check add fnction) it gives its parent name from where it is called
print("MODULE "+__name__)
print(res1,res2)
# print(add(10,12))
