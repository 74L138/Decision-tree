from math import log
import operator

# ������Ϣ��
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)  # ������
    labelCounts = {}
    for featVec in dataSet:  # ����ÿ������
        currentLabel = featVec[-1]  # ��ǰ���������
        if currentLabel not in labelCounts.keys():  # ��������ֵ�
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:  # ������Ϣ��
        prob = float(labelCounts[key]) / numEntries
        shannonEnt = shannonEnt - prob * log(prob, 2)
    return shannonEnt

# �������ݼ���axis:���ڼ������Ի��֣�value:Ҫ���ص��Ӽ���Ӧ������ֵ
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

# ѡ����õ����ݼ����ַ�ʽ
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1  # ���Եĸ���
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoC45 = 0.0
    bestFeature = -1
    for i in range(numFeatures):  # ��ÿ�����Լ�����Ϣ����
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)  # �����Ե�ȡֵ����
        newEntropy = 0.0
        IV=0.0
        for value in uniqueVals:  # ��ÿһ��ȡֵ������Ϣ����
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
            IV += -prob * log(prob,2)
        infoC45 = (baseEntropy - newEntropy)/IV
        print(infoC45)
        if (infoC45 > bestInfoC45):  # ѡ����������������
            bestInfoC45 = infoC45
            bestFeature = i
    return bestFeature

# ͨ�����򷵻س��ִ����������
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# �ݹ鹹��������
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]  # �������
    if classList.count(classList[0]) == len(classList):  # ���ֻ��һ����𣬷���
        return classList[0]
    if len(dataSet[0]) == 1:  # ����������������������ˣ����س��ִ����������
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)  # ���Ż������Ե�����
    bestFeatLabel = labels[bestFeat]  # ���Ż������Եı�ǩ
    print(bestFeatLabel)
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])  # �Ѿ�ѡ����������ٲ������
    featValues = [example[bestFeat] for example in dataSet]
    uniqueValue = set(featValues)  # ���������п���ȡֵ��Ҳ���ǽڵ�ķ�֧
    for value in uniqueValue:  # ��ÿ����֧���ݹ鹹����
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(
            splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree