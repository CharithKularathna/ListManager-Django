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

#addProduct("product_list.txt",["AB000","Test Product","$100"])
#print (getLists("product_list.txt"))
#addProduct("product_list.txt",["AB000","Test Product","$100"])
#print (getLists("product_list.txt"))


