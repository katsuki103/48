<img src="https://i.loli.net/2020/08/19/21HPdw8r94XFlgz.png" ></a>

# Any2Excel

一款使用 Python 编写的图像内表格数据提取工具，可以高效识别 PDF 原件、扫描件、复印件、彩色（黑白）照片、截图内的数据表格，提取后转为 Excel 文件输出。

这是一款开源工具，我给它取名叫`Any2Excel`。顾名思义，往后的目标就是提取任意格式文件中的数据图表到可被结构化处理的 Excel 文件。

识别度高，操作简单，使用场景广泛。

_支持手机拍照、扫描件、原件、复印件等等_

# 快速开始

## Python PIP 依赖

```
pip install -r .\requirements.txt
```

## 外部依赖

```cmd
poppler 安装后将其bin路径加入系统变量中
```

## 配置腾讯云

`cp config+sample.yml config.yml`后补全`config.yml`中的配置信息。

## 工作原理

- 将 PDF 按每页转为 JPG 图像文件

- 暂时只取 PDF 第一页内容

- 提交 OCR 识别这个图像文件

- 将识别结果转为 Excel 导出

- 清除 Excel 文件的全部样式

## 命令行（CLI）

### PDF 转 Excel

```shell
cd PDF2Excel
python3 pdf2excel.py test.pdf
```

### 图片 转 Excel

```shell
cd PDF2Excel
python3 image2excel.py capture.jpg
```

## 可视化拖拽

将需要转换的 PDF 文件/图片文件，拖拽到程序上就会自动执行

## 输出文件

`*.xlsx` 包含了样式的 Excel 文件，可能会因为样式过多而文件过大。

`*.xls` 移除了样式的 Excel 文件，推荐。

# 配置

`config.yml` 内包含了腾讯云的相关鉴权信息

# 演示

## 动画

### Image To Excel

![](https://oss.liujunyang.com/blog/images/1.gif)

### PDF To Excel

![](https://oss.liujunyang.com/blog/images/2.gif)

## 截图对比

### 原始文件

![](https://www.famio.cn/img/posts/14/1.jpg)

### 提取后

![](https://www.famio.cn/img/posts/14/2.jpg)

# 贡献

感谢以下开源项目：

pdf2image

PyMuPDF

PyYAML

Laravel-Admin

所有的贡献者都在本项目的贡献清单中。

# 安全漏洞

如果您在 Any2Excel 中发现安全漏洞，请通过 famio@qq.com 发送电子邮件告知我。

# 开源协议

遵循 MIT 开源协议。
