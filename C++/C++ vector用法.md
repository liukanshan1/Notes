# C++ vector用法（详解！！函数，实现）


１，简述一下vector的基本操作，它的ｓｉｚｅ，capacity（），ｃｌｅａｒ，ｒｅｖｅｒｓｅ，ｒｅｓｅｒｖｅ，

　　push_back等！！！

２，说说，ｖｅｃｔｏｒ的存储特性，是顺序存储还是如同链表般，如果是顺序存储的话，那么是如何执行

　　ｅｒａｓｅ，ｉｎｓｅｒｔ等函数，？？？（假如后面的空间不够的话，我们需要合理的算法来重新找出一块

　　相应的空间吗？？？拷贝，回收吗？？？是不是特别麻烦），如果是链式存储的话，那么它又是如何做到快速

　　的访问的（通过下标来的）！！！



1 基本操作

(1)头文件#include<vector>.

(2)创建vector对象，vector<int> vec;

(3)尾部插入数字：vec.push_back(a);

(4)使用下标访问元素，cout<<vec[0]<<endl;记住下标是从0开始的。

(5)使用迭代器访问元素.

​    

<span style="font-size:18px;">vector<int>::iterator it;
for(it=vec.begin();it!=vec.end();it++)
    cout<<*it<<endl;</span>

(6)插入元素：    vec.insert(vec.begin()+i,a);在第i个元素后面插入a;

(7)删除元素：    vec.erase(vec.begin()+2);删除第3个元素

　　　　　　　 vec.erase(vec.begin()+i,vec.end()+j);删除区间[i,j-1];区间从0开始

(8)向量大小:vec.size();

(9)清空:vec.clear()　　　//清空之后，vec.size()为０


一个简单的程序：

<span style="font-size:18px;">#include<stdio.h>
#include<vector>
#include<iostream>
using namespace std;
int main()
{
        int i=0;
        vector<int> vec;
        for(i=0; i<10; i++)
        {
                vec.push_back(i);　　　//10个元素依次进入，结果为10
        }

        for(unsigned int i=0; i<vec.size(); i++)
        {
        cout<<"初始化遍历："<<vec[i]<<endl;
        }
        //结果为：０，１，２，３，４，５，６，７，８，９
        vector<int>::iterator it;
     
        for(it = vec.begin(); it!=vec.end(); it++)
        {
        cout<<"迭代遍历："<<*it<<endl;
        }
　　//结果为：０，１，２，３，４，５，６，７，８，９
　　 vec.insert(vec.begin()+4,0);
　　//结果为:11
        for(unsigned int i=0; i<vec.size(); i++)
        {
        cout<<"插入遍历："<<vec[i]<<endl;
        }
        //结果为：０，１，２，３，０，４，５，６，７，８，９
        vec.erase(vec.begin()+2);
        for(unsigned int i=0; i<vec.size(); i++)
        {
        cout<<"擦除遍历："<<vec[i]<<endl;
        }
　　//结果为：０，１，３，０，４，５，６，７，８，９
        vec.erase(vec.begin()+3,vec.begin()+5);
　　
        for(vector<int>::iterator it = vec.begin(); it!=vec.end(); it++)
        {
        cout<<"迭代遍历："<<*it<<endl;
        }
        return 0;
}


</span>

2:

vector的元素不仅仅可以使int,double,string,还可以是结构体，但是要注意：结构体要定义为全局的，否则会出错。下面是一段简短的程序代码：

<span style="font-size:18px;">#include<stdio.h>
#include<algorithm>
#include<vector>
#include<iostream>
using namespace std;

typedef struct rect
{
    int id;
    int length;
    int width;

　　//对于向量元素是结构体的，可在结构体内部定义比较函数，下面按照id,length,width升序排序。
　　bool operator< (const rect &a)  const
    {
        if(id!=a.id)
            return id<a.id;
        else
        {
            if(length!=a.length)
                return length<a.length;
            else
                return width<a.width;
        }
    }
}Rect;

int main()
{
    vector<Rect> vec;
    Rect rect;
    rect.id=1;
    rect.length=2;
    rect.width=3;
    vec.push_back(rect);
    vector<Rect>::iterator it=vec.begin();
    cout<<(*it).id<<' '<<(*it).length<<' '<<(*it).width<<endl;    

return 0;

}</span>

3  算法



(1) 使用reverse将元素翻转：需要头文件#include<algorithm>

     reverse(vec.begin(),vec.end());将元素翻转(在vector中，如果一个函数中需要两个迭代器，
    
     一般后一个都不包含.)

(2)使用sort排序：需要头文件#include<algorithm>，

sort(vec.begin(),vec.end());(默认是按升序排列,即从小到大).

可以通过重写排序比较函数按照降序比较，如下：

定义排序比较函数：

bool Comp(const int &a,const int &b)
{
    return a>b;
}
调用时:sort(vec.begin(),vec.end(),Comp)，这样就降序排序。







vector ： C++ STL中的顺序容器，封装数组

 

1. vector容器的内存自增长 

与其他容器不同，其内存空间只会增长，不会减小。先来看看"C++ Primer"中怎么说：为了支持快速的随机访

问，vector容器的元素以连续方式存放，每一个元素都紧挨着前一个元素存储。设想一下，当vector添加一个元素时，

为了满足连续存放这个特性，都需要重新分配空间、拷贝元素、撤销旧空间，这样性能难以接受。因此STL实现者在对

vector进行内存分配时，其实际分配的容量要比当前所需的空间多一些。就是说，vector容器预留了一些额外的存储

区，用于存放新添加的元素，这样就不必为每个新元素重新分配整个容器的内存空间。

关于vector的内存空间，有两个函数需要注意：size()成员指当前拥有的元素个数；capacity()成员指当前(容器必须分

配新存储空间之前)可以存储的元素个数。reserve()成员可以用来控制容器的预留空间。vector另外一个特性在于它的

内存空间会自增长，每当vector容器不得不分配新的存储空间时，会以加倍当前容量的分配策略实现重新分配。例如，

当前capacity为50，当添加第51个元素时，预留空间不够用了，vector容器会重新分配大小为100的内存空间，作为新

连续存储的位置。



<span style="font-size:18px;">#include <iostream>
using namespace std;
#include <vector>

int main()
{
        vector<int> arry;
        //arry.reserve(10);
        cout << arry.capacity() <<endl;
        arry.push_back(1);
        cout<<arry.capacity() <<endl;
        arry.push_back(2);
        cout<<arry.capacity() <<endl;
        arry.push_back(3);
        cout<<arry.capacity() <<endl;

}
</span>
运行结果：


当我们将上面的那句注释去掉之后：





2. vector内存释放

由于vector的内存占用空间只增不减，比如你首先分配了10,000个字节，然后erase掉后面9,999个，留下一个有效元素，但是内存占

用仍为10,000个。所有内存空间是在vector析构时候才能被系统回收。empty()用来检测容器是否为空的，clear()可以清空所有元素。

但是即使clear()，vector所占用的内存空间依然如故，无法保证内存的回收。

如果需要空间动态缩小，可以考虑使用deque。如果非vector不可，可以用swap()来帮助你释放内存。具体方法如下：

<span style="font-size:18px;">vector<int> nums; 
nums.push_back(1);
nums.push_back(1);
nums.push_back(2);
nums.push_back(2); 
vector<int>().swap(nums); //或者nums.swap(vector<int> ())</span>

或者如下所示，使用一对大括号，意思一样的：
<span style="font-size:18px;">//加一对大括号是可以让tmp退出{}的时候自动析构
{ 
    std::vector<int> tmp =   nums;  
    nums.swap(tmp); 
}

</span>

 swap()是交换函数，使vector离开其自身的作用域，从而强制释放vector所占的内存空间，总而言之，释放vector内存最简单的方法是vector<int>.swap(nums)。当时如果nums是一个类的成员，不能把vector<int>.swap(nums)写进类的析构函数中，否则会导致double free or corruption (fasttop)的错误，原因可能是重复释放内存。标准解决方法如下：
<span style="font-size:18px;">template < class T >
void ClearVector( vector< T >& vt ) 
{
    vector< T > vtTemp; 
    veTemp.swap( vt );
}</span>

3. 利用vector释放指针

如果vector中存放的是指针，那么当vector销毁时，这些指针指向的对象不会被销毁，那么内存就不会被释放。如下面这种情况，vector中的元素时由new操作动态申请出来的对象指针：

