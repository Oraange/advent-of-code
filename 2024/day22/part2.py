from tqdm import tqdm

with open("2024/day22/input.txt") as f:
    data = f.read()
    secrets = data.splitlines()

step1 = lambda x: (x ^ (x * 64)) % 16777216
step2 = lambda x: (x ^ (x // 32)) % 16777216
step3 = lambda x: (x ^ (x * 2048)) % 16777216


def get_2000_secret(secret):
    secret_num = [secret % 10]
    profit = {}

    for i in range(2000):
        secret = step3(step2(step1(secret)))
        secret_num.append(secret % 10)

        if i >= 5:
            changes = [secret_num[j] - secret_num[j - 1] for j in range(i - 2, i + 2)]
            if not tuple(changes) in profit:
                profit[tuple(changes)] = secret % 10

    return profit


profits = [get_2000_secret(int(secret)) for secret in tqdm(secrets)]


def get_total_profit(secret):
    ans = 0
    for profit in profits:
        if secret in profit:
            ans += profit[secret]

    return ans


scrs = set()
for profit in tqdm(profits):
    scrs = scrs.union(profit.keys())

best = 0
for s in tqdm(scrs):
    best = max(best, get_total_profit(s))

print(best)
