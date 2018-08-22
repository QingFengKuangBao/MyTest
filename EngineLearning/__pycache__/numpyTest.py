import numpy as np

# 创建ndarray
# print("zeros......")
# print(np.zeros((2, 5)))
# print("empty.......")
# print(np.empty((2, 5)))
# print(np.logspace(2,3,20))
# print(np.geomspace(100,1000,20))
a = np.arange(20)
print(a)


# ndarray的属性
print("\nnumpy...属性.......")
print("ndim:...%s" % a.ndim)  # 行数
print('itemsize:....%s' % a.itemsize)  # 一个元素的字节数
print("shape:.....%s" % a.shape)  # 结构
print('size:....%s' % a.size)  # 元素的个数
print("dtype:.....%s" % a.dtype)  # 元素的类型
# print(a.flags)
print("nbytes:.....%s" % a.nbytes)  # 总字节数
print("ndim:.....%s" % a.ndim)  # 几维数组


print("\nndarray的操作方法.....")
# 改变ndarray的结构 reshape
b = np.reshape(a, (4, 5))
print("矩阵b....\n%s" % b)

# 转换为一行 ravel()
# print("矩阵b的ravel...\n%s" % np.ravel(b))

# 矩阵的转置
# print("矩阵b的转置T...\n%s" % b.T)

# 横向拼接
# c=np.zeros((4,3),dtype=b.dtype)
# print(np.hstack((b,c)))


# 竖向拼接
# c=np.zeros((1,5),dtype=b.dtype)
# print(np.vstack((b,c)))

# 切割
# print(np.vsplit(b,2))
# print(np.hsplit(b,(2,3)))

x1=[1,2,3,4]
x2=[1,5]
print(np.outer(x1,x2))