import random
def get_zigzag_range(num_of_bits):
    lower_bound = - 2**(num_of_bits - 1)
    upper_bound = 2**(num_of_bits - 1) - 1
    return (lower_bound, upper_bound)

def random_array_generator():
    return random.randint(-4, 3)


def main():
    # print("3", get_zigzag_range(3))
    # print("4", get_zigzag_range(4))
    # print("8", get_zigzag_range(8))
    # print("10", get_zigzag_range(10))
    # print("16", get_zigzag_range(16))

    print([random_array_generator() for _ in range(14)])


if __name__ == "__main__":
    main()