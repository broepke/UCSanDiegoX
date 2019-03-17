
def conditional__probability(rA, wA, rB, wB):
    # inputs: all of them are of type 'float'
    # output: a variable of type 'float'

    # First calcluate the total probability
    total_prob = (.5 * wA/(rA+wA)) + (.5 * wB/(rB+wB))

    # bayes rule
    bayes = wA/(rA+wA) * .5 / total_prob

    return bayes


assert( abs(conditional__probability(2., 4., 3., 3.) -0.5714285714285715) < 10**-5)
assert( abs(conditional__probability(1., 3., 5., 2.) -0.7241379310344829) < 10**-5)
