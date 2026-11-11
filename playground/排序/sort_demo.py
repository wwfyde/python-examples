a = [[123, 'a', 2], [123, 'c', 4], [123, 'b', 5], [124, 'd', 6], [122, 'b', 7]]
b = [[123, 'a', 2], [123, 'c', 4], [123, 'b', 5], [124, 'd', 6], [122, 'b', 7]]
a.sort()
sorted(b)
# a.sort(key=lambda x: (x[1], x[0]))
# print(a)

# s = "Sorting1234"
# "".join(sorted(s, k/ey=lambda x: (x.isdigit(),
#                                  x.isdigit() and int(x) % 2 == 0,
#                                  x.isupper(),
#                                  x.islower(),
#                                  x)))

