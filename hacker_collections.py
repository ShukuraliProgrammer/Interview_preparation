def calculate_sum_earned(shoes_sizes, sizes_prices):
    earned_money = 0

    for item in sizes_prices:
        if item[0] in shoes_sizes:
            shoes_sizes.remove(item[0])
            earned_money += int(item[1])
    return earned_money


if __name__ == '__main__':
    number_shoes = int(input())
    shoes_sizes = list(map(int, input().split()))
    customers_count = int(input())
    sizes_prices = []
    for i in range(customers_count):
        size_price = list(map(int, input().split()))
        sizes_prices.append(size_price)
    print(calculate_sum_earned(shoes_sizes, sizes_prices))
