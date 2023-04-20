""" Matrix - Tetris
You are given a following process.

There is a platform with n columns. 1×1 squares are appearing one after another
in some columns on this platform. If there are no squares in the column, a
square will occupy the bottom row. Otherwise, a square will appear at the top
of the highest square of this column.

When all the n columns have at least one square in them, the bottom row is
being removed. You will receive 1 point for this, and all the squares left
will fall down one row.

Your task is to calculate the amount of points you will receive.

3 9  n, m
1 1 2 2 2 3 1 2 3


[1, 0, 0, 1] => False
[1, 1, 1, 1] => True
"""


def check_row(row: list) -> bool:
    return all(row)


arr = [1, 1, 2, 2, 2, 3, 1, 2, 3]
matrix = [
    [],
    [],
    [],
]
