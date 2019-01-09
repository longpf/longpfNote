## 目录

* <a href="#面向对象0">面向对象问题</a> , <a href="#面向对象1">面向对象知识点</a> 
* <a href="#KVO0">KVO问题</a> , <a href="#KVO1">KVO知识点</a> 
* <a href="#KVC0">KVC问题</a> , <a href="#KVC1">KVC知识点</a> 
* <a href="#Category0">Category问题</a> , <a href="#Category1"> Category知识点</a> 
* <a href="#Block0">Block问题</a> , <a href="#Block1">Block知识点</a>
* <a href="#Runtime0">Runtime问题</a> , <a href="#Runtime1">Runtime知识点</a>


<a id="面向对象0"></a>

### 面向对象

* **一个NSObject对象占用多少内存？**
 
	系统分配了16个字节给NSObject对象（通过`malloc_size`,runtime.h头文件函数获得）,oc对象的allocwithzone:的内部分配内存的时候,会按照16的倍数分配,方便操作系统分配内存.这个可以看libmalloc源码,[https://opensource.apple.com/tarballs/](https://opensource.apple.com/tarballs/)
	
	但NSObject对象内部只使用了8个字节的空间（64bit环境下，可以通过`class_getInstanceSize`函数获得）.`class_getInstanceSize`获得NSObject实例对象的成员变量所占用的大小8.转成C++后是一个`NSObject_IMPL`的结构体,这个结构体中只有一个isa的成员变量.如果一个类继承NSObject并且有一个long类型的成员变量,那么用`class_getInstanceSize`获取到的为16字节.如果不是long是int类型,还是16.因为结构体对齐.8+4=12然后在对齐.他和sizeof的区别:sizeof是运算符,一编译就会生成一个常数,他传入的参数是类型.`class_getInstanceSize`传入的是一个对象,是程序运行时的

*  **对象的isa指针指向哪里？**

	* instance对象的isa指向class对象
	* class对象的isa指向meta-class对象
	* meta-class对象的isa指向基类的meta-class对象

* **OC的类信息存放在哪里？**
	* 对象方法、属性、成员变量、协议信息，存放在class对象中
	* 类方法，存放在meta-class对象中
	* 成员变量的具体值，存放在instance对象

<a id="KVO0"></a>

### KVO

* **iOS用什么方式实现对一个对象的KVO？(KVO的本质是什么？)**

	利用RuntimeAPI动态生成一个子类，并且让instance对象的isa指向这个全新的子类
当修改instance对象的属性时，会调用Foundation的`_NSSetXXXValueAndNotify`函数,这个函数会调用下面方法

	willChangeValueForKey:

	父类原来的setter

	didChangeValueForKey:
	内部会触发监听器（Oberser）的监听方法( observeValueForKeyPath:ofObject:change:context:）
	
* **如何手动触发KVO？**

	手动调用willChangeValueForKey:和didChangeValueForKey:(这个会检查willChange...有没有调用)
	
* **直接修改成员变量会触发KVO么？**
	
	不会触发KVO

<a id="KVC0"></a>

### KVC

* **通过KVC修改属性会触发KVO么？**
	
	会触发KVO.即使只声明成员变量,没有setter方法.也会触发.说明`setValue:forKey:`内部会做willChangeValueForKey:和didChangeValueForKey:
	
* **KVC的赋值和取值过程是怎样的？原理是什么？**

	<a href="#__kvc">看下面KVC原理</a>

<a id="Category0"></a>

### Category

* **Category的使用场合是什么？**

	一个类拆解模块...

* **Category的实现原理**

	Category编译之后的底层结构是struct category_t，里面存储着分类的对象方法、类方法、属性、协议信息
	
	在程序运行的时候，runtime会将Category的数据，合并到类信息中（类对象、元类对象中）
	
* **Category和Class Extension的区别是什么？**

	Class Extension在编译的时候，它的数据就已经包含在类信息中
	
	Category是在运行时，才会将数据合并到类信息中

* **Category中有load方法吗？load方法是什么时候调用的？load 方法能继承吗？**

	有load方法
	
	load方法在runtime加载类、分类的时候调用
	
	load方法可以继承，但是一般情况下不会主动去调用load方法，都是让系统自动调用

* **load、initialize方法的区别什么？它们在category中的调用的顺序？以及出现继承时他们之间的调用过程？**

	* 调用方式
		* load是根据函数地址直接调用
		* initialize是通过objc_msgSend调用
	* 调用时刻
		* load是runtime加载类,分类的时候调用(只调用一次)
		* initialize是类第一次接受到消息的时候调用.每一个类只会initilaize一次(父类的initialize可能会被调用多次)
	* load,initialize调用用顺序?
	* load:
		* 先调用类的load,先编译的类,优先调用load,调用子类的load之前会先调用父类的load
		* 再调用分类的load.先编译的分类,有限调用load
	* initialzie
		* 先初始化父类,再初始化子类(可能最终调用的是父类的initialize方法)

* **Category能否添加成员变量？如果可以，如何给Category添加成员变量？**

	如果是类,写一个属性,编译器在编译的时候会自动声明setter和getter方法声明和实现.还会添加一个成员变量
	
	如果是分类,他只会自动添加setter和getter方法的声明
	
	不能直接给Category添加成员变量，但是可以间接实现Category有成员变量的效果


<a id="Block0"></a>

### Block


* **block的原理是怎样的？本质是什么？**

	封装了函数调用以及调用环境的OC对象 

* **__block的作用是什么？有什么使用注意点？**

	<a href="#__block修饰符">看下面</a>

* **block的属性修饰词为什么是copy？使用block有哪些使用注意？**

	block一旦没有进行copy操作，就不会在堆上
	
	使用注意：循环引用问题

* **block在修改NSMutableArray，需不需要添加__block？**

	不需要.
	
	```objective-c
	NSMutableArray *array = [NSMutableArray array];
	dispatch_block_t block = ^{
		[array addObject:@1];
	};
	```
	
<a id="Runtime0"></a>	

### Runtime


* **讲一下 OC 的消息机制**

	OC中的方法调用其实都是转成了`objc_msgSend`函数的调用，给receiver（方法调用者）发送了一条消息（selector方法名）
	
	`objc_msgSend`底层有3大阶段
消息发送（当前类、父类中查找）、动态方法解析、消息转发

* **消息转发机制流程**

	<a href="#__objc_msgSend">看下面</a>
	
* **什么是Runtime？平时项目中有用过么？**

	OC是一门动态性比较强的编程语言，允许很多操作推迟到程序运行时再进行
	OC的动态性就是由Runtime来支撑和实现的，Runtime是一套C语言的API，封装了很多动态性相关的函数
	平时编写的OC代码，底层都是转换成了Runtime API进行调用

	具体应用
	
	 * 利用关联对象（AssociatedObject）给分类添加属性
	 *	遍历类的所有成员变量（修改textfield的占位文字颜色、字典转模型、自动归档解档）
	* 交换方法实现（交换系统的方法）
	* 利用消息转发机制解决方法找不到的异常问题
	......

