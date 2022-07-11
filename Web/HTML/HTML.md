# [HTML](https://www.runoob.com/html/html-tutorial.html)

# [HTML 手册](https://www.runoob.com/tags/html-reference.html)

# [HTML5](https://www.runoob.com/html/html5-intro.html)

## 常用格式

```HTML
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>网页的标题</title>
</head>
<body>
 
<h1>我的第一个标题</h1>
<h2>这是一个标题。</h2>
<!-- 这是一个注释 -->
<!-- <h1> 定义最大的标题。 <h6> 定义最小的标题。 -->
 
<p>我的第一个段落。
	<br /> 标签定义换行
	<hr> 标签在 HTML 页面中创建水平线。
	<q>Build a future where people live in harmony with nature.</q>
	<!-- 上面是引用 -->
	<del>blue</del> <ins>red</ins>!
	<!-- 删除线和下划线 -->
</p>

<p><bdo dir="rtl">该段落文字从右到左显示。</bdo></p>  

<b>这个文本是加粗的</b>
<strong>这个文本是加粗的</strong>
<big>这个文本字体放大</big>
<em>这个文本是斜体的</em>
<i>这个文本是斜体的</i>
<small>这个文本是缩小的</small>
这个文本包含
<sub>下标</sub>
这个文本包含
<sup>上标</sup>
<ins>定义插入字</ins>
<blockquote>定义长的引用</blockquote>
<cite>定义引用、引证</cite>
<dfn>定义一个定义项目。</dfn>

<pre>
此例演示如何使用 pre 标签
对空行和    空格
进行控制
</pre>

<code>计算机输出</code>
<br />
<kbd>键盘输入</kbd>
<br />
<tt>打字机文本</tt>
<br />
<samp>计算机代码样本</samp>
<br />
<var>计算机变量</var>
<br />
<!-- 这些标签常用于显示计算机/编程代码。 -->

<address>
Written by <a href="mailto:webmaster@example.com">Jon Doe</a>.<br> 
Visit us at:<br>
Box 564, Disneyland<br>
USA
</address>
<!-- 链接和地址 -->

 
</body>
</html>

```

## 缩写和首字母缩写

```HTML
<!DOCTYPE html> 
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<abbr title="etcetera">etc.</abbr>
<br />
<acronym title="World Wide Web">WWW</acronym>

<p>在某些浏览器中，当您把鼠标移至缩略词语上时，title 可用于展示表达的完整版本。</p>

<p>仅对于 IE 5 中的 acronym 元素有效。</p>

<p>对于 Netscape 6.2 中的 abbr 和 acronym 元素都有效。</p>

</body>
</html>
```

## HTML 链接语法

```HTML
<a href="url">链接文本</a>
```

### target 属性

使用 target 属性，你可以定义被链接的文档在何处显示。

下面的这行会在新窗口打开文档：

```HTML
<a href="https://www.runoob.com/" target="_blank" rel="noopener noreferrer">访问菜鸟教程!</a>
```

### id 属性

id 属性可用于创建一个 HTML 文档书签。

提示: 书签不会以任何特殊方式显示，即在 HTML 页面中是不显示的，所以对于读者来说是隐藏的。

在HTML文档中插入ID：

```HTML
<a id="tips">有用的提示部分</a>
```

在HTML文档中创建一个链接到"有用的提示部分(id="tips"）"：

```HTML
<a href="#tips">访问有用的提示部分</a>
```

或者，从另一个页面创建一个链接到"有用的提示部分(id="tips"）"：

```HTML
<a href="https://www.runoob.com/html/html-links.html#tips">
访问有用的提示部分</a>
```

### 基本的注意事项 - 有用的提示
注释： 请始终将正斜杠添加到子文件夹。假如这样书写链接：href="https://www.runoob.com/html"，就会向服务器产生两次 HTTP 请求。这是因为服务器会添加正斜杠到这个地址，然后创建一个新的请求，就像这样：href="https://www.runoob.com/html/"。

## 图片链接

```HTML
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<p>创建图片链接:
<a href="//www.runoob.com/html/html-tutorial.html">
<img  border="10" src="smiley.gif" alt="HTML 教程" width="32" height="32"></a></p>

<p>无边框的图片链接:
<a href="//www.runoob.com/html/html-tutorial.html">
<img border="0" src="smiley.gif" alt="HTML 教程" width="32" height="32"></a></p>

</body>
</html>
```

