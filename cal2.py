import operator

arithmetic_operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '**': operator.pow,
    '//': operator.floordiv,
}


def simple_calculator(frst_num, secnd_num, opr):
        result = arithmetic_operators[opr](frst_num, secnd_num)
        print("The result is: ", result)
    

def cal(numbers:list, opr):
    if len(numbers) == 2:
        return simple_calculator(numbers[0], numbers[1], opr)
    elif (numbers) < 2:
        print("Error")
    else:
        return simple_calculator(numbers.pop(), cal(numbers, opr), opr)

num = input("Enter list numbers and seprate them by ',' : ").split(",")
numbers = [int(x.strip()) for x in num]
opr = input("Enter the operator : ")
cal(numbers, opr)