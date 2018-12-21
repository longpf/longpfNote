这里是MJ的C++课做的笔记

## 目录

* <a href="#常用语法"><font size=5 color=#1061ed face="微软雅黑">常用语法</font></a>
* <a href="#函数重载">1. 函数重载</a>
* <a href="#extern C">2. extern "C"</a>
* <a href="#默认参数">3. 默认参数</a>
* <a href="#内联函数">4. 内联函数</a>
* <a href="##pragma once">4. #pragma once</a>
* <a href="#引用">5. 引用</a>
* <a href="#const">6. const</a>
* <a href="#常引用">7. 常引用</a>
* <a href="#数组的引用">8. 数组的引用</a>
* <a href="#程序的本质">9. 程序的本质</a>
* <a href="#x86_64 简单基础">10. x86_64 简单基础</a>
* <a href="#引用的本质">11. 引用的本质</a>
* <a href="#面向对象"><font size=5 color=#1061ed face="微软雅黑">面向对象</font></a>
* <a href="#类">1. 类</a>
* <a href="#this">2. this</a>
* <a href="#封装">3. 封装</a>
* <a href="#内存空间的布局">4. 内存空间的布局</a>
* <a href="#对象的内存">5. 对象的内存</a>
* <a href="#构造函数">6. 构造函数</a>
* <a href="#构造函数的调用">7. 构造函数的调用</a>
* <a href="#成员变量的初始化">8. 成员变量的初始化</a>
* <a href="#析构函数">9. 析构函数</a>
* <a href="#strcpy过期问题解决">10. strcpy过期问题解决</a>
* <a href="#声明和实现分离">11. 声明和实现分离</a>
* <a href="#命名空间">12. 命名空间</a>
* <a href="#命名空间的嵌套">13. 命名空间的嵌套</a>
* <a href="#命名空间的合并">14. 命名空间的合并</a>
* <a href="#继承">15. 继承</a>
* <a href="#初始化列表">16. 初始化列表</a>
* <a href="#构造函数的相互调用">17. 构造函数的相互调用</a>
* <a href="#初始化列表与默认参数配合使用">18. 初始化列表与默认参数配合使用</a>
* <a href="#父类的构造函数">19. 父类的构造函数</a>
* <a href="#继承体系下的构造函数示例">20. 继承体系下的构造函数示例</a>
* <a href="#构造,析构顺序">21. 构造,析构顺序</a>
* <a href="#父类指针,子类指针">22. 父类指针,子类指针</a>
* <a href="#多态">23. 多态</a>
* <a href="#虚函数">24. 虚函数</a>
* <a href="#虚表">25. 虚表</a>
* <a href="#虚表汇编分析">26. 虚表汇编分析</a>
* <a href="#虚析构函数">27. 虚析构函数</a>
* <a href="#纯虚函数">28. 纯虚函数</a>
* <a href="#多继承">29. 多继承</a>
* <a href="#多继承体系下的构造函数调用">30. 多继承体系下的构造函数调用</a>
* <a href="#多继承-虚函数">31. 多继承-虚函数</a>
* <a href="#多继承的同名函数和同名变量">32. 多继承的同名函数和同名变量</a>
* <a href="#菱形继承">33. 菱形继承</a>
* <a href="#虚继承">34. 虚继承</a>
* <a href="#静态成员">35. 静态成员</a>
* <a href="#静态成员变量经典应用-单例模式">36. 静态成员变量经典应用-单例模式</a>
* <a href="#const 成员">37. const 成员</a>
* <a href="#引用类型成员">38. 引用类型成员</a>
* <a href="#拷贝构造函数">39. 拷贝构造函数</a>
* <a href="#调用父类的拷贝构造函数">40. 调用父类的拷贝构造函数</a>
* <a href="#浅拷贝,深拷贝">41. 浅拷贝,深拷贝</a>
* <a href="#对象型参数和返回值">42. 对象型参数和返回值</a>
* <a href="#匿名对象(临时对象)">43. 匿名对象(临时对象)</a>
* <a href="#隐式构造">44. 隐式构造</a>
* <a href="#编译器自动生成的构造函数">45. 编译器自动生成的构造函数</a>
* <a href="#友元">46. 友元</a>
* <a href="#内部类">47. 内部类</a>
* <a href="#局部类">48. 局部类</a>
* <a href="#其他语法"><font size=5 color=#1061ed face="微软雅黑">其他语法</font></a>
* <a href="#运算符重载">1. 运算符重载</a>
* <a href="#运算符重载-Point">2. 运算符重载-Point</a>
* <a href="#运算符重载-String">3. 运算符重载-String</a>
* <a href="#调用父类的运算符重载函数">4. 调用父类的运算符重载函数</a>
* <a href="#仿函数">5. 仿函数</a>
* <a href="#运算符重载注意点">6. 运算符重载注意点</a>
* <a href="#模板\函数模板">7. 模板\函数模板</a>
* <a href="#类模板">8. 类模板</a>
* <a href="#类型转化">9. 类型转化</a>
* <a href="#c++11 新特性">10. c++11 新特性</a>
* <a href="#Lambda表达式">11. Lambda表达式</a>
* <a href="#Lambda表达式 - 外部变量捕获">12. Lambda表达式 - 外部变量捕获</a>
* <a href="#Lambda表达式 - mutable">13. Lambda表达式 - mutable</a>
* <a href="#c++14 ">14. c++14 </a>
* <a href="#异常">15. 异常</a>
* <a href="#智能指针">16. 智能指针</a>

<a id="常用语法"></a>

## 常用语法

<a id="函数重载"></a>

### 函数重载(overload)

函数名相同,参数个数不同,参数类型不同,参数顺序不同

* 如果两个函数只有返回值不同, 这么写会报错. 如果不接收返回值不知道调用那个函数

	```cpp
	void test(){};
	int test(){};
	
	test(); //这么写会报错,因为不确定这个test()调用的哪个函数
	```
* 调用函数时,实参的隐式转换可以产生二义性

	```cpp
	void display(long a){}; //dispaly_l
	void display(double a){};//dispaly_d
	
	display(10); //这么写会报错, 因为10不确定是转成long还是double
	``` 
	
* 本质: 采用name mangling(压碎)或者叫name decoration(装饰)技术.c++编译器默认会对符号名(变量名,函数名等)惊醒改变,修饰,重载时会生成多个不同的函数名,不同的编译器(MSVC,g++)有不同的生成规则.通过IDA禁止优化可以看到.

<a id="extern C"></a>

### extern "C"

* 被extern "C" 修饰的代码会按照c语言的方式去编译

	```cpp
	下面这中写法会报错,因为c语言不支持函数重载
	extern "C" void func(){}
	extern "C" void func(int age){}
	```

* c/c++混合开发时,c++在调用c语言api时,需要使用extern "C"修饰C语言的函数声明
	
	```c
	sum.h
	#ifndef __SUM_H
	#define __SUM_H
	int sum(int a,int b);
	#endif
	
	sum.c
	int sum(int a,int b){
		return a+b;
	}	
	
	main.cpp
	extern "C" {
		#include "sum.h"
	}
	int main(){
		sum(10,20);
		return 0;
	}
	```

* 有时候也会在Cyuyan代码中直接使用extern "C",这样就可以直接被c++调用,通过`__cplusplus`来区分c/c++环境

	```c
	sum.h
	#ifndef __SUM_H
	#define __SUM_H
	
	#ifdef __cplusplus
	extern "C" {
	#endif
	int sum(int a,int b);
	#ifdef __cplusplus
	}
	#endif
	
	#endif
	
	main.cpp
	#include "sum.h"
	```

<a id="默认参数"></a>

### 默认参数

* c++允许函数设置默认参数,在调用时可以根据情况省略实参.
* 默认参数只能按照右到左的顺序
* 如果函数同事又声明,实现,默认参数只能放在函数声明中
* 默认参数的值可以是常量,全局符号(全局变量,函数名)

```cpp
int age = 33;
void test(){}
void display(int a=11,int b=22,int c= age,void(*func)()=test){
	cout<<a<<endl;
	cout<<b<<endl;
	cout<<c<<endl;
	func();
}
int main(){
	display();
	reutrn 0;
}
```

* 函数重载,默认参数可能产生冲突,二义性(建议先选择使用默认参数)

	```cpp
	void display(int a,int b=20){}
	void display(int a){}
	
	int main(){
		//报错,会产生二义性
		display(10);
		return 0;
	}
	```

<a id="内联函数"></a>

### 内联函数

* 使用inline修饰函数的声明或实现,可以使其变成内联函数,建议声明和实现都增加inline修饰
* 特点: 编译器会将函数调用直接展开为函数体代码,可以减少函数调用的开销.会增大代码体积
* 注意: 尽量不要内联超过10行代码的函数,有些函数计时声明为inline,也不一定会被编译器内联,比如递归函数(内联将函数体拿过来,一直拿死循环,inline只是一个建议性的)
* 函数与宏:
	* 内联函数和宏都可以减少函数调用的开销
	* 对比宏,内联函数多了语法检测和函数特性(传参,赋值)

