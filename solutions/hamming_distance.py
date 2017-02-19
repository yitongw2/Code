
def hammingDistance(x, y):
        x = x^y
        y = 0
        while (x):
            y += 1
            x = x & (x-1)
        return y
        
