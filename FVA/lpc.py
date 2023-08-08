import numpy as np

def autocorr(x, nlags=None):
    N = len(x)
    if nlags == None: nlags = N
    r = np.zeros(nlags)
    for lag in range(nlags):
        for n in range(N - lag):
            r[lag] += x[n] * x[n + lag]
    return r


def LevinsonDurbin(r, lpcOrder):
    a = np.zeros(lpcOrder + 1)
    e = np.zeros(lpcOrder + 1)
    a[0] = 1.0
    a[1] = - r[1] / r[0]
    e[1] = r[0] + r[1] * a[1]
    lam = - r[1] / r[0]
    for k in range(1, lpcOrder):
        lam = 0.0
        for j in range(k + 1):
            lam -= a[j] * r[k + 1 - j]
        lam /= e[k]
        U = [1]
        U.extend([a[i] for i in range(1, k + 1)])
        U.append(0)
        V = [0]
        V.extend([a[i] for i in range(k, 0, -1)])
        V.append(1)
        a = np.array(U) + lam * np.array(V)
        e[k + 1] = e[k] * (1.0 - lam * lam)
    return a, e[-1]
def lpc(s, lpcOrder=32):
    r = autocorr(s, lpcOrder + 1)
    a, e  = LevinsonDurbin(r, lpcOrder)
    return a,e
def residual_error(a, s):
    lpcOrder=len(a)
    r_error=s.copy()

    for i in range(lpcOrder, len(s)):
        for j in range (0,lpcOrder):
            r_error[i] += (a[j] * s[i-j-1])
    r_error[0:lpcOrder-1]=0.0

    return r_error