### 在当前界面链接到指定位置

```HTML
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<p>
<a href="#C4">查看章节 4</a>
</p>

<h2>章节 1</h2>
<p>这边显示该章节的内容……</p>

<h2>章节 2</h2>
<p>这边显示该章节的内容……</p>

<h2>章节 3</h2>
<p>这边显示该章节的内容……</p>

<h2><a id="C4">章节 4</a></h2>
<p>这边显示该章节的内容……</p>

</body>
</html>
```

### 跳出框架

```HTML
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<p>跳出框架?</p> 
<a href="//www.runoob.com/" target="_top">点击这里!</a> 

</body>
</html>
```

### 创建电子邮件链接

```HTML
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<p>
这是一个电子邮件链接：
<a href="mailto:someone@example.com?Subject=Hello%20again" target="_top">
发送邮件</a>
</p>

<p>
<b>注意:</b> 单词之间空格使用 %20 代替，以确保浏览器可以正常显示文本。
</p>

</body>
</html>
```

```HTML
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<p>
这是另一个电子邮件链接：
<a href="mailto:someone@example.com?cc=someoneelse@example.com&bcc=andsomeoneelse@example.com&subject=Summer%20Party&body=You%20are%20invited%20to%20a%20big%20summer%20party!" target="_top">发送邮件!</a>
</p>

<p>
<b>注意:</b> 单词之间的空格使用 %20 代替，以确保浏览器可以正常显示文本。
</p>

</body>
</html>
```

## HTML\<head>

### HTML\<head>元素

\<head> 元素包含了所有的头部标签元素。在 \<head>元素中你可以插入脚本（scripts）, 样式文件（CSS），及各种meta信息。

可以添加在头部区域的元素标签为: \<title>, \<style>, \<meta>, \<link>, \<script>, \<noscript> 和 \<base>。

### HTML\<style>元素

```HTML
<head>
<style type="text/css">
body {background-color:yellow}
p {color:blue}
</style>
</head>
```

### HTML \<base> 元素

\<base> 标签描述了基本的链接地址/链接目标，该标签作为HTML文档中所有的链接标签的默认链接:

```HTML
<head>
<base href="http://www.runoob.com/images/" target="_blank">
</head>
```

### HTML\<link>元素

\<link> 标签定义了文档与外部资源之间的关系。

\<link> 标签通常用于链接到样式表:

```HTML
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

### HTML \<meta> 元素

meta标签描述了一些基本的元数据。

\<meta> 标签提供了元数据.元数据也不显示在页面上，但会被浏览器解析。

META 元素通常用于指定网页的描述，关键词，文件的最后修改时间，作者，和其他元数据。

元数据可以使用于浏览器（如何显示内容或重新加载页面），搜索引擎（关键词），或其他Web服务。

\<meta> 一般放置于 \<head> 区域

为搜索引擎定义关键词:

```HTML
<meta name="keywords" content="HTML, CSS, XML, XHTML, JavaScript">
```

为网页定义描述内容:

```HTML
<meta name="description" content="免费 Web & 编程 教程">
```

定义网页作者:

```HTML
<meta name="author" content="Runoob">
```

每30秒钟刷新当前页面:

```HTML
<meta http-equiv="refresh" content="30">
```

### HTML\<title>元素

在左侧显示logo

```HTML
<!doctype HTML>
<html>
<head>
<link rel="shortcut icon" href="图片url">
<title>这是一个带图片的标签</title>
</head>
<body>
  ......  
</body>
</html>
```

## HTML图像

定义图像的语法是：

```HTML
<img src="url" alt="some_text">
```

alt 属性用来为图像定义一串预备的可替换的文本。

```html
<img src="boat.gif" alt="Big Boat">
```

height（高度） 与 width（宽度）属性用于设置图像的高度与宽度。

属性值默认单位为像素:

```html
<img src="pulpit.jpg" alt="Pulpit rock" width="304" height="228">
```

### 如何在文字中排列图像

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<h4>默认对齐的图像 (align="bottom"):</h4>
<p>这是一些文本。 <img src="smiley.gif" alt="Smiley face" width="32" height="32"> 这是一些文本。</p>

<h4>图片使用 align="middle":</h4>
<p>这是一些文本。 <img src="smiley.gif" alt="Smiley face" align="middle" width="32" height="32">这是一些文本。</p>

<h4>图片使用 align="top":</h4>
<p>这是一些文本。 <img src="smiley.gif" alt="Smiley face" align="top" width="32" height="32">这是一些文本。</p>

<p><b>注意:</b>在HTML 4中 align 属性已废弃，HTML5 已不支持该属性，可以使用 CSS 代替。</p>

</body>
</html>
```

