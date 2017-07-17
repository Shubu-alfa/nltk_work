house_cost = []
diff = 9999999999
house_data = int(input())
if 2 <= house_data <= (2 * (10**5)):
    try:
        house_cost = [int(x) for x in input().split()]

        for i in range(0, house_data):
            if 1 <= house_cost[i] <= (10**16):
                for m in range(i+2, house_data):
                    if 0 < house_cost[i] - house_cost[m] < diff:
                        diff = house_cost[i] - house_cost[m]

            else:
                print("Unaffordable price!")
                break
    except Exception as e:
        print("Array out of range")
    if diff != 9999999999:
        print(diff)
    else:
        print("The house cannot be sold at a price greater than or equal to the cost price")
else:
    print("Alot of test cases")