#### Python练习 2

1. 让用户向空列表里依次输入10个整数，结束后输出这个列表

2. 不使用列表的reverse方法，将以下列表反转

   ```python
   list_a = [9, 80, 39, 48, 26, 2, 6, 77, 58, 25, 65]
   ```

3. 不使用列表的sort或sorted，使用while或if或for对以下列表排序

   ```python
   list_b = [9, 80, 39, 48, 26, 2, 6, 77, 58, 25, 65]
   ```

4. Fibonacci数列是这样一个数列，他的后一项等于前两项之和，前两项为1，因此该数列为 $1,\ 1,\ 2,\ 3,\ 5,\ 8,...$ 现从用户那里输入一个大于等于3的正整数n，输出Fibonacci数列的前n项

5. 欧几里得是古希腊著名数学家，他提出了一种计算两个数最大公因数的算法，欧几里得算法或辗转相除法，通过编写代码用欧几里得算法求下面两个数的最大公因数

   ```python
   a = 2813
   b = 3589
   ```

​		辗转相除法就是用a和b较大的那个数去除以较小的那个数，将得到的余数替换掉较大的数，以此类推直到a和b有一个数为0，此时另一个数就是最大公因数

​		例如(12, 20) = (12, 8) = (4, 8) = (4, 0)，因此12和20的最大公因数是4

6. 牛顿迭代法在数值计算中常常用于求方程的数值近似解，请编写一段代码使用牛顿迭代法计算 $\sqrt{2}$ 和 $\sqrt{3}$ 的近似值。（迭代100次，初始值使用x=1.0）![截屏2024-08-02 20.19.47](/Users/jason_han/Library/Application Support/typora-user-images/截屏2024-08-02 20.19.47.png)

   提示: 以 $\sqrt{2}$ 为例，我们要求解的方程是 $x^2-2=0$. 首先画出 $y=x^2-2$ 的图像，然后随便选取曲线上的一点A做切线，这条切线和x轴交于B点，过B做x轴垂线交抛物线于C点，再过C点做切线交x轴于D点，再过D点做x轴垂线交抛物线为E点... 如此反复，切线和x轴的交点会无限接近函数零点

   从这个方法出发，我们可以构造迭代式，具体过程如下

   $(x_n,\ y_n)$ 为抛物线上一点，那么他的切线为 $y-y_n=f'(x_n)(x-x_n)$，这条切线与x轴的交点的横坐标是 $x=x_n-\frac{y_n}{f'(x_n)}$，这个横坐标同时就是下一次迭代选取的抛物线上的点的对应的横坐标，因此 $x_{n+1}=x_n-\frac{y_n}{f'(x_n)}=x_n-\frac{x_n^2-2}{2x_n}$

   换言之，满足递推关系 $x_{n+1}=x_n-\frac{x_n^2-2}{2x_n}$ 的数列将收敛到 $\sqrt{2}$

7. 算术基本定理告诉我们每一个大于1的自然数可以唯一分解为质数的乘积，编写一段代码判断用户输入的数字是否为质数

   提示: 判断一个数 $n$ 是否是素数，只需要判断这个数有没有小于等于 $\sqrt{n}$ 的因子

8. 水仙花数是指一个三位数，它每个数位的立方和等于它本身，找到所有的水仙花数并输出

   (例如 $153=1^3+5^3+3^3$)