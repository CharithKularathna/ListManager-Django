def lineCounter(fname):
    count=0
    with open(fname, 'r') as f:
        for line in f: # pylint: disable=unused-variable
            count += 1
    return count

#print(lineCounter("product_list.txt"))


def getLists(path):
    entryList = []
    fo = open(path,'r')
    lineCount = lineCounter(path)
    for i in range(lineCount): # pylint: disable=unused-variable
        line = fo.readline()
        if (i!=(lineCount-1)):
            line = line[0:-1]
        tempList = line.split(',')
        p_id = tempList[0]
        price = tempList[-1]
        p_name = ",".join(tempList[1:-1])
        entry = [p_id,p_name,price]
        entryList.append(entry)
    fo.close()
    return entryList[1:]



def addProduct(path, product):
    fo = open(path,'a')
    pString = ','.join(product)
    fo.write('\n'+pString)
    fo.close()

def removeProduct(path, product_id):
    readList = getLists(path)
    for entry in readList:
        if (product_id == entry[0]):
            readList.remove(entry)
            writeList(path,readList)
            return 1
    return 0

def writeList(path,p_list):
    fo = open(path,'w')
    w_list=['id,product_name,price']
    for entry in p_list:
        w_list.append(','.join(entry))
    fo.write('\n'.join(w_list))

#print(str(removeProduct("product_list.txt","AB333")))
#addProduct("product_list.txt",["AB000","Test Product","$100"])
#print (getLists("product_list.txt"))
#addProduct("product_list.txt",["AB000","Test Product","$100"])
#print (getLists("product_list.txt"))


