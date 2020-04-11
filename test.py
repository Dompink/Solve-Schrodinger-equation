# test测试文档
import numpy as np
import matplotlib.pyplot as plt
N = 128
a = 2*np.pi
x = np.linspace(0,2*np.pi,N)
h = x[1]-x[0] # Should be equal to 2*np.pi/(N-1)
y = np.sin(x)

#一阶差分
# np.ones(N)，创造一个含N个元素的一维数据，对np.diag(v,k)，如果v是1D数组，返回一个v作为相对对角
# 线k位置的2维数组，如果v是2D数组，返回对角线数值，注意，若输入一个1*4，k=1，会返回一个5*5，原先
# 的数值在对角线靠右1单位的位置
Md = 1./h*(np.diag( -1.*np.ones(N),0) + np.diag(np.ones(N-1),1))
# 求Md和y的点积，效果与np.dot(Md,y)相同
yp = Md.dot(y)

#二阶差分,二阶差分的第一个点和最后一个点都不能用
Mdd = 1./(h*h)*(np.diag(np.ones(N-1),-1) + np.diag( -2.*np.ones(N),0) + np.diag(np.ones(N-1),1))
ypp = Mdd.dot(y)
plt.figure(figsize=(10,7))
plt.plot(x,y)
plt.plot(x[:-1],yp[:-1])     # Last value is invalid, don't plot
plt.plot(x[1:-1],ypp[1:-1])  # First and last value is invalid.
plt.show()