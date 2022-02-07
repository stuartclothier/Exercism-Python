def total(basket):
    price_list = {1: 800, 2: 1520, 3: 2160, 4: 2560, 5: 3000}
    counter = 1
    groups = {}

    while basket:

        groups[counter] = list(set(basket))
        [basket.remove(each) for each in groups[counter]]
        counter += 1

    group_len = [len(each) for each in groups.values()]

    while 5 in group_len and 3 in group_len:
        group_len.remove(5)
        group_len.remove(3)
        group_len += [4, 4]

    price = sum(price_list[each] for each in group_len)

    return price
