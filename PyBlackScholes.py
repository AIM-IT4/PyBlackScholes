from scipy.stats import norm

def cnd(x):
    return norm.cdf(x)

def d1(S, K, r, T, sigma):
    return (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))

def d2(S, K, r, T, sigma):
    return d1(S, K, r, T, sigma) - sigma * np.sqrt(T)

def black_scholes(type, S, K, r, T, sigma):
    if type == "call":
        return S * cnd(d1(S, K, r, T, sigma)) - K * np.exp(-r * T) * cnd(d2(S, K, r, T, sigma))
    elif type == "put":
        return K * np.exp(-r * T) * cnd(-d2(S, K, r, T, sigma)) - S * cnd(-d1(S, K, r, T, sigma))
