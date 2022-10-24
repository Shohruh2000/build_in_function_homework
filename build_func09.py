# the task condition is placed in the README file
# https://github.com/codeschool43/Build_in_function_homework#build_func09

from math import pow
def main(x,y):
    s = 1
    s *=2*(pow(y,3)+pow(x,2)*y)
    return int(s)
answer = main(2,4)
print(answer)