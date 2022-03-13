import random

acorns = [1 ,2 ,3 ,4 ,5 ,6]
print(random.choice([True] * len(acorns) + [False] * (10 - len(acorns))))