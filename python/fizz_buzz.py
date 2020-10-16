# Fizz Buzz
cfb, cf, cb = 0, 0, 0

for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print("Fizz Buzz")
        cfb += 1
    elif x % 3 == 0:
        print("Fizz")
        cf += 1
    elif x % 5 == 0:
        print("Buzz")
        cb += 1
    else:
        print(x)

print(f"Fizz: {cf} | Buzz: {cb} | Fizz Buzz: {cfb}")