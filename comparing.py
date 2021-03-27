def aprioriMatrix(rowNo, colNo, dataList):
    mat = []
    for i in range(rowNo):
        row = []
        for j in range(colNo):
            row.append(dataList[rowNo * i + j])
        mat.append(rowList)

    return mat

def aprioriTable(support, confidence, lift):
    table = ['item A and B', support[0], confidence[0], lift[0], 'item A and C', support[1], confidence[1], lift[1], 'item A and D', support[2], confidence[2], lift[2], 'item A and E', support[3], confidence[3], lift[3]]
    mat = aprioriMatrix(4,4,table)
    print (mat)
    
def compare(confidence, lift):
  big_confidence=0
  big_lift=0
  for i in range(4):
    if(big_confidence<confidence[i]):
      big_confidence = confidence[i]
      recommendItem = 
      
  for i in range(4):
    if(big_lift<lift[i]):
      big_lift = lift[i]    
      
      
