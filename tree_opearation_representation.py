"""
Arithmetic Operations visualized in a tree
This is the basic model of the project, updated as of 24/08/2023

"""
__author__ = "Selvaganapathy K"
__email__ = "selvaganz1285@gmail.com"

import re

precedence = []
arith_operators = ["+", "-", "*", "/"]
st_ind_order = None
CRED = "\033[91m"
CEND = "\033[37m"


class operator:
    """
    Individual Nodeswhich carries an operator, left operand, right operand
    and the right-left childs to parse through
    """

    def __init__(self, op, l, r):
        """
        Initial declaration of operator , left operand and right operand
        """
        self.op = op
        self.l = l
        self.r = r
        self.result = None
        self.left = None
        self.right = None

    def representation(self):
        """
        Basic representation function to visualize individual node

        """
        print(str(self.l) + " " * (len(str(self.result))) + str(self.r))
        print(
            " " * (len(str(self.l)) - 1)
            + "\\"
            + self.op.center((len(str(self.result))), " ")
            + "/"
        )
        print(" " * len(str(self.l)) + str(self.result))


def splitter(operation):
    """
    Splits the given input by parsing through and instantiates them as operator nodes.

    """
    ext = ""
    recent = None
    op_bracks = 0
    cl_bracks = 0
    negatives = []
    order = 0
    for i in range(len(operation)):
        if operation[i].isdigit():
            pass
        elif operation[i] == "(":
            op_bracks += 1
            order += 1
        elif operation[i] == ")":
            cl_bracks += 1
            order -= 1
        elif operation[i] in arith_operators and i not in negatives and i != 0:
            oper = operation[i]
            left = ""
            for j in range(i - 1, -1, -1):
                if operation[j].isdigit():
                    left += operation[j]
                elif operation[j] == "-":
                    left += operation[j]
                    break
                elif operation[j]==" ":
                    pass
                else:
                    break
            left = left[::-1]
            right = ""
            for j in range(i + 1, len(operation)):
                if operation[j].isdigit():
                    right += operation[j]
                elif operation[j] == "-" and right == "":
                    right += operation[j]
                    negatives.append(j)
                elif operation[j] in "() ":
                    pass
                else:
                    break
            root = operator(oper, left, right)
            if not recent:
                recent = root
            else:
                root.left = recent
                recent.right = root
                recent = recent.right

            if oper in "*/":
                precedence[order][0].append(root)
            else:
                precedence[order][1].append(root)
            ext = ""
            global st_ind_order
            if st_ind_order is None:
                st_ind_order = root
        elif operation[i] == "-" and i == 0:
            ext += operation[i]


def valid_operation(operation):
    """
    check if given input is a valid Arithmetic Operation
    """
    pattern = r"^[-()0-9][0-9+\-*/() ]*[0-9()]$"
    op = 0
    cl = 0
    cond = True if re.match(pattern, operation) else False
    if "(" in operation:
        for i in operation:
            if i == "(":
                op += 1
            elif i == ")":
                cl += 1
                if cl > op:
                    cond = False
    if op != cl:
        cond = False
    return cond


def parse():
    """
    Parses through the Arithmetic operation and executes
        1. Follow precedence rule

    """
    global st_ind_order
    for parser in precedence[::-1]:
        combine = parser[0] + parser[1]
        if combine != []:
            for Ele in combine:
                Ele.result = int(eval(str(Ele.l) + Ele.op + str(Ele.r)))
                x = st_ind_order
                st = ""
                while x:
                    simple_st = ""
                    if st == "":
                        simple_st += str(x.l)+" "+x.op+" "+str(x.r)
                    else:
                        simple_st += " "+x.op+" "
                        if x.right == Ele:
                            simple_st += CRED + str(x.r) + CEND
                        else:
                            simple_st += str(x.r)
                    if x == Ele:
                        st += CRED + simple_st + CEND
                    else:
                        st += simple_st
                    x = x.right
                print(st)
                print("-" * len(st))
                Ele.representation()
                print("-" * len(st))
                if Ele.left:
                    Ele.left.r = Ele.result
                    Ele.left.right = Ele.right
                else:
                    if Ele.right:
                        Ele.right.left = None
                    st_ind_order = Ele.right
                if Ele.right:
                    Ele.right.l = Ele.result
                    Ele.right.left = Ele.left
    print("Result:", Ele.result)


def main():
    operation = input("Input Arithmetic Operation:").strip()
    global precedence
    precedence = [[[], []] for i in range(operation.count("(") + 1)]
    if valid_operation(operation):
        splitter(operation)
        parse()
    else:
        print("INVALID OPERATION")


if __name__ == "__main__":
    main()
