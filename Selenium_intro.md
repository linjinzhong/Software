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
2. 访问页面：  
```python  
browser.get('https://www.baidu.com')  
print(browser.page_source)  
browser.close()  
```  
3. 查找元素：  
```python   
	A = browser.find_element_by_id('css_index')  
	B = browser.find_element_by_css_selector('#css_index')  
	C = browser.find_element_by_xpath('//*[@id="css_index"]')  
	print(A)  
	print(B)  
	print(C)  
```  

4. 多元素查找：  
```python  
	browser.find_elements_by_id('xx xx')  

	```

5. 元素交互：  
```python  
	input_str = browser.find_element_by_id('kw')  
	input_str.send_keys("apple")  
	time.sleep(1)  
	input_str.clear()  
	input_str.send_keys("watch")  
	button = browser.find_element_by_id('su')  
	# button = browser.find_element_class_name('bg s_btn')  
	# 复合class使用如下替换  
	# button = browser.find_element_by_css_selector('.bg.s_btn')  
	button.click()  
	# browser.close()  
	# 当使用browser.find_elements_by_id('su')，报错  
	# AttributeError: 'list' object has no attribute 'click'  
	# 这是因为不是多元素查找，替换为find_element_by_id  

	```

6. 执行JavaScript（登录知乎并且滑动到页面底部并弹框提示你）：  
```python
	browser = webdriver.Chrome()  
	browser.get("http://www.zhihu.com/explore")  
	browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')  
	browser.execute_script('alert("To Bottom")')  

	```  

7. 获取属性、文本、ID、位置：  
```python
	logo = browser.find_element_by_id('zh-top-link-logo')  
	print(logo)  
	print(logo.get_attribute('class'))  
	input = browser.find_element_by_class_name('zu-top-add-question')  
	print(input.text)  
	input = browser.find_element_by_class_name('zu-top-add-question')  
	print(input.id)  
	print(input.location)  
	print(input.tag_name)  
	print(input.size)  

	```

8. 等待：  
	1. 隐式等待：  
	```python  
		browser = webdriver.Chrome()  
		browser.get('https://www.zhihu.com/explore')  
		**browser.implicitly_wait(5)**  
		input_str = browser.find_element_by_class_name('zu-top-add-question')  
		print(input_str)  

		```

	2. 显示等待：显式等待,就是明确的要等到某个元素的出现或者是某个元素的可点击等条件,等不到,就一直等,除非在规定的时间之内都没找到,那么就跳出Exception。    
	```python  
		from selenium import webdriver  
		**from selenium.webdriver.common.by import By**  
		**from selenium.webdriver.support.ui import WebDriverWait**  
		**from selenium.webdriver.support import expected_conditions as EC**  
		browser = webdriver.Chrome()  
		browser.get('https://www.taobao.com/')  
		**wait = WebDriverWait(browser, 10)  
		input_str = wait.until(EC.presence_of_element_located((By.ID, 'q')))  
		button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))**  
		print(input_str, button)  

		```

	3. 常见判断条件：    
	```python  
		title_is 标题是某内容  
		title_contains 标题包含某内容  
		presence_of_element_located 元素加载出，传入定位元组，如(By.ID, 'p')  
		visibility_of_element_located 元素可见，传入定位元组  
		visibility_of 可见，传入元素对象  
		presence_of_all_elements_located 所有元素加载出  
		text_to_be_present_in_element 某个元素文本包含某文字  
		text_to_be_present_in_element_value 某个元素值包含某文字  
		frame_to_be_available_and_switch_to_it frame加载并切换  
		invisibility_of_element_located 元素不可见  
		element_to_be_clickable 元素可点击  
		staleness_of 判断一个元素是否仍在DOM，可判断页面是否已经刷新  
		element_to_be_selected 元素可选择，传元素对象  
		element_located_to_be_selected 元素可选择，传入定位元组  
		element_selection_state_to_be 传入元素对象以及状态，相等返回True，否则返回False  
		element_located_selection_state_to_be 传入定位元组以及状态，相等返回True，否则返回False  

		```	 

9. 前进和后退：  
```python  
	import time  
	from selenium import webdriver  
	browser = webdriver.Chrome()  
	browser.get('https://www.baidu.com/')  
	browser.get('https://www.taobao.com/')  
	browser.get('https://www.python.org/')  
	browser.back()  
	browser.forward()    
	browser.close()  

	```

10. cookie操作：  
```python  
	from selenium import webdriver  
	browser = webdriver.Chrome()  
	browser.get('https://www.zhihu.com/explore')  
	**print(browser.get_cookies())**  
	**browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'zhaofan'})**  
	print(browser.get_cookies())  
	**browser.delete_all_cookies()**  
	print(browser.get_cookies())  

	```

11. 选项卡管理：通过执行js命令实现新开选项卡**`window.open()`**，不同选项卡是存在列表**`browser.window_handles`**，通过**`browser.window_handles[0]`**可以取到第一个选项卡  
```python  
	import time  
	from selenium import webdriver  
	browser = webdriver.Chrome()  
	browser.get('https://www.baidu.com')  
	**browser.execute_script('window.open()')**  
	**print(browser.window_handles)**  
	**browser.switch_to.window(browser.window_handles[1])**  
	browser.get('https://www.taobao.com')  
	time.sleep(2)  
	browser.switch_to.window(browser.window_handles[0])  
	browser.get('https://python.org')  

	```

12. 异常处理（查找一个不存在的元素例子）：     
```python  
	from selenium import webdriver  
	**from selenium.common.exceptions import TimeoutException,NoSuchElementException**  
	browser = webdriver.Chrome()  
	try:  
		browser.get('https://www.baidu')  
	except TimeoutException:  
		print('Time Out')  
	try:  
		browser.find_element_by_id('hello')  
	except NoSuchElementException:  
		print('No Element')  
	finally:  
		browser.close()  

```

Reference  
[参考1](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains)
[参考２](https://blog.csdn.net/qq_29186489/article/details/78661008)