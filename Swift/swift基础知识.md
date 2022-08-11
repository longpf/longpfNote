## swift和OC的异同

#### 相同点

* OC中大多数的概念,比如引用计数,ARC,属性,协议,接口,初始化,扩展类等在swift中继续有效
* swift和OC公用一套运行时环境,swift跟OC的类型可以相互桥接

### swift优点

* swift注重面向协议编程,函数式编程,面向对象编程,OC注重面向对象编程
* swift注重类型,OC注重指针和引用
* swift是**静态语言**,所有声明的方法,属性都是静态编译编译期就确定了,同事swift支持动态绑定和动态派发,只需要将class里的属性或者方法声明为`@objc dynamic`即可,swift的动态特性使用oc runtime来实现
	* `@objc`:为了将 Swift 的方法属性甚至类型暴露给 ObjC 使用,声明为@objc的类需要继承NSObject,
	*  如果要使用动态特性，需要声明dynamic
* swift文件结构简化, 只有.swift文件,语法也简化
* swift中提供高阶函数(函数式编程),map,filter,reduce
* 独有的元组类型tuples, 将多个值组合成复合值

### swift缺点

* 版本不稳定
* 使用程度不高

### swift中class和struct的区别

* 都可以定义属性用于存储
* 都可以定义方法提供功能
* 都可以通过扩展增加默认实现,swift中的扩展类似oc的分类,可以为enum,struct.class,协议添加新功能,可以添加方法,计算属性,下边,协议等
	* [https://www.jianshu.com/p/59df02d67ff6](https://www.jianshu.com/p/59df02d67ff6)
	* 不能覆盖原有的功能
	* 不能添加存储属性
	* 不能添加父类
* 都可以遵循协议
* clas可以继承,stuct不能
* class有引用计数,struct没有
* class可以类型转换,struct没有
* class有析构方法释放资源,struct没有

#### 值 vs 引用

* stuct和enum是值类型, class 是引用类型
* String,Array,Dictionary都是结构体, NSString,NSArray,NSDictionary是类,所以是引用的方式
* struct比class更轻量级

#### 指针

* swift中的常量/变量引用一个引用类型的实例 与 C语言的指针类型,不同的是并不直接指向内存中某个地址,也不需要使用星号(*)来表示一个引用

#### 什么时候选择class, 什么时候选择struct

* 任何情况下休闲考虑struct
* 使用结构体的情况: 	
	* 实例被拷贝时,不受拷贝后的新实例影响
	* 几何图形的大小,可以封装
	* 指向连续范围的方法,可以封装start,length,都是Int类型

* 使用class的情况: 
	* 需要被继承
	* 被递归调用的时候
	* 属性数据复杂
	* 希望引用而不是拷贝

	
### 协议与OC中的区别

* swift可以做到协议方法的默认实现,通过extension扩展实现
* 使用mutating关键字修饰方法是为了能在该方法中修改 struct 或是 enum 的变量

```swift
protocol Human {
  
  func read()
  func eat()
}

extension Human {
  
  func read() {}
}

struct Man: Human {
  
  func eat() {}
}


// mutating 关键字
protocol ExampleProtocol {
    var simpleDescription: String { get }
    mutating func adjust()
}

class SimpleClass: ExampleProtocol {
    var simpleDescription: String = "A very simple class"
    var anotherProperty: Int = 110
    // 在 class 中实现带有mutating方法的接口时，不用mutating进行修饰。因为对于class来说，类的成员变量和方法都是透明的，所以不必使用 mutating 来进行修饰
    func adjust() {
        simpleDescription += " Now 100% adjusted"
    }
}

struct SimpleStruct: ExampleProtocol {
    var simpleDescription: String = "A simple structure"
    mutating func adjust() {
        simpleDescription += "(adjusted)"
    }
}

enum SimpleEnum: ExampleProtocol {
    case First, Second, Third
    var simpleDescription: String {
        get {
            switch self {
            case .First:
                return "first"
            case .Second:
                return "second"
            case .Third:
                return "third"
            }
        }

        set {
            simpleDescription = newValue
        }
    }
    
    mutating func adjust() {

    }
}
```

### 面向协议与面向对象

* 最明显的区别是 对抽象数据的使用方式, 面向对象采用的是继承,而面向协议 采用的是 遵守协议
* 不得先说OOP,他的缺点:
	* 程序开发之前就能设计好整个程序的框架、结构、事物间的连接关系。这要求开发者必须有很好的分类设计能力，将不同的属性和方法分配的合适的层次里面去
	* OOP 建立的结构天生对改动有抵抗特性,例如我们要改变继承结构中的一个点，我们同样要关心它的父类和子类（如果有），改变这个地方之后父类和子类是否也要做相应的修改，这样就导致了代码的维护非常复杂。
	* 继承机制带来了另一个问题：很多语言（如 Java）都不提供多继承，我们不得不在父类塞入更多的内容，子类中会存在无用的父类属性和方法，而这些冗余代码会给子类带来一定的风险
	* 编码,调试不友好,调用链深
* OOP 主要关心的是对象 “是什么”，这个对象是个数组、按钮还是输入框；而 POP 主要关心对象能 “做什么”，具体能 “做什么” 是由各种协议来定义的。


### 函数式/ 响应式/ 链式

* 函数式编程是一种编程范式,将计算描述为表达式求值.
* 函数式编程思想:是将操作尽可能写在一起!嵌套的函数!! 本质:就是往方法里面传入Block,方法中嵌套Block调用
*  命令式编程，命令式编程往往是我们大多数人固有的编程思维，这中模式依赖于我们希望自己的程序如何完成某项任务
*  声明式编程，它关心是任务的目的是什么，而不是具体如何实现。这把程序员从那些细枝末节中解放了出来
*  函数响应式编程正是声明式编程的一个子范式
*  链式编程,方法的返回值必须是方法的调用者
*  响应式编程解决的痛点： 在程序开发中：a ＝ b ＋ c,赋值之后 b 或者 c 的值变化后，a 的值不会跟着变化. KVO/RAC
*  RxSwift? 将数据或时间变成可观察的,达到订阅的目的


### 方法调度

#### 静态派发

* 值类型对象的函数的调用方式是静态调用，即直接地址调用
* 这个函数指针在编译、链接完成后，当前函数的地址就已经确定了，拿在执行代码的过程中就直接跳转到这个地址来执行当前对应的方法，存放在代码段，而结构体内部并不存放方法。因此可以直接通过地址直接调用


#### 动态派发

* 类中声明的方法是通过V-table函数表来进行调度的
* 函数表类似数组,声明在class内部的方法在不加任何关键字的修饰过程中,连续存放在我们当前的地址空间
* 如果在class的扩展中声明的方法,是直接调用. 原因:
	* 正常子类会将父类的方法拷贝到子类中
	* 子类将父类的函数表全部继承了，如果此时子类增加函数，会继续在连续的地址中插入
	* 假设extension函数也在函数表中，则意味着子类也有，但是子类无法并没有相关的指针记录函数是父类方法还是子类方法，所以不知道方法该从哪里插入，导致extension中的函数无法安全的放入子类中
	* 这里可以侧面证明extension中的方法是直接调用的，且只属于类，子类是无法继承的


* 继承方法和属性，不能写extension中
* 而extension中创建的函数，一定是只属于自己类，但是其子类也有其访问权限，只是不能继承和重写

#### 扩展

* final 的作用 final 关键字的作用：使用它修饰的变量、方法、类不可继承, 方法都是直接调用
* 使用@objc关键字是将swift中的方法暴露给OC，@objc修饰的方法是函数表调度
* 如果只是通过@objc修饰函数，OC还是无法调用swift方法的，因此如果想要OC访问swift，class需要继承NSObject
* dynamic修饰 使用dynamic的意思是可以动态修改，以为着当继承自NSObject时，可以使用method-swizzling

#### 参考阅读

* [https://juejin.cn/post/6917607385334808583](https://juejin.cn/post/6917607385334808583)
* [https://www.jianshu.com/p/e848b843b959](https://www.jianshu.com/p/e848b843b959)

## 闭包 和 block

* [https://juejin.cn/post/6950477928123596814](https://juejin.cn/post/6950477928123596814)
* [https://juejin.cn/post/6844903521553219598#heading-8](https://juejin.cn/post/6844903521553219598#heading-8)
* [https://juejin.cn/post/6935797942435446791#heading-7](https://juejin.cn/post/6935797942435446791#heading-7)
* 闭包的本质是代码块，它是函数的升级版本，函数是有名称、可复用的代码块，闭包则是比函数更加灵活的匿名代码块。
* 闭包会自动持有被捕获的变量
	* 如果捕获的变量在闭包捕获列表中,那会变成拷贝捕获,闭包类型也会变比如`()->()变成(Int)->()`
	* 如果不在捕获列表中,那就是引用的捕获,不拷贝一份
* 如果在闭包内和闭包外没有修改变量,那么直接持有,不会捕获
* 例子
	* 下面没有循环引用
	* a不是A类型,而是一个可选类型,内部封装A的实例对象
	* 闭包截获的是可选类型变量a
	* 当a = nil时,并不是释放了变量a,而是释放了a中包含的A实例对象
	* 所以A的deinit会执行
	* 由于可选链,就会打印nil

	```swift
    class A : NSObject{
        var name: String = "";
        var block: (() -> ())?
        init(name: String){
            self.name = name
        }
        deinit{
            print("A 释放了")
        }
    }        var a: A? = A()
    var block = {
        print(a?.name)
    }
    a?.block = block
    a = nil
    block()
    
    // 结果
	A 释放了
	nil
	```
* 一个闭包底层由16个字节组成，前8个字节存放的是函数代码实现地址的指针，一般指向代码段，后8个字节存放指向捕获值地址的指针，一般指向堆区
	
#### 闭包的 weak strong 

* 解决循环引用可以用weak和unowned
* 用weak的话,self变成可选类型,调用属性/方法的时候需要加?. 并且涉及SideTable,效率低
* unowned 不会
* 方式1: if let
	
	```swift
	func doClosure() {
	    dispatch_async(dispatch_get_global_queue(0, 0)) { [weak self] in
	        if let strongSelf = self {  // <-- 这里就是精髓了
	            strongSelf.log("before sleep")
	            usleep(500)
	            strongSelf.log("after sleep")
	        }
	    }
	}
	
	// or in Swift 2, using `guard let`:
	dispatch_async(dispatch_get_global_queue(0, 0)) { [weak self] in
	    guard let strongSelf = self else { return }  // <-- 这里就是精髓了
	    strongSelf.log("before sleep")
	    usleep(500)
	    strongSelf.log("after sleep")
	}
	```
	
* 方式2: withExtendedLifetime

	```swift
	func doClosure() {
	    dispatch_async(dispatch_get_global_queue(0, 0)) { [weak self] in
	        withExtendedLifetime(self) {
	            self!.log("before sleep")
	            usleep(500)
	            self!.log("after sleep")
	        }
	    }
	}
	```




### 多线程

* 快捷方式

	```swift
	Thread.detachNewThread {
		print(i)
	}
	```
	
* 初始化器

	```swift
	class ObjectThread {
	    func threadTest() {
	        let thread = Thread(target: self, selector: #selector(threadExecute), object: nil)
	        thread.start()
	    }
	    
	    @objc func threadExecute() {
	        print("threadExecuting1")
	    }
	}
	let obj = ObjectThread();
	obj.threadTest()
	```
	
* operation / operationQueue

	```swift
	//BlockOperation实现(代码可以多运行几次)
	class ObjectOperation {
	    func threadTest() {
	        let operation = BlockOperation {[ weak self] in 
	            self?.threadExecute()
	        }
	        let queue = OperationQueue()
	        queue.addOperation(operation)
	    }
	    
	    func threadExecute() {
	        print("threadExecuting")
	    }
	}
	
	let objOperation = ObjectOperation()
	objOperation.threadTest()
	print("after invoke test")
	
	//自定义Operation实现
	class ObjectOperation {
	    func threadTest() {
	        let operation = MyOperation()
	        let queue = OperationQueue()
	        queue.addOperation(operation)
	    }
	}
	
	class MyOperation: Operation {
	    override func main() {
	        sleep(1)
	        print("in MyOperation main")
	    }
	}
	
	let objOperation = ObjectOperation()
	objOperation.threadTest()
	print("after invoke test")
	```
	
* GCD

	```swift
	let queue = DispatchQueue(label: "myQueue", qos: DispatchQoS.default, attributes: DispatchQueue.Attributes.concurrent, autoreleaseFrequency: DispatchQueue.AutoreleaseFrequency.inherit, target: nil)
	
	queue.sync {
	    sleep(1)
	    print("in queue sync")
	}
	
	queue.async {
      sleep(1)
      print("in queue async")
      	 }
      	 
	queue.asyncAfter(deadline: .now() + 1 ){
   		 print("in asyncAfter")
	}
	
	print("after invoke queue method")
	```
	
	
## 协程

[https://www.bennyhuo.com/2021/10/11/swift-coroutines-01-intro/](https://www.bennyhuo.com/2021/10/11/swift-coroutines-01-intro/)

* 协程（Coroutines）不是一个语言特有的概念,是一种非抢占式或者说协作式的计算机程序并发调度的实现，程序可以主动挂起或者恢复执行
* 在提到线程，基本上指的就是操作系统的内核线程；而提到协程，绝大多数都是编程语言层面实现的任务载体 
* 我们看待一个线程，就好像一艘轮船一样，而协程似乎就是装在上面的一个集装箱
* 从任务的承载上来讲，线程比协程更重；从调度执行的能力来讲，线程是由操作系统调度的，而协程则是由编程语言的运行时调度的。所以绝大多数的编程语言当中实现的协程都具备更加轻量和更加灵活的特点。对于高负载的服务端，协程的轻量型就表现地很突出；而对于复杂的业务逻辑，特别是与外部异步交互的场景，协程的灵活性就可以发挥作用。
* 对于 Swift 而言，主要应对的自然是简化复杂的异步逻辑。而针对类似的场景，各家实际上已经给出了近乎一致的语法：async/await。其中 async 用于修饰函数，将其声明为一个异步函数，await 则用于非阻塞地等待异步函数的结果 