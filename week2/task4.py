def get_number(index):
    A = index // 3
    B = index % 3
    if B == 1:
        result = 7 * A + 4
    elif B == 2:
        result = 7 * A + 8
    else:
        result = 7 * A
    print(result)

get_number(1)  # print 4
get_number(5)  # print 15
get_number(10) # print 25
get_number(30) # print 70