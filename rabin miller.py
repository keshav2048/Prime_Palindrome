import random
import time
list_ = []
link = []
q = int(input("enter the first number: \n"))
y = int(input("enter the second number: \n"))
start_time = time.time()

if q == 1:
    q += 1
if q <= 0:
    q = 2


def is_prime(j, y=5):
    k = 1
    if j in [2, 3]:
        return True
    if j % 2 == 0 or j % 3 == 0:
        return False
    # first step j-1 = 2k.n
    n = j-1
    while n % 2 == 0:
        k += 1
        n = n/2
    for i in range(y):
        # second step 1<a<j-1
        a = random.randint(2, j - 1)
        # Third step b= a^n mod j
        b = pow(a, int(n), j)
        if b == 1 or b == j-1:
            continue
        for _ in range(k - 1):
            b = pow(int(b), 2, j)
            if b == j - 1:
                break
        else:
            return False
    return True


if len(str(q)) % 2 == 0:
    g = int((len(str(q))/2)-1)
else:
    g = int(len(str(q))/2)

m = int(q / (10 ** g))
if m > 10:
    m -= 10

for i in range(int(m/10), y+1):
    num = str(i//10)+str(i)[::-1]
    num = int(num)
    if num < q:
        continue
    if num > y:
        break
    if is_prime(num):
        list_.append(num)

if q <= 11 <= y:
    if len(list_) == 0:
        list_.append(11)
    for i in list_:
        if i > 11:
            w = list_.index(i)
            list_.insert(w, 11)
            break
        if list_[-1] < 11:
            list_.append(11)
            break

length = len(list_)
end_time = time.time()
elapsed_time = end_time-start_time
if length >= 6:
    link = list_[0], list_[1], list_[2], list_[-3], list_[-2], list_[-1]
    print(f"{length}.{link}. time taken = {elapsed_time}")
else:
    print(f"{length}.{list_}. \n time taken = {elapsed_time}")
