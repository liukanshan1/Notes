

# JavaScript

## 简介

### 直接写入 HTML 输出流

```javascript
document.write("<h1>这是一个标题</h1>");
document.write("<p>这是一个段落。</p>");
```

### 对事件的反应

```javascript
<button type="button" onclick="alert('欢迎!')">点我!</button>
```

alert() 函数在 JavaScript 中并不常用，但它对于代码测试非常方便。

onclick 事件只是您即将在本教程中学到的众多事件之一。

### 改变 HTML 内容

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>
	
<h1>我的第一段 JavaScript</h1>
<p id="demo">
JavaScript 能改变 HTML 元素的内容。
</p>
<script>
function myFunction()
{
	x=document.getElementById("demo");  // 找到元素
	x.innerHTML="Hello JavaScript!";    // 改变内容
}
</script>
<button type="button" onclick="myFunction()">点击这里</button>
	
</body>
</html>
```

您会经常看到 **document.getElementById("*****some id*****")**。这个方法是 HTML DOM 中定义的。DOM (**D**ocument **O**bject **M**odel)（文档对象模型）是用于访问 HTML 元素的正式 W3C 标准。

### 改变 HTML 图像

```javascript
<script>
function changeImage()
{
    element=document.getElementById('myimage')
    if (element.src.match("bulbon"))
    {
        element.src="/images/pic_bulboff.gif";
    }
    else
    {
        element.src="/images/pic_bulbon.gif";
    }
}
</script>
<img loading="lazy" id="myimage" onclick="changeImage()" src="/images/pic_bulboff.gif" width="100" height="180">
```

### 改变 HTML 样式

```javascript
x=document.getElementById("demo")  //找到元素 
x.style.color="#ff0000";           //改变样式
```

### 验证输入

```html
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>
	
<h1>我的第一段 JavaScript</h1>
<p>请输入数字。如果输入值不是数字，浏览器会弹出提示框。</p>
<input id="demo" type="text">
<script>
function myFunction()
{
	var x=document.getElementById("demo").value;
	if(x==""||isNaN(x))
	{
		alert("不是数字");
	}
}
</script>
<button type="button" onclick="myFunction()">点击这里</button>
	
</body>
</html>
```

以上实例只是普通的验证，如果要在生产环境中使用，需要严格判断，如果输入的空格，或者连续空格 isNaN 是判别不出来的。可以添加正则来判断（后续章节会说明）：

```javascript
if(isNaN(x)||x.replace(/(^\s*)|(\s*$)/g,"")==""){
    alert("不是数字");
}
```

## 用法

HTML 中的脚本必须位于 \<script> 与 \</script> 标签之间。

脚本可被放置在 HTML 页面的 \<body> 和 \<head> 部分中。

### 在 \<head> 或者 \<body> 的JavaScript

您可以在 HTML 文档中放入不限数量的脚本。

脚本可位于 HTML 的 \<body> 或 \<head> 部分中，或者同时存在于两个部分中。

通常的做法是把函数放入 \<head> 部分中，或者放在页面底部。这样就可以把它们安置到同一处位置，不会干扰页面的内容。

#### \<head> 中的 JavaScript 函数

```html
<!DOCTYPE html>
<html>
<head>
<script>
function myFunction()
{
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}
</script>
</head>
<body>
<h1>我的 Web 页面</h1>
<p id="demo">一个段落</p>
<button type="button" onclick="myFunction()">尝试一下</button>
</body>
</html>
```

### 外部的 JavaScript

也可以把脚本保存到外部文件中。外部文件通常包含被多个网页使用的代码。

外部 JavaScript 文件的文件扩展名是 .js。

如需使用外部文件，请在 \<script> 标签的 "src" 属性中设置该 .js 文件：

```html
<!DOCTYPE html>
<html>
<body>
<script src="myScript.js"></script>
</body>
</html>
```

myScript.js 文件代码如下：

```javascript
function myFunction()
{
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}
```

外部脚本不能包含 \<script> 标签。

### 笔记

在标签中填写 onclick 事件调用函数时，不是 **onclick=函数名**， 而是 **onclick=函数名+()**，代码如下：

```html
<script> 
    function myfunction(){
         document.getElementById("demo").innerHTML="onclick事件触发";
        }</script>
    </head>
<body>
    <h1 id="demo">一个段落</h1>
    <button onclick="myfunction()" type="button">点击这里</button>
</body>
```

HTML 输出流中使用 document.write，相当于添加在原有html代码中添加一串html代码。而如果在文档加载后使用（如使用函数），会覆盖整个文档。

使用函数来执行document.write代码如下：

```html
<script>
function myfunction(){
    document.write("使用函数来执行doucment.write，即在文档加载后再执行这个操作，会实现文档覆盖");
}
document.write("<h1>这是一个标题</h1>");
document.write("<p>这是一个段落。</p>");
</script>
<p >
您只能在 HTML 输出流中使用 <strong>document.write</strong>。
如果您在文档已加载后使用它（比如在函数中），会覆盖整个文档。
</p>
<button type="button" onclick="myfunction()">点击这里</button>
```

## JavaScript 输出

### JavaScript 显示数据

JavaScript 可以通过不同的方式来输出数据：

- 使用 **window.alert()** 弹出警告框。
- 使用 **document.write()** 方法将内容写到 HTML 文档中。
- 使用 **innerHTML** 写入到 HTML 元素。
- 使用 **console.log()** 写入到浏览器的控制台。

### 使用 window.alert()

```html
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个页面</h1>
<p>我的第一个段落。</p>

