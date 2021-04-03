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
    return itemsetFreq                                   # return a dict with frequency of each itemset {itemset: frequency}

def findSupport(itemsetCount, transactions):
    support = dict()
    for i in itemsetCount:
        support[i] = itemsetCount[i]/len(transactions)
    return support


def check(itemsetSupport, minSupport):
    print(itemsetSupport.values())
    for itemset in itemsetSupport:
        


def main():
    minSupport=0.6
    numProducts = 5
    products = set(range(1, numProducts+1))              # items_lst;
    numTransactions = 10
    transactions = generateDataset(numProducts, products, numTransactions)
    listItemsInTransactions = [] #array of number of items bought in every transaction
    for i in range(1,numTransactions+1):
        listItemsInTransactions.append(len(transactions[i]))

    #setting up all Candidates
    allCandidates = []
    allCandidates.append(products)
    for i in range(2, max(listItemsInTransactions)+1):
        candidateItemsetList = set(combinations(products, i))
        allCandidates.append(candidateItemsetList)


    frequentItemsets = []                                   # items_grater_then_min_support;
    itemsetFreqHistory = []                              # itemcount_track; so itemsetFreqHistory is be a dictionary of itemsets of size i and their respective frequency
    itemFrequency = frequence(products, transactions)    # items_counts; itemFrequency is a dict of item:frequency for every item in products
    itemsetFreqHistory.append(itemFrequency)
    for i in findSupport(itemFrequency, transactions).items(): # i is (item:support), i[0]=item, i[1]=support of the item
        if i[1]>minSupport:
            frequentItemsets.append({i[0]:i[1]})
    

    print(allCandidates)
    for i in range(0,len(allCandidates)):
        itemFrequency = frequence(allCandidates[i], transactions)
        #print(itemFrequency)
        itemsetSupport = findSupport(itemFrequency, transactions)
        #print(itemsetSupport)
        check(itemsetSupport, minSupport)


    itemsetFreqHistory.append(itemFrequency)
    if list({j[0]:j[1] for j in findSupport(itemFrequency, transactions).items() if j[1]>minSupport}.keys()) != []:
        frequentItemsets.append({j[0]:j[1] for j in findSupport(itemFrequency, transactions).items() if j[1]>minSupport})

    #print(frequentItemsets)



main()
