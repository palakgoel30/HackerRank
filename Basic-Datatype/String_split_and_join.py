def split_and_join(line):
    line = line.split(" ")
    return "-".join(line)

line = input()
print(split_and_join(line))