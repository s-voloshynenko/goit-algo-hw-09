import time

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count

    return result

def find_min_coins(amount):
    result = {}
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i] > dp[i - coin] + 1:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    while amount > 0:
        coin = coin_used[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result

def measure_time(amount, algo, runs=10):
    start_time = time.perf_counter()

    for _ in range(runs):
        result = algo(amount)

    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) / runs

    print(f"Average search time of '{algo.__name__}' over {runs} runs is {elapsed_time:.6f} secs.")
    print(f"Result: {result}")

def main():
    amount_to_test = [
        113,
        616,
        10012
    ]

    for amount in amount_to_test:
        print(f"\nAmount: {amount}")
        measure_time(amount, find_coins_greedy)
        measure_time(amount, find_min_coins)

if __name__ == "__main__":
    main()
