#简述：一维无限深方势阱的数值求解，并输出n=1-5的本征值和本征函数
#方法：二阶差分，步长512，但是第一个点和最后一个点需要去掉（见二阶差分矩阵可知）
#其他：m设为1，hbar设为1，势阱为-1/2到1/2
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as scl
#array全部输出
np.set_printoptions(threshold=np.inf)

hbar=1
m=1
N = 512
a = 1.0
x = np.linspace(-a/2.,a/2.,N)
h = x[1]-x[0] # Should be equal to 2*np.pi/(N-1)
V = 0.*x
Mdd = 1./(h*h)*(np.diag(np.ones(N-1),-1) -2* np.diag(np.ones(N),0) + np.diag(np.ones(N-1),1))
H = -(hbar*hbar)/(2.0*m)*Mdd + np.diag(V) 
E,psiT = np.linalg.eigh(H) # This computes the eigen values and eigenvectors，求特征值和特征向量
# psiT是ndarray类型，512*512的二维数组，用于存放同类型的一个多维数组对象。每一个元素在内存中都有相同大小的存储空间。
# transpose对二维数组默认转置,因为H是对称矩阵，故H的转置等于H，又因为H是实矩阵，所以H*=H，综上，H是厄米矩阵
psi = np.transpose(psiT)   # We take the transpose of psiT to the wavefunction vectors can accessed as psi[n]


#多条线一起画
#plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
plt.figure(figsize=(10,7))
for i in range(5):
    plt.plot(x,psi[i],label="$E_{}$={:>8.3f}".format(i,E[i]))
    plt.title("Solutions to the Infinite Square Well")
#for i in range(5):
#    if psi[i][N-10] < 0:   # Flip the wavefunctions if it is negative at large x, so plots are more consistent.
#        plt.plot(x,-psi[i]/np.sqrt(h),label="$E_{}$={:>8.3f}".format(i,E[i]))
#    else:
#        plt.plot(x,psi[i]/np.sqrt(h),label="$E_{}$={:>8.3f}".format(i,E[i]))
#    plt.title("Solutions to the Infinite Square Well")
#plt.legend()
#plt.savefig("Infinite_Square_Well_WaveFunctions.pdf")
plt.show()