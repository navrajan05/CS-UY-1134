
'''
I don't think this is technically linear time,
since multiplication is only constant time for
fixed-size integers, which python doesn't use.
Still, with the tools currently allowed in the
course, I don't think it's worth worrying about
that technicality.
'''


def e_approx(n):
    current_factorial = 1
    current_total = 1
    for i in range(1, n+1):
        current_factorial *= i
        current_total += (1/current_factorial)

    return current_total


'''
def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)
        
        
main()
'''