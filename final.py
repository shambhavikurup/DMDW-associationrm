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
            if temp.issubset(set(transaction[1])): # if the itemset is a subset of the itemset in transaction, increase count of frequency by 1
                if isinstance(itemset,int):
                    if itemset in itemsetFreq:           
                        itemsetFreq[itemset] += 1       
                    else:
                        itemsetFreq[itemset] = 1 
                else:
                    if tuple(itemset) in itemsetFreq:           
                        itemsetFreq[tuple(itemset)] += 1       
                    else:
                        itemsetFreq[tuple(itemset)] = 1 
    return itemsetFreq                                   # return a dict with frequency of each itemset {itemset: frequency}

def findSupport(itemsetCount, transactions):
    support = dict()
    for i in itemsetCount:
        support[i] = itemsetCount[i]/len(transactions)
    return support


def deleteInfrequent(itemsetSupport, minSupport, allCandidates, listItemsInTransactions):
    for itemset in itemsetSupport.items():
        itemset = list(itemset)
        if isinstance(itemset[0],int): #will be true only for itemsets of size 1
            temp = set([itemset[0]])
        else:
            temp = set(itemset[0])
        if(itemset[1]<minSupport):
            for i in range(1,len(allCandidates)):
                allCandidates[i] = list(allCandidates[i])
                j=0
                while(j<len(allCandidates[i])):
                    allCandidates[i][j] = set(allCandidates[i][j])
                    if(temp.issubset(set(allCandidates[i][j]))):
                        del allCandidates[i][j]
                    else:
                        j+=1
    return(allCandidates)
        


def main():
    minSupport=0.5
    numProducts = 5
    products = set(range(1, numProducts+1))             
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


    frequentItemsets = []                                   
    itemFrequency1 = frequence(products, transactions)    # itemFrequency is a dict of item:frequency for every item in products
    for i in findSupport(itemFrequency1, transactions).items(): # i is (item:support), i[0]=item, i[1]=support of the item
        if i[1]>minSupport:
            frequentItemsets.append({i[0]:i[1]})
    
    for i in range(0,len(allCandidates)):
        itemFrequency = frequence(allCandidates[i], transactions)
        itemsetSupport = findSupport(itemFrequency, transactions)
        allCandidates = deleteInfrequent(itemsetSupport, minSupport, allCandidates, listItemsInTransactions)

    
    allCandidates[0] = list(allCandidates[0])
    temp=[]
    for each in (itemFrequency1.items()):
        if (each[1]/numTransactions)>=minSupport:
            temp.append(each[0])
    allCandidates[0] = set(temp)

    print("Frequent itemsets: ")
    for each in allCandidates:
        if (len(each)>0):
            print(each)



main()
