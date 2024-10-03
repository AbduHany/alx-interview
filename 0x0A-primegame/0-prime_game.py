#!/usr/bin/python3
""" This module defines the isWinner function
"""


def is_prime(n):
    """ This function returns True if n is a prime number
    """
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 5
    while f <= r:
        print('\t', f)
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def isWinner(x, nums):
    """ This function prints the winner of the primeGame.
    either Ben or Maria.
    Args:
        x (int): number of rounds
        nums (list): list of numbers
    """
    rounds = dict()
    maria_wins = 0
    ben_wins = 0
    for number in nums:
        if number in rounds:
            if rounds[number] == "Maria":
                maria_wins += 1
            else:
                ben_wins += 1
            continue
        roster = [x for x in range(1, number + 1)]
        maria = []
        ben = []
        maria_turn = True
        i = 0
        while i < len(roster):
            if len(roster) == 1 and (not is_prime(roster[0])):
                if maria_turn:
                    rounds[number] = "Ben"
                    ben_wins += 1
                else:
                    rounds[number] = "Maria"
                    maria_wins += 1
            choice = roster[i]
            if is_prime(choice):
                if maria_turn:
                    maria.append(choice)
                    roster.remove(choice)
                    j = 0
                    while j < len(roster):
                        if roster[j] % choice == 0:
                            maria.append(roster[j])
                            roster.remove(roster[j])
                        j += 1
                else:
                    ben.append(choice)
                    roster.remove(choice)
                    j = 0
                    while j < len(roster):
                        if roster[j] % choice == 0:
                            ben.append(roster[j])
                            roster.remove(roster[j])
                        j += 1
                i = 0
                maria_turn = not maria_turn
            else:
                i += 1
    return "Ben" if ben_wins > maria_wins else "Maria"
