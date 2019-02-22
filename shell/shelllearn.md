1. `#!/bin/bash`  #!跟用shell命令的完全路径,作用:显示后期命令以哪种shell来执行这些命令. 没有指定的话,就用当前的shell
2. `#`开头表示注释
3. `chmod u+x ..` 修改执行权限

### 变量

* 使用变量时要在前面加`$`
* 用`=`赋值,左右没有空格
* 将一个命令执行结果赋给变量
	
	```bash
	A=`date`
	# 这样会输出当前时间
	echo $A 
	```
* 可以利用变量和其他字符组成一个新的字符串

	```bash
	MYDIR=/test
	echo $MYDIR/testA
	
	DAY=mon
	echo Today is $DAY day
	# {}会表示DAY是一个变量
	echo Today is ${DAY}day
	```
* `set`会列出全部的变量。`set | grep`过滤
* 给变量多个单词
	
	```bash
	NAME='xiaoming'	
	NAME="xiaoming $DAY"
	```

* 单引号和双引号的区别
	* 单引号之前的内容原封不动地指定给了变量
	* 双引号取消了空格的作用,特殊符号的含义保留.
* 删除变量 `unset NAME`
* 位置变量:命令行的第一个字作为命令名,其他作为参数

	```bash
	./example.sh file1 file2 file3
	$0 这个程序的文件名 example.sh
	$n 这个程序的第n个参数值n=1...N
	```
	
* 特殊变量

	```bash
	$*		这个程序的所有参数
	$#		参数个数
	$$		程序PID
	$!		上一个后台进程PID
	$?		执行上一个指令的返回值
	```
		
### Read命令

* 作用: 从键盘读取数据,赋给变量

	```bash
	read a b c
	echo $a $b $c
	```
		
### expr命令

* 作用: shell变量的算术运算
* 语法`expr 表达式` 注意: 表达式之间有空格

	```bash
	expr 3 + 5
	var1=8
	var2=2
	# *号有特殊意义,要用转义
	expr $var1 \* $var2
	expr $var2 \ $var2
	```
	
	```bash
	#! /bin/sh
	a=10
	b=20
	c=30
	value1=`expr $a + $b + $c`
	echo "the value of value is $value1"
	
	# 整除
	value2=`expr $c / $b`
	```

* 复杂的运算

	```bash
	var4=8
	expr `expr 5 + 11` / $var4
	```
	
### test判断语句

* `test 测试条件`
* 测试范围: 证书,字符串,文件
* 测试字符串
	
	```bash
	# 是否相等
	test $str1 == $str2
	# 是否不相等
	test $str1 != $str2
	# 如果不为空,则返回真
	test $str1
	# 如果字符串长度不为0,返回真
	test -n $str1
	test -z $str1
	
	# 以上可以简写下面的[]形式
	[ $str1 == $str2 ]
	```
	
* 测试整数

	```bash
	test int1 -eq int2
	# >=
	test int1 -ge int2
	# >
	test int1 -gt int2
	# <=
	test int1 -le int2
	# < 
	test int1 -lt int2
	# !=
	test int1 -ne int2
	
	# 也可以简写成系列形式
	[ int1 -lt int2 ]
	```
	
* 文件测试

	```bash
	test -d file		# 是否为目录
	test -f file		# 是否为文件
	test -x file		# 是否有可执行权限
	test -r file		
	test -w file
	test -e file		# 文件是否存在
	test -s file		# 测试大小是否为空,是否为空文件
	test -c file 		# 字符
	test -b file		# block,块文件
	
	# 也可以简写
	test -x file
	[ -x file ]
	```

### 条件控制if

* 语法为

	```bash
	if 条件
	then
	语句
	fi
	
	# 也可以这样
	if 条件 ; then
	语句
	fi
	
	# 复杂的if语句
	if 条件1 ; then
		命令1
	else
		命令2
	if
	
	# 更负责的if else
	if 条件1 ; then
		命令1
	elif 条件2 ; then
		命令2
	else
		命令3
	fi
	
	```
	
* 上面的`;`和`&&`的区别为: `&&`是前一个语句执行成功再回之前`&&`后面的语句.
* `-a`或`&&`表示逻辑与
* `-o`或`||`表示逻辑或
	
	```bash
	#! /bin/bash
	
	echo "input a file name"
	read file_name
	
	if [ -d $file_name ] ; then
		echo "$file_name is a dir"
	elif [ -f $file_name ] ; then
		echo "$file_name is a file"
	elif [ -c $file_name -o $file_name ] ; then
		echo "$file_name is a device file"
	else
		echo "$file_name is an unknown file"
	fi
	```