SAMPLE = False

CHAR_TO_DIGIT = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
}

DIGIT_TO_CHAR = {
    2: '2',
    1: '1',
    0: '0',
    -1: '-',
    -2: '=',
}

def snafu_to_decimal(snafu):
    decimal = 0
    for ind, char in enumerate(reversed(snafu)):
        decimal += pow(5, ind) * CHAR_TO_DIGIT[char]
    return decimal

def decimal_to_snafu(decimal):
    snafu = ''
    digit = 0
    while decimal > 0:
        mod = decimal % 5
        if mod >= 3:
            snafu = DIGIT_TO_CHAR[mod - 5] + snafu
            decimal = int((decimal + mod) / 5)
        else:
            snafu = DIGIT_TO_CHAR[mod] + snafu
            decimal = int((decimal - mod) / 5)
        digit += 1
    return snafu

DECIMAL_SNAFU = [
    (1, '1'),
    (2, '2'),
    (3, '1='),
    (4, '1-'),
    (5, '10'),
    (6, '11'),
    (7, '12'),
    (8, '2='),
    (9, '2-'),
    (10, '20'),
    (15, '1=0'),
    (20, '1-0'),
    (2022, '1=11-2'),
    (12345, '1-0---0'),
    (314159265, '1121-1110-1=0'),
]

for decimal, snafu in DECIMAL_SNAFU:
    assert snafu_to_decimal(snafu) == decimal
    assert decimal_to_snafu(decimal) == snafu

with open(f"dec25{'-sample' if SAMPLE else ''}.txt") as file:
    snafu_numbers = [line.rstrip() for line in file]
    decimal_numbers = [snafu_to_decimal(snafu) for snafu in snafu_numbers]
    print(f'Part One: {decimal_to_snafu(sum(decimal_numbers))}')
