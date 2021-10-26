x = int(input())
y = int(input())
z = int(input())
n = int(input())
pos_coords = list(zip([i for i in range(x+1)], [j for j in range(y+1)], [k for k in range(z+1)]))
print(pos_coords)
check_sum = 0
result_coord = []
for coords in pos_coords:
    for axes in coords:
        # print(axes)
        check_sum += axes
        if sum == n:
            continue
        else:
            result_coord.append(coords)
# print(result_coord)