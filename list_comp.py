def square(num):
    return num**2


arr = [square(i) for i in range(10) if i % 2 == 0]
print(arr)


