oper_value = [0, 1, 2, 3, 4, 5, 6, 7]
output = []


def parse_input(data):
    registers, operations = data.split("\n\n")
    regA, regB, regC = list(
        map(lambda x: int(x.split(":")[-1]), registers.splitlines())
    )
    program = list(map(int, operations[operations.index(":") + 1 :].split(",")))
    program = [program[i : i + 2] for i in range(0, len(program), 2)]
    return regA, regB, regC, program


# opcode: 0
def adv(operand):
    oper_value[4] //= 2 ** oper_value[operand]


# opcode: 1
def bxl(operand):
    oper_value[5] ^= operand


# opcode: 2
def bst(operand):
    oper_value[5] = oper_value[operand] % 8


# opcode: 3
def jnz():
    return oper_value[4] != 0


# opcode: 4
def bxc():
    oper_value[5] ^= oper_value[6]


# opcode: 5
def out(operand):
    output.append(oper_value[operand] % 8)


# opcode: 6
def bdv(operand):
    oper_value[5] = oper_value[4] // 2 ** oper_value[operand]


# opcode: 7
def cdv(operand):
    oper_value[6] = oper_value[4] // 2 ** oper_value[operand]


def main(data):
    regA, regB, regC, program = parse_input(data)
    oper_value[4] = regA
    oper_value[5] = regB
    oper_value[6] = regC
    i = 0
    while i < len(program):
        opcode, operand = program[i]
        print(oper_value[4:7], opcode, operand)
        if opcode == 0:
            adv(operand)
        elif opcode == 1:
            bxl(operand)
        elif opcode == 2:
            bst(operand)
        elif opcode == 3:
            if jnz():
                i = operand
                continue
        elif opcode == 4:
            bxc()
        elif opcode == 5:
            out(operand)
        elif opcode == 6:
            bdv(operand)
        elif opcode == 7:
            cdv(operand)

        i += 1

    return ",".join(map(str, output))


if __name__ == "__main__":
    with open("2024/day17/test.txt", "r") as f:
        data = f.read()
    print(main(data))
