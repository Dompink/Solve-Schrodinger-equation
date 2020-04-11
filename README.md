
# 求解薛定谔方程

使用数值方法求解薛定谔方程，可以先运行test文件来进行简单的运行测试。  
薛定谔方程为:  
$$\frac{-\hbar^2}{2m}\frac{d^2}{dx^2}\psi+V\psi=E\psi$$
化简为：  
$$(\frac{-\hbar^2}{2m}\frac{d^2}{dx^2}+V)\psi=E\psi$$  
即：  
$$H\psi=E\psi$$  
哈密顿量为：  
$$H=\frac{-\hbar^2}{2m}
\left( \begin{array}{ccc}
    -2&  1&   0&   0&    \\
     1& -2&   1&   0&    \\
     0&  1&  -2&   1&    \\
      &   & ...& ...& ...\\
      &   &    &   1&  -2\\
\end{array}\right)$$
矩阵部分即为二阶差分，以用来数值求解薛定谔方程。  
二阶差分：  
$$f'=(f_{i+1}-2f_i+f_{i-1})/h^2$$

## 一维无限深方势阱/Infinite_Square_Well

在m设为1，hbar设为1，势阱为-1/2到1/2的情况下，利用二阶差分求解薛定谔方程。

## 一维有限深方势阱/Finite_Square_Well
