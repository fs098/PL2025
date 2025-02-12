import sys


SumState = tuple[int, bool]


def adder(text: str, sum: int = 0, on: bool = True) -> tuple[SumState, list[int]]:
    """
    Sums all sequences of digits found in the string `text` to the variable `sum`.
    The keywords 'off' and 'on' (case-insensitive) control pausing and resuming this summing behavior.

    Returns the final values of the variables `sum` and `on`, along with a list of sums that were recorded
    each time the '=' character was encountered.
    """
    text = text.lower()

    result = []
    current_number = ""

    i = 0
    while i < len(text):
        if on and text[i].isdigit():
            current_number += text[i]

        else:
            if len(current_number) > 0:
                sum += int(current_number)
                current_number = ""

            if text[i] == "=":
                result.append(sum)

            elif text[i] == "o":
                try:
                    if text[i + 1] == "n":  # On
                        on = True
                        i += 1

                    elif text[i + 1] == "f" and text[i + 2] == "f":  # Off
                        on = False
                        i += 2

                except IndexError:
                    pass
        i += 1

    return (sum, on), result


def main() -> None:
    match len(sys.argv):
        case 1:
            sum = 0
            on = True

            for line in sys.stdin:
                if line == "exit\n":
                    sys.exit()

                (sum, on), values = adder(line, sum, on)
                for val in values:
                    print(f"(=) {val}")

        case 2:
            _, values = adder(sys.argv[1])
            for val in values:
                print(f"(=) {val}")

        case _:
            print("invalid number of arguments", file=sys.stderr)


if __name__ == "__main__":
    main()
