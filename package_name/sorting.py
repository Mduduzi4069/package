def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''

    z = len(items)
    for d in range(z):
        for itm in range(0, z-d-1):
            if items[itm] > items[itm+1] :
                items[itm], items[itm+1] = items[itm+1], items[itm]
    return items



def merge_sort(items):

    '''Return array of items, sorted in ascending order'''

    if len(items) > 1:
        le, rgt = map(lambda l: list(reversed(merge_sort(l))), (items[::2], items[1::2]))
        items.clear()
        while le and rgt:
            items.append(le.pop() if le[-1] < rgt[-1] else rgt.pop())
        items.extend(le[::-1])
        items.extend(rgt[::-1])
    return items


def quick_sort(items):

    '''Return array of items, sorted in ascending order'''

    if len(items) == 1 or len(items) == 0:
        return items
    else:
        pvt = items[0]
        i = 0
        for j in range(len(items)-1):
            if items[j+1] < pvt:
                items[j+1],items[i+1] = items[i+1], items[j+1]
                i += 1
        items[0],items[i] = items[i],items[0]
        first_part = quick_sort(items[:i])
        second_part = quick_sort(items[i+1:])
        first_part.append(items[i])
        return first_part + second_part        
