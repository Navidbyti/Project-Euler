import re

handle = open("regex_sum_1573961.txt")
num_sum = 0
for line in handle:
    num_sum += sum( [int(i) for i in re.findall('[0-9]+', line)])
print(num_sum)


#All the code above in one line:

print( sum( [int(i) for i in re.findall('[0-9]+', open("regex_sum_1573961.txt").read())]))