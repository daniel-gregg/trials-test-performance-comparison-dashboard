"""
Module to return prices as fixed prices or simulated prices
"""

# data packages
import pandas as pd
import numpy as np
rng = np.random.default_rng() # Creates a default random number generator


def wheat_price_sim(s = 100):
    # Simulate wheat prices from normal distribution
    # Wheat prices appear roughly normally distributed but with a censored lower tail at ~$210 AUD (real prices)
    # see here: https://agprice.sfs.org.au/
    rands = rng.normal(loc=350, scale=60, size=s)
    rands[rands < 200] = 200

    return rands

def get_decile_prices_value_from_dict(decile_dict, rand_value):

    # check rand_value is a float
    if not isinstance(rand_value, float):
        ValueError("rand_value must be a float between 0 and 1")
    # check rand_value is between 0 and 1
    if rand_value < 0:
        ValueError("rand_value must be between 0 and 1")
    if rand_value >1:
        ValueError("rand_value must be between 0 and 1")

    if rand_value < 0.1:
        return {'lower' : decile_dict["0"], "upper" : decile_dict["1"]}
    elif rand_value < 0.2:
        return {'lower' : decile_dict["1"], "upper" : decile_dict["2"]}
    elif rand_value < 0.3:
        return {'lower' : decile_dict["2"], "upper" : decile_dict["3"]}
    elif rand_value < 0.4:
        return {'lower' : decile_dict["3"], "upper" : decile_dict["4"]}
    elif rand_value < 0.5:
        return {'lower' : decile_dict["4"], "upper" : decile_dict["5"]}
    elif rand_value < 0.6:
        return {'lower' : decile_dict["5"], "upper" : decile_dict["6"]}
    elif rand_value < 0.7:
        return {'lower' : decile_dict["6"], "upper" : decile_dict["7"]}
    elif rand_value < 0.8:
        return {'lower' : decile_dict["7"], "upper" : decile_dict["8"]}
    elif rand_value < 0.9:
        return {'lower' : decile_dict["8"], "upper" : decile_dict["9"]}
    elif rand_value < 1.0:
        return {'lower' : decile_dict["9"], "upper" : decile_dict["10"]}

def fababean_price_sim(s = 100):
    # Fababean distributions are highly non-normal with bimodality and other peak/tail patterns
    # that are not easily described by a distribution
    # We use a decile approach with each decile having a uniform distribution and sampling from each of those
    #  with a probability of 10% (as they are deciles)

    decile_dict = {
        "0" : 281,
        "1" : 319,
        "2" : 338,
        "3" : 346,
        "4" : 407,
        "5" : 449,
        "6" : 475,
        "7" : 490,
        "8" : 500,
        "9" : 571,
        "10": 746
    }
    # note '0' refers to min and '10' refers to max

    rands = rng(size = s)

    rands = [
        rng.uniform(low = get_decile_prices_value_from_dict(decile_dict, i)['lower'],
                    high = get_decile_prices_value_from_dict(decile_dict, i)['upper'])
        for i in rands
    ]

    return rands


def peas_price_sim(s = 100):
    # Peas price distributions are highly non-normal with bimodality and other peak/tail patterns
    # that are not easily described by a distribution
    # We use a decile approach with each decile having a uniform distribution and sampling from each of those
    #  with a probability of 10% (as they are deciles)

    decile_dict = {
        "0" : 357,
        "1" : 402,
        "2" : 422,
        "3" : 438,
        "4" : 458,
        "5" : 472,
        "6" : 482,
        "7" : 498,
        "8" : 556,
        "9" : 587,
        "10": 666
    }
    # note '0' refers to min and '10' refers to max

    rands = rng(size = s)

    rands = [
        rng.uniform(low = get_decile_prices_value_from_dict(decile_dict, i)['lower'],
                    high = get_decile_prices_value_from_dict(decile_dict, i)['upper'])
        for i in rands
    ]

    return rands


