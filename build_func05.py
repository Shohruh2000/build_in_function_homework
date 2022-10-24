# the task condition is placed in the README file
# https://github.com/codeschool43/Build_in_function_homework#build_func05
from math import pow 
def main(n,x):
    s = 1
    s *=pow(x,n)+pow(n,x)
    return int(s)
answer = main(3,6)
print(answer)