<span style="font-size:18px;">#include <vector> 
using namespace std; 

vector<void *> v;</span>

每次new之后调用v.push_back()该指针，在程序退出或者根据需要，用以下代码进行内存的释放：
<span style="font-size:18px;">for (vector<void *>::iterator it = v.begin(); it != v.end(); it ++) 
    if (NULL != *it) 
    {
        delete *it; 
        *it = NULL;
    }
v.clear();</span>








３，

vector是线性容器,它的元素严格的按照线性序列排序,和动态数组很相似,和数组一样,它的元素存储在一块连续的存储空间中,这也意味着我们不仅可以使用迭代器(iterator)访问元素,还可以使用指针的偏移方式访问,和常规数组不一样的是,vector能够自动存储元素,可以自动增长或缩小存储空间,

vector的优点:

1.       可以使用下标访问个别的元素

2.       迭代器可以按照不同的方式遍历容器

3.       可以在容器的末尾增加或删除元素

和数组相比,虽然容器在自动处理容量的大小时会消耗更多的内存,但是容器能提供和数组一样的性能,而且能很好的调整存储空间大小

和其他标准的顺序容器相比(deques or lists),能更有效访问容器内的元素和在末尾添加和删除元素,在其他位置添加和删除元素,vector则不及其他顺序容器,在迭代器和引用也不比lists支持的好

容器的大小和容器的容量是有区别的,大小是指元素的个数,容量是分配的内存大小,容量一般等于或大于容器的大小,vector::size()返回容器的大小,vector::capacity()返回容量值,容量多于容器大小的部分用于以防容器的增加使用,每次重新分配内存都会很影响程序的性能,所以一般分配的容量大于容器的大小,若要自己指定分配的容量的大小,则可以使用vector::reserve(),但是规定的值要大于size()值,



1.构造和复制构造函数

explicit vector ( const Allocator& = Allocator() );

explicit vector ( size_type n, const T& value= T(), const Allocator& = Allocator() );

template <class InputIterator>

vector ( InputIterator first, InputIterator last, const Allocator& = Allocator() );

vector ( const vector<T,Allocator>& x );

 

explicit:是防止隐式转换, Allocator是一种内存分配模式,一般是使用默认的

 

vector<int> A;  //创建一个空的的容器

vector<int> B(10,100); //创建一个个元素,每个元素值为

vector<int> C(B.begin(),B.end()); //使用迭代器,可以取部分元素创建一个新的容器

vector<int> D(C); //复制构造函数,创建一个完全一样的容器

 

2.析构函数

 ~vector()

销毁容器对象并回收了所有分配的内存

 

3.重载了=符号

vector<int> E;

E = B; //使用=符号

B = vector<int>(); //将B置为空容器

 

 

4. vector::begin()  返回第一个元素的迭代器

  函数原型：

  iterator begin ();  //返回一个可变迭代器

const_iterator begin () const; //返回一个常量的迭代器，不可变

 

5.vector::end()  返回的是越界后的第一个位置，也就是最后一个元素的下一个位置

  iterator end ();

const_iterator end () const;

 

6.vector::rbegin() 反序的第一个元素，也就是正序最后一个元素

  reverse_iterator rbegin();

const_reverse_iterator rbegin() const;

 

7.vector::rend() 反序的最后一个元素下一个位置，也相当于正序的第一个元素前一个位置

  reverse_iterator rend();

const_reverse_iterator rend() const;

和vector::end()原理一样

 

8.vector::size() 返回容器中元素个数

  size_type size() const;

  注意与vector::capacity()的区别

 

9.vector::max_size()

  size_type max_size () const;

  返回容器的最大可以存储的元素个数，这是个极限，当容器扩展到这个最大值时就不能再自动增大

 

10. vector::resize()

  void resize ( size_type sz, T c = T() );

  重新分配容器的元素个数，这个还可以改容器的容量，如果重新分配的元素个数比原来的小，将截断序列，后面的部分丢弃，如果大于原来的个数，后面的值是c的值，默认为0

 

11. vector::capacity()

   size_type capacity () const;

   返回vector的实际存储空间的大小，这个一般大于或等于vector元素个数，注意与size()函数的区别

 