def oats_price_sim(s = 100):
    # Oats price distributions are highly non-normal with bimodality and other peak/tail patterns
    # that are not easily described by a distribution
    # We use a decile approach with each decile having a uniform distribution and sampling from each of those
    #  with a probability of 10% (as they are deciles)

    decile_dict = {
        "0" : 251,
        "1" : 287,
        "2" : 298,
        "3" : 314,
        "4" : 324,
        "5" : 340,
        "6" : 370,
        "7" : 400,
        "8" : 440,
        "9" : 474,
        "10": 561
    }
    # note '0' refers to min and '10' refers to max

    rands = rng(size = s)

    rands = [
        rng.uniform(low = get_decile_prices_value_from_dict(decile_dict, i)['lower'],
                    high = get_decile_prices_value_from_dict(decile_dict, i)['upper'])
        for i in rands
    ]

    return rands


def lupins_price_sim(s = 100):
    # Lupins price distributions are highly non-normal with bimodality and other peak/tail patterns
    # that are not easily described by a distribution
    # We use a decile approach with each decile having a uniform distribution and sampling from each of those
    #  with a probability of 10% (as they are deciles)

    decile_dict = {
        "0" : 232,
        "1" : 287,
        "2" : 299,
        "3" : 324,
        "4" : 342,
        "5" : 349,
        "6" : 358,
        "7" : 375,
        "8" : 388,
        "9" : 448,
        "10": 591
    }
    # note '0' refers to min and '10' refers to max

    rands = rng(size = s)

    rands = [
        rng.uniform(low = get_decile_prices_value_from_dict(decile_dict, i)['lower'],
                    high = get_decile_prices_value_from_dict(decile_dict, i)['upper'])
        for i in rands
    ]

    return rands


def barley_price_sim(s = 100):
    # Simulate barley prices from normal distribution
    # Barley prices appear roughly normally distributed but with a censored lower tail at ~$150 AUD (real prices)
    # see here: https://agprice.sfs.org.au/
    rands = rng.normal(loc=310, scale=50, size=s)
    rands[rands < 150] = 150

    return rands


def canola_price_sim(s = 100):
    # Canola price distributions are highly non-normal with bimodality and other peak/tail patterns
    # that are not easily described by a distribution
    # We use a decile approach with each decile having a uniform distribution and sampling from each of those
    #  with a probability of 10% (as they are deciles)

    decile_dict = {
        "0" : 495,
        "1" : 540,
        "2" : 559,
        "3" : 578,
        "4" : 599,
        "5" : 630,
        "6" : 664,
        "7" : 700,
        "8" : 731,
        "9" : 811,
        "10": 1134
    }
    # note '0' refers to min and '10' refers to max

    rands = rng(size = s)

    rands = [
        rng.uniform(low = get_decile_prices_value_from_dict(decile_dict, i)['lower'],
                    high = get_decile_prices_value_from_dict(decile_dict, i)['upper'])
        for i in rands
    ]

    return rands


def lucerne_price_sim(s = 100):
    # Lucerne price distributions are highly non-normal with bimodality and other peak/tail patterns
    # that are not easily described by a distribution
    # We use a decile approach with each decile having a uniform distribution and sampling from each of those
    #  with a probability of 10% (as they are deciles)

    decile_dict = {
        "0" : 198,
        "1" : 327,
        "2" : 355,
        "3" : 373,
        "4" : 396,
        "5" : 414,
        "6" : 449,
        "7" : 498,
        "8" : 529,
        "9" : 621,
        "10": 805
    }
    # note '0' refers to min and '10' refers to max

    rands = rng(size = s)

    rands = [
        rng.uniform(low = get_decile_prices_value_from_dict(decile_dict, i)['lower'],
                    high = get_decile_prices_value_from_dict(decile_dict, i)['upper'])
        for i in rands
    ]

    return rands


def pasture_price_sim(s = 100):
    # Pasture price distributions are highly non-normal with bimodality and other peak/tail patterns
    # that are not easily described by a distribution
    # We use a decile approach with each decile having a uniform distribution and sampling from each of those
    #  with a probability of 10% (as they are deciles)

    decile_dict = {
        "0" : 102,
        "1" : 173,
        "2" : 190,
        "3" : 207,
        "4" : 226,
        "5" : 243,
        "6" : 277,
        "7" : 304,
        "8" : 342,
        "9" : 394,
        "10": 591
    }
    # note '0' refers to min and '10' refers to max

    rands = rng(size = s)

    rands = [
        rng.uniform(low = get_decile_prices_value_from_dict(decile_dict, i)['lower'],
                    high = get_decile_prices_value_from_dict(decile_dict, i)['upper'])
        for i in rands
    ]

    return rands