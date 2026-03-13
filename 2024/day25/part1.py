import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    data = f.read().strip()


class TumblerLock:
    def __init__(self, schematic, lock_type):
        self.schematic = schematic
        self.lock_type = lock_type

    def get_pin_scheme(self):
        scheme = []

        for j in range(len(self.schematic[0])):
            pin_counter = 0
            for i in range(len(self.schematic)):
                if self.lock_type == "lock":
                    if i == 0:
                        continue
                else:
                    if i == len(self.schematic) - 1:
                        continue
                pin_counter += self.schematic[i][j] == "#"

            scheme.append(pin_counter)

        return scheme

    @staticmethod
    def is_matched_pin(lock: "TumblerLock", key: "TumblerLock"):
        lock_scheme = lock.get_pin_scheme()
        key_scheme = key.get_pin_scheme()

        for lock, key in zip(lock_scheme, key_scheme):
            if lock + key > 5:
                return False

        return True


def parse(data):
    lock_set = data.split("\n\n")
    locks, keys = [], []

    for lock in lock_set:
        if lock.startswith("#"):
            locks.append(lock.splitlines())
        else:
            keys.append(lock.splitlines())

    return locks, keys


def main(data):
    locks, keys = parse(data)
    ans = 0

    for lock in locks:
        lock_obj = TumblerLock(lock, "lock")
        for key in keys:
            key_obj = TumblerLock(key, "key")
            ans += TumblerLock.is_matched_pin(lock_obj, key_obj)

    return ans


print(main(data))