### 如何使图片浮动至段落的左边或右边

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<p>
<img src="smiley.gif" alt="Smiley face" style="float:left" width="32" height="32"> 一个带图片的段落，图片浮动在这个文本的左边。
</p>

<p>
<img src="smiley.gif" alt="Smiley face" style="float:right" width="32" height="32"> 一个带图片的段落，图片浮动在这个文本的右边。
</p>

<p><b>注意:</b> 在这里我们使用了 CSS float 属性，在HTML 4 中 float 属性已废弃，HTML5 已不支持该属性，可以使用 CSS 代替。</p>

</body>
</html>
```

### 将图像作为一个链接

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<p>创建图片链接:
<a href="//www.runoob.com/html/html-tutorial.html">
<img  border="10" src="smiley.gif" alt="HTML 教程" width="32" height="32"></a></p>

<p>无边框的图片链接:
<a href="//www.runoob.com/html/html-tutorial.html">
<img border="0" src="smiley.gif" alt="HTML 教程" width="32" height="32"></a></p>

</body>
</html>
```

### 创建带有可供点击区域的图像地图

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<p>点击太阳或其他行星，注意变化：</p>

<img src="planets.gif" width="145" height="126" alt="Planets" usemap="#planetmap">

<map name="planetmap">
  <area shape="rect" coords="0,0,82,126" alt="Sun" href="sun.htm">
  <area shape="circle" coords="90,58,3" alt="Mercury" href="mercur.htm">
  <area shape="circle" coords="124,58,8" alt="Venus" href="venus.htm">
  <!-- 该段代码中的shape指的是点击区域的形状，coords指的应该是链接区域在图片中的坐标（像素为单位） -->
</map>

</body>
</html>

```

1、矩形：(左上角顶点坐标为(x1,y1)，右下角顶点坐标为(x2,y2))

```html
<area shape="rect" coords="x1,y1,x2,y2" href=url>
```

2、圆形：(圆心坐标为(X1,y1)，半径为r)

```html
<area shape="circle" coords="x1,y1,r" href=url>
```

3、多边形：(各顶点坐标依次为(x1,y1)、(x2,y2)、(x3,y3) ......)

```html
<area shape="poly" coords="x1,y1,x2,y2 ......" href=url>
```

## HTML 表格

表格由 \<table> 标签来定义。每个表格均有若干行（由 \<tr> 标签定义），每行被分割为若干单元格（由 \<td> 标签定义）。字母 td 指表格数据（table data），即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。

\<caption>\<colgroup>\<col>\<thead>\<tbody>\<tfoot>见HTML参考手册

使用边框属性来显示一个带有边框的表格：

```html
<table border="1">
    <tr>
        <td>Row 1, cell 1</td>
        <td>Row 1, cell 2</td>
    </tr>
</table>
```

表格表头

```html
<table border="1">
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>
```

### 没有边框的表格

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<h4>这个表格没有边框:</h4>
<table>
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
<tr>
  <td>400</td>
  <td>500</td>
  <td>600</td>
</tr>
</table>

<h4>这个表格没有边框:</h4>
<table border="0">
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
<tr>
  <td>400</td>
  <td>500</td>
  <td>600</td>
</tr>
</table>

</body>
</html>
```

### 表格表头水平和竖直

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<h4>水平标题:</h4>
<table border="1">
<tr>
  <th>Name</th>
  <th>Telephone</th>
  <th>Telephone</th>
</tr>
<tr>
  <td>Bill Gates</td>
  <td>555 77 854</td>
  <td>555 77 855</td>
</tr>
</table>

<h4>垂直标题:</h4>
<table border="1">
<tr>
  <th>First Name:</th>
  <td>Bill Gates</td>
</tr>
<tr>
  <th>Telephone:</th>
  <td>555 77 854</td>
</tr>
<tr>
  <th>Telephone:</th>
  <td>555 77 855</td>
</tr>
</table>

</body>
</html>
```

### 带有标题的表格

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<table border="1">
  <caption>Monthly savings</caption>
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
  <tr>
    <td>February</td>
    <td>$50</td>
  </tr>
</table>

</body>
</html>
```

