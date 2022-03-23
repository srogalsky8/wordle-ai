input = open('data/CSW19.txt')
out = open('data/CSW19-5.txt', 'w')

out.write("".join([line for line in input if len(line.strip()) == 5]))

input.close()
out.close()