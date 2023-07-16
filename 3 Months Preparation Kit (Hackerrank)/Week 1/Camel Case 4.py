# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

instructions = [line.rstrip("\n\r") for line in sys.stdin.readlines()]

for command in instructions:
    op_type = command[:1]
    operation = command[2:3]
    keyword = command[4:]
    res = ""

    if op_type == "C":
        if operation == "M":
            res = (
                keyword.split()[0].lower()
                + "".join([alpha.capitalize() for alpha in keyword.split()[1:]])
                + "()"
            )
        elif operation == "C":
            res = "".join([alpha.capitalize() for alpha in keyword.split()])
        else:
            res = keyword.split()[0].lower() + "".join(
                [alpha.capitalize() for alpha in keyword.split()[1:]]
            )
    else:
        if operation == "M":
            step = 0
            for i in range(len(keyword)):
                if keyword[i].isupper():
                    res += keyword[step:i] + " "
                    step = i
            res += keyword[step:-2]
            res = res.lower()
        elif operation == "C":
            step = 0
            for i in range(1, len(keyword)):
                if keyword[i].isupper():
                    res += keyword[step:i] + " "
                    step = i
            res += keyword[step:]
            res = res.lower()
        else:
            step = 0
            for i in range(len(keyword)):
                if keyword[i].isupper():
                    res += keyword[step:i] + " "
                    step = i
            res += keyword[step:]
            res = res.lower()
    print(res)