12. vector::empty()

   bool empty () const;

   当元素个数为0时返回true，否则为false，根据的是元素个数而不是容器的存储空间的大小

 

 

13. vector::reserve()

   void reserve ( size_type n );

重新分配空间的大小，不过这个n值要比原来的capacity()返回的值大，不然存储空间保持不变，n值要比原来的实际存储空间大才能重新分配空间，但是最大值不可以大于max_size的值，否则会抛出异常

 

14. vector::operator[]  //重载了[]符号

   reference  operator[] ( size_type n );

const_reference  operator[] ( size_type n ) const;

实现了下标访问元素

 

15. vector::at()

   const_reference at ( size_type n ) const;

   reference at ( size_type n );

   在函数的操作方面和下标访问元素一样，不同的是当这个函数越界时会抛出一个异常out_of_range

 

16. vector::front()

   reference front ( );

const_reference front ( ) const;

返回第一个元素的值，与begin()函数有区别，begin()函数返回的是第一个元素的迭代器

 

17. vector::back()

   reference back ( );

const_reference back ( ) const;

同样，返回最后一个元素的值，注意与end()函数的区别

 

18. vector::assign()

   template <class InputIterator> void assign ( InputIterator first, InputIterator last );

void assign ( size_type n, const T& u );

将丢弃原来的元素然后重新分配元素，第一个函数是使用迭代器，第二个函数是使用n个元素，每个元素的值为u。

 

19. vector::push_back()

   void push_back ( const T& x );

   在容器的最后一个位置插入元素x,如果size值大于capacity值，则将重新分配空间

 

20. vector::pop_back()

   void pop_back ( );

   删除最后一个元素

 

 

21. vector::insert()

   iterator insert ( iterator position, const T& x );

   void insert ( iterator position, size_type n, const T& x );

template <class InputIterator>

void insert ( iterator position, InputIterator first, InputIterator last );

   插入新的元素，

第一个函数，在迭代器指定的位置前插入值为x的元素

第二个函数，在迭代器指定的位置前插入n个值为x的元素

第三个函数，在迭代器指定的位置前插入另外一个容器的一段序列迭代器first到last

若插入新的元素后总得元素个数大于capacity，则重新分配空间

 

22. vector::erase()

   iterator erase ( iterator position );

iterator erase ( iterator first, iterator last );

删除元素或一段序列

 

23. vector::swap()

   void swap ( vector<T,Allocator>& vec );

   交换这两个容器的内容，这涉及到存储空间的重新分配

 

24. vector::clear()

   void clear ( );

   将容器里的内容清空，size值为0，但是存储空间没有改变


