import random
from itertools import combinations

def generateDataset(numProducts, products, numTransactions):
    transactions = dict()
    for i in range(numTransactions):
        randomProdList = random.sample(products, random.randint(1,numProducts)) 
        transactions[i+1] = sorted(randomProdList)
    return transactions

def frequence(itemsets, transactions):
    itemsetFreq = dict() 
    for itemset in itemsets:  #itemset is a tuple when itemsets of size>1 are taken
        if isinstance(itemset,int): #will be true only for itemsets of size 1
            temp = set([itemset])
        else:
            temp = set(itemset)
        for transaction in transactions.items():        # for every transaction; transaction[0] = TID, transaction[1] = transaction's itemset
            if temp.issubset(set(transaction[1])):      # if the itemset is a subset of the itemset in transaction, increase count of frequency by 1
                if itemset in itemsetFreq:           
                    itemsetFreq[itemset] += 1       
                else:
                    itemsetFreq[itemset] = 1 
    infrequent = itemsets - itemsetFreq
    print("frequent:")
    print(itemsetFreq)
    print(infrequent)
    return itemsetFreq                                   # return a dict with frequency of each itemset {itemset: frequency}

def findSupport(itemsetCount, transactions):
    support = dict()
    for i in itemsetCount:
        support[i] = itemsetCount[i]/len(transactions)
    return support

def main():
    minSupport=0.1
    numProducts = 5
    products = set(range(1, numProducts+1))              # items_lst;
    numTransactions = 10
    transactions = generateDataset(numProducts, products, numTransactions)
    listItemsInTransactions = [] #array of number of items bought in every transaction
    for i in range(1,numTransactions+1):
        listItemsInTransactions.append(len(transactions[i]))

    allCandidates = list()
    for i in range(1, max(listItemsInTransactions)+1):
        candidateItemsetList = set(combinations(products, i))
        allCandidates.append(candidateItemsetList)


    frequentItemsets = []                                   # items_grater_then_min_support;
    itemsetFreqHistory = []                              # itemcount_track; so itemsetFreqHistory is be a dictionary of itemsets of size i and their respective frequency
    itemFrequency = frequence(products, transactions)    # items_counts; itemFrequency is a dict of item:frequency for every item in products
    itemsetFreqHistory.append(itemFrequency)
    for i in findSupport(itemFrequency, transactions).items(): # i is (item:support), i[0]=item, i[1]=support of the item
        if i[1]>minSupport:
            frequentItemsets.append({i[0]:i[1]})
    
    # so frequentItemsets is a list that contains elements of the form {item:support} for frequent itemsets. For now, it only
    # contains frequent itemsets of size 1 (basically singular items)

    # tempFreq = []               #[1,2,3,4,5]
    # for i in frequentItemsets:
    #     for itemset in i:
    #         tempFreq.append(itemset)    
    
    # itemList = combinations(tempFreq, 2)
        for i in range(len(allCandidates))
            itemFrequency = frequence(allCandidates[i], transactions)

        itemsetFreqHistory.append(itemFrequency)
        if list({j[0]:j[1] for j in findSupport(itemFrequency, transactions).items() if j[1]>minSupport}.keys()) != []:
            frequentItemsets.append({j[0]:j[1] for j in findSupport(itemFrequency, transactions).items() if j[1]>minSupport})

    #print(frequentItemsets)



main()
