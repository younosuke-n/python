import sys

sum = 0
for num in sys.argv[1:]:
    sum += int(num)

print(sum)