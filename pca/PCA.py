#!/usr/bin/python
# -*- coding: utf-8 -*-

'主成分分析法'
__author__ = 'lemur'

import numpy as np

#极差归一化
def mmn(m):
    for j in range(0,m.shape[1]):
        maxnum = float(max(m[:,j]))
        minnum = float(min(m[:,j]))
        for i in range(0,m.shape[0]):
            m[i,j] = ( m[i,j]-minnum ) / (maxnum-minnum)

def pca(m):
    print '原始数据：'
    print m

    #极差归一化
    mmn(m)
    print '极差归一化后的数据：'
    print m

    #相关系数矩阵，特征值，特征向量
    r = np.corrcoef(m.T)
    evals, evecs = np.linalg.eig(r)
    print '相关系数矩阵R：'
    print r
    print '特征值λ：'
    print evals
    print '特征向量a：'
    print evecs

    #贡献率
    con_rate = [evals[i] / sum(evals) for i in range(0,evals.shape[0])]
    sum_rate = 0
    for i in range(0,len(con_rate)):
        print '弟%d个主成分的贡献率为:%.2f' % (i+1, 100*con_rate[i])
        if sum_rate <0.9:
            sum_rate += con_rate[i]
            num = i+1
    print '前%d个主成分的贡献率超过90%%' % (num)
    
    #主成分评分
    score = m*evecs[:, 0:num]
    print '前%d个主成分评分为：' % (num)
    print score

    #使用贡献率加权的单一指标评分
    score2 = score * np.mat(con_rate[0:num]).T
    print '单一指标评分：'
    print score2

if __name__ == '__main__':
    #pca(m)