<script>
window.alert(5 + 6);
</script>

</body>
</html>
```

### 操作 HTML 元素

如需从 JavaScript 访问某个 HTML 元素，您可以使用 document.getElementById(*id*) 方法。

请使用 "id" 属性来标识 HTML 元素，并 innerHTML 来获取或插入元素内容：

```html
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个 Web 页面</h1>

<p id="demo">我的第一个段落</p>

<script>
document.getElementById("demo").innerHTML = "段落已修改。";
</script>

</body>
</html>
```

以上 JavaScript 语句（在 \<script> 标签中）可以在 web 浏览器中执行：

**document.getElementById("demo")** 是使用 id 属性来查找 HTML 元素的 JavaScript 代码 。

**innerHTML = "段落已修改。"** 是用于修改元素的 HTML 内容(innerHTML)的 JavaScript 代码。

出于测试目的，您可以将JavaScript直接写在HTML 文档中：

```html
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个 Web 页面</h1>

<p>我的第一个段落。</p>

<script>
document.write(Date());
</script>

</body>
</html>
```

 请使用 document.write() 仅仅向文档输出写内容。如果在文档已完成加载后执行 document.write，整个 HTML 页面将被覆盖。

```html
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个 Web 页面</h1>

<p>我的第一个段落。</p>

<button onclick="myFunction()">点我</button>

<script>
function myFunction() {
    document.write(Date());
}
</script>

</body>
</html>
```

### 写到控制台

如果您的浏览器支持调试，你可以使用 **console.log()** 方法在浏览器中显示 JavaScript 值。

浏览器中使用 F12 来启用调试模式， 在调试窗口中点击 "Console" 菜单。

```html
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个 Web 页面</h1>

<script>
a = 5;
b = 6;
c = a + b;
console.log(c);
</script>

