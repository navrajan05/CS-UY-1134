from ArrayStack import ArrayStack

variables = {}


def is_number(num):  # We're using this instead of isnumeric() to handle decimals properly
    try:
        float(num)
        return True
    except ValueError:
        return False


def solve_postfix(exp_lst):
    stack = ArrayStack()
    for x in exp_lst:

        # is x a number?
        if is_number(x):
            m = float(x)
            stack.push(m)

        # is x an arithmetic operator?
        elif x == "-":
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.push(arg1 - arg2)
        elif x == "+":
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.push(arg1 + arg2)
        elif x == "/":
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.push(arg1 / arg2)
        elif x == "*":
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.push(arg1 * arg2)

        # is x a variable?
        else:
            val = variables[x]
            stack.push(val)

    return stack.top()


breakout = False
while breakout is not True:
    user_in = input("--> ")

    if user_in == "done()":
        breakout = True

    else:
        statement = user_in.split()
        if len(statement) >= 2 and statement[1] == "=":
            variableName = statement[0]
            variableValue = solve_postfix(statement[2:])

            variables.update({variableName: variableValue})
            print(variableName)
        else:
            out = solve_postfix(statement)
            if out == int(out):
                print(int(out))
            else:
                print(out)