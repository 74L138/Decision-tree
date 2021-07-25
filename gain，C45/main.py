import gain
import huizhi
import C45


fr = open(r'xigua2.txt')
listWm = [i.strip().split(',') for i in fr.readlines()]
print(listWm)
labels = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感']
classList = [example[-1] for example in listWm]
Trees = C45.createTree(listWm, labels)
# Trees = gain.createTree(listWm, labels)
#huizhi.createPlot(Trees)
