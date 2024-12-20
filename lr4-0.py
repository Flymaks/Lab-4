class Item:
    def __init__(self, weight, value, name):
        self.weight = weight
        self.value = value
        self.name = name

def new_res(res, capacity): # converting an array of responses to a string
    res = res[::-1]
    s = ""
    for i in res:
        if len(s) < capacity: 
            s += i
    return s

def ans(res, h, w): # converting an array of responses into a two-dimensional array
    answer = [[0 for i in range(w)] for j in range(h)]
    c = 0
    for i in range(h):
        for j in range(w):
                if i == j == 0:
                    answer[i][j] = "i"
                else:
                    if res[i * w + j - 1] == res[i * w + j - 2] and j == 0:
                        answer[i][w-1] = res[i * w + j - 1]
                        c += 1
                    else:
                        answer[i][j - c] = res[i * w + j - 1]
    return answer

def full_v(items): # summ of values
    summ = 0
    for i in items:
        summ += i.value
    return summ

def knapsack(items, capacity):
    def node_bound_count(i, weight, value):
        if weight > capacity:
            return 0
        node_value = value
        j = i
        total_weight = weight

        while j < len(items) and total_weight + items[j].weight <= capacity:
            node_value += items[j].value
            total_weight += items[j].weight
            j += 1
        if j < len(items):
            node_value += (capacity - total_weight) * (items[j].value / items[j].weight)
        return node_value
    

    def branch_bound(i, weight, value):
        nonlocal max_value
        if i == len(items):
            return 0
        if weight <= capacity and value > max_value:
            max_value = value
        if node_bound_count(i, weight, value) > max_value:
            branch_bound(i+1, weight, value)
        if value + (capacity - weight) * (items[i].value / items[i].weight) > max_value:
            branch_bound(i+1, weight + items[i].weight, value + items[i].value)
            res.append(items[i].name * items[i].weight)

    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    max_value = 0
    branch_bound(0, 0, 0)
    return max_value


if __name__ == '__main__':
    items = [Item(3, 25, "r"), Item(1, 15, "k"), Item(2, 15, "p"),
             Item(2, 15, "a"), Item(2, 20, "m"), Item(3, 20, "x"), 
             Item(1, 25, "t"), Item(1, 15, "f"), Item(1, 10, "d"),
               Item(2, 20, "s"), Item(2, 20, "c")]
    height, width = 2, 4
    capacity = height * width - 1
    health_points = 10
    res = []
    full_value = full_v(items)
    health_points += knapsack(items, capacity) + 5
    res = new_res(res, capacity)
    answer = ans(res, height, width)
    for i in range(height):
        if i>=1: print()
        for j in range(width):
            print(f"[{answer[i][j]}]",end="")
    print()
    print(f"Итоговые очки выживания: {health_points *2 - full_value}")