<a id="#pragma once"></a>
	
### #pragma once

* 我们经常使用#ifndef,#define,#endif来防止头文件的内容被重复包含
* `#pragma once`可以防止整个文件的内容被重复包含
* 区别: #ifndef,#define,#endif受吃c\c++标准的支持,不受编译器的任何限制,还可以针对一个文件中的部分代码. 有些编译器不支持`#pragma once`.

<a id="引用"></a>

### 引用(Reference)

* 在c语言中,使用指针可以间接获取,修改某个变量的值
* 在c++中,使用引用可以起到跟指针类似的功能

	```cpp
	int age = 20;
	//rage就是一个引用
	int &rage = age;
	```
	
* 注意点: 
	* 引用相当于是变量的别名(基本数据类型,枚举,结构体,类,指针,数组等都可以有引用)
	* 对引用做计算,就是对引用所指向的变量做计算
	* 在定义的时候必须初始化,一旦指向了某个变量,就不可以改变,'从一而终'
	* 可以利用引用初始化另一个引用,相当于某个变量的多个别名
	* 不存在引用的引用,指向引用的指针,引用数组
* 引用存在的价值之一: 比指针更安全(从一而终,一旦指向,不可改变.指针可以乱指向),函数返回值可以被赋值

```cpp
int age = 10;
int &func(){
	age = ....;
	return age;
}
func() = 30; //可以赋值.age是全局变量

void swap(int &a,int &b){
	int tmp = a;
	b = a;
	a = tmp;
}
```

<a id="const"></a>

### const

* const 是常量的意思,被修饰的变量不可修改,如果修饰额是类,结构体(的指针),其成员也不可以更改
* const 修改的是其右边的内容

	```cpp
	int age = 10;
	const int * p0 = &age; //*p0是常量,p0不是常量.*p0=20(错误).p0 =   &...   *p0不能修改,p0能修改
	int const *p1 = &age; //*p0是常量,p0不是常量
	int * const p2 = &age; //p2常量,*p2不是可以通过*p2修改值
	const int * const p3 = &age;//p3,*p3都是常量
	int const * const p4 = &age;//p4,*p4都是常量
	```
	
<a id="常引用"></a>

### 常引用
	
* 引用可以被const修饰,这样就无法通过引用修改数据,可以成为常引用
* const必须写在&符号的左边,才能算是长引用
* const引用的特点:
	* 可以指向临沭数据(常量,表达式,函数返回值)
		
		```cpp
		int age = 10;
		int a = 10;
		int b = 20;
		const int &rAge = 40; //可以这样写
		int &rAge = 40;//写法错误,如果可以这么写那rAge=50;就是把50赋值给40 不成立
		
		const &rAge = a + b; //可以这么些. const表示不可改变之后
		
		const double &double = age; //可以证明写const表示不可改变之后
		```
	* 作为函数参数时 (此规则也适用于const指针)
		* 可以接受const和非const实参(非const引用只能接受非const实参)
		
		```cpp
		//可以接受const,非const参数
		int sum(cosnt int &a,int &b){
			return a+b;
		}
		```
		* 可以跟非const引用构成重载,如果去掉引用则不构成重载

* 当常引用指向了不同类型的数据时,会产生临时变量,即引用指向的并不是初始化时的那个变量

```cpp
int age = 10;
const int &rAge = age;
age = 30;

cout << age << endl;
cout << rage << endl;

打印出来两个30. 因为引用的本质是指针,rAge指向age的地址,age=30后age地址存放的值是30.
```

<a id="数组的引用"></a>

### 数组的引用

```cpp
int array[] = {10,20,30};
int (&ref1)[3] = array;
//加const是来限制ref2=100类似这种错误的赋值
int * const &ref2 = array;
```
 
<a id="程序的本质"></a>

### 程序的本质 扫盲

程序/软件先是安装在硬盘,打开的时候装载到内存中,cpu去读和写内存以及控制显示器,印象等设备.cpu包括寄存器,运算器,控制器.运算器是加减乘除等操作.操作时候比如a+b,会先将a的值取到寄存器,再将寄存器的值和b地址的值相加赋值给寄存器.为什么?因为运算器从寄存器取值比从内存中取值快.控制器就是控制设备的.

<a id="x86_64 简单基础"></a>

### x86_64 简单基础 扫盲

一个cpu有很多寄存器

64 bit寄存器: RAX,RBX,RCX,RDX,RBP,RSI,RDI,R8,R0,R10,R11,R12,R13,R14,R15

32 bit寄存器: EAX,EBX....

但一个cpu只有一个RAX

64位一个寄存器有8字节,32为4字节.X64是兼容x86的,所以RAX寄存器会拿出来一半(低四位)的字节来给EAX用

```
mov dest,src  将src的内容赋值给dest
mov eax, [0132423432H]从这个地址取4个字节给结存器eax,eax省略4字节,代表16进制

[地址值] 中括号[]里面放的都是内存地址

word是2字节,dword是4字节(double word),qward是8字节(quad word)

call 函数地址

lea dest, [地址值] 将地址值给dest
lea eax,[0132423432H] 将0132423432H地址值给eax,eax=0132423432H
mov是取地址对应存储空间给dest,lea是直接将地址给dest

ret 函数返回

xor op1,op2
xor是异或,将op1和op2异或的结果赋值给op1，类似于op1 = op1 ^ op2
 
add op1,op2 类似于op1 = op1+op2

sub op1,op2 类似于op1=op1-op2

inc op 类似op=op+1

dec op 类似于op=op-1

jmp 内存地址 
跳到摸个内存地址取执行代码,类似goto语句.
j开头的一般都是跳转,大多是待条件的跳转,一般跟test、cmp等指令配合使用
jmp 0132423432H 无条件的跳转
jz 0132423432H/jn 0132423432H 有条件的跳转

cmp eax,ebx  比较这两个寄存器的值是否相等
jz 0132423432H 如果比较相等跳转过去,不相等继续执行
```

<a id="引用的本质"></a>
	
### 引用的本质

* 引用的本质就是指针,只是编译器削弱了他的功能,所以引用就是弱化了的指针.
* 一个引用占用一个指针的大小

<a id="面向对象"></a>

## 面向对象

<a id="类"></a>

### 类

* c++中可以使用struct,class来定义一个类
* struct和class的区别
	* struct的默认成员权限是public
	* class的默认权限是private
* 反汇编struct和class完全相同
* c++编程规范,没有特殊规定的话建议写法
	* 全局变量: g_
	* 成员变量: m_
	* 静态变量: s_
	* 常量: c_
	* 使用驼峰标识

<a id="this"></a>

### this

* this是指向当前对象的指针,this->..访问成员变量
* 对象在调用成员函数的时候,会自动传入当前对象的内存地址


<a id="封装"></a>

### 封装

成员变量私有化,提供公共的getter和setter给外界去访问成员变量

```cpp
struct Person{
private:
    int m_age;
public:
    void setAge(int age){
        this->m_age = age;
    }
    int getAge(){
        return this->m_age;
    }
};

Person person;
person.setAge(20);
cout << person.getAge() << endl;
```




<a id="内存空间的布局"></a>

### 内存空间的布局

每个应用都有自己独立的内存空间,其内存空间一般都有一下几大区域

