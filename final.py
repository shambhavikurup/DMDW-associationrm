import random
def read_data():
    numProducts = 5
    products = list(range(1, numProducts+1))
    print(products)
    numTransactions = 10
    transactions = dict()

    for i in range(numTransactions):
        randomProdList = random.sample(products, random.randint(1,numProducts)) 
        transactions[i+1] = sorted(randomProdList)
    print(transactions)

def frequence(items_list, trans):
    items_count = dict() 
    for i in items_list:  #for every item that is present in the dataset 
        if(len(items_list[i]=1)): 
            itemset = {i}
        else:
            itemset = set(i)     
        for j in trans.items():  #for every transaction
            if itemset.issubset(set(j[1])):   #if the itemset is a subset of that transaction
                if i in items_count:           
                    items_count[i] += 1       #the frequency of the itemset increases by 1
                else:
                    items_count[i] = 1        #otherwise it remains 1
    return items_count                        #return the frequency of each itemset

def findSupport(itemsetCount, transaction):
    support = dict()
    totalTransactions = len(transaction)
    for i in itemsetCount:
        support[i] = itemsetCount[i]/totalTransactions
    return support

def main():
    transactions = read_data()

    for i in transactions.values():
        numberOfTransactions = len(i) 
    
    ListOfItems = set()

     for i in transactions.values():
        for j in i:
            ListOfItems.add(j)

main()
