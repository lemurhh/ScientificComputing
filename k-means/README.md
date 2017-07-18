K-Means
============

Python实现的K-Means算法。

### 1、功能
实现K-Means算法

### 2、使用
将```KMeans.py```放入环境变量包含的的目录内，导入模块，输入样本集合，选取合适的k值，调用kmeans函数即可。
```
import KMeans

sample_set = [ [0,0],[1,0],[0,1],[1,1],[2,1],[1,2],[2,2],[3,2],[6,6],[7,6],[7,7],[8,8],[9,9],[8,9],[9,8]  ] #样本集合
kmeans(2,sample_set) #k=2

```
### 3.输出格式
默认将样本数据编号（1,2，...,n），输出结果以编号代替原始样本，若想输出原始样本，请更改样本类里的```__str__()```方法。
同一行的编号表示编号对应的样本位于同一聚类。