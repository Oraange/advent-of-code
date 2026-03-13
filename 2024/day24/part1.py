import re
from collections import deque

with open("2024/day24/input.txt") as f:
    data_input, data_opr = map(lambda x: x.splitlines(), f.read().split("\n\n"))

ops = {}
dq = deque()

for do in data_opr:
    var1, opr, var2, _, res = do.split()
    dq.append((var1, opr, var2, res))

for di in data_input:
    key, val = di.split(": ")
    ops[key] = int(val)

while dq:
    oprd1, oprator, oprd2, res = dq.popleft()
    if oprd1 in ops and oprd2 in ops:
        match oprator:
            case "OR":
                ops[res] = ops[oprd1] | ops[oprd2]
            case "AND":
                ops[res] = ops[oprd1] & ops[oprd2]
            case "XOR":
                ops[res] = ops[oprd1] ^ ops[oprd2]
        continue
    dq.append((oprd1, oprator, oprd2, res))

z_values = list(filter(lambda x: re.match(r"^z\d\d$", x), ops.keys()))
z_values.sort()

ans = 0
for i in range(len(z_values)):
    ans += ops[z_values[i]] * 2**i

print(ans)
