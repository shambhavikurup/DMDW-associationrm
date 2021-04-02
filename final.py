import random

def generateDataset(numProducts, products, numTransactions):
    transactions = dict()
    for i in range(numTransactions):
        randomProdList = random.sample(products, random.randint(1,numProducts)) 
        transactions[i+1] = sorted(randomProdList)
    return transactions

def frequence(products, transaction):
    products_count = dict() 
    for i in products:  #for every product that is present in the dataset 
        if(len(products[i]=1)): 
            itemset = {i}
        else:
            itemset = set(i)     
        for j in transaction.items():  #for every transaction
            if itemset.issubset(set(j[1])):   #if the itemset is a subset of that transaction
                if i in productss_count:           
                    products_count[i] += 1       #the frequency of the itemset increases by 1
                else:
                    products_count[i] = 1        #otherwise it remains 1
    return products_count                        #return the frequency of each itemset

def findSupport(itemsetCount, transaction):
    support = dict()
    totalTransactions = len(transaction)
    for i in itemsetCount:
        support[i] = itemsetCount[i]/totalTransactions
    return support

def main():
    numProducts = 5
    products = list(range(1, numProducts+1))
    numTransactions = 10
    transactions = generateDataset(numProducts, products, numTransactions)

    for i in transactions.values():
        numberOfTransactions = len(i) 
    
    ListOfItems = set()

     for i in transactions.values():
        for j in i:
            ListOfItems.add(j)

main()