<span style="font-size:18px;">#include <vector>
#include <iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{

        //构造函数,复制构造函数(元素类型要一致),
    vector<int> A;  //创建一个空的的容器
    vector<int> B(10,100); //创建一个10个元素,每个元素值为100
    vector<int> C(B.begin(),B.end()); //使用迭代器,可以取部分元素创建一个新的容器
    vector<int> D(C); //复制构造函数,创建一个完全一样的容器
    
          //重载=
    vector<int> E;
    E = B;
     
    //vector::begin()，返回的是迭代器
       
    vector<int> F(10); //创建一个有10个元素的容器
           for (int i = 0; i < 10; i++)
          {
        F[i] = i;
          }
     
    /*
    vector<int> F; //创建一个空容器
    for (int i = 0; i < 10; i++)
    {
        F.push_back(i);
    } 
        */
     
    vector<int>::iterator BeginIter = F.begin();
    cout << *BeginIter << endl; //输出0
     
    //vector::end() 返回迭代器
    vector<int>::iterator EndIter = F.end();
    EndIter--; //向后移一个位置
    cout << *EndIter << endl; //输出9
     
    //vector::rbegin() 返回倒序的第一个元素，相当于最后一个元素
    vector<int>::reverse_iterator ReverBeIter = F.rbegin();
    cout << *ReverBeIter << endl; //输出9
     
    //vector::rend() 反序的最后一个元素下一个位置，也相当于正序的第一个元素前一个位置
    vector<int>::reverse_iterator ReverEnIter = F.rend();
    ReverEnIter--;
    cout << *ReverEnIter << endl; //输出0
     
    //vector::size() 返回元素的个数
    cout << F.size() << endl; //输出10
     
    //vector::max_size()
    cout << F.max_size() << endl; //输出1073741823，这个是极限元素个数
     
    //vector::resize()
    cout << F.size() << endl; //输出10
    F.resize(5);
    for(int k = 0; k < F.size(); k++)
        cout << F[k] << "  "; //输出 0 1 2 3 4
         cout << endl;
    
    //vector::capacity()
    cout << F.size() << endl; //5
    cout << F.capacity() << endl; //10
     
    //vector::empty()
         B.resize(0);
    cout << B.size() << endl; //0
    cout << B.capacity() << endl; //10
    cout << B.empty() << endl; //true
     
    //vector::reserve() //重新分配存储空间大小
           cout << C.capacity() << endl; //10
    C.reserve(4);
    cout << C.capacity() << endl; //10
    C.reserve(14);
    cout << C.capacity() << endl; //14
     
    //vector::operator []
    cout << F[0] << endl; //第一个元素是0
     
    //vector::at()
    try
    {
      cout << "F.size = " << F.size() << endl; //5
           cout << F.at(6) << endl; //抛出异常
    }
    catch(out_of_range)
    {    
       cout << "at()访问越界" << endl;
    }
     
    //vector::front() 返回第一个元素的值
           cout << F.front() << endl; //0
     
    //vector::back()
    cout << F.back() << endl; //4
     
    //vector::assign()
    cout << A.size() << endl; //0
    vector<int>::iterator First = C.begin();
    vector<int>::iterator End = C.end()-2;
    A.assign(First,End);
    cout << A.size() << endl; //8
    cout << A.capacity() << endl; //8
     
    A.assign(5,3); //将丢弃原来的所有元素然后重新赋值
    cout << A.size() << endl; //5
    cout << A.capacity() << endl; //8
     
    //vector::push_back()
    cout << *(F.end()-1) << endl; //4
    F.push_back(100);
    cout << *(F.end()-1) << endl; //100
     
    //vector::pop_back()
    cout << *(F.end()-1) << endl; //100
    F.pop_back();
    cout << *(F.end()-1) << endl; //4
     
    //vector::swap()
    F.swap(D); //交换这两个容器的内容
    for(int f = 0; f < F.size(); f++)
        cout << F[f] << " ";
    cout << endl;
    for (int d = 0; d < D.size(); d++)
        cout << D[d] << " ";
         cout << endl;
    //vector::clear()
    F.clear();
    cout << F.size() << endl;     //0
    cout << F.capacity() << endl; //10
     
    return 0;
}


</span>




本文借鉴与：http://www.cnblogs.com/wang7/archive/2012/04/27/2474138.html

                     http://blog.csdn.net/bizhu12/article/details/6769976
　　　　　　http://www.cnblogs.com/summerRQ/articles/2407974.html
————————————————
版权声明：本文为CSDN博主「L未若」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/msdnwolaile/article/details/52708144

# C++（笔记）浅析vector容器的实例


一、什么是vector
向量（Vector）是一个封装了动态大小数组的顺序容器（Sequence container）。跟任意其它类型容器一样，它能够存放各种类型的对象。可以简单的认为，向量是一个能够存放任意类型的动态数组。

二、容器特性
1.顺序序列
顺序容器中的元素按照严格的线性顺序排序。可以通过元素在序列中的位置访问对应的元素。

2.动态数组
支持对序列中的任意元素进行快速直接访问，甚至可以通过指针算述进行该操作。操供了在序列末尾相对快速地添加/删除元素的操作。

3.能够感知内存分配器的（Allocator-aware）
容器使用一个内存分配器对象来动态地处理它的存储需求。

