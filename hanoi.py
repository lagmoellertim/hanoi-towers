def generate_order(n):
    s = []
    for i in range(1, n + 1):
        s.append(i)
        s.extend(s[:-1])
    return s


def generate_movement(n):
    s = [2]
    for i in range(n - 1):
        for i2 in range(-1, len(s)):
            if i % 2:
                s.append((s[i2] + 1) % 3)
            else:
                s.append((s[i2] - 1) % 3)
    return s


def output(n):
    order, movement = generate_order(n), generate_movement(n)
    if n % 2:
        filter_map = {0: "left", 1: "middle", 2: "right"}
    else:
        filter_map = {0: "left", 1: "right", 2: "middle"}

    for i in range(len(order)):
        print(
            "Move disk nr. {} to the {}".format(
                order[i],
                filter_map[movement[i]]
            )
        )


output(int(input("How many disks does your hanoi tower have?\n")))
