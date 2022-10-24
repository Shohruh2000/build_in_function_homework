# the task condition is placed in the README file
# https://github.com/codeschool43/Build_in_function_homework#build_func08
from math import pow 
def main(x,y):
    s = 1
    s *= (5*(pow(x,2)*pow(y,3))+x*pow(y,2))
    return int(s)

answer = main(7,1)
print(answer)