### 跨行或跨列的表格单元格

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<h4>单元格跨两列:</h4>
<table border="1">
<tr>
  <th>Name</th>
  <th colspan="2">Telephone</th>
</tr>
<tr>
  <td>Bill Gates</td>
  <td>555 77 854</td>
  <td>555 77 855</td>
</tr>
</table>

<h4>单元格跨两行:</h4>
<table border="1">
<tr>
  <th>First Name:</th>
  <td>Bill Gates</td>
</tr>
<tr>
  <th rowspan="2">Telephone:</th>
  <td>555 77 854</td>
</tr>
<tr>
  <td>555 77 855</td>
</tr>
</table>

</body>
</html>
```

### 表格内的标签

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<table border="1">
<tr>
  <td>
   <p>这是一个段落</p>
   <p>这是另一个段落</p>
  </td>
  <td>这个单元格包含一个表格:
   <table border="1">
   <tr>
     <td>A</td>
     <td>B</td>
   </tr>
   <tr>
     <td>C</td>
     <td>D</td>
   </tr>
   </table>
  </td>
</tr>
<tr>
  <td>这个单元格包含一个列表
   <ul>
    <li>apples</li>
    <li>bananas</li>
    <li>pineapples</li>
   </ul>
  </td>
  <td>HELLO</td>
</tr>
</table>

</body>
</html>
```

### 单元格边距(Cell padding)

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<h4>没有单元格边距:</h4>
<table border="1">
<tr>
  <td>First</td>
  <td>Row</td>
</tr>   
<tr>
  <td>Second</td>
  <td>Row</td>
</tr>
</table>

<h4>有单元格边距:</h4>
<table border="1" 
cellpadding="10">
<tr>
  <td>First</td>
  <td>Row</td>
</tr>   
<tr>
  <td>Second</td>
  <td>Row</td>
</tr>
</table>

</body>
</html>
```

### 单元格间距(Cell spacing)

``` html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<h4>没有单元格间距:</h4>
<table border="1">
<tr>
  <td>First</td>
  <td>Row</td>
</tr>
<tr>
  <td>Second</td>
  <td>Row</td>
</tr>
</table>

<h4>单元格间距="0":</h4>
<table border="1" cellspacing="0">
<tr>
  <td>First</td>
  <td>Row</td>
</tr>
<tr>
  <td>Second</td>
  <td>Row</td>
</tr>
</table>

<h4>单元格间距="10":</h4>
<table border="1" cellspacing="10">
<tr>
  <td>First</td>
  <td>Row</td>
</tr>
<tr>
  <td>Second</td>
  <td>Row</td>
</tr>
</table>

</body>
</html>
```

## HTML 列表

### 无序列表

无序列表是一个项目的列表，此列项目使用粗体圆点（典型的小黑圆圈）进行标记。

无序列表使用\<ul> 标签

```html
<ul>
<li>Coffee</li>
<li>Milk</li>
</ul>
```

### 有序列表

同样，有序列表也是一列项目，列表项目使用数字进行标记。 有序列表始于 \<ol> 标签。每个列表项始于 \<li> 标签。

列表项使用数字来标记。

```html
<ol>
<li>Coffee</li>
<li>Milk</li>
</ol>
```

### 自定义列表

自定义列表不仅仅是一列项目，而是项目及其注释的组合。

自定义列表以 \<dl> 标签开始。每个自定义列表项以 \<dt> 开始。每个自定义列表项的定义以 \<dd> 开始。

```html
<dl>
<dt>Coffee</dt>
<dd>- black hot drink</dd>
<dt>Milk</dt>
<dd>- white cold drink</dd>
</dl>
```

### 不同类型的有序列表

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<h4>编号列表：</h4>
<ol>
 <li>Apples</li>
 <li>Bananas</li>
 <li>Lemons</li>
 <li>Oranges</li>
</ol>  

<h4>大写字母列表：</h4>
<ol type="A">
 <li>Apples</li>
 <li>Bananas</li>
 <li>Lemons</li>
 <li>Oranges</li>
</ol>  

<h4>小写字母列表：</h4>
<ol type="a">
 <li>Apples</li>
 <li>Bananas</li>
 <li>Lemons</li>
 <li>Oranges</li>
</ol>  

<h4>罗马数字列表：</h4>
<ol type="I">
 <li>Apples</li>
 <li>Bananas</li>
 <li>Lemons</li>
 <li>Oranges</li>
</ol>  

<h4>小写罗马数字列表：</h4>
<ol type="i">
 <li>Apples</li>
 <li>Bananas</li>
 <li>Lemons</li>
 <li>Oranges</li>
</ol>  

</body>
</html>
```

