import argparse

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(
        description="Simple CLI temperature converter: Celsius ↔ Fahrenheit"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-c", "--celsius", type=float, help="Temperature in Celsius")
    group.add_argument("-f", "--fahrenheit", type=float, help="Temperature in Fahrenheit")

    args = parser.parse_args()

    if args.celsius is not None:
        converted = c_to_f(args.celsius)
        print(f"{args.celsius}°C is {converted:.2f}°F")
    elif args.fahrenheit is not None:
        converted = f_to_c(args.fahrenheit)
        print(f"{args.fahrenheit}°F is {converted:.2f}°C")

if __name__ == "__main__":
    main()
