# the task condition is placed in the README file
# https://github.com/codeschool43/Build_in_function_homework#build_func10
from math import pow
def main(x,y):
    s = 1
    s *=( 3*pow(y,(1/2))+pow(x,(2/3)))
    return s

answer = main(8,4)
print(answer)
