import argparse

def parser_function():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format",
                        help='set format of output',
                        default='stylish', type=str
    )

    return parser.parse_args()

def main():
    parser_function()


if __name__ == "__main__":
    main()