### 不同类型的无序列表

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<p><b>注意：</b> 在 HTML 4中 ul 属性已废弃，HTML5 已不支持该属性，因此我们使用 CSS 代替来定义不同类型的无序列表如下：</p>

<h4>圆点列表：</h4>
<ul style="list-style-type:disc">
 <li>Apples</li>
 <li>Bananas</li>
 <li>Lemons</li>
 <li>Oranges</li>
</ul>  

<h4>圆圈列表：</h4>
<ul style="list-style-type:circle">
 <li>Apples</li>
 <li>Bananas</li>
 <li>Lemons</li>
 <li>Oranges</li>
</ul>  

<h4>正方形列表：</h4>
<ul style="list-style-type:square">
 <li>Apples</li>
 <li>Bananas</li>
 <li>Lemons</li>
 <li>Oranges</li>
</ul>

</body>
</html>
```

### 嵌套列表

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<h4>嵌套列表：</h4>
<ul>
  <li>Coffee</li>
  <li>Tea
    <ul>
      <li>Black tea</li>
      <li>Green tea
        <ul>
          <li>China</li>
          <li>Africa</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Milk</li>
</ul>

</body>
</html>
```

## HTML \<div> 和\<span>

### HTML \<div> 元素

HTML \<div> 元素是块级元素，它可用于组合其他 HTML 元素的容器。

<div> 元素没有特定的含义。除此之外，由于它属于块级元素，浏览器会在其前后显示折行。

如果与 CSS 一同使用，\<div> 元素可用于对大的内容块设置样式属性。

\<div> 元素的另一个常见的用途是文档布局。它取代了使用表格定义布局的老式方法。使用 \<table> 元素进行文档布局不是表格的正确用法。\<table> 元素的作用是显示表格化的数据。

### HTML \<span> 元素

HTML\ <span> 元素是内联元素，可用作文本的容器

\<span> 元素也没有特定的含义。

当与 CSS 一同使用时，\<span> 元素可用于为部分文本设置样式属性。

## HTML 布局

### 使用 \<div> 元素

使用五个 div 元素来创建多列布局：

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>
 
<div id="container" style="width:500px">
 
<div id="header" style="background-color:#FFA500;">
<h1 style="margin-bottom:0;">主要的网页标题</h1></div>
 
<div id="menu" style="background-color:#FFD700;height:200px;width:100px;float:left;">
<b>菜单</b><br>
HTML<br>
CSS<br>
JavaScript</div>
 
<div id="content" style="background-color:#EEEEEE;height:200px;width:400px;float:left;">
内容在这里</div>
 
<div id="footer" style="background-color:#FFA500;clear:both;text-align:center;">
版权 © runoob.com</div>
 
</div>
 
</body>
</html>
```

### 使用表格

使用 HTML \<table> 标签是创建布局的一种简单的方式。

大多数站点可以使用 \<div> 或者 \<table> 元素来创建多列。CSS 用于对元素进行定位，或者为页面创建背景以及色彩丰富的外观。

下面的例子使用三行两列的表格 - 第一和最后一行使用 colspan 属性来横跨两列：

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>
 
<table width="500" border="0">
<tr>
<td colspan="2" style="background-color:#FFA500;">
<h1>主要的网页标题</h1>
</td>
</tr>
 
<tr>
<td style="background-color:#FFD700;width:100px;">
<b>菜单</b><br>
HTML<br>
CSS<br>
JavaScript
</td>
<td style="background-color:#eeeeee;height:200px;width:400px;">
内容在这里</td>
</tr>
 
<tr>
<td colspan="2" style="background-color:#FFA500;text-align:center;">
版权 © runoob.com</td>
</tr>
</table>
 
</body>
</html>
```

## HTML 表单和输入

### HTML 表单

表单是一个包含表单元素的区域。

表单元素是允许用户在表单中输入内容,比如：文本域(textarea)、下拉列表、单选框(radio-buttons)、复选框(checkboxes)等等。

表单使用表单标签 \<form> 来设置:

```html
<form>
.
input 元素
.
</form>
```

### 输入元素

多数情况下被用到的表单标签是输入标签（\<input>）。

输入类型是由类型属性（type）定义的。大多数经常被用到的输入类型如下：

#### 文本域（Text Fields）

