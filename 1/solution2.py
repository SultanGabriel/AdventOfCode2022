
top_three = [-1, -1, -1]
print(type(top_three))
with open("./input.txt") as input: 
    csum = 0
    for line in input:
        if (line != "\n"):
            csum += int(line)
        else:
            for c_top_sum in top_three:
                if( < csum):
                    top_three = csum
                    break
            csum = 0

sum_all = csum(top_three)

print("The elf with the most food has {} calories.".format(sum_all))