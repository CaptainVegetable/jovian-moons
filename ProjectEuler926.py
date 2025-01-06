
def decimal_to_base(number: int, base: int) -> str:
    import math
    highest_power = int(math.log(number, base))
    exponents = [base ** power for power in range(highest_power, -1, -1)]
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_in_base = ''
    for ex in exponents:
        number_in_base += digits[(number // ex)]
        number %= ex
    return number_in_base


def decimal_to_base_zeros_only(number: int, base: int) -> str:
    import math
    highest_power = int(math.log(number, base))
    exponents = [base ** power for power in range(highest_power, -1, -1)]
    number_in_base = ''
    for ex in exponents:
        if ex > number: number_in_base += '0'
        else: number_in_base += '*'
        number %= ex
    return number_in_base


def rounding_count(number: int, base: int) -> int:
    import math
    highest_power = int(math.log(number, base))
    exponents = [base ** power for power in range(highest_power, -1, -1)]
    rounding = 0
    for ex in exponents:
        if ex > number: rounding += 1
        else: rounding = 0
        number %= ex
    return rounding


def rounding_count2(number: int, base: int) -> int:
    import math
    highest_power = int(math.log(number, base))
    rounding = 0
    for power in range(1, highest_power + 1):
        if number % (base ** power) == 0: 
            rounding = power
        else: 
            break
    return rounding


def rounding_count3(number: int, base: int, highest_power: int) -> int:
    rounding = 0
    for power in range(1, highest_power + 1):
        if number % (base ** power) == 0: 
            rounding = power
        else: 
            break
    return rounding


def main():
    testing = True
    while testing:
        num, base = tuple(map(lambda k: int(k), input("Enter: number,base or 0,0 to quit ").split(',')))
        if num > 0 and base > 1:
            print(f"{num} base {base} = {decimal_to_base(num, base)}")
        else:
            testing = False


def main2():
    import math, time
    # num = 20
    num = math.factorial(12)
    total_roundness = 0
    start_time = time.perf_counter()
    for b in range(2, num + 1):
        if num % b == 0:
            roundness = 0
            num_in_base = decimal_to_base_zeros_only(num, b)
            for digit in num_in_base[::-1]:
                if digit == '0':
                    roundness += 1
                else:
                    break
            print(f"{num} base {b} = {num_in_base}. Roundness: {roundness}")
            total_roundness += roundness
    print(f"R({num}) = {total_roundness}")
    print(f"Elapsed time: {time.perf_counter() - start_time}")


def main3():
    import math, time
    # num = 20
    num = math.factorial(12)
    total_roundness = 0
    start_time = time.perf_counter()
    for base in range(2, num + 1):
        if num % base == 0:
            roundness = rounding_count2(num, base)
            print(f"{num} base {base} Roundness: {roundness}")
            total_roundness += roundness
    print(f"R({num}) = {total_roundness}")
    print(f"Elapsed time: {time.perf_counter() - start_time}")


def main4():
    import math, time
    num = math.factorial(12)
    highest_power = int(math.log(num, 2))
    total_roundness = 0
    start_time = time.perf_counter()
    for base in range(2, num + 1):
        if num % base == 0:
            roundness = rounding_count3(num, base, highest_power)
            print(f"{num} base {base} Roundness: {roundness}")
            total_roundness += roundness
    print(f"R({num}) = {total_roundness}")
    print(f"Elapsed time: {time.perf_counter() - start_time}")


if __name__ == "__main__":
    main4()