文本域通过\<input type="text"> 标签来设定，当用户要在表单中键入字母、数字等内容时，就会用到文本域。

**注意:**表单本身并不可见。同时，在大多数浏览器中，文本域的默认宽度是 20 个字符。

```html
<form>
First name: <input type="text" name="firstname"><br>
Last name: <input type="text" name="lastname">
</form>
```

#### 密码字段

密码字段通过标签\<input type="password"> 来定义:

**注意:**密码字段字符不会明文显示，而是以星号或圆点替代。

```html
<form>
Password: <input type="password" name="pwd">
</form>
```

#### 单选按钮（Radio Buttons）

\<input type="radio"> 标签定义了表单单选框选项

```html
<form>
<input type="radio" name="sex" value="male">Male<br>
<input type="radio" name="sex" value="female">Female
</form>
```

#### 复选框（Checkboxes）

\<input type="checkbox"> 定义了复选框. 用户需要从若干给定的选择中选取一个或若干选项。

```html
<form>
<input type="checkbox" name="vehicle" value="Bike">I have a bike<br>
<input type="checkbox" name="vehicle" value="Car">I have a car
</form>
```

#### 提交按钮(Submit Button)

\<input type="submit"> 定义了提交按钮.

当用户单击确认按钮时，表单的内容会被传送到另一个文件。表单的动作属性定义了目的文件的文件名。由动作属性定义的这个文件通常会对接收到的输入数据进行相关的处理。

```html
<form name="input" action="html_form_action.php" method="get">
Username: <input type="text" name="user">
<input type="submit" value="Submit">
</form>
```

#### 简单的下拉列表

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<form action="">
<select name="cars">
<option value="volvo">Volvo</option>
<option value="saab">Saab</option>
<option value="fiat">Fiat</option>
<option value="audi">Audi</option>
</select>
</form>

</body>
</html>
```

#### 预选下拉列表

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<form action="">
<select name="cars">
<option value="volvo">Volvo</option>
<option value="saab">Saab</option>
<option value="fiat" selected>Fiat</option>
<option value="audi">Audi</option>
</select>
</form>

</body>
</html>
```

#### 创建文本域（多行文本输入控件）

用户可在文本域中写入文本。可写入字符的字数不受限制。

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<textarea rows="10" cols="30">
我是一个文本框。
</textarea>

</body>
</html>
```

### 表单实例

#### 带边框的表单

在数据周围绘制一个带标题的框。

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<form action="">
<fieldset>
<legend>Personal information:</legend>
Name: <input type="text" size="30"><br>
E-mail: <input type="text" size="30"><br>
Date of birth: <input type="text" size="10">
</fieldset>
</form>

</body>
</html>
```

#### 带有输入框和确认按钮的表单

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<form action="demo-form.php">
First name: <input type="text" name="FirstName" value="Mickey"><br>
Last name: <input type="text" name="LastName" value="Mouse"><br>
<input type="submit" value="提交">
</form>

<p>点击"提交"按钮，表单数据将被发送到服务器上的“demo-form.php”。</p>

</body>
</html>
```

#### 带有复选框的表单

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<form action="demo-form.php" method="get">
  <input type="checkbox" name="vehicle[]" value="Bike"> I have a bike<br>
  <input type="checkbox" name="vehicle[]" value="Car" checked="checked"> I have a car<br>
  <input type="submit" value="提交">
</form>

</body>
</html>
```

#### 带有单选按钮的表单

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<form action="demo-form.php" method="get">
  <input type="radio" name="sex" value="Male"> Male<br>
  <input type="radio" name="sex" value="Female" checked="checked"> Female<br>
  <input type="submit" value="提交">
</form>

</body>
</html>
```

#### 从表单发送电子邮件

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>

<h3>发送邮件到 someone@example.com:</h3>

<form action="MAILTO:someone@example.com" method="post" enctype="text/plain">
Name:<br>
<input type="text" name="name" value="your name"><br>
E-mail:<br>
<input type="text" name="mail" value="your email"><br>
Comment:<br>
<input type="text" name="comment" value="your comment" size="50"><br><br>
<input type="submit" value="发送">
<input type="reset" value="重置">
</form>

</body>
</html>
```

