import pandas as pd
import requests
import pickle
import json
import csv
import os

def getCategories():
    try:
        return json.loads(requests.get(f"{os.getenv('SERVER')}/category/fetch").text)['categoryList']
    except Exception as e:
        return []

def getProducts(slug):
    try:
        return json.loads(requests.get(f"{os.getenv('SERVER')}/product/{slug}").text)['products']
    except Exception as e:
        return []
    
def findAncestors(categoryList, categoryId):
    ancestors = []
    discardList = ['']
    currentList = categoryList
    key = categoryId
    iteration = 0

    while True:
        if len(currentList) == iteration:
            discardList.append(currentList[iteration - 1]["parentId"])
            currentList = categoryList
            iteration = 0
            continue
        
        if currentList[iteration]['_id'] in discardList:

            iteration += 1
            continue

        if currentList[iteration]["_id"] == key:
            ancestors.insert(0, currentList[iteration]["name"])

            if "parentId" in currentList[iteration]:
                key = currentList[iteration]["parentId"]
                currentList = categoryList
                iteration = 0
                continue
            else:
                break

        elif len(currentList[iteration]["children"]) == 0:
            iteration += 1
            continue

        else:
            currentList = currentList[iteration]["children"]
            iteration = 0
            continue

    return ancestors

def parseProducts(categories):
    if len(categories) ==0:
         return False
    products=[]
    discardList=[]
    iteration=0
    currCategory=categories

    while True:
        
        if len(currCategory) == iteration:
            if "parentId" in currCategory[iteration-1]:

                discardList.append(currCategory[iteration-1]["parentId"])
                iteration=0
                currCategory=categories
                continue
            
            else:
                return products

        if currCategory[iteration]["_id"] in discardList:
            
            iteration+=1
            continue

        
        if len(currCategory[iteration]["children"]) !=0:  # if Category have sub cateogry
            currCategory=currCategory[iteration]["children"]
            iteration=0
            continue
        else:
            rawProducts=getProducts(currCategory[iteration]["slug"])
            print(f"---- Categroy: {currCategory[iteration]['name']} -----")
            if len(rawProducts)!=0:
                for product in rawProducts:
                    products.append({
                "id":product["_id"],
                "name":product["name"],
                "price":product["price"],
                "description":product["description"],
                "categories":findAncestors(categories,product["category"])
                })
                    print(f"Product: {product['name']}")

            discardList.append(currCategory[iteration]["_id"])
            iteration+=1

def writeCSV(products):
    try:
        if len(products)>0:
            with open('../data/dataset.csv', mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["id", "name", "price", "description", "categories"])
                writer.writeheader()
                for product in products:
                    product['categories']=' '.join(product['categories'])
                    writer.writerow(product)
            return True
        return 'asd'
    except Exception as error:
        return error
    
def readCSV():
    try:
        return pd.read_csv(os.getenv('DATASET_PATH'),encoding="ISO-8859-1")
    except Exception as error:
        return False

def preprocess(rawData):
    try:
        rawData['text']=rawData['name']+ " "+rawData['description']+" "+rawData['categories']
        rawData=rawData.drop(['name','description','categories','price'],axis=1)
        return rawData
    except Exception as error:
        return False
    
def saveModel(JSON):
    try:
        with open(f"{os.getenv('VECTOR_PATH')}", 'wb') as f:
            pickle.dump(JSON['vector'], f)
        with open(f"{os.getenv('MODEL_PATH')}", 'wb') as f:
            pickle.dump(JSON['model'], f)
        return True
    except Exception as error:
        return False