* 代码段(代码区), 用于存放代码
* 数据段(全局区), 用于存放全局变量等
* 栈空间, 每调用一个函数就会给他分配一段连续的栈空间,等函数调用完毕后会自动回收这段栈空间. 是自动分配和回收
	* 栈空间是从高到低分布,为什么呢?
		* 惯例, 以前单进程的操作系统时候,可以最大化共享内存,不用事先给栈一个深度
		* 程序大小是固定的,加载程序的时候分配内存是从低到高分配的.如果栈也是从高到低分布,则程序大小就不会固定
	* 堆栈平衡: 堆栈平衡就是指栈平衡.程序经过编译连接,高级语言中的一个语句转成一段汇编代码.而这段汇编代码执行前后,esp,ebp应该保持不变.也就是说每个子程序调用前后(函数调用前后)esp,ebp不应该改变,才能让一段代码的执行不影响到以前各次调用的返回地址,从而保证整个程序的正确运行.具体例子方面可以参见[https://bbs.pediy.com/thread-106551.htm](https://bbs.pediy.com/thread-106551.htm)
		* esp 栈指针寄存器,保存函数调用栈中栈顶地址,这个地址随着push,pop而改变
		* ebp 基址指针寄存器,保存函数栈中栈底地址.
* 堆空间, 需要主动去申请和释放

```cpp
malloc \ free
new \ delete
new[] \delete[]
```
* 堆空间的初始化

```cpp
int *p1 = (int *)malloc(sizeof(int)); //*p1未初始化
int *p2 = (int *)malloc(sizeof(int));
memset(p2,0,sizeof(int));//将*p2的每一个字节都初始化为0

int *p1 = new int; //未初始化
int *p2 = new int(); // 初始化为0
int *p3 = new int(5); //被初始为5
int *p4 = new int[3]; //数组元素未被初始化
int *p5 = new int[3](); //3个数组元素都被初始化为0
int *p6 = new int[3]{}; //3个数组元素都被初始化为0
int *p7 = new int[3]{5};//数组首元素被初始化为5,其他初始化0
```

* memset函数时将较大的数据结构(比如对象,数组等)内存清零的比较快的方法

```cpp
Person person;
person.m_id = 1;
person.m_age = 20;
person.m_height = 180;
memset(&person,0,sizeof(person));

Person persons[] = {{1,20,180},{2,25,165},{3,27,170}};
memset(persons,0,sizeof(persons));
```

<a id="对象的内存"></a>

### 对象的内存

对象的内存可以在3中地方

* 全局区(数据段): 全局变量
* 栈空间: 函数里面的局部变量
* 堆空间: 动态申请内存(malloc,new等)

```cpp
// 全局区
Person g_person;
int main(){
	//栈空间
	Person person;
	
	//堆空间
	Person *p = new Person;
	return 0;
}
```

<a id="构造函数"></a>

### 构造函数(Constructor)

* 构造函数(构造器),在对象创建的时候自动调用.一般用于初始化操作
* 特点:
	* 函数名与类同名,无返回值(void都不能写),可以有参数,可以重载,可以有多个构造函数
	* 一旦自定义了构造函数,必须用其中一个自定义的构造函数来初始化对象
* 注意: 通过malloc分配的对象不会调用构造函数
* 一个错误结论: 编译器回味每一个类生成空的无参的构造函数.

```cpp
class Person{
	
};
这个类就不会生成构造函数.这个类什么都没有.可以在window的vs转为反汇编查看汇编可知. 比如这个类什么都没有,那么在有的编译器中他占用一个字节
```

<a id="构造函数的调用"></a>

### 构造函数的调用
	
```cpp
struct Person{
	int m_age;
	Person(){
		cout << "Person()" << endl;
	}
	Person(int age){
		cout << "Person(int age)" << endl;
	}
}

//全局区
Person g_p1; //调用Person()
Person g_p2; //这是一个函数声明,函数名叫g_p2
Person g_p3; //调用Person(int)

int main(){
	//栈空间
	Person p1; //调用Person()
	Person p2(); //这是一个函数声明,函数名为p2
	Person p3{20};//调用Person(int)
	
	//堆空间
	Person *p4 = new Person; //调用Person()
	Person *p5 = new Person(); //调用Person()
	Person *p6 = new Person(20);//调用Person(20)
	return 0;
}
```	

<a id="成员变量的初始化"></a>

### 成员变量的初始化

#### 默认情况下

```cpp
struct Person{
	int m_age;
}

//全局区(成员变量初始化为0)
Person g_p1;

int main(){
	//栈空间(成员变量不回被初始化)
	Person p1;
	
	//堆空间
	Person *p2 = new Person; //成员变量不会被初始化
	Person *p3 = new Person(); //成员变量被初始化为0
	Person *p4 = new Person[3]; //成员变量不回被初始化
	Person *p5 = new Person[3](); //3个Person对象的成员变量都初始化为0
	Person *p6 = new Person[3]{};//3个Person对象的成员变量都初始化为0
	return 0;
}
```

#### 成员变量的初始化
	
```cpp
Person(){
	memset(this,0,sizeof(Person));
}
```

<a id="析构函数"></a>
	
### 析构函数

* 析构函数,子啊对象销毁的时候自动调用,一般用于完成对象的清理工作
* 函数名以~开头,与类名相同,无返回值(void都不能写),无参,不可以重载,有且只有一个析构函数
* 通过malloc分配的对象free的的时候不会调用构造函数
* 构造函数,析构函数要声明为public,才能被外界正常使用

<a id="strcpy过期问题解决"></a>

### strcpy过期问题解决

![](https://github.com/longpf/Resource/blob/master/img/strcpy_outdate_issue.png?raw=true)
	
	
<a id="声明和实现分离"></a>	

### 声明和实现分离

```cpp
Person.h
#prama once
class Person{
private:
	int m_age;
public:
	void setAge(int age);
	int getAge();
	Person();
	~Person();
}

Person.cpp
#include "Person.h"

Person::Person(){

}

void Person::setAge(int age){
	this->m_age = age;
}

int Person::getAge(){
	return this->m_age;
}

Person::~Person(){

}
```
	
<a id="命名空间"></a>
	
### 命名空间

* 命名空间可以用来避免命名冲突

```cpp
namespace MJ{
	int g_age;
	
	class Person{
	
	};
	
	void test(){
	
	}
}

int main(){
	MJ::g_age = 20;
	MJ::Person *p = new MJ::Person();
	MJ::test();
	return 0;
}

或

using namespace MJ;

g_age = 20;
Person *p = new Person();
test();


using MJ::g_age;
g_age = 20;
```

* 命名空间不影响内存布局
	
* 下面的代码编译不过,有二义性

```cpp
namespace MJ {
    int g_age;
}

namespace FX {
    int g_age;
}

using namespace MJ;
using namespace FX;

g_age = 20;
```
	
<a id="命名空间的嵌套"></a>

### 命名空间的嵌套

```cpp
namespace MJ{
	namespace SS {
		int g_age;
	}
}

int main(){
	MJ::SS::g_age = 10;
	
	using namespace MJ::SS;
	g_age = 20;
	
	using MJ::SS::g_age;
	g_age = 30;
	return 0;
}
```
		
* 有个默认的全局命名空间,我们创建的命名空间默认都嵌套在他里面

```cpp
int g_no;

namespace MJ{
	namespace SS{
		int g_age;
	}
}

int main(){
	::g_no = 20;
	
	::MJ::SS::g_age = 30;
	return 0;
}
```

<id a="命名空间的合并"></a>

### 命名空间的合并

* 下面的2中写法是等价的

```cpp
namespace MJ {
	int g_age;
}

namespace MJ{
	int g_no;
}

namespace MJ{
	int g_age;
	int g_no;
}
```
	
```cpp
Person.h
#prama once
namespace MJ{
	class Person{
	public:
		Person();
		~Person();
	};
}

Person.cpp
#include "Person.h"
namespace MJ{
	Person::Person(){
	}
	
	Person::~Person(){
	}
}
```

<a id="继承"></a>
	
### 继承

* 继承可以让子类拥有父类的所有成员
* 内存布局的时候是父类的成员变量在前,子类的成员边量在后
* 成员访问权限
	* public: 公共的(struct默认的)
	* protected: 当前类和子类内部可以访问
	* private: 私有的,只有当前类的内部可以访问.(class默认)
	* 这3个关键字既可以用来修饰成员变量,成员函数又可以在继承的时候来修饰
* 子类内部访问父类的成员的权限,是一下2项中权限最小的那个
	* 成员本身的访问权限
	* 上一级父类的继承方式
* 开发中用的最多的继承方式是public
* 访问权限不影响对象的内存布局

<a id="初始化列表"></a>

### 初始化列表 

* 只能用在构造函数中
* 初始化顺序只跟成员变量的声明顺序有关

```cpp
初始化的时候会先初始化m_age,在去初始化m_height
struct Person{
    int m_age;
    int m_height;
    Person(int age,int height):m_height(height),m_age(age){
        
    }
    void des(){
        cout << "m_age = " << m_age << " ,m_height = " << m_height << endl;
    }
};
```

* 下面的写法等价

```cpp
struct Person{
	int m_age;
	int m_height;
	Person(int age,int height):m_age(age),m_height(height){
	
	}
}

struct Person{
	int m_age;
	int m_height;
	Person(int age,int height){
		this->m_age = age;
		this->m_height = height;
	}
}
```

<a id="构造函数的相互调用"></a>

### 构造函数的相互调用

* 构造函数调用其他构造函数值能放在初始化列表中

```cpp
struct Person {
	int m_age;
	int m_height;
	Perosn(): Person(0,0){}
	Person(int age,int height):m_age(age),m_height(height);
};
```

<a id="初始化列表与默认参数配合使用"></a>

### 初始化列表与默认参数配合使用

```cpp
class Person {
	int m_age;
	int m_height;
public:
	Person(int age=0,int height=0):m_age(age),m_height(height){
	}
};

int main(){
	Person person1;
	Person Person2(20);
	Person Person3(20,180);
	return 0;
}
```

* 如果函数声明和实现是分离的
	* 初始化列表只能写在函数的实现中
	* 默认参数只能写在函数的声明中
	
<a id="父类的构造函数"></a>

### 父类的构造函数

* 子类的构造函数默认会先调用父类的无参构造函数,在调用奔雷的构造函数
* 如果子类的构造函数显示的调用父类的有参构造函数,就不会调用默认的无参的构造函数
* 如果父类缺少无参构造函数,子类的构造函数必须显式调用父类有参构造函数

<a id="继承体系下的构造函数示例"></a>

### 继承体系下的构造函数示例

```cpp
struct Person{
    int m_age;
    Person(): Person(0){
    }
    Person(int age):m_age(age){
    }
};

struct Student: Person{
    int m_no;
    Student():Student(0,0){}
    Student(int age,int no):Person(age),m_no(no){
    }
};
```

<a id="构造,析构顺序"></a>

### 构造,析构顺序

* 构造和析构顺序相反

```cpp
struct Person{
    Person(){
        cout << "Perosn()" << endl;
    }
    ~Person(){
        cout << "~Person()" << endl;
    }
};

struct Student : Person{
    Student(){
        cout << "Student()" << endl;
    }
    ~Student(){
        cout << "~Student()" << endl;
    }
};

输出结果为:
Perosn()
Student()
~Student()
~Person()
```

<a id="父类指针,子类指针"></a>
	
### 父类指针,子类指针

* 父类指针可以指向子类对象,是安全的,开发中经常遇到(继承方式必须是public)
* 子类指针指向父类对象是不安全的

<a id="多态"></a>

### 多态

* 默认情况下,编译器只会根据指针类型调用对应的函数,不存在多态
* 多态是面向对象非常重要的一个特性
	* 同一个操作作用于不同的对象,可以有不同的解释,产生不同的执行结果
	* 在运行时,可以识别出真正的对象类型,调用对应子类中的函数
* 多态的要素
	* 子类重写父类的成员函数(override)
	* 父类指针指向子类对象
	* 利用父类指针调用重写的成员函数


<a id="虚函数"></a>

### 虚函数

* c++中的多态通过虚函数来实现
* 虚函数: 被virtual修饰的成员函数
* 只要在父类中声明为虚函数,子类中重写的函数也自动变成虚函数(也就是说子类中可以省略virtual关键字)

<a id="虚表"></a>

### 虚表

* 虚函数的实现原理是虚表,这个虚表里面存储着最终需要调用的虚函数地址,这个虚表也叫虚函数表

```cpp
class Animal{
public:
    int m_age;
    virtual void speak(){
        cout << "Animal::speak()" << endl;
    }
    virtual void run(){
        cout << "Animal::run()" << endl;
    }
};

class Cat: public Animal{
public:
    int m_life;
    void speak(){
        cout << "Cat::speak()" << endl;
    }
    void run(){
        cout << "Cat::run()" << endl;
    }
};

Animal *cat = new Cat();
cat->m_age = 20;
cat->speak();
cat->run();
```

* x86环境的图

![](https://github.com/longpf/Resource/blob/master/img/xubiao_x86_example.png?raw=true)

* 所有的Cat对象,不管在全局区,栈,堆公用一份虚表

<a id="虚表汇编分析"></a>

### 虚表汇编分析

```x86asm
// 调用Cat::speak
// 取出cat指针变量里面存储的地址值
// eax里面存放的是Cat对象的地址值
mov		eax,dword ptr [cat]
// 取出Cat对象的前面4个字节给edx
// edx里面存储的是虚表的地址
mov 	edx,dword ptr [eax]
// 取出虚表中的前4个字节个eax
// eax存放的就是Cat::speak的函数地址
mov		eax,dword ptr [edx]
call 	eax
```

```x86asm
// 调用Cat::run
// 取出cat指针变量里面存储的地址值
// eax里面存放的是Cat对象的地址值
mov		eax,dword ptr [cat]
// 取出Cat对象的前4个字节给edx
// edx里面存储的是虚表的地址
mov		edx,dword ptr [eax]
// 取出虚表中第5-8个字节(run函数地址)给eax
// eax存放的就是Cat::run的函数地址
mov		eax,dword ptr [edx+4]
call	eax
```

<a id="虚析构函数"></a>

### 虚析构函数

* 含有虚函数的类,应该将析构函数声明为虚函数(虚析构函数)
* delete父类指针时,参会调用子类的析构函数,保证析构的完整性

```cpp
class Person{
public:
    virtual void run(){
        cout << "Person::run()" << endl;
    }
    //如果不声明virtual 那么Person s = new Student();delete  s;这种情况下不调用Student的析构函数
    virtual ~Person(){
        cout << "Person::~Person()" << endl;
    }
};

class Student: public Person{
public:
    void run(){
        cout << "Student::run()" << endl;
    }
    ~Student(){
        cout << "Student::~Student()" << endl;
    }
};
```

<a id="纯虚函数"></a>

### 纯虚函数

* 没有函数体且初始化为0的虚函数,用来定义接口规范
* 类似java中接口,抽象类.类似oc中的协议protocol
* 抽象类
	* 含有纯虚函数的类,不可以实例化(不可以创建对象)
	* 抽象类也可以包含非纯虚函数
	* 如果父类是抽象类,子类没有完全实现纯虚函数,那么这个子类依然是抽象类

```cpp
class Animal{
    virtual void speak() = 0;
    virtual void run() = 0;
};
class Cat: public Animal{
public:
    void run(){
        cout << "Cat::run()" << endl;
    }
};
class WhiteCat: public Cat{
public:
    void speak(){
        cout << "WhiteCat::speak()" << endl;
    }
    void run(){
        cout << "WhiteCat::run()" << endl;
    }
};
```

<a id="多继承"></a>

### 多继承

c++允许一个类可以有多个父类(不建议使用会增加程序设计复杂度)

![](https://github.com/longpf/Resource/blob/master/img/duojicheng.png?raw=true)

<a id="多继承体系下的构造函数调用"></a>

### 多继承体系下的构造函数调用

```cpp
class Student{
    int m_score;
public:
    Student(int score){
        this->m_score = score;
    }
};

class Worker{
    int m_salary;
public:
    Worker(int salary){
        this->m_salary = salary;
    }
};

class Undergraduate: public Student, public Worker{
public:
    Undergraduate(int score,int salary): Student(score),Worker(salary){
    }
};
```

<a id="多继承-虚函数"></a>

### 多继承-虚函数

* 如果子类继承的多个父类都有虚函数,那么子类对象就会产生对应的多张虚表

![](https://github.com/longpf/Resource/blob/master/img/duojicheng_xuhanshu.png?raw=true)

<a id="多继承的同名函数和同名变量"></a>

### 多继承的同名函数和同名变量

#### 同名函数

```cpp
class Student {
public:
    void eat(){
        cout << "Student::eat()" << endl;
    }
};

class Worker{
public:
    void eat(){
        cout << "Worker::eat()" << endl;
    }
};

class Undergraduate: public Student,public Worker{
public:
    void eat(){
        cout << "Undergraduate::eat()" << endl;
    }
};

Undergraduate ug;
ug.Student::eat(); //Student::eat()
ug.Worker::eat();  //Worker::eat()
ug.Undergraduate::eat();//Undergraduate::eat()
ug.eat();       //Undergraduate::eat()
```

#### 同名成员变量

![](https://github.com/longpf/Resource/blob/master/img/duojicheng_tongmingbianliang.png?raw=true)

<a id="菱形继承"></a>

### 菱形继承

* 菱形继承带来的问题:
	* 最底下子类从街垒继承的成员变量冗余,重复
	* 最底下子类无法访问基类的成员,二义性

<div align="center">
<img src="https://github.com/longpf/Resource/blob/master/img/lingxingjicheng.png?raw=true" width="240" height="280">
</div>

* 内存分布

![](https://github.com/longpf/Resource/blob/master/img/lingxingjicheng2.png?raw=true)



<a id="虚继承"></a>

### 虚继承

* 虚继承可以解决菱形继承带来的问题
* Person类可以称为虚基类

<div align="center">
<img src="https://github.com/longpf/Resource/blob/master/img/xujicheng.png?raw=true" width="240" height="280">
</div>

* 虚继承的内存分布

![](https://github.com/longpf/Resource/blob/master/img/xujicheng_neicunfenbu.png?raw=true)

### 静态成员

* 静态成员: 被static修饰的成员\函数
* 可以通过对象(对象.静态成员),对象指针(对象指针->静态成员),类访问(类名::成员变量)
* 静态成员变量:
	* 存储在数据段(全局区,类似于全局变量),整个程序运行过程中只有一份内存
	* 对比全局变量,他可以设定访问权限(public,protected,private)达到局部共享的目的
	* 必须初始化,必须在类外面初始化,初始化时不能带static,如果类的声明和实现分离(在实现.cpp中初始化)
* 静态函数
	* 内部不能使用this指针(this指针只能在非静态成员变量函数内部)
	* 不能是虚函数(虚函数只能是非静态成员函数)
	* 函数内部不能访问非静态成员变量\函数,只能访问静态成员变量\函数
	* 非静态成员函数可以访问静态成员变量\函数
	* 构造函数,析构函数不能是静态的(是静态就不能访问成员变量)
	* 当声明和实现分离时,实现部分不能带static
	
```cpp
class Car {
    int m_price;
    static int ms_count;
public:
    static int getCount(){
        return ms_count;
    }
    Car(int price=0) :m_price(price){
        ms_count++;
    }
    ~Car(){
        ms_count--;
    }
};
int Car::ms_count = 0;
```
	
<a id="静态成员变量经典应用-单例模式"></a>
	
### 静态成员变量经典应用-单例模式

```cpp
class Rocket {
public:
    //c++的静态成员函数类似java,oc的类方法
    static Rocket *shareRocket(){
        if (ms_instance==NULL) {
            ms_instance = new Rocket();
        }
        return ms_instance;
    };
private:
    Rocket() {}; // 不让外界调用构造
    Rocket(const Rocket &rocket) {};// 禁止外界调用拷贝构造
    static Rocket* ms_instance;
    void &operator=(const Rocket &rocket){}// 运算符重载禁止外界进行等号赋值
};
Rocket *Rocket::ms_instance = NULL;
```
	
<a id="const 成员"></a>
	
### const 成员

* const成员: 被const修饰的成员变量,非静态成员函数
* const成员变量:
	* 必须初始化(类内部初始化),可以在声明的时候直接初始化赋值
	* 非static的const成员变量还可以在初始化列表中初始化
* const成员函数(非静态)
	* const关键字写在参数列表后面,函数的声明和实现都必须带const
	* 内部不能修改费static成员变量
	* 内部只能调用const 成员函数，static成员函数
	* 非const成员函数可以调用const成员函数
	* const成员函数和非const成员函数构成重载
	* 非const对象(指针)优先调用非const成员函数
	* const对象（指针）只能调用const成员函数，static成员函数

	
<a id="引用类型成员"></a>
	
### 引用类型成员

* 引用类型成员变量必须初始化(不考虑static情况)
	* 在声明的时候直接初始化
	* 通过初始化列表初始化

```cpp
class Car{
    int age;
    int &m_price = age;
public:
    Car(int &price):m_price(price){}
};
```
		
<a id="拷贝构造函数"></a>

### 拷贝构造函数

* 拷贝构造函数时构造函数的一种
* 当利用已存在的对象创建一个新对象时(类似于拷贝),就会调用新对象的拷贝构造函数进行初始化
* 拷贝构造函数的格式是固定的,接受一个const引用作为参数

```cpp
//浅拷贝: 指针类型仅仅是拷贝地址值
//深拷贝: 拷贝d内容到新申请的内存空间

class Car{
    int m_price;
    char *m_name;
public:
    Car(int price=0,const char *name = NULL) : m_price(price){
        if (name==NULL) {
            m_name = NULL; //防止m_name指向乱七八糟的数据
            return;
        }
        // 申请堆空间储存字符串内容
        this->m_name = new char[strlen(name)+1]{};
        // 拷贝字符串内容到堆空间
        strcpy(this->m_name, name);
    }
    
    Car(const Car &car): m_price(car.m_price){
        if (car.m_name==NULL) return;
        //申请堆空间存储字符串内容
        this->m_name = new char[strlen(car.m_name)+1]{};
        strcpy(this->m_name, car.m_name);
    }
    ~Car(){
        if (this->m_name==NULL) return;
        delete [] this->m_name;
        this->m_name = NULL;
    }
};

Car car1(100,"bmw");
//下面两个都是拷贝构造函数,用已有的对象来创建新对象
Car car2 = car1;
Car car3(car1);
Car car4;
//这么写有问题,这个是浅赋值,就是car3的值拷贝到car4,m_name指向通一个堆空间,析构的时候m_name会被释放两次
car4 = car3;
```

<a id="调用父类的拷贝构造函数"></a>

### 调用父类的拷贝构造函数

```cpp
class Person{
    int m_age;
public:
    Person(int age): m_age(age){}
    Person(const Person &person): m_age(person.m_age){}
};

class Student: public Person{
    int m_score;
public:
    Student(int age, int score): Person(age),m_score(score){}
    Student(const Student &student): Person(student), m_score(student.m_score){}
};
```

<a id="浅拷贝,深拷贝"></a>

### 浅拷贝,深拷贝

* 编译器默认的提供的拷贝是浅拷贝
	* 将一个对象中所有成员变量的值拷贝到另一个对象
	* 如果某个成员变量是个指针,只会拷贝指针中储存的地址值,并不糊拷贝指针指向的内存空间
	* 可能会导致对空间多次free的情况
* 如果需要实现深拷贝,就需要自定义拷贝构造函数
	* 将指针类型的成员变量所指向的内存空间,拷贝到新的内存空间
	
<a id="对象型参数和返回值"></a>

### 对象型参数和返回值

* 使用对象类型作为函数的参数或返回值, 可能会产生一些不必要的中间对象
	
```cpp
class Car{
    int m_price;
public:
    Car(){}
    Car(int price): m_price(price){ }
    Car(const Car&car):m_price(car.m_price){}
};
//会调用拷贝构造,不回改原始传进来的对象
void test1(Car car){
}
//可以改传进来的car
void test2(Car &car){
}
Car test3(){
    Car car(20);
    return car;
}
int main(int argc, const char * argv[]) {
    //会调用一次构造,一次拷贝构造,
    //对象作为返回值会调用一次对象的拷贝构造,因为test3函数产生的对象是在test3的函数栈里面.
    //如果返回给外部用会不安全,所以返回的时候会调用一次拷贝构造,拷贝构造的空间在main函数的栈空间. 
    //这里只是做了优化,用test3()创建一个新的对象,只调用了一次拷贝构造
    Car car1 = test3();
    // 会调用两次构造,一次拷贝狗仔
    Car car2 ;
    car2 = test3();
}
```

### 匿名对象(临时对象)

* 匿名对象: 没有变量名,没有被指针指向的对象,用完后马上调用析构

```cpp
Car(10); //创建后就被释放
Car(10).dispaly(); //调用玩display函数后就被释放
```

* 有时候编译器对匿名对象有优化,比如匿名对象作为参数,作为返回值,如:

```cpp
test1(Person());
```

<a id="隐式构造"></a>

### 隐式构造

* c++中存在隐式构造的现象: 某些情况下,会隐式调用单参数的构造函数

```cpp
class Person {
    int m_age;
public:
    Person()  {
        cout << "Person() - " << this << endl;
    }
    //explicit关键字会禁止隐式的构造函数,加上之后Person = 20;会编译不过
    explicit Person(int age) :m_age(age) {
        cout << "Person(int) - " << this << endl;
    }
    Person(const Person &person) {
        cout << "Person(const Person &person) - " << this << endl;
    }
    ~Person() {
        cout << "~Person() - " << this << endl;
    }
    void display() {
        cout << "display() - age is " << this->m_age << endl;
    }
};
void test1(Person person) {
}
//返回值会调构造函数
Person test2() {
    return 30;
}
int main(){
	
	Person p = 20; //会调用单参数的构造函数
	
	return 0;
}
```

<a id="编译器自动生成的构造函数"></a>
	
### 编译器自动生成的构造函数

* c++的编译器在某些特定的情况下,会给类自动生成无参的构造函数,比如
	* 成员变量在声明的同事进行了初始化
	
	 ```cpp
	 class Person {
	  public:
		  int m_age = 10;
	  };
	 ```
	* 有定义虚函数,因为初始化后需要向对象前4字节(32位)放虚表地址
	* 虚继承了其他类,因为虚继承对象头部会多出来虚表指针
	* 包含了对象类型的成员,	且这个成员会有构造函数.这时候会调用对象成员变量的构造函数
	* 父类有构造函数

* 总结: 对象创建后,需要做一些额外的操作时(比如内存操作操作,函数调用),编译器一般都会为其自动生成无参的构造函数
	
<a id="友元"></a>

### 友元

* 友元抱愧友元函数和友元类
* 如果将函数A(非成员函数)声明为类C的友元函数,那么函数A就能直接访问C对象的所有成员(成员函数,成员变量)
* 如果将类A声明为类C的友元类,那么类A的所有成员函数都能直接访问类C对象的所有成员
* 友元函数破坏了面向对象的封装性,但在某些频繁访问成员变量的地方可以提高性能
	
```cpp
class Point{
    friend Point add(const Point&,const Point &);
    friend class Math;
private:
    int m_x;
    int m_y;
    void foo(){}
public:
    Point(){}
    Point(int x,int y):m_x(x),m_y(y){}
};

Point add(const Point&p1,const Point &p2){
    return Point(p1.m_x+p2.m_x,p1.m_y+p2.m_y);
}

class Math{
    void test(){
        Point point;
        point.m_x = 10;
        point.m_y = 20;
    }
    static void test2(){
        Point point;
        point.m_x = 10;
        point.m_y = 20;
    }
};
```	

<a id="内部类"></a>

### 内部类

* 内部类的特点
	* 支持public,protected,private权限
	* 成员函数可以直接访问其外部类对象的所有成员(返过来则不行)
	* 成员函数可以直接不带类名,对象名访问其外部类的static成员
	* 不回影响外部类的内存布局
	* 可以在外部类内部声明,在外部类外面进行定义
	
	
```cpp
class Point{
    static void test1(){
        cout << "Point::test1()" << endl;
    }
    int m_x;
    int m_y;
    static int ms_test2;
public:
    class Math{
    public:
        void test3(){
            cout << "Point::Math::test3()" << endl;
            test1();
            ms_test2 = 10;
            
            Point point;
            point.m_x = 10;
            point.m_y = 20;
        }
    };
};
int Point::ms_test2 = 1;
```

* 声明和实现分开的情况

```cpp
// # 1
class Point {
    class Math{
        void test();
    };
};
void Point::Math::test(){
}

// # 2
class Point{
    class Math;
};
class Point::Math{
    void test(){};
};

// # 3
class Point{
    class Math;
};
class Point::Math{
    void test();
};
void Point::Math::test(){}
```

<a id="局部类"></a>

### 局部类

* 在一个函数内部定义的类,称为局部类
* 局部类的特点
	* 作用域仅限于所在的内部函数
	* 其所有的成员必须定义在类内部,不允许定义static 成员变量
	* 成员函数不能直接访问函数的局部变量(static变量除外)


```cpp
int age = 0;
void test(){
    static int s_age1 = 0;
    int age2 = 0;
    class Point{
        int m_x;
        int m_y;
    public:
        static void display(){
            age = 10;
            s_age1 = 20;
        }
    };
}
```

<a id="其他语法"></a>

## 其他语法

<a id="运算符重载"></a>

### 运算符重载

* 运算符重载(操作符重载): 可以为运算符增加一些新的功能

```cpp
class Point{
public:
    int m_x;
    int m_y;
    Point(int x,int y):m_x(x),m_y(y){}
    Point(const Point&point): m_x(point.m_x),m_y(point.m_y){}
    void display(){
        cout << "x = " << this->m_x << ", y = " << this->m_y << endl;
    }
};

Point operator+(const Point &p1,const Point &p2){
    return Point(p1.m_x+p2.m_x,p1.m_y+p2.m_y);
}

Point p1(10,20);
Point p2(20,30);
// 这么写的本质就是调用operator+这个函数 ,相当于p1.operation+(p2)
Point p3 = p1+p2;
p3.display();
```

<a id="运算符重载-Point"></a>

### 运算符重载-Point

```cpp
// Point.h
#include <iostream>
using namespace std;
class Point{
    // cout << p; 这种对象在运算符右边,p这这里是个参数,则不应写成成员函数,cout其实是ostream的对象
    // 平常可以 cout << 1; 这种是 ostreamz重载了<<运算符
    friend ostream &operator<<(ostream &,const Point&);
    // istream是输入控制,ostream是输出控制, 
    // 还有对比上面少了const,因为这里要改变输入的point
    friend istream &operator>>(istream &,Point &);
    int m_x;
    int m_y;
public:
    Point(int x,int y);
    Point operator+(const Point &point) const;
    Point operator-(const Point &point) const;
    const Point operator-() const; // -p,取反. 两个const的原因是const变量只能调用const函数
    Point &operator+=(const Point &point);
    Point &operator-=(const Point &point);
    bool operator==(const Point &point);
    bool operator!=(const Point &point);
    // 前++
    Point &operator++();
    // 后++ (int)这个语法糖 规定这么写是后++
    const Point operator++(int);
};

// Point.cpp
#include "Point.h"
#include <stdio.h>
Point::Point(int x,int y):m_x(x),m_y(y) {}
Point Point::operator+(const Point &point) const{
    return Point(this->m_x+point.m_x,this->m_y+point.m_y);
}
Point Point::operator-(const Point &point) const{
    return Point(this->m_x-point.m_x,this->m_y-point.m_y);
}
const Point Point::operator-() const {
    return Point(-this->m_x,-this->m_y);
}
// 不加&可能调用拷贝构造,这里返回this,不会被释放,安全
Point &Point::operator+=(const Point &point){
    this->m_x+= point.m_x;
    this->m_y+= point.m_y;
    return *this;//返回的是对象,不是指针
}
Point &Point::operator-=(const Point &point){
    this->m_x -= point.m_x;
    this->m_y -= point.m_y;
    return *this;
}
bool Point::operator==(const Point &point){
    return (this->m_x==point.m_x)&&(this->m_y==point.m_y);
}
bool Point::operator!=(const Point &point){
    return (this->m_x!=point.m_x)||(this->m_y!=point.m_y);
}
// 前++
Point &Point::operator++(){
    this->m_x++;
    this->m_y++;
    return *this;
}
// 后++ 返回一临时变量,调用者++
const Point Point::operator++(int){
    Point point(this->m_x,this->m_y);
    this->m_x++;
    this->m_y++;
    return point;
}
ostream &operator<<(ostream &cout, const Point &point){
    return cout << "(" << point.m_x << ", " << point.m_y << ")";
}

istream &operator>>(istream &cin, Point &point){
    return cin>>point.m_x>>point.m_y;
}
```

<a id="运算符重载-String"></a>

### 运算符重载-String

```cpp
String.h
#pragma once
#include <iostream>
using namespace std;

class String{
    friend ostream &operator<<(ostream &,const String &);
public:
    String();
    String(const char *cstring);
    String(const String &string);
    ~String();
    String &operator=(const char *cstring);
    String &operator=(const String &string);
    String operator+(const char *cstring);
    String operator+(const String &string);
    String &operator+=(const char *cstring);
    String &operator+=(const String &string);
    bool operator>(const char *cstring);
    bool operator>(const String &string);
    char operator[](int index);
private:
    char *m_cstring;
    String &assign(const char *cstring);
    char *join(const char *cstring1,const char *cstring2);
};

String.cpp
#include "String.h"
#include <stdio.h>

String::String():String::String(NULL){
}

String::String(const char *cstring){
    assign(cstring);
}

String::String(const String &string){
    assign(string.m_cstring);
}

String::~String(){
    assign(NULL);
}

String &String::operator=(const char *cstring){
    return assign(cstring);
}

String &String::operator=(const String &string){
    return assign(string.m_cstring);
}

String String::operator+(const char *cstring){
    String str;
    char *newCString = join(this->m_cstring, cstring);
    if (newCString) {
        // 释放旧的堆空间
        str.assign(NULL);
        // 直接指向新开辟的对空间
        str.m_cstring = newCString;
    }
    return str;
}

String String::operator+(const String &string){
    return operator+(string.m_cstring);
}

String &String::operator+=(const char *cstring){
    char *newCString = join(this->m_cstring, cstring);
    if (newCString) {
        this->assign(NULL);
        this->m_cstring = newCString;
    }
    return *this;
}

String &String::operator+=(const String &string){
    return operator+=(string.m_cstring);
}

bool String::operator>(const char *cstring){
    if (!this->m_cstring||!cstring) return 0;
    return strcmp(this->m_cstring, cstring)>0;
}

bool String::operator>(const String &string){
    return operator>(string.m_cstring);
}

char String::operator[](int index){
    if (!this->m_cstring||index<0) return '\0';
    if (index>=strlen(this->m_cstring)) return '\0';
    return this->m_cstring[index];
}

char *String::join(const char *cstring1, const char *cstring2){
    if (!cstring1||!cstring2) return NULL;
    char *newCString = new char[strlen(cstring1)+strlen(cstring2)+1];
    strcat(newCString, cstring1);
    strcat(newCString, cstring2);
    cout << "new[] - " << newCString << endl;
    return newCString;
}

String &String::assign(const char* cstring){
    // 指向一样的堆空间
    if (this->m_cstring==cstring) return *this;
    //释放旧的字符串
    if (this->m_cstring){
        cout << "delete[] - " << this->m_cstring << endl;
        delete [] this->m_cstring;
        this->m_cstring = NULL;
    }
    // 指向新的字符串
    if (cstring){
        cout << "new[] -" << cstring << endl;
        this->m_cstring = new char[strlen(cstring)+1]{};
        strcpy(this->m_cstring, cstring);
    }
    return *this;
}

ostream &operator<<(ostream &cout,const String &string){
    if (!string.m_cstring) return cout;
    return cout << string.m_cstring;
}
```

<a id="调用父类的运算符重载函数"></a>

### 调用父类的运算符重载函数

```cpp
class Person{
    int m_age;
public:
    // 这里其实没必要重载=,以为是成员变量为基本类型. 这里只说明调用父类运算符重载函数
    Person &operator=(const Person &person){
        this->m_age = person.m_age;
        return *this;
    }
};
class Student : public Person{
    int m_score;
public:
    Student &operator=(const Student &student){
        Person::operator=(student);
        this->m_score = student.m_score;
        return *this;
    }
};
```

<a id="仿函数"></a>

### 仿函数

* 仿函数: 将一个对象当做一个函数一样来使用
* 对比普通函数,他作为对象可以保存状态

```cpp
class Sum{
public:
    int operator()(int a,int b){
        return a+b;
    }
};

Sum sum;
sum(10,20);
```

<a id="运算符重载注意点"></a>

### 运算符重载注意点

* 有些运算符不可以被重载,比如:
	* 对象成员访问运算符: `.`
	* 域运算符: `::`
	* 三目运算符: `?:`
	* `sizeof`
* 有些运算符只能重载为成员函数,比如
	* 赋值运算符: `=`
	* 下标运算符: `[]`
	* 函数运算符: `()`
	* 指针访问成员: `->`

<a id="模板\函数模板"></a>

### 模板\函数模板

* 泛型,是一种将类型参数化以达到代码复用的技术,c++中使用模板来实现泛型
* 模板的使用格式如下:
	* `template <typename\class T>`
	* `typename`和`class`是等价的
* 模板没有被使用时,是不会被实例化出来的(就是不会生成对应类型的函数)
* 模板的声明和实现如果分离到.h和.cpp中, 会导致连接错误
* 一般讲模板的声明和实现统一到一个.hpp文件中

```cpp
Swap.hpp
#pragma once
template <class T> void swapValues(T &v1, T &v2) {
	T tmp = v1;
	v1 = v2;
	v2 = tmp;
}
```

* 为什么模板的声明和实现分离会导致链接错误?? 因为如果是Swap.h,Swap.cpp的话.编译的时候main.cpp和Swap.cpp会单独的编译.main.cpp中调用Swap.h的方法,只引用的Swap.h.在编译的时候函数的地址值不是正确的.在link过程会去修正函数地址.因为模板在被使用的时候才会生成对应的参数的函数.所以Swap.cpp单独编译的时候没有对应的参数类型.所以链接过程时,去修正main里面用到的Swap函数调用的话会找不到对应的函数地址

* 多参数模板

```cpp
template <clas T1,class T2>
void display(const T1 &v1,const T2 &v2){
	cout << v1 << endl;
	cout << v2 << endl;
}

display(20,1.7);
```

<a id="类模板"></a>

###  类模板

```cpp
Array.hpp
template <class Item>
class Array{
	// 友元函数这比较特殊需要用一个新的类型, 可能原因是友元函数不属于这个类, 所以Item 他用不了
    template <class Element> friend ostream &operator<<(ostream &cout,const Array<Element> &array);
    int m_size = 0; //大小
    int m_capacit = 0; //容量
    Item *m_data = NULL; //指向开始数据
public:
    Array(int capacity=0);
    ~Array();
    void add(Item value);
    Item get(int index);
    int size();
};

template <class Item>
Array<Item>::Array(int capacity){
    if (capacity<=0) return;
    this->m_data = new Item[capacity]{};
    this->m_capacit = capacity;
}

template <class Item>
Array<Item>::~Array<Item>(){
    if (!this->m_data) return;
    delete [] this->m_data;
    this->m_data = NULL;
}

template <class Item>
void Array<Item>::add(Item value){
    if (this->m_size==this->m_capacit) {
    	  // 需要扩容
        cout << "数组已满" << endl;
        return;
    }
    this->m_data[this->m_size++] = value;
}

template <class Item>
Item Array<Item>::get(int index){
    if (index <0 || index >= this->m_size) return NULL;
    return  this->m_data[index];
}

template <class Item>
int Array<Item>::size(){
    return this->m_size;
}

template <class Element>
ostream &operator<<(ostream &cout,const Array<Element> &array){
    cout << "[";
    for (int i=0; i<array.m_size; i++) {
        cout << &array.m_data[i];
        if (i!=array.m_size-1)
            cout << ",";
    }
    return cout << "]";
}
```

<a id="类型转化"></a>

### 类型转化

* c语言风格的类型转换符
	* (type)expression
	* type(expression)
	
	```c
	int a = 10;
	double d = (double)a;
	double d2 = double(a);
	```

* c++中4种类型转换符,一般用于对象,基本类型直接用C语言的方式就可以
	* static_cast
	* dynamic_cast
	* reinterpret_cast
	* const_cast
	* 使用格式为: `xx_cast<type>(expression)`

#### const_cast

* 一般用于去除const属性,将const转换成非const

```cpp
const Person *p1 = new Person();
// 报错
p1->m_age = 10; 

// p2,p1指向一个对象
Person *p2 = const_cast<Person *>(p1);
p2->m_age = 20;

// 下面这个也是可以,只是const_cast多了c++风格,语义明确点
Person *p3 = (Person *)p1;
p3->m_age = 30;
```

#### dynamic_cast

* 一般用于多态类型的转换,有运行时安全监测

```cpp
class Person{
	virtual void run(){}
};
class Student: public Person{};
class Car {};

Person *p1 = new Person();
Person *p2 = new Student();

Student *stu1 = dynamic_cast<Student *>(p1); //NULL 安全监测不通过
Student *stu2 = dynamic_cast<Student *>(p2);
Car *car = dynamic_cast<Car *>(p1); //NULL
```

#### static_cast

* 对比dynamic_cast,缺乏运行时安全监测
* 不能交叉转换(不是同一个继承体系的,无法转换)
* 常用语基本类型的转换,非const转成const

```cpp
Person *p1 = new Person();
Person *p2 = new Student();
Student *stu1 = static_cast<Student *>(p1);//不是NULL
Student *stu1 = static_cast<Student *>(p1); 
// 这个编译报错,不是一个继承体系
Car *car = static_cast<Car *><p1>;
```

#### reinterpret_cast

* 属于比较地城的强制转换,没有任何类型检查和格式转换,仅仅是简单的二进制数据拷贝
* 可以交叉转换
* 可以将指针和证书互相转换

```cpp
//int和double相互转换有些特殊,int在内存中是以整数的形式存储,
double则是以科学计数法的形式存储,
比如x86总double八字节的话,就有1为存符号位,11为存指数,52为存尾数
//比如-1.01*2^3,符号位为1代表负数,指数是3,尾数是1.01
// 所有int double转换有存储方式的转换
int i = 10;
double d = i;
```

```cpp
// 这里就是直接将i里面额赋值给d里面的
// x86中i的表示(16进制) 0a 00 00 00 
// d 的表示为 0a 00 00 00 cc cc cc cc (cc是栈空间的占位符号)
int i = 10;
//这个需要写引用&,语法糖,必须这么写,当类型不匹配的时候就要加&或*
double d = reinterpret_cast<double&>(i);
```

```cpp
Student *stu1 = reinterpret_cast<Student *>(p1);
Student *stu2 = reinterpret_cast<Student *>(p2);
Car *car = reinterpret_cast<Car *>(p1);

// 直接将100赋值给p指针的存储空间
int *p = reinterpret_cast<int *>(100);
```

<a id="c++11 新特性"></a>

### c++11 新特性

#### auto

* 可以从初始化表达式中推断出变量的类型,大大简化编程工作
* 属于编译器特性,不影响最终的机器码质量,不影响运行效率

```cpp
auto i = 10;
auto str = "bmw";
auto p = new Person();
p->run();
```

#### decltype

* 可以获取变量的类型

```cpp 
int a = 10;
decltype(a) b = 20; // int
```

#### nullptr

* 可以解决NULL的二义性问题,nullptr值也是0 不过可以解决NULL二义性问题

```cpp
void func(int v){}
void func(int *v){}

//NULL 就是0
func(0);
func(NULL); //会调用void func(int v){}
func(nullptr); // 会调用void func(int *v){}
```

#### 快速遍历

```cpp
int array[] = {11,22,33,44,55};
for(int item: array){
	cout << item << endl;
}
```

#### 更加简洁的初始化方式

```cpp
int array[]{11,22,33,44,55};
```

<a id="Lambda表达式"></a>

### Lambda表达式

* Lambda表达式有点类似js中的闭包,ios中的block,本质就是函数
* 完整的结构`[capture list](params list) mutable exception ->return type {funcetion body}`
	* capture list: 捕获外部变量列表
	* params list: 参数列表,不能使用默认参数,不能省略参数名
	* mutalbe: 是否可以修改捕获的变量
	* exception: 异常的设定
	* return type: 返回值类型
	* function body: 函数体
* 有时可以省略部分结构
	* [capture list] (params list) -> return type {function body}
	* [capture list] (params list) {function body}
	* [capture list] {function body}
 
 
```cpp
int (*p1)(int,int) = [](int v1,int v2)->int{
	return v1+v2;
};
cout << p1(10,20) << endl;
// 直接调用
[](int v1,int v2)->int{
	return v1+v2;
}();

//省略返回值
[](int v1,int v2){
	return v1+v2;
}();

// 省略参数
[]()->int{
	cout << 123;
};
```

* 应用

```cpp
int exec(int a,int b,int(*func)(int,int)){
	if (func==nullptr) return 0;
	return func(a,b);
}

exec(20,10,[](int v1,int v2){return v1+v2});
exec(20,10,[](int v1,int v2){return v1-v2});
```

<a id="Lambda表达式 - 外部变量捕获"></a>

### Lambda表达式 - 外部变量捕获

* 值捕获

```cpp
int a = 10;
int b = 20;
// h值捕获
auto func = [a,b]{
    cout << a << endl;
    cout << b << endl;
};
a = 11;
b = 22;
func();
```

* 地址捕获

```cpp
int a = 10;
int b = 20;
// a是引用(地址)捕获,b是值捕获
auto func = [&a,b]{
    cout << a << endl;
    cout << b << endl;
};
a = 11;
b = 22;
func();
```

* 隐式捕获

隐式捕获,值捕获,用到谁捕获谁

```cpp
nt a = 10;
int b = 20;
auto func = [=]{
    cout << a << endl;
    cout << b << endl;
};
a = 11;
b = 22;
func();
```

隐式捕获,地址捕获

```cpp
nt a = 10;
int b = 20;
auto func = [&]{
    cout << a << endl;
    cout << b << endl;
};
a = 11;
b = 22;
func();
```

a是值捕获,其余是地址捕获

```cpp
nt a = 10;
int b = 20;
auto func = [&,a]{
    cout << a << endl;
    cout << b << endl;
};
a = 11;
b = 22;
func();
```

<a id="Lambda表达式 - mutable"></a>
	
### Lambda表达式 - mutable

* 可修改值捕获的值,但外面的值不变

```cpp
int a = 10;
auto func = [a]() mutalbe{
	cout << ++a << endl;
};
func(); // 11
cout << a << endl; // 10
```
	
<a id="c++14 "></a>

### c++14 

#### 泛型 Lambda

```cpp
auto func = [](auto v1,auto v2) {return v1+v2};
```

#### 对捕获的变量可以进行初始化

```cpp
int a;
auto func = [a =10](){
	cout << a << endl;
};
```

<a id="异常"></a>

### 异常

* 异常没有被处理,会导致程序终止

```cpp
try{
	// 被检测的代码
}catch(异常类型 变量名){
	// 异常处理代码
}catch(异常类型 变量名){
	// 异常处理代码
}

// 如果想捕捉所有类型的异常
try{

}catch(...){

}
```

throw抛出异常后,会在当前函数中查找匹配的catch,找不到就终止当前代码,去上一层函数查找,如果最终找不到匹配的catch,程序终止. 试了下,xcode 不能像上一层函数去查找,sublime会,vs也会

* 为了增强可读性和方便团队协作,如果函数内部可能会抛出异常,建议函数声明下异常类型

```cpp
// 抛出任意可能的异常
void func1(){}

// 不破啊出任何异常
void func2() throw() {}

// 只抛出int,double类型的异常
void func3() throw(int,double) {}
```

#### 自定义异常

* 标准异常 std::exception.  exception是所有一同异常的父类

* 自定义异常

```cpp
class Exception {
public:
	virtual const char *what() const = 0;
};

class DivideException : public Exception {
public:
	const char *what() const {
		return "不能除以0";
	}
};

class AddException : public Exception {
public:
	const char *what() const {
		return "加法有问题";
	}
};

int divide2(int a, int b) {
	if (b == 0) throw DivideException();
	return a / b;
}
```

<a id="智能指针"></a>

### 智能指针

* 传统指针存在的问题
	* 需要手动管理内存
	* 容易发生内存泄露
	* 释放之后产生野指针 

* 智能指针就是为了解决传统指针存在的问题
	* `auto_ptr`: 属于C++98标准，在C++11中已经不推荐使用(有缺陷，比如不能用于数组)
	* `shared_ptr`:属于C++11标准
	* `unique_ptr`:属于C++11标准
 
智能指针智能用于堆空间的对象,如果是栈空间的话,会被重复释放,栈空间也不需要手动管理内存.智能指针销毁的时候会释放堆空间的对象,对于`auto_ptr`则会delete操作,不是`delete[]`操作,所以`auto_ptr`对数组不可用


#### 智能指针的简单实现

```cpp
template<class T>
class SmartPointer {
	T *m_pointer;
public:
	SmartPointer(T *pointer): m_pointer(pointer){}
	~SmartPointer(){
		if (m_pointer==nullptr) return;
		delete m_pointer;
	}
	T *operator->(){
		return m_pointer;
	}
};
```

#### shared_ptr

* 多个`shared_ptr`可以指向同一个对象,当最后一个`shared_ptr`在作用域范围内结束时,对象会被自动释放
* 针对数组的用法

```cpp
shared_ptr<Person> ptr1(new Person[5]{},[](Person *p){ delete[] p;});

shared_ptr<Person[]> persons(new Person[5]{});
``` 

* shared_ptr的原理
	* 一个`shared_ptr`会对一个对象产生强引用
	* 每个对象都有个与之对应的强引用计数,记录着当前对象被多少个`shared_ptr`强引用着,可以通过`shared_ptr`的`use_count`函数获得强引用计数
	* 当有一个新的`shared_ptr`指向对象时,对象的引用计数就会+1
	* 当有一个`shared_ptr`销毁时,(比如作用域结束),对象的强引用计数就会-1
	* 当一个对象的的强医用计数为0时,(没有任何`shared_ptr`指向对象时),对象就会销毁

```cpp
shared_ptr<Person> p1(new Person()); // p1.use_count 1
shared_ptr<Person> p2 = p1;	// p1.use_count 2
shared_ptr<Person> p3 = p1;	// p1.use_count 3
```	

#### shared_ptr的注意点

* 不要使用裸指针来初始化只能指针

下面的代码会走两次析构函数

```cpp
Person *p = new Person();

{
	shared_ptr<Person> p1(p);
}

{
	shared_ptr<Person> p1(p);
}
```

应该写成下面形式:

```cpp
shared_ptr<Person> p1(new Person());
shared_ptr<Person> p2(p1);
```

#### shared_ptr的循环引用问题

```cpp
class Person;
class Car{
public:
    shared_ptr<Person> m_person = nullptr;
    Car(){
        cout << "Car()" << endl;
    }
    ~Car(){
        cout << "~Car()" << endl;
    }
};
class Person{
public:
    shared_ptr<Car> m_car = nullptr;
    Person(){
        cout << "Person()" << endl;
    }
    ~Person(){
        cout << "~Person()" << endl;
    }
};

int main(){
	 shared_ptr<Person> person(new Person());
    shared_ptr<Car> car(new Car());
    person->m_car = car;
    car->m_person = person;
	return 0;
}
```

上面的代码Person,Car的析构都没有调用.为什么?person,car这个智能指针对象放在栈空间,堆空间有Person对象和Car对象.`m_person`强引用Person对象,`m_car`强引用Car对象. 当main函数执行完后,person,car这两个智能指针对象释放,被回收,不再强引用Person对象,Car对象. 但`m_person`和`m_car`还强引用Person,Car对象,引用计数为为1.造成无法释放.解决方法是将`m_person`或`m_car`变成弱引用

#### weak_ptr

* `weak_ptr` 会对一个对象产生弱引用
* `weak_ptr`可以指向对象解决`shared_ptr`的循环引用问题

```cpp
class Person;
class Car{
public:
    weak_ptr<Person> m_person; // 弱引用不用初始化
};
class Person{
public:
    shared_ptr<Car> m_car = nullptr;
};
```

#### unique_ptr

* `unique_ptr`也会对一个对象产生强引用,他可以确保同一时间只有1个指针指向对象
* `unique_ptr`销毁时(作用域结束时),其指向的对象就自动销毁
* 可以使用`std::move`函数转义`unique_ptr`的所有权

```cpp
// ptr1强引用Person对象
unique_ptr<Person> ptr1(new Person());
// 转移之后,ptr2强引用着Person对象
unique_ptr<Person> ptr2 = std::move(ptr1);
```
