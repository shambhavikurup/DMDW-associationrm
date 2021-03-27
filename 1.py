# Anjali Sajith         1020191420
# Stuti Khandelwal      1020191308
# Shambhavi Kurup       1020191577

import random

# transactions is a list of lists
# every element of transactions is a transaction which is a list of 2 elements - TID and itemset
# suppose we have five items in total: namely, 0,1,2,3,4, and 10 transactions
# so each transaction looks like this: transactions[i] = {TID, {itemset}}
# so for i'th transaction, transactions[i][0] = TID, transaction[i][1] = {list of items}
# list support: support[i] = number of transactions in which i features
# random.sample(range(x,y), z) generates a list of length z containing numbers in the range [x,y) without duplicates 


numProducts = 5
products = list(range(0, numProducts))
numTransactions = 10
transactions = []

# setting up randomly generated dataset
for i in range(numTransactions):
    transactions.append([i])
    randomList = random.sample(range(0, 5), random.randint(1,numProducts)) 
    transactions[i].append(sorted(randomList)) # is sorting necessary/advantageous?
print(transactions)

# setting up arrays presentIn and support
# presentIn[i] is a list of transaction IDs that product i is present in
# so len(presentIn[i]) = support of i because it's essentially the number of transactions i is part of
presentIn = [[] for i in range(numProducts)]
for i in range(numProducts):
    for j in range(numTransactions):
        for item in transactions[j][1]:
            if (products[i]==item): 
                presentIn[i].append(transactions[j][0])
                break
support = []
for each in presentIn:
    support.append(len(each)/range(transactions))


# confidence(x,y) = number of transactions x and y are both in / those that only 
# x is in
# intersection is the list of common elements of presentIn[x] and presentIn[y], so basically
# all the transaction IDs for transactions in which x and y both feature
def findConfidence(x,y):
    intersection = [value for value in presentIn[x] if value in presentIn[y]]  
    lenIntersection = len(intersection)
    confidence = lenIntersection/len(presentIn[x])
    return confidence

# parameter S is the support threshold i.e. minimum number of transactions an item 
# has to be in to be considered a frequent item
# findFrequentItems returns a list of the frequent items
def findFrequentItems(S): 
    frequentItems = []
    for i in range(numProducts):
        if support[i]>= S:
            frequentItems.append(i)
    return frequentItems 

    
# def compare(confidence, lift):
#   big_confidence=0
#   for i in range(4):
#     if(big_confidence<confidence[i]):
#       big_confidence = confidence[i]
      
    

def main:
    sup_threshold = 5
    frequent = findFrequentItems(sup_threshold)
    print("Frequent items when support threshold = " + sup_threshold + "is: " + frequent)
    for product1 in products:
        for product2 in products:
            if (product1 != product2):
                p1_p2 = findConfidence(product1, product2)
                print("Likelihood of " + product2 + " being bought when " + product1 + " is bought is " + p1_p2)
                
