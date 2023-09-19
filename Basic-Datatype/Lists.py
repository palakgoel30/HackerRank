if __name__ == '__main__':
    N = int(input())
    count = 0
    list1 = []
    while count < N:
        item = input()
        item = item.split()

        if (item[0] == 'insert'):
            list1.insert(int(item[1]), int(item[2]))
        elif (item[0] == 'print'):
            print(list1)
        elif (item[0] == 'remove'):
            list1.remove(int(item[1]))
        elif (item[0] == 'append'):
            list1.append(int(item[1]))
        elif (item[0] == 'sort'):
            list1.sort()
        elif (item[0] == 'pop'):
            list1.pop(-1)
        elif (item[0] == 'reverse'):
            list1.reverse()
        count += 1

