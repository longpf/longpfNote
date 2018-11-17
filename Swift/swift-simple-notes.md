
# Swift基础简单笔记

[菜鸟Swift](http://www.runoob.com/swift/swift-tutorial.html)

目录
==============

* 1. [渣渣](#渣渣)
* 2. [函数](#函数)
* 3. [闭包](#闭包)
* 4. [枚举](#枚举)
* 5. [结构体](#结构体)
* 6. [类](#类)
* 7. [属性](#属性)
* 8. [方法](#方法)
* 9. [下标脚本](#下标脚本)
* 10. [继承](#继承)
* 11. [构造,析构,可选链](#构造,析构,可选链)
* 12. [自动引用计数](#自动引用计数)
* 13. [类型转换](#类型转换)
* 14. [扩展](#扩展)
* 15. [协议](#协议)
* 16. [泛型](#泛型)
* 17. [访问控制](#访问控制)


<span id="渣渣"></span>

```
var aa:Float
aa = 3.14
print(aa)
```

输出
==============

```
var name = "666"
var site = "777"
print("\(name)dddd\(site)")
```

**16进制小数 :**
0xFp2 表示 15 ⨉ 2^2，也就是 60；同样，0xFp-2 表示 15 ⨉ 2^-2，也就是 3.75

区间运算
==============

```
for index in 1...5 {
    print(index)
}
    
for index in 1..<5 {
    print("\(index)")
}
```

[fallthrough 贯穿case](http://www.runoob.com/swift/swift-fallthrough-statement.html)

字符串
==============

```
//使用字符串字面量
var stringA = "Hello,World!"
//String实例化
var stringB = String("Hello,World!")
//拼接
var str = "123"
str += "890"
//插入
var stringA = "\(varA) 乘于 \(constA) 等于 \(varC * 100)"
//比较
varA == varB
varA < varB
//empty
str.isEmpty
//是否有前缀...
hasPrefix
//转化为int
Int(String)
//长度
String.characters.count
//utf8
utf8

```

字符
==============

```
//创建 
let char1: Character = "A" //不能创建空字符 ""

//遍历
for ch in "Runoob".characters {
    print(ch)
}

//拼接
var varA:String = "Hello "
let varB:Character = "G"
varA.append( varB )
```

数组
==============

```
var someInts = [Int](repeatElement(0, count: 3))
someInts[1] = 1
someInts.append(6)
someInts += [40,8]
someInts.insert(99, at: 0)
someInts.count
someInts.isEmpty
arr1 + arr2

//遍历
for item in someInts {
}
    
for (index,item) in someInts.enumerated() {
    print("index = \(index),item = \(item)")
}
```

字典
==============

```
var someDict = [Int: String]() //空字典
ar someDic:[Int:String] = [1:"one",2:"two"]
someDic[1] = "999"
someDic.updateValue("888", forKey: 1)

someDic.count
someDic.keys
someDic.values
someDic.isEmpty

//遍历
for (key,value) in someDic {
	print("key \(key),value \(value)")
}
    
for (key,value) in someDic.enumerated() {
	print("key \(key),value \(value)")
}
```
元组(tuple)
==============

元组与数组类似,不同的是,元组中的元素可以是任意类型的,使用的是圆括号
(a:Int,b String)

<span id="函数"></span>

函数
==============

```
func minMax(array:[Int]) -> (min: Int,max: Int) {
var currentMin = array[0];
var currentMax = array[0]
for value in array[1..<array.count] {
    if value < currentMin{
        currentMin = value
    }else if value > currentMax{
        currentMax = value
    }
}
return (currentMin,currentMax)
}
//考虑参数为nil,返回一个可选的元组
if let bounds = minMax(array: [8, -6, 2, 109, 3, 71]) {
    print("最小值为 \(bounds.min)，组大值为 \(bounds.max)")
}

//没有返回值
func runoob(site: String) {
}

//firstArg外惨 a是局部参数,如果提供了外部参数名,那么函数在被调用时,必须使用外部参数名
func pow(firstArg a:Int,secondArg b:Int) -> Int{
    var res = a
    for _ in 1..<b {
        res = res * a
    }
    print(res)
    return res
}

//可变参数
//可变参数可以接受零个或多个值.函数调用时,你可以用可变参数来指定函数参数
func vari<N>(members: N...) {
    for i in members {
        print(i)
    }
}
vari(members: 4,3,5)

//常量，变量及 I/O 参数
//一般默认在函数中定义的参数都是参量参数,也就是这个参数你只可以参训使用,不能改变它的值.如果想要声明一个变量参数,可以在参数定义前加inout关键字,这样就可以改变这个参数的值了.
func  getName(_ name: inout String).........
一般默认的参数传递都是传值调用的,而不是传引用,所以传入的参数在函数内改变,并不影响原来的那个参数.传入的只是这个参数的副本
但传入的参数作为输入输出参数时,需要在参数名钱加&符,表示这个值可以被修改
func swapTwoInts(_ a:inout Int,_ b:inout Int){
    let temporaryA = a
    a = b
    b = temporaryA
}
var x = 1
var y = 5
swapTwoInts(&x, &y)
print("x现在的值\(x),y现在的值\(y)")


//函数类型
var addition: (Int,Int) ->Int = sum;
解析: 定义一个叫做addition的变量,参数与返回值类型都是Int,并让这个新变量指向sum函数.sum和addition有同样的类型/.
func sum(a: Int,b:Int) ->Int {
    return a+b;
}
var addition: (Int,Int) -> Int = sum
print("输出结果:\(addition(40,89))")

//函数类型用作参数和返回类型
func another(addition: (Int, Int) -> Int, a: Int, b: Int) {
    print("输出结果: \(addition(a, b))")
}

//函数嵌套
//函数嵌套指的是函数内定义一个新的函数,外部的函数可以调用函数内定义的函数
func calcDecrement(forDecrement total: Int) -> () -> Int {
    var overallDecrement = 0
    func decrementer() -> Int {
        overallDecrement -= total
        return overallDecrement
    }
    return decrementer;
}
let decrem = calcDecrement(forDecrement: 30)
print(decrem())

```

<span id="闭包"></span>

闭包
==============

```
{(parameters) -> return type in
   statements
}

let divide = {(val1: Int, val2: Int) -> Int in 
   return val1 / val2 
}
let result = divide(200, 20)
print (result)

//sorted方法
sorted(by:)方法需要传入两个参数:
1. 已知类型的数组
2. 闭包函数

let names = ["AT","AE","D","S","BE"]
func backwards(s1:String,s2:String) -> Bool{
    return s1 > s2
}
var reversed = names.sorted(by: backwards)
print(reversed)

Swift的string类型定义了关于大于号(>)的字符串实现,所以可以简写成
var reversed = names.sorted(by: >)
```

**尾随闭包**

尾随闭包是一个书写在函数括号之后的闭包表达式,函数支持将其作为最后一个参数调用

```
个参数调用
func someFunctionThatTakesAClosure(closure: () -> Void) {
    // 函数体部分
    print("1");
    closure();
    print("3");
}

//以下是不适用尾随闭包进行函数调用
someFunctionThatTakesAclosure({
    //闭包主体部分
    print("2");
})

//以下是使用尾随闭包进行函数调用
someFunctionThatTakesAClosure() {
  // 闭包主体部分
  print("2");
}
或是
someFunctionThatTakesAClosure {
	print("2");
}
```
```
let names = ["AT","AE","D","S","BE"]
        
//尾随闭包
var reversed = names.sorted(){$0 > $1}
print(reversed)

//如果函数只需要闭包表达式一个参宿,当您使用尾随闭包时,可以把()省略
reversed = names.sorted { $0 > $1 }
```

**捕获值**

闭包可以在其定义的上下文中捕获常量或变量.即使定义这些常量和变量的原域已经不存在,闭包仍然可以在闭包函数体内引用和修改这些值.swift最简单的闭包形式是嵌套函数,也就是定义在其他函数的函数体内的函数.嵌套函数可以捕获其外部函数所有的参数以及定义的常量和变量.看这个例子:

```
func  makeIncrementor(forIncrement amount: Int) -> ()->Int {
    var runningTotal = 0;
    func incrementor() -> Int{
        runningTotal += amount
        return runningTotal
    }
    return incrementor
}
let incrementByTen = makeIncrementor(forIncrement: 10);
print(incrementByTen());
print(incrementByTen())
print(incrementByTen())
输入 10  20  30
```
函数体内,声明了变量runningTotal和一个函数incrementor. incrementor函数并没有获取任何参数,但是在函数体内访问了runningTotal和amount变量.这是因为其通过捕获在包含他的函数体内已经存在的runningTotal和amount变量而实现.由于没有修改amount变量,incrementor实际上捕获并存储了改变量的一个副本,二该副本随着incrementor一同被存储.所以调用这个函数时会累加

**闭包是引用类型**

上面的例子中,incrementByTen是常量,但是这些常量指向的闭包仍然可以增加其捕获的变量值.这是因为函数和闭包都是引用类型.无论你讲函数/闭包赋值给一个常量还是变量,你实际上都是讲常量/变量的值设置为对应函数/闭包的引用.上面的例子中,incrementByTen指向闭包的引用是一个常量,而并非闭包内容本身.这也意味着如果你讲闭包赋值给两个不同的常量/变量,两个值都会指向同一个闭包


<span id="枚举"></span>

枚举
==============

```
enum DaysofaWeek {
    case Sunday
    case Monday
    case TUESDAY
    case WEDNESDAY
    case THURSDAY
    case FRIDAY
    case Saturday
}
var weekDay = DaysofaWeek.THURSDAY
weekDay = .THURSDAY //已经知道weekDay是DaysofaWeek类型后,之后的复制可以简写成这样
```
Sunday，Monday是这个枚举的成员值.case关键词表示这一行的成员值将被定义.和C和OC不同,swift的枚举成员在被创建时不会被赋予一个默认的整型值.相反,这些枚举成员本身就有完备的值.这些值是已经明确定义好的DaysofaWeek

**相关值和原始值**

枚举可分为相关值和原始值

相关值		   			  | 原始值
--------------- 		  |--------------
不同的数据类型	  		  | 相同的数据类型
enum {10,0.8,"Hello"} |  enum {10,35,50}
值得创建基于常量或变量	  |  预先填充的值
相关值是当在创建一个基于枚举成员的新常量或变量时才会被设置,并且每次当你这么做得实惠,它的值可以是不同的 |原始值始终是相同的

* 1 相关值

```
enum Student {
    case Name(String)
    case Mark(Int,Int,Int)
}
var studDetails = Student.Name("Runoob")
var studMarks = Student.Mark(98, 97, 95)
switch studMarks {
case .Name(let studName):
    print("学生的名字是: \(studName)")
case .Mark(let Mark1, let Mark2, let Mark3):
    print("学生的成绩是: \(Mark1),\(Mark2),\(Mark3)。")
}
输出    学生的成绩是: 98,97,95。
```
* 2 原始值

原始值可以是字符串，字符，或者任何整型值或浮点型值。每个原始值在它的枚举声明中必须是唯一的。
在原始值为整数的枚举时，不需要显式的为每一个成员赋值，Swift会自动为你赋值。
例如，当使用整数作为原始值时，隐式赋值的值依次递增1。如果第一个值没有被赋初值，将会被自动置为0。

```
enum Month: Int {
        case January = 1, February, March, April, May, June, July, August, September, October, November, December
}

let yearMonth = Month.May.rawValue
print("数字月份为: \(yearMonth)。")

输出:    数字月份为: 5。
```

<span id="结构体"></span>

结构体
==============

与C和OC不同的是 :

* 结构体不需要包含实现文件和接口
* 结构体允许我们创建一个单一文件,且系统工会自动生成面向其他代码的外部接口

```
struct studentMarks {
   var mark1 = 100
   var mark2 = 78
   var mark3 = 98
}
let marks = studentMarks()
print("Mark1 是 \(marks.mark1)")
```
**结构体的应用**

结构体实例总是通过值传递来定义你的自定义数据类型.符合下面的一或多个条件可以考虑构建结构体: 

* 结构体的主要目的是用来封装少量相关简单的数据.
* 有理由预计一个结构体实例在复制或传递时,封装的数据将会被拷贝而不是被引用
* 任何结构体中储存的值类型属性,也将会被拷贝,而不是被引用
* 结构体不需要去集成另一个已存在的类型的属性或行为

举例来说,以下情景适合使用结构体:

* 几何形状的大小，封装一个width属性和height属性，两者均为Double类型
* 一定范围内的路径，封装一个start属性和length属性，两者均为Int类型。
* 三维坐标系内一点，封装x，y和z属性，三者均为Double类型 

结构体实例是通过值传递而不是通过引用传递

```
struct markStruct{
    var mark1: Int
    var mark2: Int
    var mark3: Int
    
    init(mark1: Int, mark2: Int, mark3: Int){
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    }
}
    
print("优异成绩:")
var marks = markStruct(mark1: 98, mark2: 96, mark3:100)
print(marks.mark1)
print(marks.mark2)
print(marks.mark3)
    
print("糟糕成绩:")
var fail = markStruct(mark1: 34, mark2: 42, mark3: 13)
print(fail.mark1)
print(fail.mark2)
print(fail.mark3)

输出:
优异成绩:
98
96
100
糟糕成绩:
34
42
13
```
以上实例中我们定义了结构体 markStruct，三个成员属性：mark1, mark2 和 mark3。结构体内使用成员属性使用 self 关键字。

<span id="类"></span>

类
==============

与其他编程语言所不同的是，Swift 并不要求你为自定义类去创建独立的接口和实现文件。你所要做的是在一个单一文件中定义一个类，系统会自动生成面向其它代码的外部接口。

类定义:

```
class student{
    var studname: String = ""
    var mark: Int = 0
    var mark2: Int = 0
}
```

实例化

```
let studrecord = student()
```

属性访问

```
class studentMarks {
   var mark1 = 300
   var mark2 = 400
   var mark3 = 900
}
let marks = studentMarks()
print("Mark1 is \(marks.mark1)")
print("Mark2 is \(marks.mark2)")
print("Mark3 is \(marks.mark3)")
```

**恒等运算符**

恒等运算符			|	不恒等运算符
-------------  	|  ------------
运算符为 ===	   | 运算符为 !==
如果两个常量或者变量引用同一个类实例则返回true   |  如果两个常量或者变量引用不同一个类型实例则返回 true

```
let spClass1 = SampleClass(s: "Hello");
let spClass2 = SampleClass(s: "Hello")
    
if spClass1 === spClass2 {// false
    print("引用相同的类实例 \(spClass1)")
}
    
if spClass1 !== spClass2 {// true
    print("引用不相同的类实例 \(spClass2)")
}
输入:   引用不相同的类实例 SampleClass
```


<span id="属性"></span>

属性
==============

swift属性将值跟特定的类,结构或枚举关联

存储属性				|   计算属性
------------		   |  -------------
存储常量或变量作为实例的一部分 | 计算（而不是存储）一个值
用于类和结构体			| 用于类、结构体和枚举

**存储属性**

```
struct Number
{
   var digits: Int
   let pi = 3.1415
}

var n = Number(digits: 12345)
n.digits = 67

print("\(n.digits)")
print("\(n.pi)")
```

**延迟存储属性**

在属性声明前使用lazy来标示一个延迟存储属性  属性必须声明成var

延迟存储属性一般用于:

* 延迟对象的创建
* 当属性的值依赖于其他未知类

```
class sample{
    lazy var no = number();
}
    
class number{
    var name = "runoob swift"
}

var firstsample = sample()
print(firstsample.no.name)
```

**计算属性**

计算属性不直接存储值,而是提供一个getter来获取值,一个可选的setter来间接设置其他属性或变量的值.

```
class sample {
    var no1 = 0.0, no2 = 0.0
    var length = 300.0, breadth = 150.0
    
    var middle: (Double, Double) {
        get{
            return (length / 2, breadth / 2)
        }
        set(axis){
            no1 = axis.0 - (length / 2)
            no2 = axis.1 - (breadth / 2)
        }
    }
}

var result = sample()
print(result.middle)
result.middle = (0.0, 10.0)

print(result.no1)
print(result.no2)
```

**只读计算属性**

只读计算属性总是返回一个值,可以通过点(.)运算符访问,但不能设置新的值

```
class film {
    var head = ""
    var duration = 0.0
    var metaInfo: [String:String] {
        return [
            "head": self.head,
            "duration":"\(self.duration)"
        ]
    }
}

var movie = film()
movie.head = "Swift 属性"
movie.duration = 3.09

print(movie.metaInfo["head"]!)
print(movie.metaInfo["duration"]!)
```

**属性观察器**

注意: 不需要为无法重载的计算属性添加属性观察器,以为可以通过setter直接监控和响应值得变化

可以为属性添加如下的一个或全部观察器

 * willSet在设置新值之前调用
 * didSet在新的值被设置之后立即调用
 * willSet和didSet观察器在属性初始化过程中不回被调用


```
class Samplepgm {
    var counter: Int = 0{
        willSet(newTotal){
            print("计数器: \(newTotal)")
        }
        didSet{
            if counter > oldValue {
                print("新增数 \(counter - oldValue)")
            }
        }
    }
}
let NewCounter = Samplepgm()
NewCounter.counter = 100
NewCounter.counter = 800

输出:
计数器: 100
新增数 100
计数器: 800
新增数 700

```
 
**类型属性**

类型属性是作为类型定义的一部分写在类型最外层的花括号{}内.
使用关键字static来定义值类型的类型属性,关键字class来为类定义类型属性.

```
struct Structname {
   static var storedTypeProperty = " "
   static var computedTypeProperty: Int {
      // 这里返回一个 Int 值
   }
}

enum Enumname {
   static var storedTypeProperty = " "
   static var computedTypeProperty: Int {
      // 这里返回一个 Int 值
   }
}

class Classname {
   class var computedTypeProperty: Int {
      // 这里返回一个 Int 值
   }
}
```

**获取和设置类型属性的值**

```
struct StudMarks {
   static let markCount = 97
   static var totalCount = 0
   var InternalMarks: Int = 0 {
      didSet {
         if InternalMarks > StudMarks.markCount {
            InternalMarks = StudMarks.markCount
         }
         if InternalMarks > StudMarks.totalCount {
            StudMarks.totalCount = InternalMarks
         }
      }
   }
}

var stud1Mark1 = StudMarks()
var stud1Mark2 = StudMarks()

stud1Mark1.InternalMarks = 98
print(stud1Mark1.InternalMarks) 

stud1Mark2.InternalMarks = 87
print(stud1Mark2.InternalMarks)
```


<span id="方法"></span>


swift方法
==============


**在实例方法中修改值类型**


swift语言中结构体和枚举是值类型.一般情况下,值类型的属性不能在它的的实例方法中被修改.
但是,如果你确实需要在某个具体的方法中修改结构体或者枚举的属性,你可以选择变异(mutating)这个方法,然后方法就可以从方法内部改变它的属性;并且它做的任何改变在方法结束时还会保留在原始结构中.
方法还可以给它隐含的属性赋值一个全新的实例,这个新实例在方法结束后替换原来的实例.


```
struct area {
    var length = 1
    var breadth = 1
    
    func area() -> Int {
        return length * breadth
    }
    
    mutating func scaleBy(res: Int) {
        length *= res
        breadth *= res
        
        print(length)
        print(breadth)
    }
}

var val = area(length: 3, breadth: 5)
val.scaleBy(res: 3)
val.scaleBy(res: 30)

输出: 
9
15
270
450
```

**类型方法**


```
class Math
{
    class func abs(number: Int) -> Int
    {
        if number < 0
        {
            return (-number)
        }
        else
        {
            return number
        }
    }
}

struct absno
{
    static func abs(number: Int) -> Int
    {
        if number < 0
        {
            return (-number)
        }
        else
        {
            return number
        }
    }
}

let no = Math.abs(number: -35)
let num = absno.abs(number: -5)

print(no)
print(num)

输出: 
35
5
```

<span id="下标脚本"></span>

swift下标脚本
==============

下标脚本 可以定义在类(Class),结构体(stucture)和枚举(enumeration)这些目标中,可以认为是访问对象,集合或序列的快捷方式.someDictionary[key],someArray[index]

**语法及应用**

下标脚本允许你通过在实例后面的方括号中传入一个或者多个索引值来对实例进行访问和赋值.

语法类似于实例方法和计算型属性的混合.

与定义实例方法类似,定义下标脚本使用subscript关键字,显式声明入参(一个或多个)和返回类型,

与实例方法不同的是下标脚本可以设定为读写或只读.这种方式又有点像计算型属性的setter和getter

```
struct subexample {
    let decrementer: Int
    subscript(index: Int) -> Int {
        return decrementer / index
    }
}
let division = subexample(decrementer: 100)

print("100 除以 9 等于 \(division[9])")
print("100 除以 2 等于 \(division[2])")
print("100 除以 3 等于 \(division[3])")
print("100 除以 5 等于 \(division[5])")
print("100 除以 7 等于 \(division[7])")

输出:
100 除以 9 等于 11
100 除以 2 等于 50
100 除以 3 等于 33
100 除以 5 等于 20
100 除以 7 等于 14

//通过下标脚本来得到结果，比如 division[2] 即为 100 除以 2。
```
```
class daysofaweek {
    private var days = ["Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "saturday"]
    subscript(index: Int) -> String {
        get {
            return days[index]   // 声明下标脚本的值
        }
        set(newValue) {
            self.days[index] = newValue   // 执行赋值操作
        }
    }
}
var p = daysofaweek()

print(p[0])
print(p[1])
print(p[2])
print(p[3])

输出: 
Sunday
Monday
Tuesday
Wednesday
```

**下标脚本选项**

* 下标脚本允许任意数量的入参索引,并且每个入参类型也没有限制.
* 下标脚本的返回值也可以是任何类型
* 下标脚本可以使用变量参数和可变参数
* 一个类或结构体可以根据机身需要提供多个下标脚本实现,在定义下标脚本时通过入参数的类型进行区分,使用下标脚本时会自动匹配合适的下标脚本实现运行,这就是**下标脚本的重载**

```
struct Matrix {
    let rows: Int, columns: Int
    var print: [Double]
    init(rows: Int, columns: Int) {
        self.rows = rows
        self.columns = columns
        print = Array(repeating: 0.0, count: rows * columns)
    }
    subscript(row: Int, column: Int) -> Double {
        get {
            return print[(row * columns) + column]
        }
        set {
            print[(row * columns) + column] = newValue
        }
    }
}
// 创建了一个新的 3 行 3 列的Matrix实例
var mat = Matrix(rows: 3, columns: 3)

// 通过下标脚本设置值
mat[0,0] = 1.0
mat[0,1] = 2.0
mat[1,0] = 3.0
mat[1,1] = 5.0

// 通过下标脚本获取值
print("\(mat[0,0])")
print("\(mat[0,1])")
print("\(mat[1,0])")
print("\(mat[1,1])")
```

<span id="继承"></span>

继承
==============

关键字 override

```
class SuperClass {
    func show() {
        print("这是超类 SuperClass")
    }
}

class SubClass: SuperClass  {
    override func show() {
        print("这是子类 SubClass")
        super.show()
    }
}

let superClass = SuperClass()
superClass.show()

let subClass = SubClass()
subClass.show()

输出: 
这是超类 SuperClass
这是子类 SubClass
这是超类 SuperClass
```

**重写属性**

* 如果你在重写舒心各种提供了setter,那么你也一定要提供getter
* 如果你不想再重写版本中的getter离修改继承来的属性值,你可以直接通过super.someProperty来返回继承来的值,之中someProperty是你要重写的属性的名字

```
class Circle {
    var radius = 12.5
    var area: String {
        return "矩形半径为 \(radius) "
    }
}

class Rectangle: Circle {
    var print = 7
    override var area: String {
        return super.area + " ，但现在被重写为 \(print)"
    }
}


let rect = Rectangle()
rect.radius = 25.0
rect.print = 3
print("半径: \(rect.area)")

class Square: Rectangle {
    override var radius: Double {
        didSet {
            print = Int(radius/5.0)+1
        }
    }
}

let sq = Square()
sq.radius = 100.0
print("半径: \(sq.area)")

输出: 
半径: 矩形半径为 25.0  ，但现在被重写为 3
半径: 矩形半径为 100.0  ，但现在被重写为 21
```

**防止重写**

关键字 final

```
final class Circle {
    final var radius = 12.5
}
```

<span id="构造,析构,可选链"></span>

构造过程
==============

**可选属性类型**

如果你定制的类型包含一个逻辑上允许取值为空的存储型属性,要讲它定义为可选类型optional type(可选属性类型)

当存储属性声明为可选时,将自动初始化为nil

```
struct Rectangle {
    let length: Double?
    
    init(frombreadth breadth: Double) {
        length = breadth * 10
    }
    
    init(frombre bre: Double) {
        length = bre * 30
    }
    
    init(_ area: Double) {
        length = area
    }
}
let rectarea = Rectangle(180.0)
print("面积为：\(rectarea.length)")
输出:
面积为：Optional(180.0)
```
只要在构造过程结束前常量的值能确定, 你可以在构造过程中的任意时间点修改常量属性的值.

对于某个类实例来说,他的常量属性只能在定义的类的构造过程中修改;不能再子类中修改.

尽管length属性现在是常量,我们仍然可以在其类的构造器中设置它的值,上面的例子就是

**默认构造器**

如果结构体对所有存储型属性提供了默认值且自身没有提供定制的构造器,它们能自动获得一个**逐一成员构造器**.我们在调用逐一成员构造器时,通过与成员属性名相同的参数名进行传值来完成对成员属性的初始赋值.

```
struct Rectangle {
    var length = 100.0, breadth = 200.0
}
let area = Rectangle(length: 24.0, breadth: 32.0)
```
结构体 Rectangle 自动获得了一个逐一成员构造器 init(width:height:)。 你可以用它来为 Rectangle 创建新的实例。

**值类型的构造器代理**

构造器可以通过调用其他构造器来完成实例的部分构造过程.这一过程称为构造器搭理,它能减少多个构造器间的代码重复.

```
struct Size {
    var width = 0.0, height = 0.0
}
struct Point {
    var x = 0.0, y = 0.0
}

struct Rect {
    var origin = Point()
    var size = Size()
    init() {}
    init(origin: Point, size: Size) {
        self.origin = origin
        self.size = size
    }
    init(center: Point, size: Size) {
        let originX = center.x - (size.width / 2)
        let originY = center.y - (size.height / 2)
        self.init(origin: Point(x: originX, y: originY), size: size)
    }
}


let basicRect = Rect()
print("Size 结构体初始值: \(basicRect.size.width, basicRect.size.height) ")
print("Rect 结构体初始值: \(basicRect.origin.x, basicRect.origin.y) ")

let originRect = Rect(origin: Point(x: 2.0, y: 2.0),
    size: Size(width: 5.0, height: 5.0))

print("Size 结构体初始值: \(originRect.size.width, originRect.size.height) ")
print("Rect 结构体初始值: \(originRect.origin.x, originRect.origin.y) ")


//先通过center和size的值计算出origin的坐标。
//然后再调用（或代理给）init(origin:size:)构造器来将新的origin和size值赋值到对应的属性中
let centerRect = Rect(center: Point(x: 4.0, y: 4.0),
    size: Size(width: 3.0, height: 3.0))

print("Size 结构体初始值: \(centerRect.size.width, centerRect.size.height) ")
print("Rect 结构体初始值: \(centerRect.origin.x, centerRect.origin.y) ")

```

构造器代理规则

**值类型** :不支持继承,所有构造器代理的过程相对简单,因为它们只能代理给本身提供的其他构造器.你可以使用self.init在自定义的构造器中引用其他的属于相同值类型的构造器.

**类类型** :它可以继承自其他类,这以为着类有责任保证其所有继承的存储属性在构造时也能正确的初始化.

**指定构造器**就是普通的构造器

**便利构造器**

可以定义便利构造器来调用同一个类中的指定构造器,并未其参数提供默认值.你也可以定义便利构造器来创建一个特殊用途或特定输入的实例.

```
class mainClass {
    var no1 : Int // 局部存储变量
    init(no1 : Int) {
        self.no1 = no1 // 初始化
    }
}

class subClass : mainClass {
    var no2 : Int
    init(no1 : Int, no2 : Int) {
        self.no2 = no2
        super.init(no1:no1)
    }
    // 便利方法只需要一个参数
    override convenience init(no1: Int)  {
        self.init(no1:no1, no2:0)
    }
}
let res = mainClass(no1: 20)
let res2 = subClass(no1: 30, no2: 50)

print("res 为: \(res.no1)")
print("res2 为: \(res2.no1)")
print("res2 为: \(res2.no2)")
```

**类的可失败构造器**

语法为在init关键字后面加添问号(init?)
或是(init!)

```
struct Animal {
    let species: String
    init?(species:String){
        if species.isEmpty{
            return nil
        }
        self.species=species
    }
}
    
let somecreature = Animal(species:"")
```

析构过程
==============

**注意**

```
class Outer {
    let value = "5555"
    var inner = Inner()
    
    func fooo() {
        inner.foo()
    }
    
    class Inner {
        weak var parent: Outer! = nil
        func foo() {
            let bar = parent.value
            print(parent.value)
        }
        
    }
    
    init() {
        inner.parent = self
    }
    
}

var outer = Outer()
outer.fooo()

输出:
5555

```

```
class Outer_m {
    var counter = 0
    var inner :Inner_m? = Inner_m()
    class Inner_m {
        weak var outer: Outer_m! = nil
        init(){
//                outer.counter += 1 // 这样会报错,  因为Inner_m的init先于Outer_m的init执行
        }
        func be(){
            outer.counter += 1
        }
        deinit {
            outer.counter -= 1
        }
    }
    init(){
        inner?.outer = self
    }
    
    func foo(){
        inner?.be()
        print(counter)
        inner = nil
        print(counter)
    }
}
```

可选链 ? !
==============

```
class Person {
    var residence: Residence?
}
    
class Residence {
    var numberOfRooms = 1
}
    
let john = Person()
    
//将导致运行时错误
//        let roomCount = john.residence!.numberOfRooms
```
想使用感叹号（!）强制解析获得这个人residence属性numberOfRooms属性值，将会引发运行时错误，因为这时没有可以供解析的residence值。

``` 
// 链接可选residence?属性，如果residence存在则取回numberOfRooms的值
if let roomCount = john.residence?.numberOfRooms {
    print("John 的房间号为 \(roomCount)。")
} else {
    print("不能查看房间号")
}
输出: 不能查看房间号
```
因为这种尝试获得numberOfRooms的操作有可能失败，可选链会返回Int?类型值，或者称作"可选Int"。当residence是空的时候（上例），选择Int将会为空，因此会出现无法访问numberOfRooms的情况。
要注意的是，即使numberOfRooms是非可选Int（Int?）时这一点也成立。只要是通过可选链的请求就意味着最后numberOfRooms总是返回一个Int?而不是Int。


<span id="自动引用计数"></span>

自动引用计数(ARC)
==============

**解决实例之间循环强引用** :

* 若引用
* 无主引用

弱引用实例

```
class Module {
    let name: String
    init(name: String) { self.name = name }
    var sub: SubModule?
    deinit { print("\(name) 主模块") }
}

class SubModule {
    let number: Int
    
    init(number: Int) { self.number = number }
    
    weak var topic: Module?
    
    deinit { print("子模块 topic 数为 \(number)") }
}

var toc: Module?
var list: SubModule?
toc = Module(name: "ARC")
list = SubModule(number: 4)
toc!.sub = list
list!.topic = toc

toc = nil
list = nil

输出:
ARC 主模块
子模块 topic 数为 4

```

无主引用实例

```

class Student {
    let name: String
    var section: Marks?
    
    init(name: String) {
        self.name = name
    }
    
    deinit { print("\(name)") }
}
class Marks {
    let marks: Int
    unowned let stname: Student
    
    init(marks: Int, stname: Student) {
        self.marks = marks
        self.stname = stname
    }
    
    deinit { print("学生的分数为 \(marks)") }
}

var module: Student?
module = Student(name: "ARC")
module!.section = Marks(marks: 98, stname: module!)
module = nil

输出:
ARC
学生的分数为 98

```

**解决闭包引起的循环强引用**

当闭包和捕获的实例总是相互引用时并且总是同时销毁时,将闭包内的捕获定义为无主引用.

相反的,当捕获引用有时可能会为nil时,将闭包内的捕获定义为弱引用.

如果捕获的引用绝对不会置为nil,应该用无主引用,而不是弱引用.


```

class HTMLElement {
    
    let name: String
    let text: String?
    
    lazy var asHTML: () -> String = {
        [unowned self] in
        if let text = self.text {
            return "<\(self.name)>\(text)</\(self.name)>"
        } else {
            return "<\(self.name) />"
        }
    }
    
    init(name: String, text: String? = nil) {
        self.name = name
        self.text = text
    }
    
    deinit {
        print("\(name) 被析构")
    }
    
}

//创建并打印HTMLElement实例
var paragraph: HTMLElement? = HTMLElement(name: "p", text: "hello, world")
print(paragraph!.asHTML())

// HTMLElement实例将会被销毁，并能看到它的析构函数打印出的消息
paragraph = nil

输出:
<p>hello, world</p>
p 被析构

```

<span id="类型转换"></span>

swift类型转换
==============

swift中类型转换使用is和as操作符实现,is用于检测值得类型,as用于转换类型.

类型转换也可以用来检查一个类是否实现了某个协议.

操作符is来检查一个实例是否属于特定子类型.


```

class Subjects {
    var physics: String
    init(physics: String) {
        self.physics = physics
    }
}

class Chemistry: Subjects {
    var equations: String
    init(physics: String, equations: String) {
        self.equations = equations
        super.init(physics: physics)
    }
}

class Maths: Subjects {
    var formulae: String
    init(physics: String, formulae: String) {
        self.formulae = formulae
        super.init(physics: physics)
    }
}

let sa = [
    Chemistry(physics: "固体物理", equations: "赫兹"),
    Maths(physics: "流体动力学", formulae: "千兆赫"),
    Chemistry(physics: "热物理学", equations: "分贝"),
    Maths(physics: "天体物理学", formulae: "兆赫"),
    Maths(physics: "微分方程", formulae: "余弦级数")]
    
var chemCount = 0
var mathsCount = 0
for item in sa {
    // 如果是一个 Chemistry 类型的实例，返回 true，相反返回 false。
    if item is Chemistry {
        ++chemCount
    } else if item is Maths {
        ++mathsCount
    }
}

```

**向下转型** :操作符 as? 或 as!

当你不确定向下转型可以成功时,用类型转换的条件形式(as?).条件形式的类型转换总是返回一个可选值(optional value),并且若下转是不可能的,可选值将是nil.

只有你可以确定想下转型一定会成功时,才使用强制形式(as!).当你试图下转类型为一个不正确的类型是,强制的类型转换会触发一个运行时错误.


```

for item in sa {
    // 类型转换的条件形式
    if let show = item as? Chemistry {
        print("化学主题是: '\(show.physics)', \(show.equations)")
        // 强制形式
    } else if let example = item as? Maths {
        print("数学主题是: '\(example.physics)',  \(example.formulae)")
    }
}


```

**Any和AnyObject的类型转换**

* AnyObject可以代表任何class的实例.
* Any可以表示任何类型,包括方法类型(function types)

```

// 可以存储Any类型的数组 exampleany
var exampleany = [Any]()

exampleany.append(12)
exampleany.append(3.14159)
exampleany.append("Any 实例")
exampleany.append(Chemistry(physics: "固体物理", equations: "兆赫"))

for item2 in exampleany {
    switch item2 {
    case let someInt as Int:
        print("整型值为 \(someInt)")
    case let someDouble as Double where someDouble > 0:
        print("Pi 值为 \(someDouble)")
    case let someString as String:
        print("\(someString)")
    case let phy as Chemistry:
        print("主题 '\(phy.physics)', \(phy.equations)")
    default:
        print("None")
    }
}

输出:
整型值为 12
Pi 值为 3.14159
Any 实例
主题 '固体物理', 兆赫

```

```

// [AnyObject] 类型的数组
let saprint: [AnyObject] = [
    Chemistry(physics: "固体物理", equations: "赫兹"),
    Maths(physics: "流体动力学", formulae: "千兆赫"),
    Chemistry(physics: "热物理学", equations: "分贝"),
    Maths(physics: "天体物理学", formulae: "兆赫"),
    Maths(physics: "微分方程", formulae: "余弦级数")]
    
```

在一个switch语句的case中使用强制形式的类型转换操作符(as,而不是as?)来检查和转换到一个明确的类型.

<span id="扩展"></span>

扩展
==============

* 添加计算型属性和计算型静态属性
* 定义实例方法和类型方法
* 提供新的构造器
* 定义下标
* 定义和使用新的嵌套类型
* 使一个已有类型符合某个协议

**扩展协议**
```
extension SomeType: SomeProtocol, AnotherProctocol {
    // 协议实现写到这里
}
```

**计算型属性**

```

extension Int {
   var add: Int {return self + 100 }
}
let addition = 3.add
print("加法运算后的值：\(addition)")

```

**构造器**

扩展可以向类中添加新的便利构造器init(),但是他们不能像类中添加新的指定构造器或析构函数deinit().

**可变实例方法**

```

extension Double {
   mutating func square() {
      let pi = 3.1415
      self = pi * self * self
   }
}

var Trial1 = 3.3
Trial1.square()
print("圆的面积为: \(Trial1)")

```

**下标** 

```

extension Int {
   subscript(var multtable: Int) -> Int {
      var no1 = 1
      while multtable > 0 {
         no1 *= 10
         --multtable
      }
      return (self / no1) % 10
   }
}
    
print(12[0])
print(7869[1])

输出:
2
6

```

<span id="协议"></span>

协议
==============

如果类在遵循协议的同时拥有父类，应该将父类名放在协议名之前，以逗号分隔。

```

class SomeClass: SomeSuperClass, FirstProtocol, AnotherProtocol {
    // 类的内容
}

```

**对属性的规定**

协议用于指定特定的实例属性或类属性,而不用指定是存储属性或计算属性.此外还必须指明是只读的还是刻毒可写的.

协议中的通常用var来声明变量属性,在类型声明后加上{set get}来表示属性是可读可写的,只读属性则用{get}来表示.

```

protocol classa {
    
    var marks: Int { get set }
    var result: Bool { get }
    
    func attendance() -> String
    func markssecured() -> String
    
}

```

**对 Mutating方法的规定**

有时候需要在方法中改变它的实例.

例如: 值类型(结构体,枚举)的实例方法中,将mutating作为函数的前缀,写在func之前,表示可以在该方法中修改它所属的实例及其实例属性的值.

```

protocol daysofaweek {
    mutating func show()
}

enum days: daysofaweek {
    case sun, mon, tue, wed, thurs, fri, sat
    mutating func show() {
        switch self {
        case .sun:
            self = .sun
            print("Sunday")
        case .mon:
            self = .mon
            print("Monday")
        case .tue:
            self = .tue
            print("Tuesday")
        case .wed:
            self = .wed
            print("Wednesday")
        case .thurs:
            self = .thurs
            print("Wednesday")
        case .fri:
            self = .fri
            print("Wednesday")
        case .sat:
            self = .sat
            print("Saturday")
        default:
            print("NO Such Day")
        }
    }
}

var res = days.wed
res.show()

```

**对构造器的规定**

协议可以要求他的遵循者实现指定的构造器.

```

protocol tcpprotocol {
   init(aprot: Int)
}

```

**协议类型** : 可以作为参数,返回值,常量,变量,属性,容器的属性

**makeIterator(),map**

```

protocol Generator {
    associatedtype members
    func next() -> members?
}

var items = [10,20,30].makeIterator()
while let x = items.next() {
    print(x)
}

for lists in [1,2,3].map( {i in i*5}) {
    print(lists)
}

print([100,200,300])
print([1,2,3].map({i in i*10}))

输出:
10
20
30
5
10
15
[100, 200, 300]
[10, 20, 30]

```

可以在扩展中添加协议

**协议的继承**

协议能够继承一个或多个其他协议,可以在继承的协议继承上增加新的内容要求.

协议的继承语法与类的继承想死,多个被继承的协议间用都好分隔:

```

protocol InheritingProtocol: SomeProtocol, AnotherProtocol {
    // 协议定义
}

```

**类专属协议:**

可以在协议的继承列表中,通过天剑class关键字,限制协议只能适配到类(class)类型.

该class关键字必须是第一个出现在协议的继承列表中,其后,才是其他继承协议,

```

protocol SomeClassOnlyProtocol: class, SomeInheritedProtocol {
    // 协议定义
}

```

**协议合成**

swift支持合成多个协议,这在我们需要同时遵守多个协议是非常有用

```

protocol Stname {
    var name: String { get }
}

protocol Stage {
    var age: Int { get }
}

struct Person: Stname, Stage {
    var name: String
    var age: Int
}

func show(celebrator: Stname & Stage) {
    print("\(celebrator.name) is \(celebrator.age) years old")
}

let studname = Person(name: "Priya", age: 21)
print(studname)

let stud = Person(name: "Rehan", age: 29)
print(stud)

let student = Person(name: "Roshan", age: 19)
print(student)

输出:
Person(name: "Priya", age: 21)
Person(name: "Rehan", age: 29)
Person(name: "Roshan", age: 19)

```

**检验协议的一致性**

可以使用is和as操作符来检查是否遵循某一协议或强制转化为某已类型.

* is操作符用来检查视力是否遵循了某个协议
* as?返回一个可选值,当视力遵循协议时,返回该协议类型;否则返回nil
* as用以强制向下转型,如果强转失败,会引起运行时错误.

```

protocol HasArea {
    var area: Double { get }
}

// 定义了Circle类，都遵循了HasArea协议
class Circle: HasArea {
    let pi = 3.1415927
    var radius: Double
    var area: Double { return pi * radius * radius }
    init(radius: Double) { self.radius = radius }
}

// 定义了Country类，都遵循了HasArea协议
class Country: HasArea {
    var area: Double
    init(area: Double) { self.area = area }
}

// Animal是一个没有实现HasArea协议的类
class Animal {
    var legs: Int
    init(legs: Int) { self.legs = legs }
}

let objects: [AnyObject] = [
    Circle(radius: 2.0),
    Country(area: 243_610),
    Animal(legs: 4)
]

for object in objects {
    // 对迭代出的每一个元素进行检查，看它是否遵循了HasArea协议
    if let objectWithArea = object as? HasArea {
        print("面积为 \(objectWithArea.area)")
    } else {
        print("没有面积")
    }
}

输出:
面积为 12.5663708
面积为 243610.0
没有面积

```

<span id="泛型"></span>

swift 泛型
==============

```

// 定义一个交换两个变量的函数
func swapTwoValues<T>(_ a: inout T, _ b: inout T) {
    let temporaryA = a
    a = b
    b = temporaryA
}
 
var numb1 = 100
var numb2 = 200
 
print("交换前数据:  \(numb1) 和 \(numb2)")
swapTwoValues(&numb1, &numb2)
print("交换后数据: \(numb1) 和 \(numb2)")
 
var str1 = "A"
var str2 = "B"
 
print("交换前数据:  \(str1) 和 \(str2)")
swapTwoValues(&str1, &str2)
print("交换后数据: \(str1) 和 \(str2)")

输出:
交换前数据:  100 和 200
交换后数据: 200 和 100
交换前数据:  A 和 B
交换后数据: B 和 A

```

泛型使用了占位类型名(在这里用字母T来表示)来代替视力类型名(例如Int,String或Double)

swapTwoValues后面跟着占位类型名(T),并用尖括号括起来(<T>).这个尖括号告诉swift那个T是swapTwoValues(_:_:)函数定义内的一个占位类型名,因此swift不会去查找名为T的实际类型.

**泛型类型**

```

struct Stack<Element> {
    var items = [Element]()
    mutating func push(_ item: Element) {
        items.append(item)
    }
    mutating func pop() -> Element {
        return items.removeLast()
    }
}
 
var stackOfStrings = Stack<String>()
print("字符串元素入栈: ")
stackOfStrings.push("google")
stackOfStrings.push("runoob")
print(stackOfStrings.items);
 
let deletetos = stackOfStrings.pop()
print("出栈元素: " + deletetos)
 
var stackOfInts = Stack<Int>()
print("整数元素入栈: ")
stackOfInts.push(1)
stackOfInts.push(2)
print(stackOfInts.items);

输出:
字符串元素入栈: 
["google", "runoob"]
出栈元素: runoob
整数元素入栈: 
[1, 2]

```

这些方法被标记为mutating,因为他们需要修改结构体的items数组.

**扩展泛型类型**

```

extension Stack {
    var topItem: Element? {
       return items.isEmpty ? nil : items[items.count - 1]
    }
}
if let topItem = stackOfStrings.topItem {
    print("栈中的顶部元素是：\(topItem).")
}

```

我们也可以通过扩展一个存在的类型来指定关联类型.

例如swift的Array类型已经提供append(_:)方法,一个count属性,以及一个接受Int类型索引的下标用以检索其元素.这三个功能都符合Container协议的要求,所以你只需简单地声明Array采纳该协议就可以扩展Array.以下实例创建一个空扩展即可:

`extension Array:Container()`


**类型约束**

类型约束指定了一个必须继承自指定类的类型参数,或者遵循一个特定的协议或协议构成.

```
func someFunction<T: SomeClass, U: SomeProtocol>(someT: T, someU: U) {
    // 这里是泛型函数的函数体部分
}
```

上面这个函数有两个类型参数.第一个类型参数T,有一个要求T必须是SomeClass子类的类型约束,第二个类型参数U,有一个要求U必须符合SomeProtocol协议的类型约束.

实例

```

// 非泛型函数，查找指定字符串在数组中的索引
func findIndex(ofString valueToFind: String, in array: [String]) -> Int? {
    for (index, value) in array.enumerated() {
        if value == valueToFind {
            // 找到返回索引值
            return index
        }
    }
    return nil
}
 
 
let strings = ["google", "weibo", "taobao", "runoob", "facebook"]
if let foundIndex = findIndex(ofString: "runoob", in: strings) {
    print("runoob 的索引为 \(foundIndex)")
}

输出:
runoob 的索引为 3

```

**关联类**

swift中使用associatedtype关键字来设置关联类型实例.

下面例子定义了一个Cont协议,改协议定义了一个关联类型ItemType.

Container协议只指定了三个任何遵从Container协议的类型必须提供的功能.遵从协议的类型在满足这三个条件的情况下也可以提供其他额外的功能.

```

// Container 协议
protocol Container {
    associatedtype ItemType
    // 添加一个新元素到容器里
    mutating func append(_ item: ItemType)
    // 获取容器中元素的数
    var count: Int { get }
    // 通过索引值类型为 Int 的下标检索到容器中的每一个元素
    subscript(i: Int) -> ItemType { get }
}

// Stack 结构体遵从 Container 协议
struct Stack<Element>: Container {
    // Stack<Element> 的原始实现部分
    var items = [Element]()
    mutating func push(_ item: Element) {
        items.append(item)
    }
    mutating func pop() -> Element {
        return items.removeLast()
    }
    // Container 协议的实现部分
    mutating func append(_ item: Element) {
        self.push(item)
    }
    var count: Int {
        return items.count
    }
    subscript(i: Int) -> Element {
        return items[i]
    }
}

var tos = Stack<String>()
tos.push("google")
tos.push("runoob")
tos.push("taobao")
// 元素列表
print(tos.items)
// 元素个数
print( tos.count)

输出:
["google", "runoob", "taobao"]
3

```

**Where语句**

类型约束能够确保类型符合泛型函数或类的定义约束.

可以在参数列表中通过where语句定义参数的约束.

```

// 扩展，将 Array 当作 Container 来使用
extension Array: Container {}
 
func allItemsMatch<C1: Container, C2: Container>
    (_ someContainer: C1, _ anotherContainer: C2) -> Bool
    where C1.ItemType == C2.ItemType, C1.ItemType: Equatable {
        
        // 检查两个容器含有相同数量的元素
        if someContainer.count != anotherContainer.count {
            return false
        }
        
        // 检查每一对元素是否相等
        for i in 0..<someContainer.count {
            if someContainer[i] != anotherContainer[i] {
                return false
            }
        }
        
        // 所有元素都匹配，返回 true
        return true
}
var tos = Stack<String>()
tos.push("google")
tos.push("runoob")
tos.push("taobao")
 
var aos = ["google", "runoob", "taobao"]
 
if allItemsMatch(tos, aos) {
    print("匹配所有元素")
} else {
    print("元素不匹配")
}

输出:
匹配所有元素

```

<span id="访问控制"></span>

访问控制
==============

访问控制基于模块与源文件.

模块指的是以独立单元构建和发布的Framework或Application.在swift中的一个模块可以使用import关键字引入另外一个模块.

源文件是单个源码文件,它通常属于一个模块,源文件可以包含多个类和函数的定义.

访问级别     |  定义
----------  |--------------
public		  | 可以访问自己模块中源文件里的任何实体,别人也可以通过引入该模块来访问源文件里的所有实体.
internal    | 可以访问自己模块中源文件里的任何实体,但是别人不能访问该模块中源文件里的实体.
fileprivate | 文件内私有,只能在当前源文件中使用
private     | 只能在类中访问,离开了这个类或者结构体的作用域外面就无法访问.

public是最高级访问级别,private为最低级访问级别.

```

public class SomePublicClass {}
internal class SomeInternalClass {}
fileprivate class SomeFilePrivateClass {}
private class SomePrivateClass {}
 
public var somePublicVariable = 0
internal let someInternalConstant = 0
fileprivate func someFilePrivateFunction() {}
private func somePrivateFunction() {}

```

除非有特殊的说明,否则实体都使用默认的访问别internal.








