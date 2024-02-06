#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


import sys

def print_stats(size, status_codes, count):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
        count (int): The number of lines processed.
    """
    print("Statistics after processing {} lines:".format(count))
    print("Total file size: {} bytes".format(size))
    print("Status code counts:")
    for code, count in status_codes.items():
        print("    {}: {}".format(code, count))

if __name__ == "__main__":
    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            line_parts = line.split()

            try:
                size += int(line_parts[-1])
            except (IndexError, ValueError):
                print("Error: Invalid format for line {}, skipping.".format(count))
                continue

            try:
                code = line_parts[-2]
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1
            except IndexError:
                print("Error: No status code found for line {}, skipping.".format(count))
                continue

            if count % 10 == 0:
                print_stats(size, status_codes, count)
                size = 0
                status_codes = {}

        if count % 10 != 0:
            print_stats(size, status_codes, count)

    except KeyboardInterrupt:
        print_stats(size, status_codes, count)
        raise
