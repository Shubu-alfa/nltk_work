#list = [int(x) for x in input().split()]
count = 0
house_cost = []
k = ""
diff =100
house_data = int(input())
if 2 <= house_data <= (2 * (10**5)):
    house_cost = [int(x) for x in input().split()]
    #print(house_cost)
    for i in range(0, house_data):
        #house_cost.append(int(input()))
        count = count + 1
        if 1 <= house_cost[i] <= (10**16):
            for j in range(0, count):
                #print(house_cost[0])
                    #print(type(house_cost[j]))
                k = str(house_cost[j] + 2)
                # k = str(int(j) + 2)
                    #print(k)
                for m in range(j+2, count):
                    #print(m)
                    #diff = house_cost[j] - house_cost[m]
                    if house_cost[j] - house_cost[m] < diff:
                        diff = house_cost[j] - house_cost[m]

        else:
            print("Unaffordable price!")
            break
    print("minimum difference:")
    print(diff)
else:
    print("Alot of test cases")
#print(house_cost)