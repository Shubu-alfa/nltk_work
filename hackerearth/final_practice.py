count = 0
house_cost = []
k = ""
diff =100
house_data = int(input())
if 2 <= house_data <= (2 * (10**5)):
    house_cost = [int(x) for x in input().split()]
    for i in range(0, house_data):
        count = count + 1
        if 1 <= house_cost[i] <= (10**16):
            for j in range(0, count):
                k = str(house_cost[j] + 2)
                for m in range(j+2, count):
                    if house_cost[j] - house_cost[m] < diff:
                        diff = house_cost[j] - house_cost[m]

        else:
            print("Unaffordable price!")
            break
    print("minimum difference:")
    print(diff)
else:
    print("Alot of test cases")