# <center>bash-dash-sh 区别</center>

## Linux Shell
Shell是系统的用户界面，提供了用户与内核进行交互操作的一种接口。它接收用户输入的命令并把它送入内核去执行。  

实际上Shell是一个命令解释器，它解释由用户输入的命令并且把它们送到内核。不仅如此，Shell有自己的编程语言用于对命令的编辑，它允许用户编写由shell命令组成的程序。Shell编程语言具有普通编程语言的很多特点，比如它也有循环结构和分支控制结构等，用这种编程语言编写的Shell程序与其他应用程序具有同样的效果。

## bash
Bash(GNU Bourne-Again Shell)是许多Linux平台的内定Shell，事实上，还有许多传统UNIX上用的Shell，像tcsh、csh、ash、bsh、ksh等等。

## dash
有人把 bash 从 NetBSD 移植到 Linux 并更名为 dash (Debian Almquist Shell)，Dash Shell 比 Bash Shell 小的多，符合POSIX标准。

## sh
GNU/Linux 操作系统中的 /bin/sh 本是 bash (Bourne-Again Shell) 的符号链接，但鉴于 bash 过于复杂，，并建议将 /bin/sh 指向 dash。

## Now
Debian和Ubuntu中，/bin/sh默认已经指向dash，这是一个不同于bash的shell，它主要是为了执行脚本而出现，而不是交互，它速度更快，但功能相比bash要少很多，语法严格遵守POSIX标准。

## sh->bash/bash
1. 查看bash/dash/sh 所在位置： 
	**whereis bash**  
	**whereis dash**  
	**whereis sh**
2. 查看sh指向：  
	**ll /bin/sh**	
3. 切换sh指向：  
   	**sudo dpkg-reconfigure dash**  
   	会出现一个图片状的配置菜单，选yes/no对应是否选择dash。

## Reference
[参考1](https://baike.baidu.com/item/Linux%20Shell/10142850?fr=aladdin)  
[参考2](https://www.jianshu.com/p/762d4cccee7e)  