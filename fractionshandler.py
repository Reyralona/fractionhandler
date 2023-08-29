from math import lcm, gcd
from operator import sub, mul
from functools import reduce

def simplify_fraction(num, den):
    if (num % den == 0):
        return [num, den]
    else:
        g = gcd(abs(num), abs(den))
        num = num // g
        den = den // g
        if (num < den):
            if (num < 0):
                rem = int('-' + str(abs(num) % abs(den)))
                mi = int('-' + str(abs(num) // abs(den)))
            else:
                rem = abs(num) % abs(den)
                mi = abs(num) // abs(den)
            
            if(mi == 0):
                return[rem, den]
            else:
                return[mi, rem, den]
        elif (num % den != 0):
            mi = num // den
            rem = num % den
            return[mi, rem, den]

def equal_denominators(*fractions):
    denominators = list(i[1] for i in list(*fractions))
    return True if len(set(denominators)) == 1 else False

def invert_fractions(*fractions):
    newfractions = list([i[1], i[0]] for i in fractions)
    return newfractions

def mult_fractions(*fractions):
    return [reduce(mul, (list(i[0] for i in fractions))), reduce(mul, (list(i[1] for i in fractions)))]

def fraction_sum(*fractions):
    if (equal_denominators(fractions)):
        return simplify_fraction((sum(list(i[0] for i in fractions))), fractions[0][1])
        
    else:
        newden = lcm(*list(i[1] for i in fractions))
        return fraction_sum(*list(mult_fractions([i[0], i[1]], [newden//i[1], newden//i[1]]) for i in fractions))

def fraction_sub(*fractions):
    if (equal_denominators(fractions)):
        return simplify_fraction(reduce(sub, (list([i[0] for i in fractions]))), fractions[0][1])
    else:
        newden = lcm(*list(i[1] for i in fractions))
        return fraction_sub(*list(mult_fractions([i[0], i[1]], [newden//i[1], newden//i[1]]) for i in fractions))

def fraction_mul(*fractions):
    return simplify_fraction(*mult_fractions(*fractions))

def fraction_div(*fractions):
    first = fractions[0]
    newfractions = invert_fractions(*fractions[1:])
    return fraction_mul(first, *newfractions)

exp = fraction_sum(fraction_sum([2,3], [3,5]), fraction_sum([1,3], [3, 5]))
print(exp)
