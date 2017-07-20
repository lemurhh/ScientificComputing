PCA
============
Python实现的主成分分析法。

### 0.依赖模块
使用numpy模块。

### 1.使用
使用```import PCA```导入，调用pca函数即可。
pca函数只有一个参数：
* ```m```, 数据矩阵，使用np.mat()创建
```
import PCA

data = np.mat([ [0,0,0], [1,1,1], [2,2,2], [3,3,3] ])
pca(data)
```
### 2.输出
依次输出```原始数据、极差归一化后的数据、相关系数矩阵、特征值、特征向量、贡献率、主成分评分、使用贡献率加权主成分后的单一指标评分```