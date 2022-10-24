# the task condition is placed in the README file
# https://github.com/codeschool43/Build_in_function_homework#build_func04
from math import pow
def main(n):
    s = 1
    s *= pow(((2+n)/3),2)
    return s
answer = main(4)
print(answer)