</body>
</html>
```

## JavaScript 语法

 变量是一个**名称**。字面量是一个**值**。

**数组（Array）字面量** 定义一个数组：

``` javascript
[40, 100, 1, 5, 25, 10]
```

**对象（Object）字面量** 定义一个对象：

```javascript
{firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"}
```

**函数（Function）字面量** 定义一个函数：

```javascript
function myFunction(a, b) { return a * b;}
```

JavaScript 使用关键字 **var** 来定义变量， 使用等号来为变量赋值：

```javascript
var x, length

x = 5

length = 6
```

## JavaScript 语句

下面的 JavaScript 语句向 id="demo" 的 HTML 元素输出文本 "你好 Dolly" ：

```javascript
document.getElementById("demo").innerHTML = "你好 Dolly";
```

### JavaScript 语句标识符

JavaScript 语句通常以一个 **语句标识符** 为开始，并执行该语句。

| 语句         | 描述                                                         |
| :----------- | :----------------------------------------------------------- |
| break        | 用于跳出循环。                                               |
| catch        | 语句块，在 try 语句块执行出错时执行 catch 语句块。           |
| continue     | 跳过循环中的一个迭代。                                       |
| do ... while | 执行一个语句块，在条件语句为 true 时继续执行该语句块。       |
| for          | 在条件语句为 true 时，可以将代码块执行指定的次数。           |
| for ... in   | 用于遍历数组或者对象的属性（对数组或者对象的属性进行循环操作）。 |
| function     | 定义一个函数                                                 |
| if ... else  | 用于基于不同的条件来执行不同的动作。                         |
| return       | 退出函数                                                     |
| switch       | 用于基于不同的条件来执行不同的动作。                         |
| throw        | 抛出（生成）错误 。                                          |
| try          | 实现错误处理，与 catch 一同使用。                            |
| var          | 声明一个变量。                                               |
| while        | 当条件语句为 true 时，执行语句块。                           |

### 对代码行进行折行

您可以在文本字符串中使用反斜杠对代码行进行换行。下面的例子会正确地显示：

```javascript
document.write("你好 \
世界!");
```

不过，您不能像这样折行：

```javascript
document.write \ 
("你好世界!");
```

如果用户不能确定浏览器是否支持JavaScript脚本，那么可以应用HTML提供的注释符号进行验证。HTML注释符号是以 **<--** 开始以 **-->** 结束的。如果在此注释符号内编写 JavaScrip t脚本，对于不支持 JavaScript 的浏览器，将会把编写的 JavaScript 脚本作为注释处理。

使用 JavaScript 脚本在页面中输出一个字符串，将 JavaScript 脚本编写在 HTML 注释中，如果浏览器支持 JavaScript 将输出此字符串，如果不支持将不输出此字符串，代码如下:

```javascript
<script>
<!--
document.write("您的浏览器支持JavaScript脚本!");
//-->
</script>
```

**注意：**注释行结尾处的两条斜杠 **//** 是 JavaScript 注释符号。这可以避免 JavaScript 执行 **-->** 标签。

## JavaScript 数据类型

### JavaScript 数组

下面的代码创建名为 cars 的数组：

```javascript
var cars=new Array();
cars[0]="Saab";
cars[1]="Volvo";
cars[2]="BMW";
```

或者 (condensed array):

```javascript
var cars=new Array("Saab","Volvo","BMW");
```

或者 (literal array):

```javascript
var cars=["Saab","Volvo","BMW"];
```

### JavaScript 对象

对象由花括号分隔。在括号内部，对象的属性以名称和值对的形式 (name : value) 来定义。属性由逗号分隔：

```javascript
var person={firstname:"John", lastname:"Doe", id:5566};
```

空格和折行无关紧要。声明可横跨多行：

```javascript
var person={
firstname : "John",
lastname  : "Doe",
id        :  5566
};
```

对象属性有两种寻址方式：

```javascript
name=person.lastname;
name=person["lastname"];
```

### Undefined 和 Null

Undefined 这个值表示变量不含有值。

可以通过将变量的值设置为 null 来清空变量。

```javascript
cars=null;
```

### 声明变量类型

当您声明新变量时，可以使用关键词 "new" 来声明其类型：

```javascript
var carname=new String;
var x=      new Number;
var y=      new Boolean;
var cars=   new Array;
var person= new Object;
```

## JavaScript 事件

在以下实例中，按钮元素中添加了 onclick 属性 (并加上代码)，代码将修改自身元素的内容 (使用 **this**.innerHTML):

```javascript
<button onclick="this.innerHTML=Date()">现在的时间是?</button>
```

### 常见的HTML事件

下面是一些常见的HTML事件的列表:

| 事件        | 描述                         |
| :---------- | :--------------------------- |
| onchange    | HTML 元素改变                |
| onclick     | 用户点击 HTML 元素           |
| onmouseover | 用户在一个HTML元素上移动鼠标 |
| onmouseout  | 用户从一个HTML元素上移开鼠标 |
| onkeydown   | 用户按下键盘按键             |
| onload      | 浏览器已完成页面的加载       |

更多事件列表: [JavaScript 参考手册 - HTML DOM 事件](https://www.runoob.com/jsref/dom-obj-event.html)。

## JavaScript 字符串

你可以在字符串中使用引号，字符串中的引号不要与字符串的引号相同:

```javascript
var answer = "It's alright";
var answer = "He is called 'Johnny'";
var answer = 'He is called "Johnny"';
```

你也可以在字符串添加转义字符来使用引号：

```javascript
var x = 'It\'s alright';
var y = "He is called \"Johnny\"";
```

下表中列举了在字符串中可以使用转义字符转义的特殊字符：

| 代码 | 输出        |
| :--- | :---------- |
| \'   | 单引号      |
| \"   | 双引号      |
| \\   | 反斜杠      |
| \n   | 换行        |
| \r   | 回车        |
| \t   | tab(制表符) |
| \b   | 退格符      |
| \f   | 换页符      |

### 字符串长度

可以使用内置属性 **length** 来计算字符串的长度：

```javascript
var txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var sln = txt.length;
```

### 字符串可以是对象

通常， JavaScript 字符串是原始值，可以使用字符创建： **var firstName = "John"**

但我们也可以使用 new 关键字将字符串定义为一个对象： **var firstName = new String("John")**

```javascript
var x = "John";
var y = new String("John");
typeof x // 返回 String
typeof y // 返回 Object
```

不要创建 String 对象。它会拖慢执行速度，并可能产生其他副作用：

```javascript
var x = "John";             
var y = new String("John");
(x === y) // 结果为 false，因为 x 是字符串，y 是对象
```

=== 为绝对相等，即数据类型与值都必须相等。

### 字符串属性

| 属性        | 描述                       |
| :---------- | :------------------------- |
| constructor | 返回创建字符串属性的函数   |
| length      | 返回字符串的长度           |
| prototype   | 允许您向对象添加属性和方法 |

### 字符串方法

更多方法实例可以参见：[JavaScript String 对象](https://www.runoob.com/jsref/jsref-obj-string.html)。

| 方法                | 描述                                                         |
| :------------------ | :----------------------------------------------------------- |
| charAt()            | 返回指定索引位置的字符                                       |
| charCodeAt()        | 返回指定索引位置字符的 Unicode 值                            |
| concat()            | 连接两个或多个字符串，返回连接后的字符串                     |
| fromCharCode()      | 将 Unicode 转换为字符串                                      |
| indexOf()           | 返回字符串中检索指定字符第一次出现的位置                     |
| lastIndexOf()       | 返回字符串中检索指定字符最后一次出现的位置                   |
| localeCompare()     | 用本地特定的顺序来比较两个字符串                             |
| match()             | 找到一个或多个正则表达式的匹配                               |
| replace()           | 替换与正则表达式匹配的子串                                   |
| search()            | 检索与正则表达式相匹配的值                                   |
| slice()             | 提取字符串的片断，并在新的字符串中返回被提取的部分           |
| split()             | 把字符串分割为子字符串数组                                   |
| substr()            | 从起始索引号提取字符串中指定数目的字符                       |
| substring()         | 提取字符串中两个指定的索引号之间的字符                       |
| toLocaleLowerCase() | 根据主机的语言环境把字符串转换为小写，只有几种语言（如土耳其语）具有地方特有的大小写映射 |
| toLocaleUpperCase() | 根据主机的语言环境把字符串转换为大写，只有几种语言（如土耳其语）具有地方特有的大小写映射 |
| toLowerCase()       | 把字符串转换为小写                                           |
| toString()          | 返回字符串对象值                                             |
| toUpperCase()       | 把字符串转换为大写                                           |
| trim()              | 移除字符串首尾空白                                           |
| valueOf()           | 返回某个字符串对象的原始值                                   |

## JavaScript typeof, null, 和 undefined

### typeof 操作符

你可以使用 typeof 操作符来检测变量的数据类型。

```javascript
typeof "John"                // 返回 string
typeof 3.14                  // 返回 number
typeof false                 // 返回 boolean
typeof [1,2,3,4]             // 返回 object
typeof {name:'John', age:34} // 返回 object
```

  在JavaScript中，数组是一种特殊的对象类型。 因此 typeof [1,2,3,4] 返回 object。

### null

在 JavaScript 中 null 表示 "什么都没有"。

null是一个只有一个值的特殊类型。表示一个空对象引用。

用 typeof 检测 null 返回是object。

你可以设置为 null 来清空对象:

你可以设置为 undefined 来清空对象:

```javascript
var person = null;           // 值为 null(空), 但类型为对象
var person = undefined;     // 值为 undefined, 类型为 undefined
```

### undefined

在 JavaScript 中, **undefined** 是一个没有设置值的变量。

**typeof** 一个没有值的变量会返回 **undefined**。

任何变量都可以通过设置值为 **undefined** 来清空。 类型为 **undefined**.

```javascript
var person;                  // 值为 undefined(空), 类型是undefined
person = undefined;          // 值为 undefined, 类型是undefined
```

### undefined 和 null 的区别

null 和 undefined 的值相等，但类型不等：

```javascript
typeof undefined             // undefined
typeof null                  // object
null === undefined           // false
null == undefined            // true
```

**1、定义**

-  （1）undefined：是所有没有赋值变量的默认值，自动赋值。
-  （2）null：主动释放一个变量引用的对象，表示一个变量不再指向任何对象地址。

**2、何时使用null?**

当使用完一个比较大的对象时，需要对其进行释放内存时，设置为 null。

**3、null 与 undefined 的异同点是什么呢？**

**共同点**：都是原始类型，保存在栈中变量本地。

不同点：

（1）undefined——表示变量声明过但并未赋过值。

它是所有未赋值变量默认值，例如：

```javascript
var a;    // a 自动被赋值为 undefined
```

（2）null——表示一个变量将来可能指向一个对象。

一般用于主动释放指向对象的引用，例如：

```javascript
var emps = ['ss','nn'];
emps = null;     // 释放指向数组的引用
```

4、延伸——垃圾回收站

它是专门释放对象内存的一个程序。

-  （1）在底层，后台伴随当前程序同时运行；引擎会定时自动调用垃圾回收期；
-  （2）总有一个对象不再被任何变量引用时，才释放。

## JavaScript 类型转换

**Number() 转换为数字， String() 转换为字符串， Boolean() 转换为布尔值。**

### JavaScript 数据类型

在 JavaScript 中有 6 种不同的数据类型：

- string
- number
- boolean
- object
- function
- symbol

3 种对象类型：

- Object
- Date
- Array

2 个不包含任何值的数据类型：

- null
- undefined

### typeof 操作符

你可以使用 **typeof** 操作符来查看 JavaScript 变量的数据类型。

```javascript
typeof "John"                 // 返回 string
typeof 3.14                   // 返回 number
typeof NaN                    // 返回 number
typeof false                  // 返回 boolean
typeof [1,2,3,4]              // 返回 object
typeof {name:'John', age:34}  // 返回 object
typeof new Date()             // 返回 object
typeof function () {}         // 返回 function
typeof myCar                  // 返回 undefined (如果 myCar 没有声明)
typeof null                   // 返回 object
```

请注意：

- NaN 的数据类型是 number
- 数组(Array)的数据类型是 object
- 日期(Date)的数据类型为 object
- null 的数据类型是 object
- 未定义变量的数据类型为 undefined

如果对象是 JavaScript Array 或 JavaScript Date ，我们就无法通过 **typeof** 来判断他们的类型，因为都是 返回 object。

### constructor 属性

**constructor** 属性返回所有 JavaScript 变量的构造函数。

```javascript
"John".constructor                 // 返回函数 String()  { [native code] }
(3.14).constructor                 // 返回函数 Number()  { [native code] }
false.constructor                  // 返回函数 Boolean() { [native code] }
[1,2,3,4].constructor              // 返回函数 Array()   { [native code] }
{name:'John', age:34}.constructor  // 返回函数 Object()  { [native code] }
new Date().constructor             // 返回函数 Date()    { [native code] }
function () {}.constructor         // 返回函数 Function(){ [native code] }
```

你可以使用 constructor 属性来查看对象是否为数组 (包含字符串 "Array"):

```javascript
function isArray(myArray) {
    return myArray.constructor.toString().indexOf("Array") > -1;
}
```

你可以使用 constructor 属性来查看对象是否为日期 (包含字符串 "Date"):

```javascript
function isDate(myDate) {
    return myDate.constructor.toString().indexOf("Date") > -1;
}
```

### 将数字转换为字符串

全局方法 **String()** 可以将数字转换为字符串。

该方法可用于任何类型的数字，字母，变量，表达式：

```javascript
String(x)         // 将变量 x 转换为字符串并返回
String(123)       // 将数字 123 转换为字符串并返回
String(100 + 23)  // 将数字表达式转换为字符串并返回
```

Number 方法 **toString()** 也是有同样的效果。

```javascript
x.toString()
(123).toString()
(100 + 23).toString()
```

在 [Number 方法](https://www.runoob.com/jsref/jsref-obj-number.html) 章节中，你可以找到更多数字转换为字符串的方法：

| 方法            | 描述                                                 |
| :-------------- | :--------------------------------------------------- |
| toExponential() | 把对象的值转换为指数计数法。                         |
| toFixed()       | 把数字转换为字符串，结果的小数点后有指定位数的数字。 |
| toPrecision()   | 把数字格式化为指定的长度。                           |

### 将布尔值转换为字符串

全局方法 **String()** 可以将布尔值转换为字符串。

```javascript
String(false)        // 返回 "false"
String(true)         // 返回 "true"
```

Boolean 方法 **toString()** 也有相同的效果。

```javascript
false.toString()     // 返回 "false"
true.toString()      // 返回 "true"
```

### 将日期转换为字符串

Date() 返回字符串。

```javascript
Date()      // 返回 Thu Jul 17 2014 15:38:19 GMT+0200 (W. Europe Daylight Time)
```

全局方法 String() 可以将日期对象转换为字符串。

```javascript
String(new Date())      // 返回 Thu Jul 17 2014 15:38:19 GMT+0200 (W. Europe Daylight Time)
```

Date 方法 **toString()** 也有相同的效果。

```javascript
obj = new Date()
obj.toString()   // 返回 Thu Jul 17 2014 15:38:19 GMT+0200 (W. Europe Daylight Time)
```

在 [Date 方法](https://www.runoob.com/jsref/jsref-obj-date.html) 章节中，你可以查看更多关于日期转换为字符串的函数：

| 方法              | 描述                                        |
| :---------------- | :------------------------------------------ |
| getDate()         | 从 Date 对象返回一个月中的某一天 (1 ~ 31)。 |
| getDay()          | 从 Date 对象返回一周中的某一天 (0 ~ 6)。    |
| getFullYear()     | 从 Date 对象以四位数字返回年份。            |
| getHours()        | 返回 Date 对象的小时 (0 ~ 23)。             |
| getMilliseconds() | 返回 Date 对象的毫秒(0 ~ 999)。             |
| getMinutes()      | 返回 Date 对象的分钟 (0 ~ 59)。             |
| getMonth()        | 从 Date 对象返回月份 (0 ~ 11)。             |
| getSeconds()      | 返回 Date 对象的秒数 (0 ~ 59)。             |
| getTime()         | 返回 1970 年 1 月 1 日至今的毫秒数。        |

### 将字符串转换为数字

全局方法 **Number()** 可以将字符串转换为数字。

字符串包含数字(如 "3.14") 转换为数字 (如 3.14).

空字符串转换为 0。

其他的字符串会转换为 NaN (不是个数字)。

```java
Number("3.14")    // 返回 3.14
Number(" ")       // 返回 0
Number("")        // 返回 0
Number("99 88")   // 返回 NaN
```

在 [Number 方法](https://www.runoob.com/jsref/jsref-obj-number.html) 章节中，你可以查看到更多关于字符串转为数字的方法：

| 方法         | 描述                               |
| :----------- | :--------------------------------- |
| parseFloat() | 解析一个字符串，并返回一个浮点数。 |
| parseInt()   | 解析一个字符串，并返回一个整数。   |

### 一元运算符 +

**Operator +** 可用于将变量转换为数字：

```javascript
var y = "5";   // y 是一个字符串
var x = + y;   // x 是一个数字
```

如果变量不能转换，它仍然会是一个数字，但值为 NaN (不是一个数字):

```javascript
var y = "John";  // y 是一个字符串
var x = + y;   // x 是一个数字 (NaN)
```

### 将布尔值转换为数字

全局方法 **Number()** 可将布尔值转换为数字。

```javascript
Number(false)     // 返回 0
Number(true)      // 返回 1
```

### 将日期转换为数字

全局方法 **Number()** 可将日期转换为数字。

```javascript
d = new Date();
Number(d)          // 返回 1404568027739
```

日期方法 **getTime()** 也有相同的效果。

```javascript
d = new Date();
d.getTime()        // 返回 1404568027739
```

### 自动转换类型

当 JavaScript 尝试操作一个 "错误" 的数据类型时，会自动转换为 "正确" 的数据类型。

以下输出结果不是你所期望的：

```javascript
5 + null    // 返回 5         null 转换为 0
"5" + null  // 返回"5null"   null 转换为 "null"
"5" + 1     // 返回 "51"      1 转换为 "1" 
"5" - 1     // 返回 4         "5" 转换为 5
```

### 自动转换为字符串

当你尝试输出一个对象或一个变量时 JavaScript 会自动调用变量的 toString() 方法：

```javascript
document.getElementById("demo").innerHTML = myVar;

myVar = {name:"Fjohn"}  // toString 转换为 "[object Object]"
myVar = [1,2,3,4]       // toString 转换为 "1,2,3,4"
myVar = new Date()      // toString 转换为 "Fri Jul 18 2014 09:08:55 GMT+0200"
```

数字和布尔值也经常相互转换：

```javascript
myVar = 123             // toString 转换为 "123"
myVar = true            // toString 转换为 "true"
myVar = false           // toString 转换为 "false"
```

下表展示了使用不同的数值转换为数字(Number), 字符串(String), 布尔值(Boolean):

下表展示了使用不同的数值转换为数字(Number), 字符串(String), 布尔值(Boolean):

| 原始值              | 转换为数字 | 转换为字符串      | 转换为布尔值 |
| :------------------ | :--------- | :---------------- | :----------- |
| false               | 0          | "false"           | false        |
| true                | 1          | "true"            | true         |
| 0                   | 0          | "0"               | false        |
| 1                   | 1          | "1"               | true         |
| "0"                 | 0          | "0"               | true         |
| "000"               | 0          | "000"             | true         |
| "1"                 | 1          | "1"               | true         |
| NaN                 | NaN        | "NaN"             | false        |
| Infinity            | Infinity   | "Infinity"        | true         |
| -Infinity           | -Infinity  | "-Infinity"       | true         |
| ""                  | 0          | ""                | false        |
| "20"                | 20         | "20"              | true         |
| "Runoob"            | NaN        | "Runoob"          | true         |
| [ ]                 | 0          | ""                | true         |
| [20]                | 20         | "20"              | true         |
| [10,20]             | NaN        | "10,20"           | true         |
| ["Runoob"]          | NaN        | "Runoob"          | true         |
| ["Runoob","Google"] | NaN        | "Runoob,Google"   | true         |
| function(){}        | NaN        | "function(){}"    | true         |
| { }                 | NaN        | "[object Object]" | true         |
| null                | 0          | "null"            | false        |
| undefined           | NaN        | "undefined"       | false        |

## 正则表达式

```javascript
var patt = /runoob/i
```

**/runoob/i** 是一个正则表达式。

**runoob** 是一个**正则表达式主体** (用于检索)。

**i** 是一个**修饰符** (搜索不区分大小写)。

### 使用字符串方法

在 JavaScript 中，正则表达式通常用于两个字符串方法 : search() 和 replace()。

**search() 方法** 用于检索字符串中指定的子字符串，或检索与正则表达式相匹配的子字符串，并返回子串的起始位置。

**replace() 方法** 用于在字符串中用一些字符替换另一些字符，或替换一个与正则表达式匹配的子串。

```javascript
var str = "Visit Runoob!"; 
var n = str.search(/Runoob/i);
//输出结果为 6
```

search 方法可使用字符串作为参数。字符串参数会转换为正则表达式：

```javascript
var str = "Visit Runoob!"; 
var n = str.search("Runoob");
```

使用正则表达式且不区分大小写将字符串中的 Microsoft 替换为 Runoob :

```java
var str = document.getElementById("demo").innerHTML; 
var txt = str.replace(/microsoft/i,"Runoob");
```

### 正则表达式修饰符

**修饰符** 可以在全局搜索中不区分大小写:

| 修饰符 | 描述                                                     |
| :----- | :------------------------------------------------------- |
| i      | 执行对大小写不敏感的匹配。                               |
| g      | 执行全局匹配（查找所有匹配而非在找到第一个匹配后停止）。 |
| m      | 执行多行匹配。                                           |

### 正则表达式模式

方括号用于查找某个范围内的字符：

| 表达式 | 描述                       |
| :----- | :------------------------- |
| [abc]  | 查找方括号之间的任何字符。 |
| [0-9]  | 查找任何从 0 至 9 的数字。 |
| (x\|y) | 查找任何以 \| 分隔的选项。 |

元字符是拥有特殊含义的字符：

| 元字符 | 描述                                        |
| :----- | :------------------------------------------ |
| \d     | 查找数字。                                  |
| \s     | 查找空白字符。                              |
| \b     | 匹配单词边界。                              |
| \uxxxx | 查找以十六进制数 xxxx 规定的 Unicode 字符。 |

量词:

| 量词 | 描述                                  |
| :--- | :------------------------------------ |
| n+   | 匹配任何包含至少一个 *n* 的字符串。   |
| n*   | 匹配任何包含零个或多个 *n* 的字符串。 |
| n?   | 匹配任何包含零个或一个 *n* 的字符串。 |

### 使用 RegExp 对象

在 JavaScript 中，RegExp 对象是一个预定义了属性和方法的正则表达式对象。

#### 使用 test()

test() 方法是一个正则表达式方法。

test() 方法用于检测一个字符串是否匹配某个模式，如果字符串中含有匹配的文本，则返回 true，否则返回 false。

以下实例用于搜索字符串中的字符 "e"：

```javascript
var patt = /e/;
patt.test("The best things in life are free!");
//字符串中含有 "e"，所以该实例输出为：true
```

你可以不用设置正则表达式的变量，以上两行代码可以合并为一行：

```javascript
/e/.test("The best things in life are free!")
```

### 使用 exec()

exec() 方法是一个正则表达式方法。

exec() 方法用于检索字符串中的正则表达式的匹配。

该函数返回一个数组，其中存放匹配的结果。如果未找到匹配，则返回值为 null。

以下实例用于搜索字符串中的字母 "e":

```javascript
/e/.exec("The best things in life are free!");
//字符串中含有 "e"，所以该实例输出为:e
```

完整的 RegExp 对象参考手册，请参考我们的 [JavaScript RegExp 参考手册](https://www.runoob.com/jsref/jsref-obj-regexp.html)。

### 实例

**判断输入是否为数字、字母、下划线组成**

```javascript
function isValid(str) { return /^\w+$/.test(str); }
str = "1234abd__"
document.write(isValid(str));
document.write("<br>");

str2 = "$32343#"
document.write(isValid(str2));
document.write("<br>");
```

**判断字符串是否全部为字母**

```javascript
val = "123456"
var isletter = /^[a-zA-Z]+$/.test(val);
document.write(isletter);
document.write("<br>");

val2 = "asaaa"
var isletter2 = /^[a-zA-Z]+$/.test(val2);
document.write(isletter2);
```

**判断字符串是否全部为数字**

```javascript
val = "123456"
var isnum = /^\d+$/.test(val);
document.write(isnum);
document.write("<br>");

val2 = "as123"
var isnum2 = /^\d+$/.test(val2);
document.write(isnum2);
```

正则表达式表单验证实例：

```javascript
/*是否带有小数*/
function    isDecimal(strValue )  {  
   var  objRegExp= /^\d+\.\d+$/;
   return  objRegExp.test(strValue);  
}  

/*校验是否中文名称组成 */
function ischina(str) {
    var reg=/^[\u4E00-\u9FA5]{2,4}$/;   /*定义验证表达式*/
    return reg.test(str);     /*进行验证*/
}

/*校验是否全由8位数字组成 */
function isStudentNo(str) {
    var reg=/^[0-9]{8}$/;   /*定义验证表达式*/
    return reg.test(str);     /*进行验证*/
}

/*校验电话码格式 */
function isTelCode(str) {
    var reg= /^((0\d{2,3}-\d{7,8})|(1[3584]\d{9}))$/;
    return reg.test(str);
}

/*校验邮件地址是否合法 */
function IsEmail(str) {
    var reg=/^\w+@[a-zA-Z0-9]{2,10}(?:\.[a-z]{2,4}){1,3}$/;
    return reg.test(str);
}
```

```javascript
/**
 * [reg 百度网盘链接匹配]
 * 说明：匹配支持百度分享的两种链接格式
 * 格式一：链接: https://pan.baidu.com/s/15gzY8h3SEzVCfGV1xfkJsQ 提取码: vsuw 复制这段内容后打开百度网盘手机App，操作更方便哦
 * 格式二：http://pan.baidu.com/share/link?shareid=179436&uk=3272055266 提取码: vsuw 复制这段内容后打开百度网盘手机App，操作更方便哦
 * 匹配出下载地址和提取码，并且还支持如果没有提取码，也能匹配出下载链接。
 * @type {正则表达式}
 * @return array 返回匹配成功的链接和地址
 */

function baiduDownLinkArr( string ){
  var reg = /([http|https]*?:\/\/pan\.baidu\.com\/[(?:s\/){0,1}|(share)]*(?:[0-9a-zA-Z?=&])+)(?:.+:(?:\s)*)?([a-zA-Z]{4})?/;
  console.log(reg.exec(string));
}
```

## JavaScript 错误 - throw、try 和 catch

**try** 语句测试代码块的错误。

**catch** 语句处理错误。

**throw** 语句创建自定义错误。

**finally** 语句在 try 和 catch 语句之后，无论是否有触发异常，该语句都会执行。



**try** 语句允许我们定义在执行时进行错误测试的代码块。

**catch** 语句允许我们定义当 try 代码块发生错误时，所执行的代码块。

JavaScript 语句 **try** 和 **catch** 是成对出现的。

```javascript
try {
    ...    //异常的抛出
} catch(e) {
    ...    //异常的捕获与处理
} finally {
    ...    //结束处理
}
```

**finally** 语句不论之前的 try 和 catch 中是否产生异常都会执行该代码块。

```javascript
function myFunction() {
  var message, x;
  message = document.getElementById("p01");
  message.innerHTML = "";
  x = document.getElementById("demo").value;
  try { 
    if(x == "") throw "值是空的";
    if(isNaN(x)) throw "值不是一个数字";
    x = Number(x);
    if(x > 10) throw "太大";
    if(x < 5) throw "太小";
  }
  catch(err) {
    message.innerHTML = "错误: " + err + ".";
  }
  finally {
    document.getElementById("demo").value = "";
  }
}
```

throw 语句允许我们创建自定义错误。

正确的技术术语是：创建或**抛出异常**（exception）。

如果把 throw 与 try 和 catch 一起使用，那么您能够控制程序流，并生成自定义的错误消息。

## JavaScript 使用误区

### 浮点型数据使用注意事项

JavaScript 中的所有数据都是以 64 位**浮点型数据(float)** 来存储。

所有的编程语言，包括 JavaScript，对浮点型数据的精确度都很难确定：

```javascript
var x = 0.1;
var y = 0.2;
var z = x + y            // z 的结果为 0.30000000000000004
if (z == 0.3)            // 返回 false
//为解决以上问题，可以用整数的乘除法来解决：
var z = (x * 10 + y * 10) / 10;       // z 的结果为 0.3
```

### Undefined 不是 Null

在 JavaScript 中, **null** 用于对象, **undefined** 用于变量，属性和方法。

对象只有被定义才有可能为 null，否则为 undefined。

如果我们想测试对象是否存在，在对象还没定义时将会抛出一个错误。

错误的使用方式：

```javascript
if (myObj !== null && typeof myObj !== "undefined") 
//正确的方式是我们需要先使用 typeof 来检测对象是否已定义：
if (typeof myObj !== "undefined" && myObj !== null) 
```

### 程序块作用域

在每个代码块中 JavaScript 不会创建一个新的作用域，一般各个代码块的作用域都是全局的。

以下代码的的变量 i 返回 10，而不是 undefined：

```javascript
for (var i = 0; i < 10; i++) {
    // some code
}
return i;

```

## JavaScript 表单

### JavaScript 表单验证

HTML 表单验证可以通过 JavaScript 来完成。

以下实例代码用于判断表单字段(fname)值是否存在， 如果不存在，就弹出信息，阻止表单提交：

```javascript
function validateForm() {
    var x = document.forms["myForm"]["fname"].value;
    if (x == null || x == "") {
        alert("需要输入名字。");
        return false;
    }
}
```

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
function validateForm() {
    var x = document.forms["myForm"]["fname"].value;
    if (x == null || x == "") {
        alert("需要输入名字。");
        return false;
    }
}
</script>
</head>
<body>

<form name="myForm" action="demo_form.php"
onsubmit="return validateForm()" method="post">
名字: <input type="text" name="fname">
<input type="submit" value="提交">
</form>

</body>
</html>
```

JavaScript 常用于对输入数字的验证：

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>

<h1>JavaScript 验证输入</h1>

<p>请输入 1 到 10 之间的数字：</p>

<input id="numb">

<button type="button" onclick="myFunction()">提交</button>

<p id="demo"></p>

<script>
function myFunction() {
    var x, text;

    // 获取 id="numb" 的值
    x = document.getElementById("numb").value;

    // 如果输入的值 x 不是数字或者小于 1 或者大于 10，则提示错误 Not a Number or less than one or greater than 10
    if (isNaN(x) || x < 1 || x > 10) {
        text = "输入错误";
    } else {
        text = "输入正确";
    }
    document.getElementById("demo").innerHTML = text;
}
</script>

</body>
</html>
```

### HTML 表单自动验证

HTML 表单验证也可以通过浏览器来自动完成。

如果表单字段 (fname) 的值为空, **required** 属性会阻止表单提交：

```javascript
<form action="demo_form.php" method="post">
  <input type="text" name="fname" required="required">
  <input type="submit" value="提交">
</form>
```

### HTML 约束验证

HTML5 新增了 HTML 表单的验证方式：约束验证（constraint validation）。

约束验证是表单被提交时浏览器用来实现验证的一种算法。

HTML 约束验证基于：

- **HTML 输入属性**
- **CSS 伪类选择器**
- **DOM 属性和方法**

### 约束验证 HTML 输入属性

| 属性     | 描述                     |
| :------- | :----------------------- |
| disabled | 规定输入的元素不可用     |
| max      | 规定输入元素的最大值     |
| min      | 规定输入元素的最小值     |
| pattern  | 规定输入元素值的模式     |
| required | 规定输入元素字段是必需的 |
| type     | 规定输入元素的类型       |

完整列表，请查看 [HTML 输入属性](https://www.runoob.com/html/html5-form-attributes.html)。

### 约束验证 CSS 伪类选择器

| 选择器    | 描述                                    |
| :-------- | :-------------------------------------- |
| :disabled | 选取属性为 "disabled" 属性的 input 元素 |
| :invalid  | 选取无效的 input 元素                   |
| :optional | 选择没有"optional"属性的 input 元素     |
| :required | 选择有"required"属性的 input 元素       |
| :valid    | 选取有效值的 input 元素                 |

完整列表，请查看 [CSS 伪类](https://www.runoob.com/css/css-pseudo-classes.html)。

### E-mail 验证

下面的函数检查输入的数据是否符合电子邮件地址的基本语法。

意思就是说，输入的数据必须包含 @ 符号和点号(.)。同时，@ 不可以是邮件地址的首字符，并且 @ 之后需有至少一个点号：

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<head>
<script>
function validateForm(){
	var x=document.forms["myForm"]["email"].value;
	var atpos=x.indexOf("@");
	var dotpos=x.lastIndexOf(".");
	if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length){
		alert("不是一个有效的 e-mail 地址");
  		return false;
	}
}
</script>
</head>
<body>
	
<form name="myForm" action="demo-form.php" onsubmit="return validateForm();" method="post">
Email: <input type="text" name="email">
<input type="submit" value="提交">
</form>
	
</body>
</html>
```

