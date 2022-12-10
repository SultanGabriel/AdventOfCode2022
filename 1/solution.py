
sum_max = -1

with open("./input.txt") as input: 
    sum = 0
    for line in input:
        if (line != "\n"):
            sum += int(line)
        else:
            if(sum_max < sum):
                sum_max = sum

            sum = 0

print("The elf with the most food has {} calories.".format(sum_max))