二、基本函数实现
1.构造函数
vector():创建一个空vector
vector(int nSize):创建一个vector,元素个数为nSize
vector(int nSize,const t& t):创建一个vector，元素个数为nSize,且值均为t
vector(const vector&):复制构造函数
vector(begin,end):复制[begin,end)区间内另一个数组的元素到vector中
2.增加函数
void push_back(const T& x):向量尾部增加一个元素X
iterator insert(iterator it,const T& x):向量中迭代器指向元素前增加一个元素x
iterator insert(iterator it,int n,const T& x):向量中迭代器指向元素前增加n个相同的元素x
iterator insert(iterator it,const_iterator first,const_iterator last):向量中迭代器指向元素前插入另一个相同类型向量的[first,last)间的数据
3.删除函数
iterator erase(iterator it):删除向量中迭代器指向元素
iterator erase(iterator first,iterator last):删除向量中[first,last)中元素
void pop_back():删除向量中最后一个元素
void clear():清空向量中所有元素
4.遍历函数
reference at(int pos):返回pos位置元素的引用
reference front():返回首元素的引用
reference back():返回尾元素的引用
iterator begin():返回向量头指针，指向第一个元素
iterator end():返回向量尾指针，指向向量最后一个元素的下一个位置
reverse_iterator rbegin():反向迭代器，指向最后一个元素
reverse_iterator rend():反向迭代器，指向第一个元素之前的位置
5.判断函数
bool empty() const:判断向量是否为空，若为空，则向量中无元素
6.大小函数
int size() const:返回向量中元素的个数
int capacity() const:返回当前向量张红所能容纳的最大元素值
int max_size() const:返回最大可允许的vector元素数量值
7.其他函数
void swap(vector&):交换两个同类型向量的数据
void assign(int n,const T& x):设置向量中第n个元素的值为x
void assign(const_iterator first,const_iterator last):向量中[first,last)中元素设置成当前向量元素
8.看着清楚
1.push_back 在数组的最后添加一个数据
2.pop_back 去掉数组的最后一个数据
3.at 得到编号位置的数据
4.begin 得到数组头的指针
5.end 得到数组的最后一个单元+1的指针
6．front 得到数组头的引用
7.back 得到数组的最后一个单元的引用
8.max_size 得到vector最大可以是多大
9.capacity 当前vector分配的大小
10.size 当前使用数据的大小
11.resize 改变当前使用数据的大小，如果它比当前使用的大，者填充默认值
12.reserve 改变当前vecotr所分配空间的大小
13.erase 删除指针指向的数据项
14.clear 清空当前的vector
15.rbegin 将vector反转后的开始指针返回(其实就是原来的end-1)
16.rend 将vector反转构的结束指针返回(其实就是原来的begin-1)
17.empty 判断vector是否为空
18.swap 与另一个vector交换数据

三、基本用法
#include < vector>
using namespace std;

四、简单介绍
Vector<类型>标识符
Vector<类型>标识符(最大容量)
Vector<类型>标识符(最大容量,初始所有值)
Int i[5]={1,2,3,4,5}
Vector<类型>vi(I,i+2);//得到i索引值为3以后的值
Vector< vector< int> >v; 二维向量//这里最外的<>要有空格。否则在比较旧的编译器下无法通过
实例来咯
1.pop_back()&push_back(elem)实例在容器最后移除和插入数据
#include <string.h>　
#include <vector>
#include <iostream>
using namespace std;

int main()
{
    vector<int>obj(10,0);//最大容器为10，都初始化为0
    for(int i=0;i<10;i++)//push_back(elem)在数组最后添加数据 
    {
        obj.push_back(i);
        cout<<obj[i]<<",";
    }

    for(int i=0;i<5;i++)//去掉数组最后一个数据 
    {
        obj.pop_back();
    }
    
    cout<<"\n"<<endl;
    
    for(int i=0;i<obj.size();i++)//size()容器中实际数据个数 
    {
        cout<<obj[i]<<",";
    }
    
    return 0;
}



2.clear()清除容器中所以数据
#include <string.h>　
#include <vector>
#include <iostream>
using namespace std;

int main()
{
    vector<int>obj;
    for(int i=0;i<10;i++)//push_back(elem)在数组最后添加数据 
    {
        obj.push_back(i);
        cout<<obj[i]<<",";
    }

    obj.clear();//清除容器中所以数据
    for(int i=0;i<obj.size();i++)
    {
        cout<<obj[i]<<endl;
    }
    
    return 0;
}



