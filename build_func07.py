# the task condition is placed in the README file
# https://github.com/codeschool43/Build_in_function_homework#build_func07
from math import pow
def main(x,y):
    s = 1
    s *=(pow(x,2)+6*pow(x,3)+3*x*y)
    return int(s)
answer = main(5,2)
print(answer)
