
# 求解薛定谔方程

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

## 一维无限深方势阱
