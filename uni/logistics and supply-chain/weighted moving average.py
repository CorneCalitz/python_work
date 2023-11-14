def wma(values, weights):
    total = 0
    for i in range(len(values)):
        weighted_avg = values[i] * weights[i]
        print(i + 1, weighted_avg)
        total += weighted_avg

    print("WMA: ", total)


wma([91, 90, 89, 88, 90], [1 / 15, 2 / 15, 3 / 15, 4 / 15, 5 / 15])

wma([3716, 3249, 3120], [0.1, 0.3, 0.6])