3.排序
#include <string.h>　
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    vector<int>obj;

    obj.push_back(1);
    obj.push_back(3);
    obj.push_back(0);
    
    sort(obj.begin(),obj.end());//从小到大
    
    cout<<"从小到大:"<<endl;
    for(int i=0;i<obj.size();i++)
    {
        cout<<obj[i]<<",";  
    } 
    
    cout<<"\n"<<endl;
    
    cout<<"从大到小:"<<endl;
    reverse(obj.begin(),obj.end());//从大到小 
    for(int i=0;i<obj.size();i++)
    {
        cout<<obj[i]<<",";
    }
    return 0;
}
1.注意sort需要头文件#include < algorithm>
2.如果想sort来降序，可重写sort
bool compare(int a,int b)
{
return a< b; //升序排列，如果改为return a>b，则为降序
}
int a[20]={2,4,1,23,5,76,0,43,24,65},i;
for(i=0;i<20;i++)
cout<< a[i]<< endl;
sort(a,a+20,compare);

4.访问（直接数组访问&迭代器访问）
#include <string.h>　
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    //顺序访问
    vector<int>obj;
    for(int i=0;i<10;i++)
    {
        obj.push_back(i);   
    } 

    cout<<"直接利用数组："; 
    for(int i=0;i<10;i++)//方法一 
    {
        cout<<obj[i]<<" ";
    }
    
    cout<<endl; 
    cout<<"利用迭代器：" ;
    //方法二，使用迭代器将容器中数据输出 
    vector<int>::iterator it;//声明一个迭代器，来访问vector容器，作用：遍历或者指向vector容器的元素 
    for(it=obj.begin();it!=obj.end();it++)
    {
        cout<<*it<<" ";
    }
    return 0;
}
5.二维数组两种定义方法（结果一样）
#include <string.h>　
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int N=5, M=6; 
    vector<vector<int> > obj(N); //定义二维动态数组大小5行 
    for(int i =0; i< obj.size(); i++)//动态二维数组为5行6列，值全为0 
    { 
        obj[i].resize(M); 
    } 

    for(int i=0; i< obj.size(); i++)//输出二维动态数组 
    {
        for(int j=0;j<obj[i].size();j++)
        {
            cout<<obj[i][j]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}

#include <string.h>　
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int N=5, M=6; 
    vector<vector<int> > obj(N, vector<int>(M)); //定义二维动态数组5行6列 

    for(int i=0; i< obj.size(); i++)//输出二维动态数组 
    {
        for(int j=0;j<obj[i].size();j++)
        {
            cout<<obj[i][j]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}
—————————————
版权声明：本文为CSDN博主「浅然言而信」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/w_linux/article/details/71600574

# vector 是向量类型

它可以容纳许多类型的数据，如若干个整数，所以称其为容器。vector 是C++ STL的一个重要成员，使用它时需要包含头文件：

```
#include<vector>;
```

一、vector 的初始化：可以有五种方式,举例说明如下：

```
    (1) vector<int> a(10); //定义了10个整型元素的向量（尖括号中为元素类型名，它可以是任何合法的数据类型），但没有给出初值，其值是不确定的。
   （2）vector<int> a(10,1); //定义了10个整型元素的向量,且给出每个元素的初值为1
   （3）vector<int> a(b); //用b向量来创建a向量，整体复制性赋值
   （4）vector<int> a(b.begin(),b.begin+3); //定义了a值为b中第0个到第2个（共3个）元素
   （5）int b[7]={1,2,3,4,5,9,8};
        vector<int> a(b,b+7); //从数组中获得初值
```

 

二、vector对象的几个重要操作，举例说明如下：

 

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
    （1）a.assign(b.begin(), b.begin()+3); //b为向量，将b的0~2个元素构成的向量赋给a
    （2）a.assign(4,2); //是a只含4个元素，且每个元素为2
    （3）a.back(); //返回a的最后一个元素
    （4）a.front(); //返回a的第一个元素
    （5）a[i]; //返回a的第i个元素，当且仅当a[i]存在2013-12-07
    （6）a.clear(); //清空a中的元素
    （7）a.empty(); //判断a是否为空，空则返回ture,不空则返回false
    （8）a.pop_back(); //删除a向量的最后一个元素
    （9）a.erase(a.begin()+1,a.begin()+3); //删除a中第1个（从第0个算起）到第2个元素，也就是说删除的元素从a.begin()+1算起（包括它）一直到a.begin()+         3（不包括它）
    （10）a.push_back(5); //在a的最后一个向量后插入一个元素，其值为5
    （11）a.insert(a.begin()+1,5); //在a的第1个元素（从第0个算起）的位置插入数值5，如a为1,2,3,4，插入元素后为1,5,2,3,4
    （12）a.insert(a.begin()+1,3,5); //在a的第1个元素（从第0个算起）的位置插入3个数，其值都为5
    （13）a.insert(a.begin()+1,b+3,b+6); //b为数组，在a的第1个元素（从第0个算起）的位置插入b的第3个元素到第5个元素（不包括b+6），如b为1,2,3,4,5,9,8         ，插入元素后为1,4,5,9,2,3,4,5,9,8
    （14）a.size(); //返回a中元素的个数；
    （15）a.capacity(); //返回a在内存中总共可以容纳的元素个数
    （16）a.resize(10); //将a的现有元素个数调至10个，多则删，少则补，其值随机
    （17）a.resize(10,2); //将a的现有元素个数调至10个，多则删，少则补，其值为2
    （18）a.reserve(100); //将a的容量（capacity）扩充至100，也就是说现在测试a.capacity();的时候返回值是100.这种操作只有在需要给a添加大量数据的时候才         显得有意义，因为这将避免内存多次容量扩充操作（当a的容量不足时电脑会自动扩容，当然这必然降低性能） 
    （19）a.swap(b); //b为向量，将a中的元素和b中的元素进行整体性交换
    （20）a==b; //b为向量，向量的比较操作还有!=,>=,<=,>,<
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

三、顺序访问vector的几种方式，举例说明如下：
（1）向向量a中添加元素
1、

```
1  vector<int> a;
2 for(int i=0;i<10;i++)
3 a.push_back(i);
```

 

2、也可以从数组中选择元素向向量中添加

```
int a[6]={1,2,3,4,5,6};
vector<int> b；
for(int i=1;i<=4;i++)
b.push_back(a[i]);
```

 

 

3、也可以从现有向量中选择元素向向量中添加

```
int a[6]={1,2,3,4,5,6};
vector<int> b;
vector<int> c(a,a+4);
for(vector<int>::iterator it=c.begin();it<c.end();it++)
b.push_back(*it);
```

 

4、也可以从文件中读取元素向向量中添加

```
ifstream in("data.txt");
vector<int> a;
for(int i; in>>i)
    a.push_back(i);
```

 

5、【误区】

```
vector<int> a;
for(int i=0;i<10;i++)
    a[i]=i;
```

//这种做法以及类似的做法都是错误的。刚开始我也犯过这种错误，后来发现，下标只能用于获取已存在的元素，而现在的a[i]还是空的对象

 

（2）从向量中读取元素
1、通过下标方式读取

```
int a[6]={1,2,3,4,5,6};
vector<int> b(a,a+4);
for(int i=0;i<=b.size()-1;i++)
    cout<<b[i]<<" ";
```

 

2、通过遍历器方式读取

```
int a[6]={1,2,3,4,5,6};
vector<int> b(a,a+4);
for(vector<int>::iterator it=b.begin();it!=b.end();it++)
    cout<<*it<<" ";
```

 

四、几种重要的算法，使用时需要包含头文件：

```
#include<algorithm>
（1）sort(a.begin(),a.end()); //对a中的从a.begin()（包括它）到a.end()（不包括它）的元素进行从小到大排列
（2）reverse(a.begin(),a.end()); //对a中的从a.begin()（包括它）到a.end()（不包括它）的元素倒置，但不排列，如a中元素为1,3,2,4,倒置后为4,2,3,1
（3）copy(a.begin(),a.end(),b.begin()+1); //把a中的从a.begin()（包括它）到a.end()（不包括它）的元素复制到b中，从b.begin()+1的位置（包括它）开        始复制，覆盖掉原有元素
（4）find(a.begin(),a.end(),10); //在a中的从a.begin()（包括它）到a.end()（不包括它）的元素中查找10，若存在返回其在向量中的位置
```

 

五、参考引用：

  1、小熊的世界 http://blog.csdn.net/pandy1110/article/details/5963908

  2、MSDN http://msdn.microsoft.com/library

  3、《C++程序设计教程（第二版）》.钱能.清华大学出版社