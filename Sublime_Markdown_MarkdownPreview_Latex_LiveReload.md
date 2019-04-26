# <center>Sublime + Markdown</center>
## <center>MarkdownPreview + Latex + LiveReload</center>
***

## 目的：
在sublime text3上实现编辑markdown，同时可编辑latex公式，并且可以在浏览器实时刷新预览。  
前提：ubuntu16.04, sublime text3。

## 1. 安装 MarkdownPreview
1. 组合键盘Ctrl+Shift+P调出命令面板。
2. 输入mdp找到并选中Markdown Preview： Preview in Browser，选择markdown就是传统的本地打开。
3. 默认浏览器中显示预览结果。
4. 设置快捷键：Preferences -> Key Bindings打开的文件的右侧栏的中括号中添加一行代码：  
	**{ "keys": ["alt+m"], "command": "markdown_preview", "args": {"target": "browser", "parser":"markdown"}  }**  
	其中快捷键　**"alt+m"**　可设置为自己喜欢的按键。　　

上述设置后每次预览都要打开一个新的网页，而且需要手动操作。


## 2. 配置Latex支持
1. 打开MarkdownPreview的配置文件：	**Preferences -> Package Settings -> Markdown Preview -> Settings**
2. 输入：  
	**{
    "markdown_extensions": [
        // MathJax Support(支持 Latex)
        // Danger！！！ GitHub and GitLab is not supported with MathJax. 
        // You will have to come up with a MathJax config that works for
        // it and escape problematic syntax that GitHub may try to convert.
        {
            "pymdownx.arithmatex": {
                "generic": true,
            }
        },
    ],
    "js": {
        "markdown": [
            "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js",
            "res://MarkdownPreview/js/math_config.js"
        ],
        "github": ["default"],
        "gitlab": ["default"]
    }
}**
3. 重启sublime text3。


## 3. 安装　LiveReload
1. 打开MarkdownPreview的配置文件：**Preferences -> Package Settings -> Markdown Preview -> Settings**
2. 检查左侧"enable_autoreload"条目是否为"true"，若是，跳过。若不是，该为"true"。
3. Ctrl+Shift+p, 输入 Install Package，输入LiveReload, 回车安装。
4. 安装成功后, 再次Ctrl+shift+p, 输入LiveReload: Enable/disable plug-ins, 回车, 选择 Simple Reload with delay (400ms)或者Simple Reload，两者的区别仅仅在于后者没有延迟。


## 4. 总结
现在只要用快捷键打开网页后，每次只需要保存sublime一次，网页就会自动刷新预览。
还存在问题是，网页不会实时定位到编辑位置，所有还需要手动滑动页面。


### Reference
1. [参考网址](https://blog.csdn.net/qq_20011607/article/details/81370236)  
2. [参考网址](https://blog.csdn.net/u013019701/article/details/81676018)