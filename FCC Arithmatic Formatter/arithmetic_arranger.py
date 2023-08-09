import re


def arithmetic_arranger(problems, showOutput=False):
    answers, outputWidth, operations, numbers = [], [], [], []
    arranged_problems = ""
    err = False

    if len(problems) <= 5:  # Parse them and split them into cleaner lists
        for problem in problems:
            operands = re.split("\s+", problem)

            if operands[1] not in ("+", "-"):
                arranged_problems = "Error: Operator must be '+' or '-'."
                err = True
                break
            elif len(operands) > 3:
                arranged_problems = "Error: Too many numerical entries."
                err = True
                break
            else:
                if len(re.findall("\D", operands[0])) > 0 or len(
                        re.findall("\D", operands[2])) > 0:
                    arranged_problems = "Error: Numbers must only contain digits."
                    err = True
                    break
                elif len(operands[0]) > 4 or len(operands[2]) > 4:
                    arranged_problems = "Error: Numbers cannot be more than four digits."
                    err = True
                    break

            if operands[1] == "+":
                # addition
                answers.append(int(operands[0]) + int(operands[2]))
                operations.append("+")
            else:
                answers.append(int(operands[0]) - int(operands[2]))
                operations.append("-")

            outputWidth.append(max(len(operands[0]), len(operands[2])) + 2)
            numbers.append([operands[0], operands[2]])

    else:
        arranged_problems = "Error: Too many problems."
        err = True

    if not err:

        for count, number in enumerate(numbers):  # process the first line
            for i in range(outputWidth[count] - len(number[0])):
                arranged_problems += " "
            arranged_problems += number[0]

            if count != (len(numbers) - 1):
                arranged_problems += "    "
            else:
                arranged_problems += "\n"

        for count, operation in enumerate(operations):  # process the second line
            arranged_problems += operation

            for i in range(outputWidth[count] - len(numbers[count][1]) - 1):
                arranged_problems += " "
            arranged_problems += numbers[count][1]

            if count != (len(numbers) - 1):
                arranged_problems += "    "
            else:
                arranged_problems += "\n"

        for count, number in enumerate(numbers):  # process the third line
            for i in range(outputWidth[count]):
                arranged_problems += "-"

            if count != (len(numbers) - 1):
                arranged_problems += "    "

        if showOutput:
            arranged_problems += "\n"
            for count, answer in enumerate(answers):  # process the answer line
                for i in range(outputWidth[count] - len(str(answer))):
                    arranged_problems += " "
                arranged_problems += str(answer)

                if count != (len(answers) - 1):
                    arranged_problems += "    "

    return arranged_problems

# print(
#  arithmetic_arranger(['3801 - 2', '123 + 49']))
