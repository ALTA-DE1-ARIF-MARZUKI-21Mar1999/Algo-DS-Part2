def maximum_buy_product(money, product_price):
    product_price.sort()
    
    count = 0
    bought_indices = set()
    
    for i in range(len(product_price)):
        if i not in bought_indices and money >= product_price[i]:
            money -= product_price[i]
            count += 1
            bought_indices.add(i)
    
    return count

if __name__ == "__main__":
    print(maximum_buy_product(50000, [25000, 25000, 10000, 14000]))      # 3
    print(maximum_buy_product(30000, [15000, 10000, 12000, 5000, 3000])) # 4
    print(maximum_buy_product(10000, [2000, 3000, 1000, 2000, 10000]))   # 4
    print(maximum_buy_product(4000, [7500, 3000, 2500, 2000]))           # 1
    print(maximum_buy_product(0, [10000, 30000]))                        # 0