### HTML 表单标签
```html
<form>	    定义供用户输入的表单
<input>	    定义输入域
<textarea>	定义文本域 (一个多行的输入控件)
<label>	    定义了 <input> 元素的标签，一般为输入标题
<fieldset>	定义了一组相关的表单元素，并使用外框包含起来
<legend>	定义了 <fieldset> 元素的标题
<select>	定义了下拉选项列表
<optgroup>	定义选项组
<option>	定义下拉列表中的选项
<button>	定义一个点击按钮
<datalist>	指定一个预先定义的输入控件选项列表
<keygen>	定义了表单的密钥对生成器字段
<output>	定义一个计算结果
```

## HTML 框架

通过使用框架，你可以在同一个浏览器窗口中显示不止一个页面。

### iframe语法:

```html
<iframe src="URL"></iframe>
```

该URL指向不同的网页。

#### 高度与宽度

height 和 width 属性用来定义iframe标签的高度与宽度。

属性默认以像素为单位, 但是你可以指定其按比例显示 (如："80%")。

```html
<iframe loading="lazy" src="demo_iframe.htm" width="200" height="200"></iframe>
```

#### 移除边框

frameborder 属性用于定义iframe表示是否显示边框。

设置属性值为 "0" 移除iframe的边框:

```html
<iframe src="demo_iframe.htm" frameborder="0"></iframe>
```

#### 使用iframe来显示目标链接页面

iframe可以显示一个目标链接的页面

目标链接的属性必须使用iframe的属性，如下实例:

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head> 
<body>

<iframe src="demo_iframe.htm" name="iframe_a"></iframe>
<p><a href="//www.runoob.com" target="iframe_a">RUNOOB.COM</a></p>

<p><b>注意：</b> 因为 a 标签的 target 属性是名为 iframe_a 的 iframe 框架，所以在点击链接时页面会显示在 iframe框架中。</p>

