<!-- ## 图形用户界面和游戏开发 -->
## Basic GUI and Game Development

### tkinter module

<!-- GUI是图形用户界面的缩写，图形化的用户界面对使用过计算机的人来说应该都不陌生，在此也无需进行赘述。Python默认的GUI开发模块是tkinter（在Python 3以前的版本中名为Tkinter），从这个名字就可以看出它是基于Tk的，Tk是一个工具包，最初是为Tcl设计的，后来被移植到很多其他的脚本语言中，它提供了跨平台的GUI控件。当然Tk并不是最新和最好的选择，也没有功能特别强大的GUI控件，事实上，开发GUI应用并不是Python最擅长的工作，如果真的需要使用Python开发GUI应用，wxPython、PyQt、PyGTK等模块都是不错的选择。 -->

GUI is the abbreviation for Graphical User Interface. The default module for Python for GUI development is tkinter, which is based on TK. [TK](https://en.wikipedia.org/wiki/Tk_(software)) is a widget toolkit that provides a library of elements for GUI widgets in many programming languages. In fact, TK is not the best GUI toolkit, but Python was not meant for developing GUI applications anyway. Other options such as wxPython, PyQT, PyGTK modules also exists and are used.

<!-- 基本上使用tkinter来开发GUI应用需要以下5个步骤：

1. 导入tkinter模块中我们需要的东西。
2. 创建一个顶层窗口对象并用它来承载整个GUI应用。
3. 在顶层窗口对象上添加GUI组件。
4. 通过代码将这些GUI组件的功能组织起来。
5. 进入主事件循环(main loop)。 -->

Essentially, there are 5 steps for developing a GUI using tkinter:

1. Importing tkinter modules
2. Create a Tk object to contain all GUI
3. Add GUI widgets to the Tk object
4. Using code to connect the functions of these GUI widgets
5. Enter main loop

<!-- 
下面的代码演示了如何使用tkinter做一个简单的GUI应用。 -->

Code below demonstrates how to create a basic GUI app using tkinter

```Python
import tkinter
import tkinter.messagebox


def main():
    flag = True

    def change_label_text():
        # a nonlocal variable declares the variable not local scope.
        # For more, read https://www.w3schools.com/python/ref_keyword_nonlocal.asp
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        # label is a widget
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('Reminder', 'Are you sure you want to quit?'):
            top.quit()

    # Creating a top TK object (Window to hold everything)
    top = tkinter.Tk()
    # Configure the size
    top.geometry('240x160')
    # Configure title
    top.title('Game')
    # Create a label object and add it to the top TK object
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # Create a Frame object
    panel = tkinter.Frame(top)
    # Creating button widget objects, add it to the Frame object we just defined
    # Passing in functions as commands
    button1 = tkinter.Button(panel, text='Modify', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='Quit', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # Enter main loop
    tkinter.mainloop()


if __name__ == '__main__':
    main()
```

<!-- 需要说明的是，GUI应用通常是事件驱动式的，之所以要进入主事件循环就是要监听鼠标、键盘等各种事件的发生并执行对应的代码对事件进行处理，因为事件会持续的发生，所以需要这样的一个循环一直运行着等待下一个事件的发生。另一方面，Tk为控件的摆放提供了三种布局管理器，通过布局管理器可以对控件进行定位，这三种布局管理器分别是：Placer（开发者提供控件的大小和摆放位置）、Packer（自动将控件填充到合适的位置）和Grid（基于网格坐标来摆放控件），此处不进行赘述。 -->

GUI applications are usually triggered by events. Therefore by entering main loop, the program is listening to any mouse and keyboard events, and execute corresponding code. Because events will occur continuously, we need to enter a wait loop to listen to events. Tk has 3 geometry managers: place, grid and pack. These different geometry managers allow developers to specify location of a widget.

<!-- ### 使用Pygame进行游戏开发 -->
## Using Pygame

<!-- Pygame是一个开源的Python模块，专门用于多媒体应用（如电子游戏）的开发，其中包含对图像、声音、视频、事件、碰撞等的支持。Pygame建立在[SDL](https://zh.wikipedia.org/wiki/SDL)的基础上，SDL是一套跨平台的多媒体开发库，用C语言实现，被广泛的应用于游戏、模拟器、播放器等的开发。而Pygame让游戏开发者不再被底层语言束缚，可以更多的关注游戏的功能和逻辑。

下面我们来完成一个简单的小游戏，游戏的名字叫“大球吃小球”，当然完成这个游戏并不是重点，学会使用Pygame也不是重点，最重要的我们要在这个过程中体会如何使用前面讲解的面向对象程序设计，学会用这种编程思想去解决现实中的问题。 -->

Pygame is an open source Python module, used for writing video games, which provides support for graphics, audio, video, events and collisions. Pygame is based on [SDL](https://en.wikipedia.org/wiki/Simple_DirectMedia_Layer), which is a cross-platform software development library written in C. Pygame allows developers to be unrestricted by lower level programming languages, and focus on the function and logic of the game.

We now try to create a simple game, the point is not to complete the game, or to learn about Pygame. We should be focusing on the object oriented concepts we talked about before, and think in terms of objects/classes.

#### Creating a game window

```Python
import pygame


def main():
    # init
    pygame.init()
    # declare a screen and set the size
    screen = pygame.display.set_mode((800, 600))
    # set title
    pygame.display.set_caption('game')
    running = True
    # Enter a loop
    while running:
        # Get events and execute on them
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
```
<!-- 
#### 在窗口中绘图

可以通过pygame中draw模块的函数在窗口上绘图，可以绘制的图形包括：线条、矩形、多边形、圆、椭圆、圆弧等。需要说明的是，屏幕坐标系是将屏幕左上角设置为坐标原点`(0, 0)`，向右是x轴的正向，向下是y轴的正向，在表示位置或者设置尺寸的时候，我们默认的单位都是[像素](https://zh.wikipedia.org/wiki/%E5%83%8F%E7%B4%A0)。所谓像素就是屏幕上的一个点，你可以用浏览图片的软件试着将一张图片放大若干倍，就可以看到这些点。pygame中表示颜色用的是色光[三原色](https://zh.wikipedia.org/wiki/%E5%8E%9F%E8%89%B2)表示法，即通过一个元组或列表来指定颜色的RGB值，每个值都在0~255之间，因为是每种原色都用一个8位（bit）的值来表示，三种颜色相当于一共由24位构成，这也就是常说的“24位颜色表示法”。 -->

#### Drawing

We can use the draw module from pygame to draw images such as lines, circle, eclipse etc. The screen is composed of coordinates, with `(0,0)` at the top left corner. Horizontal is x-axis and vertical is y-axis. Pygame uses [RGB color code](https://www.w3schools.com/colors/colors_rgb.asp) to represent colors.

```Python
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('game')
    # Set the background color using fill function
    screen.fill((242, 242, 242))
    # draw a circle.
    # Params: draw(screen, color, position, radius, 0 = filled)
    pygame.draw.circle(screen, (255, 0, 0,), (100, 100), 30, 0)
    # Refresh the display to show the circle
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
```

#### Loading an image

<!-- 如果需要直接加载图像到窗口上，可以使用pygame中image模块的函数来加载图像，再通过之前获得的窗口对象的`blit`方法渲染图像，代码如下所示。 -->

If you want to directly load an image to the display screen, it can be loaded using image module from pygame, then using `blit` to add the image to the display screen.

```Python
import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('game')
    screen.fill((255, 255, 255))
    # load an image
    ball_image = pygame.image.load('./res/ball.png')
    # add the image to screen at position (50,50)
    screen.blit(ball_image, (50, 50))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
```

#### Animations

<!-- 说到[动画](https://zh.wikipedia.org/wiki/%E5%8A%A8%E7%94%BB)这个词大家都不会陌生，事实上要实现动画效果，本身的原理也非常简单，就是将不连续的图片连续的播放，只要每秒钟达到了一定的帧数，那么就可以做出比较流畅的动画效果。如果要让上面代码中的小球动起来，可以将小球的位置用变量来表示，并在循环中修改小球的位置再刷新整个窗口即可。 -->

An [animation](https://en.wikipedia.org/wiki/Animation) is a method in which pictures are manipulated to appear as moving images. So for our purpose, we want the ball to start moving. We can realize this by displaying the ball at different positions using a variable in a loop, and refresh the screen. 

```Python
import pygame


def main():

    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption('game')
    # Variable to define positions
    x, y = 50, 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0,), (x, y), 30, 0)
        pygame.display.flip()
        # refresh the screen every 50 ms
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == '__main__':
    main()
```

#### Collision detection

<!-- 通常一个游戏中会有很多对象出现，而这些对象之间的“碰撞”在所难免，比如炮弹击中了飞机、箱子撞到了地面等。碰撞检测在绝大多数的游戏中都是一个必须得处理的至关重要的问题，pygame的sprite（动画精灵）模块就提供了对碰撞检测的支持，这里我们暂时不介绍sprite模块提供的功能，因为要检测两个小球有没有碰撞其实非常简单，只需要检查球心的距离有没有小于两个球的半径之和。为了制造出更多的小球，我们可以通过对鼠标事件的处理，在点击鼠标的位置创建颜色、大小和移动速度都随机的小球，当然要做到这一点，我们可以把之前学习到的面向对象的知识应用起来。 -->

In a game, lots of collisions occur between objects. Pygame sprite module provides support for detecting collisions. Theoretically, it's very easy to detect whether 2 circles collided, we just need to calculate whether the distance between the center of 2 circles is less than the sum of radius. We can use a mouse event to create new circles. The code below uses everything we've learned so far. 

```Python
from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique
class Color(Enum):

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """eat another ball"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)
```

<!-- #### 事件处理 -->
### Event handling

<!-- 可以在事件循环中对鼠标事件进行处理，通过事件对象的`type`属性可以判定事件类型，再通过`pos`属性就可以获得鼠标点击的位置。如果要处理键盘事件也是在这个地方，做法与处理鼠标事件类似。 -->

We can use the `type` property to detect event type, and use `pos` property to retrieve where the mouse click occurred. Processing keyboard strokes are very similar. 

```Python
def main():
    balls = []
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Game')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Detecting mouse click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # Create a ball at position of mouse click
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)
        screen.fill((255, 255, 255))
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()
```

<!-- 上面的两段代码合在一起，我们就完成了“大球吃小球”的游戏（如下图所示），准确的说它算不上一个游戏，但是做一个小游戏的基本知识我们已经通过这个例子告诉大家了，有了这些知识已经可以开始你的小游戏开发之旅了。其实上面的代码中还有很多值得改进的地方，比如刷新窗口以及让球移动起来的代码并不应该放在事件循环中，等学习了多线程的知识后，用一个后台线程来处理这些事可能是更好的选择。如果希望获得更好的用户体验，我们还可以在游戏中加入背景音乐以及在球与球发生碰撞时播放音效，利用pygame的mixer和music模块，我们可以很容易的做到这一点，大家可以自行了解这方面的知识。事实上，想了解更多的关于pygame的知识，最好的教程是[pygame的官方网站](https://www.pygame.org/news)，如果英语没毛病就可以赶紧去看看啦。 如果想开发[3D游戏](https://zh.wikipedia.org/wiki/3D%E6%B8%B8%E6%88%8F)，pygame就显得力不从心了，对3D游戏开发如果有兴趣的读者不妨看看[Panda3D](https://www.panda3d.org/)。 -->

The code above combined is a complete game. The above code can be modified in a lot of places, such as the code to refresh and move the ball should not be put in a loop. After learning about multi-threaded programming, maybe using another background thread to handle these execution is a better idea. To enhance experience, we can use mixer or music module to add background music and audio effects. To know more about pygame, you can read more at https://www.pygame.org/news. If you want to develop 3-D games, then [Panda3D](https://www.panda3d.org/) is a good choice. 
