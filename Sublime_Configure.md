# <div align="center"> Sublime Configure </div>
***

# Install
1. [通过apt命令安装](https://www.sublimetext.com/docs/3/linux_repositories.html)  
```bash  

	wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -  
	sudo apt-get install apt-transport-https  
	echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list  
	sudo apt-get update  
	sudo apt-get install sublime-text  
```

2. [通过官网下载安装包](https://www.sublimetext.com/3)  
```bash  

	cd ~/download  
	tar -jxvf sublime_text_3_build_3176_x64.tar.bz2  
	mv sublime_text_3 /opt  
	cd /opt/sublime_text_3  
	mv sublime_text.desktop /usr/share/applications  
	ln -s /opt/sublime_text_3/sublime_text /usr/bin/subl  
	ln -s /opt/sublime_text_3/sublime_text /usr/local/subl  
```

## 配置  
1. 确定`sublime_text.desktop`文件里的执行路径和图片路径均符合`/opt/sublime_text_3/`下对应路径。  

2. 在左上角dash里搜索`sublime_text.desktop`，并将其拖拽到左侧任务栏。  

3. 添加软件右键打开选项  
```bash  

	cp -it ~/.local/share/applications /usr/share/applications/sublime_text.desktop  
	sudo update-desktop-database  
```  

4. 安装`package control`  
```
	调出控制台：　CTRL + \` 或者View->Show Console  
	输入：  
	import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)  
```  

5. 字体调整:`Preferences->settings`，在`User`那侧的大括号里添加`"font_size": 12,`



