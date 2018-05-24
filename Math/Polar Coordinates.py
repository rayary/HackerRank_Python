import cmath
import re

if __name__ == "__main__":
    x,y = map(float, re.findall('[+-]?\d+\.?\d*', input().strip()))

    print(abs(complex(x, y)))
    print(cmath.phase(complex(x, y)))
