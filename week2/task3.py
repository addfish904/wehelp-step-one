def func(*data):
    middlename = []
    for name in data:
        if len(name) == 2 or len(name) == 3:
            middlename.append(name[1])
        elif len(name) == 4 or len(name) == 5:
            middlename.append(name[2])
        else:
            middlename.append(None)

    count = {}
    for char in middlename:
        if char:
            count[char] = count.get(char, 0) + 1

    for name in data:
        middle = None
        if len(name) == 2 or len(name) == 3:
            middle = name[1]
        elif len(name) == 4 or len(name) == 5:
            middle = name[2]
        if count.get(middle) == 1:
            print(name)
            return
    print("沒有")

# Test cases
func("彭大牆", "陳王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆")  # print 夏曼藍波安