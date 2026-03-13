def main(data: str):
    secrets = data.splitlines()
    ans = 0
    step1 = lambda x: (x ^ (x * 64)) % 16777216
    step2 = lambda x: (x ^ (x // 32)) % 16777216
    step3 = lambda x: (x ^ (x * 2048)) % 16777216

    for secret in secrets:
        for _ in range(2000):
            secret = step3(step2(step1(int(secret))))
        ans += secret

    return ans


if __name__ == "__main__":
    with open("2024/day22/input.txt") as f:
        data = f.read()

    print(main(data))
