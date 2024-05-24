def forest(forest, bird):
    v = []
    n = len(forest)
    j, k = bird, bird

    while forest[bird] < 100 and (k < n or j >= 0):
        while k < n:
            k += 1
            if k < n and forest[k] != 0:
                forest[bird] += forest[k]
                v.append(k)
                break

        if forest[bird] >= 100:
            break

        while j >= 0:
            j -= 1
            if j >= 0 and forest[j] != 0:
                forest[bird] += forest[j]
                v.append(j)
                break

    return v

print(forest([25,0,50,0,0,0,0,15,0,0,45],4))

