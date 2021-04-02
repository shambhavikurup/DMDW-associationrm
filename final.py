import random




def main():
    numProducts = 5
    products = list(range(1, numProducts+1))
    print(products)
    numTransactions = 10
    transactions = dict()

    for i in range(numTransactions):
        randomProdList = random.sample(products, random.randint(1,numProducts)) 
        transactions[i+1] = sorted(randomProdList)
    print(transactions)

main()