"""
Arithmetic Operations visualized in a tree

This is the basic model of the project, updated as of 24/08/2023

"""
__author__ = "Selvaganapathy K"
__email__ = "selvaganz1285@gmail.com"


import re

high_precedence = []
low_precedence = []


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
    for i in range(len(operation)):
        if operation[i].isdigit():
            ext += operation[i]
        else:
            oper = operation[i]
            left = ext
            right = ""
            for j in range(i + 1, len(operation)):
                if operation[j].isdigit():
                    right += operation[j]
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
                high_precedence.append(root)
            else:
                low_precedence.append(root)
            ext = ""


def valid_operation(operation):
    """
    check if given input is a valid Arithmetic Operation
    """
    pattern = r"^[0-9][0-9+\-*/]*[0-9]$"
    return re.match(pattern, operation)


def parse():
    """
    Parses through the Arithmetic operation and executes
        1. Follow precedence rule

    """
    for Ele in high_precedence + low_precedence:
        Ele.result = int(eval(str(Ele.l) + Ele.op + str(Ele.r)))
        Ele.representation()
        if Ele.left:
            Ele.left.r = Ele.result
            Ele.left.right = Ele.right
        if Ele.right:
            Ele.right.l = Ele.result
            Ele.right.left = Ele.left
    print(Ele.result)


def main():
    operation = input().strip()
    if valid_operation(operation):
        splitter(operation)
        parse()
    else:
        print("INVALID OPERATION")


if __name__ == "__main__":
    main()
