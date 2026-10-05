"""Command-line entry point: python -m tempconv.cli 100 --to f"""

import argparse

from tempconv.convert import celsius_to_fahrenheit, fahrenheit_to_celsius


def main(argv: list[str] | None = None) -> str:
    parser = argparse.ArgumentParser(description="Convert temperatures.")
    parser.add_argument("value", type=float, help="temperature to convert")
    parser.add_argument("--to", choices=["c", "f"], required=True, help="target unit")
    args = parser.parse_args(argv)

    if args.to == "f":
        result = f"{celsius_to_fahrenheit(args.value):.2f}°F"
    else:
        result = f"{fahrenheit_to_celsius(args.value):.2f}°C"
    print(result)
    return result


if __name__ == "__main__":
    main()
