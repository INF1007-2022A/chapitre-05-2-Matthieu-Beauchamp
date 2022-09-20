#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_bill(name, data):
    INDEX_NAME = 0
    INDEX_QUANTITY = 1
    INDEX_PRICE = 2

    subTotal = 0
    for item in data:
        subTotal += item[1] * item[2]

    taxes = subTotal * 0.15
    total = subTotal + taxes

    # code is duplicated...
    facture = f"{name}\n"\
        + f"{'SOUS TOTAL': <10} {subTotal: >10.2f} $\n"\
        + f"{'TAXES': <10} {taxes: >10.2f} $\n"\
        + f"{'TOTAL': <10} {total: >10.2f} $"

    return facture


# pretty ugly isn't it
def format_number(number, num_decimal_digits):
    formatted = ""
    num = str(number).split(".")

    if (len(num) == 2):
        num[1] = str(round(int(num[1])
                           * 10**(num_decimal_digits - len(num[1]))))

    packs = []

    if len(num) == 2:
        decPacks = ["."]
        triplet = ""
        for digit in num[1]:
            triplet += digit
            if len(triplet) == 3:
                decPacks.append(triplet)
                triplet = ""

        if triplet != "":
            decPacks.append(triplet)

        packs = decPacks
        packs.reverse()

    triplet = ""
    for i in range(len(num[0])-1, 0, -1):
        digit = num[0][i]
        if digit.isdigit():
            triplet = str(digit) + triplet

        if len(triplet) == 3:
            packs.append(triplet)
            triplet = ""

    if triplet != "":
        packs.append(triplet)

    packs.reverse()

    for pack in packs:
        if len(pack) != 1:
            formatted += pack + " "
        else:
            formatted = formatted.rstrip()
            formatted += pack

    formatted = formatted.rstrip()

    return formatted


def get_triangle(num_rows):
    if num_rows < 0:
        raise ValueError("Cannot do a negative number of rows")

    width = 2 + 1 + num_rows * 2
    hori = "+" * width

    triangle = hori + "\n"
    rowNum = 0
    while rowNum < num_rows:
        nSpaces = (width - 3 - 2 * rowNum) // 2  # technically always even
        nA = 0 if num_rows == 0 else 1 + 2 * rowNum
        triangle += "+" + " " * nSpaces + "A" * nA + " " * nSpaces + "+\n"
        rowNum += 1

    return triangle + hori


if __name__ == "__main__":
    print(get_bill("Äpik Gämmör", [
          ("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

    print(format_number(-12345.678, 2))

    print(get_triangle(2))
    print(get_triangle(5))
