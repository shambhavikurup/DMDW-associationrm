import random

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
