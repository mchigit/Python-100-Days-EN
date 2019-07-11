<!-- ## Day04 - 循环结构 -->

## Day04 - Loops

<!-- ### 循环结构的应用场景

如果在程序中我们需要重复的执行某条或某些指令，例如用程序控制机器人踢足球，如果机器人持球而且还没有进入射门范围，那么我们就要一直发出让机器人向球门方向奔跑的指令。当然你可能已经注意到了，刚才的描述中其实不仅仅有需要重复的动作，还有我们上一个章节讲到的分支结构。再举一个简单的例子，比如在我们的程序中要实现每隔1秒中在屏幕上打印一个&quot;hello, world&quot;这样的字符串并持续一个小时，我们肯定不能够将`print('hello, world')`这句代码写上3600遍，如果真的需要这样做那么编程的工作就太无聊了。因此，我们需要了解一下循环结构，有了循环结构我们就可以轻松的控制某件事或者某些事重复、重复、再重复的发生。在Python中构造循环结构有两种做法，一种是`for-in`循环，一种是`while`循环。 -->

### Why do we need loops?

Sometimes, we need to execute a set of instructions repeatedly. For example, if we want our program to print "hello, world" every second for an hour, we don't want to write the code `print("hello, world")` 3600 times. If we had to do that being a developer is such a boring job.   
Therefore, we need to familiarize ourself with the concept of loops. With loops, we can easily repeat instructions. There are 2 kinds of loops in Python: `for-in` and `while`. 
<!-- 
### for-in循环

如果明确的知道循环执行的次数或者是要对一个容器进行迭代（后面会讲到），那么我们推荐使用`for-in`循环，例如下面代码中计算![$\sum_{n=1}^{100}n$](./res/formula_1.png)。 -->

### for-in loops

If we know definietely the number of repetition or iterate through a collection (we will talk about this later), then we should use `for-in`. For example, the following code calculates the summation of n for n from 1 to 100. (![$\sum_{n=1}^{100}n$](./res/formula_1.png))

```Python
"""
Use for to calculate summation

Version: 0.1
Author: 骆昊
"""

sum = 0
for x in range(101):
    sum += x
print(sum)
```
<!-- 
需要说明的是上面代码中的`range`类型，`range`可以用来产生一个不变的数值序列，而且这个序列通常都是用在循环中的，例如：

- `range(101)`可以产生一个0到100的整数序列。
- `range(1, 100)`可以产生一个1到99的整数序列。
- `range(1, 100, 2)`可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。 -->

Here is something to note:  
The above code uses `range` function, which generates a set of sequence of numbers, which is often used in loops. For example:

- `range(101)` creates a sequence of integers from 0 to 100
- `range(1, 100)` creates a sequence of integers from 1 to 99
- `range(1, 100, 2)` creates a sequence of integers from 1 to 99, step up by 2. So this sequence include (1, 3, 5, 7...99)

For more on the range function, read more at the [documentation.](https://docs.python.org/3/library/functions.html#func-range)

<!-- 知道了这一点，我们可以用下面的代码来实现1~100之间的偶数求和。 -->

The code below can be used to calculate the sum of all even numbers between 1 and 100

```Python
"""
use for to calculate sum of all even numbers between 2 and 100

Version: 0.1
Author: 骆昊
"""

sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)
```

<!-- 也可以通过在循环中使用分支结构的方式来实现相同的功能，代码如下所示。 -->

You can also nest an `if` statement to accomplish the same thing:

```Python
"""

Version: 0.1
Author: 骆昊
"""

sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)
```

<!-- ### while循环

如果要构造不知道具体循环次数的循环结构，我们推荐使用`while`循环，`while`循环通过一个能够产生或转换出`bool`值的表达式来控制循环，表达式的值为`True`循环继续，表达式的值为`False`循环结束。下面我们通过一个“猜数字”的小游戏（计算机出一个1~100之间的随机数，人输入自己猜的数字，计算机给出对应的提示信息，直到人猜出计算机出的数字）来看看如何使用`while`循环。 -->

### while loop

If we don't know the exact time of repetition, `while` loops can be used. `while` loop calculates the result of a boolean expression, and if the result is `True`, will continue to repeat. The loop will stop when the result of that expression becomes `False`. 

```Python
"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Computer generates a random integer between 1 to 100
Given user input, computer will give hints or tell user that they guessed it correctly. 

Version: 0.1
Author: 骆昊
"""

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('Please enter: '))
    if number < answer:
        print('Guess Bigger')
    elif number > answer:
        print('Guess Smaller')
    else:
        print('You got it!')
        break
print('You guessed %d times' % counter)
if counter > 7:
    print('Wow you are bad at this game')
```

<!-- > **说明：** 上面的代码中使用了`break`关键字来提前终止循环，需要注意的是`break`只能终止它所在的那个循环，这一点在使用嵌套的循环结构（下面会讲到）需要引起注意。除了`break`之外，还有另一个关键字是`continue`，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。 -->

> **Note:** Code above uses `break` keyword to terminate the loop early, also note that `break` can only terminate the immediate loop that surrounds it. This is an important concept used in nested loops (will be mentioned later). `continue` keyword is use to terminate code execution of current iteration, and continue directly into the next loop iteration. 

<!-- 和分支结构一样，循环结构也是可以嵌套的，也就是说在循环中还可以构造循环结构。下面的例子演示了如何通过嵌套的循环来输出一个九九乘法表。 -->

Same as if statement, loops can be nested as well. The below example shows how we can nest loops to find the answer of multiplying 1 through 9 by 1 through 9. 

```Python
"""

Version: 0.1
Author: 骆昊
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
```

### Exercise

#### Exercise 1：Check whether a number is prime

```Python
"""

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
from math import sqrt

num = int(input('Enter: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d is prime' % num)
else:
    print('%d is not prime' % num)
```

#### Exercise 2：Find greatest common factor and least common multiplier

```Python
"""

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d and %d greatest common factor is %d' % (x, y, factor))
        print('%d and %d least common multiplier is %d' % (x, y, x * y // factor))
        break
```

#### Exercise 3：Print the following trangle shapes

```Python
"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: 骆昊
"""

row = int(input('Enter number of rows: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
```
