denominations = sorted([50, 100, 200, 500, 1000, 2000, 5000], reverse=True)
 
def atm(n):
    result = 0
    for denomination in denominations:
        while n >= denomination:
            n -= denomination
            result += 1
    return (result if n == 0 else -1)

print(atm(7700))
