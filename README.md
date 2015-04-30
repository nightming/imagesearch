使用python制作图像搜索的本地脚本
==========
基于图像的局部颜色直方图信息，提取特征描述子，实现在一图像数据集中搜索出相似度最高的若干张图像。

---
由于目前没能加入到web框架，所以只能采用脚本方式运行

使用说明：

1.运行buildindex.py文件提取数据集，因为采用的数据集比较大，脚本运行需要一定的时间，所以可以先保存好提取到的数据集，采用命令：

`python buildindex.py -d imgfile -i index.csv`

这样可以将特征集保存在同文件夹下的index.csv。

2.实际搜索图片时运行命令`python procsearch.py -q imgname -i index.csv -o outputfile `,搜索结果保存在outputfile中，可以利用opencv函数显示

用到的主要库：cv2,argparse,numpy.
