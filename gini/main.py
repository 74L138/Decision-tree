from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing

data= open('./xigua2.txt',encoding='gbk')
reader = csv.reader(data)
for row in reader:
    headers=row
    break
    
featureList = []
labelList = []
for row in reader:
    if(len(row)==0):
        break
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1, len(row)-1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)

vec = DictVectorizer()
dummyX = vec.fit_transform(featureList) .toarray()
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)

model = tree.DecisionTreeClassifier(criterion='gini')
model = model.fit(dummyX, dummyY)

with open("tree.txt", 'w') as f:
    f = tree.export_graphviz(model
                            , feature_names = vec.get_feature_names()
                            , filled = True
                            , rounded = True
                            ,out_file=f)