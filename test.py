path = "io\\temp.txt"
fo = open(path, "r")
n = [int(x) for x in fo.readline().split()]
print(n)
