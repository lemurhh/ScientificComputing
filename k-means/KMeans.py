#!/usr/bin/python
# -*- coding: utf-8 -*-

'k-means module'

__author__ = 'lemur'

#聚类类
class Cluster(object):
    Num = 0 #聚类数量
    def __init__(self):
        self.set = [] #样本集合
        Cluster.Num += 1
    def calc_average(self): #计算聚类中心
        sum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in range(0,Sample.FeatureNum):
            for sample in self.set:
                sum[i] += sample.value[i]
        return [sum[i]/(len(self.set)) for i in range(0,Sample.FeatureNum)]
    @property
    def average(self):
        return self._average
    @average.setter
    def average(self,ave):
        self._average = ave
    #向聚类中添加样本
    def add(self,sample):
        self.set.append(sample)
    #从聚类中删除样本
    def remove(self,sample):
        self.set.remove(sample)

#样本类
class Sample(object):
    FeatureNum = 0 #样本特征数量
    Id = 0 #样本标号
    def __init__(self,val):
        self.value = val
        Sample.FeatureNum = len(val)
        Sample.Id+=1
        self.id = Sample.Id
    #样本属于哪个聚类
    @property
    def cluster(self):
        return self._cluster
    @cluster.setter
    def cluster(self,clu):
        self._cluster = clu
    #计算到各个聚类中心的距离
    def calc_distance(self,clu_set):
        dis=[]
        for i in range(0,Cluster.Num):
            distance = 0
            for j in range(0,Sample.FeatureNum):
                distance += ( self.value[j]-clu_set[i].average[j] ) ** 2
            dis.append(distance)
        return dis
    @property
    def distance(self):
        return self._distance
    @distance.setter
    def distance(self,dis):
        self._distance = dis
    def __str__(self):
        str = '(id=%d)' % self.id
        #for i in range(0,Sample.FeatureNum):
            #str += ',%.3f' % self.value[i]
        #str += ')'
        return str
        #return '(%d,%f,%f,%f,%f,%f,%f,%f)' % (self.id,self.value[0],self.value[1],self.value[2],self.value[3],self.value[4],self.value[5],self.value[6])
    __repr__ = __str__

#聚类算法实现函数，k：聚类数，sample_set:样本集合
def kmeans(k, sample_set): 
    clu_set = [Cluster() for i in range(0,k)] #聚类集合
    
    #选取前Cluster.Num个样本为初始聚类中心
    for i in range(0,Cluster.Num):
        clu_set[i].average = sample_set[i].value
    
    for sample in sample_set:
        dis = sample.calc_distance(clu_set) #得到样本离聚类中心的距离
        min_dis = min(dis)
        clu_index = dis.index(min_dis)
        clu_set[clu_index].add(sample)
        sample.cluster = clu_set[clu_index]
        
    while 1:
        flag = 0
        for i in range(0,Cluster.Num):
            if (clu_set[i].calc_average() != clu_set[i].average): #判断每一个聚类的中心是否需要更新，需要更新则更新
                flag = 1
                clu_set[i].average = clu_set[i].calc_average()
        if flag==0: #若都不需要更新，则聚类完成
            break
        #更新聚类
        for sample in sample_set:
            dis = sample.calc_distance(clu_set)
            min_dis = min(dis)
            clu_new_index = dis.index(min_dis)
            if clu_set[clu_new_index]!=sample.cluster:
                sample.cluster.remove(sample) #从原聚类中删除
                clu_set[clu_new_index].add(sample) #添加到新聚类
                sample.cluster = clu_set[clu_new_index] #更新样本属性

    for i in range(0,Cluster.Num):
        print clu_set[i].set

if __name__=='__main__':
    sample_set = [Sample(val) for val in [ [0,0,0,0,0,0.741,0],[0,0,0,0,0,1.0916,0],[0,1.7944,0,0,0,0,0],[0,0.9943,0,0,0,0.304,0],[0,0,0,0,0,0.7091,0],[5.32,2.4489,0,0.342,0,0.1077,3.1902],[0,0,0,0,0,1.8734,0],[3.901,4.18,4.3117,2.767,0,11.7965,0],[0,5.2841,0.0399,0,0.418,0,0],[0,0,0,0,0,0.957,0] ]] #样本集合
    kmeans(4,sample_set)
