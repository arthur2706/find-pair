#!/usr/bin/python

import sys
import os.path
import argparse

def sum_price(gifts):
    return sum(g['price'] for g in gifts)

def find_gifts_trio(gifts, budget):
    trio = []
    for i in range(len(gifts)):
        gifts_excluding_i = gifts[0:i-1] + gifts[i+1:]
        pair = find_gifts_pair(gifts_excluding_i, budget - gifts[i]['price'])
        # print "pair {0}".format(pair)
        if len(pair):
            candidate = [gifts[i]] + pair
            # print "candidate {0}".format(candidate)
            trio = candidate if sum_price(trio) < sum_price(candidate) else trio

    return trio


# Runtime complexity if O[N], where N is number of gifts/lines in file.
def find_gifts_pair(gifts, budget):
    high = len(gifts) - 1
    low = 0

    while high > low:
        # print "high {0}".format(gifts[high])
        # print "low {0}".format(gifts[low])
        if (gifts[low]['price'] + gifts[high]['price']) > budget:
            #print "dec high"
            high -= 1
        elif (gifts[low + 1]['price'] + gifts[high]['price']) <= budget:
            #print "inc low"
            low += 1
        else:
            #print "break"
            break

    if low != high:
        return [gifts[low], gifts[high]]
    else:
        return []


def print_result(selected_gifts):
    if len(selected_gifts):
        print ", ".join(map(lambda gift: gift['name'] + ' ' + str(gift['price']), selected_gifts))
    else:
        print "Not possible"


def validate(gifts_file, budget):
    f = open(gifts_file, "r")
    gifts = []
    for line in f:
        name, price = line.split(',')
        name = name.strip()
        price = int(price.strip())
        if not len(name) or price <= 0:
            raise ValueError("Failed to validate, provide a valid gifts price list and budget.")

        gifts.append({'name': name, 'price': price})
        # check sorted

    return gifts, int(budget)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str, help="gifts prices file")
    parser.add_argument("b", type=int, help="the budget")
    parser.add_argument("-t", action="store_true", help="run in trio mode.")
    args = parser.parse_args()

    try:
        gifts, budget = validate(args.f, args.b)
        if args.t:
            print_result(find_gifts_trio(gifts, budget))
        else:
            print_result(find_gifts_pair(gifts, budget))
    except Exception as error:
            print repr(error)


if __name__ == "__main__":
    main()
