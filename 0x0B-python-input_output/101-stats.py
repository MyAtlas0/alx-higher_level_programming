#!/usr/bin/python3
"""
Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


import sys

def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {} bytes".format(size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            line_parts = line.split()

            # Extract file size
            try:
                file_size = int(line_parts[-1])
                size += file_size
            except (IndexError, ValueError):
                print("Error: Invalid format for line {}, skipping.".format(count))
                continue

            # Extract status code
            try:
                status_code = line_parts[-2]
                if status_code in valid_codes:
                    status_codes[status_code] = status_codes.get(status_code, 0) + 1
            except IndexError:
                print("Error: No status code found for line {}, skipping.".format(count))
                continue

            # Print statistics every 10 lines
            if count % 10 == 0:
                print_stats(size, status_codes)

        # Print final statistics if lines are not multiples of 10
        if count % 10 != 0:
            print_stats(size, status_codes)

    except KeyboardInterrupt:
        # Print final statistics on keyboard interruption
        print_stats(size, status_codes)
        raise
