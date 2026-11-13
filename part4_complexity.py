
# Part 4: Count the Steps

# Single loop from 1 to 5
count = 0

for i in range(1, 6):
    print(i)
    count += 1

print("Single loop runs:", count, "times")

# Single loop for n = 20
n = 20
count = 0

for i in range(1, n + 1):
    count += 1

print("Single loop for n = 20:", count, "times")

# Nested loop from 1 to 5
count = 0

for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)
        count += 1

print("Nested loop runs:", count, "times")

# Nested loop for n = 10
n = 10
count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        count += 1

print("Nested loop for n = 10:", count, "times")
