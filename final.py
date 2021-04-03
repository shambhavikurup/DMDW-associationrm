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
    print("hello")
    print(itemsets)
    for itemset in itemsets:  #itemset is a tuple when itemsets of size>1 are taken
        if isinstance(itemset,int): #will be true only for itemsets of size 1
            temp = set([itemset])
        else:
            temp = set(itemset)
        print(temp)
        print(transactions.items())
        for transaction in transactions.items():        # for every transaction; transaction[0] = TID, transaction[1] = transaction's itemset
            if temp.issubset(set(transaction[1])): 
                print(itemsetFreq)     # if the itemset is a subset of the itemset in transaction, increase count of frequency by 1
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


def deleteInfrequent(itemsetSupport, minSupport, allCandidates, listItemsInTransactions):
    print(itemsetSupport)
    for itemset in itemsetSupport.items():
        itemset = list(itemset)
        if isinstance(itemset[0],int): #will be true only for itemsets of size 1
            temp = set([itemset[0]])
        else:
            temp = set(itemset[0])
        # print(itemset[1])
        # print(temp)
        if(itemset[1]<minSupport):
            for i in range(1,len(allCandidates)):
                allCandidates[i] = list(allCandidates[i])
                # print(allCandidates)
                # print(allCandidates[i])
                j=0
                print(allCandidates[i])
                while(j<len(allCandidates[i])):
                    print(temp)
                    # if(type(allCandidates[i][j])!=[[]]):
                    allCandidates[i][j] = set(allCandidates[i][j])
                        # if(len(temp)<len(allCandidates[i][j])):
                    print(allCandidates[i][j])
                    if(temp.issubset(set(allCandidates[i][j]))):
                        del allCandidates[i][j]
                        print("deleting")
                    else:
                        j+=1
                        print("iterating")
                print(allCandidates)
                print("done")
    return(allCandidates)
        


def main():
    minSupport=0.5
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
    
    for i in range(0,len(allCandidates)):
        itemFrequency = frequence(allCandidates[i], transactions)
        #print(itemFrequency)
        itemsetSupport = findSupport(itemFrequency, transactions)
        #print(itemsetSupport)
        allCandidates = deleteInfrequent(itemsetSupport, minSupport, allCandidates, listItemsInTransactions)
    #print(allCandidates)
        print("done" + str(i))

    itemsetFreqHistory.append(itemFrequency)
    if list({j[0]:j[1] for j in findSupport(itemFrequency, transactions).items() if j[1]>minSupport}.keys()) != []:
        frequentItemsets.append({j[0]:j[1] for j in findSupport(itemFrequency, transactions).items() if j[1]>minSupport})

    #print(frequentItemsets)



main()
