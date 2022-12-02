f = open("real.txt", "r")
result = map(lambda e: e.split("\n"), f.read().split("\n\n"))
print("File input")
#print(list(result))
#print()

result = filter(lambda e: len(e) > 0, result)
#print("Filtered")
#print(list(result))
result = map(lambda e: sum(map(int, e)), result)

print("Converted")
print(list(result))

print(f'Max is {max(result)}')

result.sort(reverse=True)

print('nn')
print(sum(result[0:3]))




