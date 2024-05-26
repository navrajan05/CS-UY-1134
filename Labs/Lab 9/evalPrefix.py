from ArrayStack import ArrayStack

def eval_prefix(exp_str):
    exp_lst = exp_str.split()
    stack = ArrayStack()
    while len(exp_lst) > 0:
        x = exp_lst.pop()

        if x.isnumeric():
            m = float(x)
            stack.push(m)
        else:
            arg1 = stack.pop()
            arg2 = stack.pop()

            if x == "-": stack.push(arg1 - arg2)
            elif x == "+": stack.push(arg1 + arg2)
            elif x == "/": stack.push(arg1 / arg2)
            elif x == "*": stack.push(arg1 * arg2)

    return (stack.top())


exp_str  = "- + * 16 5 * 8 4 20"
print(eval_prefix(exp_str))
