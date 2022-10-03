import sys
import csv


def reshape():
    print("please insert csv and press ctrl + d to finish input:\n")
    info = []

    # read from stdin, use ctrl+d to finish input
    for line in csv.reader(sys.stdin.readlines()):
        info.append(line)

    if len(info) == 0 or len(info) == 1:
        print("invalid length")

    # generate output and write to stdout
    else:
        len_row = len(info)
        len_col = len(info[0])

        padding(info, len_col)

        output = csv.writer(sys.stdout)
        output.writerow(['country', 'year', 'cases'])
        for col in range(1, len_col):
            for row in range(1, len_row):
                output.writerow([info[row][0], info[0][col], info[row][col]])


# add paddings to lines that have less element than the header
def padding(info, max_length):
    for line in info:
        while len(line) < max_length:
            line.append("NA")


if __name__ == '__main__':
    reshape()
