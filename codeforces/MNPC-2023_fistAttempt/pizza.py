

n = int(input()) # n pizzs , each has 8 slices
m = int(input()) #attendees
k = int(input()) #slices per each

if (k < 1 and m > 0):
    print("FALSE")
elif (n * 8 >= m *k):
    print("TRUE")
else:
    print("FALSE")

