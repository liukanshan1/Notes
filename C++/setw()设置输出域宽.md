# C++ setw()设置输出域宽

**头文件：**
`#include <iomanip>`

# setw()

在C++中，setw(int n)用来设置输出域宽。
例如:
`cout << 's' << setw(8) << 'a' << endl;`
输出：
`s a`
//s与a之间有7个空格

setw()只对其后面紧跟的输出产生作用，如上例中，表示’a’共占8个位置，不足的7个位置用空格填充。若紧跟的输出的内容超过setw()设置的长度，则按实际长度输出，中间不会有空格（相当于没有写setw()）。
`cout << 's' << setw(3) << 'abcd' << endl;`
输出：
`sabcd`

## setfill()

setw()默认填充的内容为空格，可以setfill()配合使用设置其他字符填充。
如
`cout << setfill('*') << setw(5) << 'a' << endl;`
则输出：
`****a`
//4个*和字符a共占5个位置。