</body>
</html>
```

出于有些网页不希望被嵌套, 响应头中有一选项

```html
X-Frame-Options
```

他有三个可配置值

```html
DENY：表示该网站页面不允许被嵌套，即便是在自己的域名的页面中也不能进行嵌套。
SAMEORIGIN：表示该页面可以在相同域名页面中被嵌套展示。
ALLOW-FROM uri：表示该页面可以在指定来源页面中进行嵌套展示。
```

## HTML 颜色

```html
<p style="background-color:rgb(255,255,0)">
通过 rbg 值设置背景颜色
</p>
<p style="background-color:rgba(255,255,0,0.25)">
通过 rbg 值设置背景颜色
</p>
<p style="background-color:rgba(255,255,0,0.5)">
通过 rbg 值设置背景颜色
</p>
<p style="background-color:rgba(255,255,0,0.75)">
通过 rbg 值设置背景颜色
</p>
```

### [HTML 颜色名](https://www.runoob.com/html/html-colornames.html)

### 颜色值

颜色值由十六进制来表示红、绿、蓝（RGB）。

每个颜色的最低值为 0(十六进制为 00)，最高值为 255(十六进制为FF)。

十六进制值的写法为 # 号后跟三个或六个十六进制字符。

三位数表示法为：#RGB，转换为6位数表示为：#RRGGBB。

## HTML 脚本

### \<script> 标签

\<script> 标签用于定义客户端脚本，比如 JavaScript。

\<script> 元素既可包含脚本语句，也可通过 src 属性指向外部脚本文件。

JavaScript 最常用于图片操作、表单验证以及内容动态更新。

```html
<script>
document.write("Hello World!");
</script>
```

### \<noscript> 标签

\<noscript> 标签提供无法使用脚本时的替代内容，比方在浏览器禁用脚本时，或浏览器不支持客户端脚本时。

\<noscript>元素可包含普通 HTML 页面的 body 元素中能够找到的所有元素。

只有在浏览器不支持脚本或者禁用脚本时，才会显示 \<noscript> 元素中的内容：

```html
<script>
document.write("Hello World!")
</script>
<noscript>抱歉，你的浏览器不支持 JavaScript!</noscript>
```

## HTML 字符实体

HTML 中的预留字符必须被替换为字符实体。

一些在键盘上找不到的字符也可以使用字符实体来替换。

在 HTML 中，某些字符是预留的。

在 HTML 中不能使用小于号（<）和大于号（>），这是因为浏览器会误认为它们是标签。

如果希望正确地显示预留字符，我们必须在 HTML 源代码中使用字符实体（character entities）。 字符实体类似这样：

```html
&entity_name;
或
&#entity_number;
显示小于号，我们必须这样写：&lt; 或 &#60; 或 &#060;
```

使用实体名而不是数字的好处是，名称易于记忆。不过坏处是，浏览器也许并不支持所有实体名称（对实体数字的支持却很好）。

### 结合音标符

发音符号是加到字母上的一个"glyph(字形)"。

一些变音符号, 如 尖音符 ( ̀) 和 抑音符 ( ́) 。

变音符号可以出现字母的上面和下面，或者字母里面，或者两个字母间。

变音符号可以与字母、数字字符的组合来使用。

以下是一些实例:

| ̀     | a    | a\&#768; | à    |
| ---- | ---- | -------- | ---- |
| ́     | a    | a\&#769; | á    |
| ̂     | a    | a\&#770; | â    |
| ̃     | a    | a\&#771; | ã    |
| ̀     | O    | O\&#768; | Ò    |
| ́     | O    | O\&#769; | Ó    |
| ̂     | O    | O\&#770; | Ô    |
| ̃     | O    | O\&#771; | Õ    |

### HTML字符实体

| 显示结果 | 描述        | 实体名称           | 实体编号 |
| :------- | :---------- | :----------------- | :------- |
|          | 空格        | \&nbsp;            | \&#160;  |
| <        | 小于号      | \&lt;              | \&#60;   |
| >        | 大于号      | \&gt;              | \&#62;   |
| &        | 和号        | \&amp;             | \&#38;   |
| "        | 引号        | \&quot;            | \&#34;   |
| '        | 撇号        | \&apos; (IE不支持) | \&#39;   |
| ￠       | 分          | \&cent;            | \&#162;  |
| £        | 镑          | \&pound;           | \&#163;  |
| ¥        | 人民币/日元 | \&yen;             | \&#165;  |
| €        | 欧元        | \&euro;            | \&#8364; |
| §        | 小节        | \&sect;            | \&#167;  |
| ©        | 版权        | \&copy;            | \&#169;  |
| ®        | 注册商标    | \&reg;             | \&#174;  |
| ™        | 商标        | \&trade;           | \&#8482; |
| ×        | 乘号        | &\times;           | \&#215;  |
| ÷        | 除号        | &\divide;          | \&#247;  |

## HTML 统一资源定位器(Uniform Resource Locators)

URL 是一个网页地址。

URL可以由字母组成，如"runoob.com"，或互联网协议（IP）地址： 192.68.20.50。大多数人进入网站使用网站域名来访问，因为 名字比数字更容易记住。

### URL - 统一资源定位器

Web浏览器通过URL从Web服务器请求页面。

当您点击 HTML 页面中的某个链接时，对应的 <a> 标签指向万维网上的一个地址。

一个统一资源定位器(URL) 用于定位万维网上的文档。

一个网页地址实例: http://www.runoob.com/html/html-tutorial.html 语法规则:

**scheme://host.domain:port/path/filename**

说明:

- - scheme - 定义因特网服务的类型。最常见的类型是 http
  - host - 定义域主机（http 的默认主机是 www）
  - domain - 定义因特网域名，比如 runoob.com
  - :port - 定义主机上的端口号（http 的默认端口号是 80）
  - path - 定义服务器上的路径（如果省略，则文档必须位于网站的根目录中）。
  - filename - 定义文档/资源的名称

### 常见的 URL Scheme

以下是一些URL scheme：

| Scheme | 访问               | 用于...                             |
| :----- | :----------------- | :---------------------------------- |
| http   | 超文本传输协议     | 以 http:// 开头的普通网页。不加密。 |
| https  | 安全超文本传输协议 | 安全网页，加密所有信息交换。        |
| ftp    | 文件传输协议       | 用于将文件下载或上传至网站。        |
| file   |                    | 您计算机上的文件。                  |

### URL 字符编码

URL 只能使用 ASCII 字符集.

来通过因特网进行发送。由于 URL 常常会包含 ASCII 集合之外的字符，URL 必须转换为有效的 ASCII 格式。

URL 编码使用 "%" 其后跟随两位的十六进制数来替换非 ASCII 字符。

URL 不能包含空格。URL 编码通常使用 + 来替换空格。

### URL 编码实例

| 字符 | URL 编码 |
| :--- | :------- |
| €    | %80      |
| £    | %A3      |
| ©    | %A9      |
| ®    | %AE      |
| À    | %C0      |
| Á    | %C1      |
| Â    | %C2      |
| Ã    | %C3      |
| Ä    | %C4      |
| Å    | %C5      |
