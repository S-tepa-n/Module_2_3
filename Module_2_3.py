my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
nember_0 = 0
while nember_0 < len(my_list):
    if my_list[nember_0] < 0:
        break
    if my_list[nember_0] == 0:
        nember_0 += 1
        continue
    print(my_list[nember_0])
    nember_0 += 1
