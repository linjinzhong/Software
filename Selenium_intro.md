# <center>Selenium</center>
![selenium](https://raw.githubusercontent.com/linjinzhong/Picture/master/selenium.png)

## 介绍
selenium是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。支持的浏览器包括IE，Mozilla Firefox，Safari，Google Chrome，Opera等。在爬虫中主要用来解决JavaScript渲染问题。当requests和urllib无法正常获取网页内容时，可以用selenium模拟浏览器进行网页加载。  

Selenium可以根据我们的指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏，或者判断网站上某些动作是否发生。Selenium自己不带浏览器，不支持浏览器的功能，它需要与第三方浏览器结合在一起才能使用。

[官方文档](https://selenium-python.readthedocs.io/installation.html)

## 安装  
1. 安装selenium: `pip install selenium`  

2. 下载驱动  
需要下载相应驱动浏览器的驱动（注意对应软件版本号和驱动号）    
| Chrome | [Chrome驱动](https://sites.google.com/a/chromium.org/chromedriver/downloads)|  
| Firefox| [Firefox驱动](https://github.com/mozilla/geckodriver/releases)|  
| Edge| [Edge驱动](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)|  
| Safari| [Safari驱动](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)|  

3. 安装驱动
解驱动解压、添加执行权限、移动到`/usr/bin` 或者 `/usr/local/bin.`  

## 基本使用
在使用python写爬虫的时候，主要使用selenium的webdriver功能。  
1. 申明浏览器对象：  
```python  
from selenium import webdriver  
browser = webdriver.Chrome()  
browser = webdriver.Firefox()  

```  
2. 


