from numpy import random

def seq_sum(n):

    s = sum(random.rand(n)>0.5)
    return s


def estimate_prob(n, k1, k2, m):
    """Estimate the probability that n flips of a fair coin result in k1 to k2 heads
         n: the number of coin flips (length of the sequence)
         k1,k2: the trial is successful if the number of heads is
                between k1 and k2-1
         m: the number of trials (number of sequences of length n)

         output: the estimated probability
         """
    count_yes = 0

    for i in range(m):
        s = seq_sum(n)
        if k1 <= s < k2:
            count_yes += 1

    return  count_yes / m

x = estimate_prob(100,45,55,1000)
print(x)
assert 'float' in str(type(x))