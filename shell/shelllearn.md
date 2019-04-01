* <a href="#echo">echo</a>
* <a href="#数组">数组</a>
* <a href="#变量">变量</a>
* <a href="#Read命令">Read命令</a>
* <a href="#expr命令">expr命令</a>
* <a href="#test判断语句">test判断语句</a>
* <a href="#条件控制if">条件控制if</a>
* <a href="#case 流控制语句">case 流控制语句</a>
* <a href="#for...done">for...done</a>
* <a href="#while"> while</a>
* <a href="#使用(())扩展shell中算术运算">使用(())扩展shell中算术运算</a>
* <a href="#循环语句嵌套">循环语句嵌套</a>
* <a href="#break - continue">break - continue</a>
* <a href="#EOF">EOF</a>
* <a href="#Shift参数左移指令">Shift参数左移指令</a>
* <a href="#shell 函数使用方法">shell 函数使用方法</a>
* <a href="#正则">正则</a>
* <a href="#输出到文件">输出到文件</a>
* <a href="#判断安装">判断安装</a>
* <a href="#githook hook commit"></a>


1. `#!/bin/bash`  #!跟用shell命令的完全路径,作用:显示后期命令以哪种shell来执行这些命令. 没有指定的话,就用当前的shell
2. `#`开头表示注释
3. `chmod u+x ..` 修改执行权限


<a id="echo"></a>

### echo

* `echo "aaa\c"` 输入内容不换行需在后面加上`\c`
* `echo * ` 表示匹配当前目录下所有文件名.所以应该`echo "*"`


<a id="数组"></a>

### 数组

```bash
初始化一个数组
arr=(a b c)
arr=("add:" "change:")

数组转字符串
str=`echo ${arr[*]}`
str=${arr[@]}

数组的长度
len=${#arr[*]}

取第一个元素
${arr[1]}

取数组的所有元素
echo ${arr[@]:0}

取数组的第1-2个元素
echo ${arr[@]:1:2}

数组增加元素
arr[${#arr[*]}]=test
```


<a id="变量"></a>

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
		
		
<a id="Read命令">	</a>
		
### Read命令

* 作用: 从键盘读取数据,赋给变量

	```bash
	read a b c
	echo $a $b $c
	```
	
<a id="expr命令"></a>
		
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
	
	
<a id="test判断语句"></a>
	
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
	
<a id="条件控制if"></a>

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
	elif [ -c $file_name -o -b $file_name ] ; then
		echo "$file_name is a device file"
	else
		echo "$file_name is an unknown file"
	fi
	```
	
<a id="case 流控制语句"></a>
	
### case 流控制语句

* 格式

	```bash
	case 变量 in 
	字符串1) 命令表1
	;;
	...
	字符串n) 命令列表n
	;;
	*) 命令列表
	;;
	esac
	```
* 例子

	```bash
	#! /bin/sh
	echo "Please select your operation"
	echo "1 Copy"
	echo "2 Delete"
	echo "3 Backup"
	read op
	case $op in
	C)
	echo "your selection is Copy"
	;;
	D)
	echo "your selection is Delete"
	;;B)
	echo "your selection is Backup"
	;;
	*)
	echo "invalide selection"
	;;
	esac
	```
	
<a id="for...done"></a>

### for...done

* 格式

	```bash
	for 变量 in 名字表
	do
	命令列表
	done
	```
	
* 例子

	```bash
	#! /bin/bash
	# \换行
	for DAY in Sunday Monday Tuesday Wednesday \
	Thursday Friday Sturday
	do
		echo "the day is:$DAY"
	done
	```

<a id="while"></a>

### while 

* 格式

	```bash
	while 条件
	do
	命令
	done
	```
	
* 例子

	```bash
	#! /bin/bash
	num=1
	while [ $num -le 100 ]
	do
	squar=`expr $num \* $num`
	echo $squar
	num=`expr $num + 1`
	done
	```
	
<a id="使用(())扩展shell中算术运算"></a>
	
### 使用(())扩展shell中算术运算

* 使用方法
	* 语法 `((表达式1,表达式2))`
	* 特点:
		* 双括号中,所有表达式可以像c语言一样.如a++,b--
		* 双括号中,可以不加入`$`符号前缀
		* 可以进行逻辑运算,四则运算
		* 双括号结构扩展了for,while,if条件测试运算
		* 支持多个表达式运算,用逗号`,`分开
		
	* 例子:
		
		```bash
		#! /bin/bash
		VAR1=1
		while ((VAR1<100))
		do
			echo "$VAR1"
			((VAR1=VAR1*2))
		done
		```

<a id="循环语句嵌套"></a>
	
### 循环语句嵌套

```bash
#! /bin/bash
read -p "please enter the line number:" line
read -p "please enter th char:" char
a=1
while [ $a -le $line ]
do 
	b=1
	while [ $b -le $a ]
	do
		echo "$char\c"
		b=`expr $b + 1`
	done
	echo
	a=`expr $a + 1`
done
```

```bash
#! /bin/bash
read -p "please enter a number:" line
for (( i = 1; i <= line; i++ )); do
	for (( j = line-i; j>0; j-- )); do
		echo " \c"
	done
	for (( k = 1; k <= 2*i-1; k++ )); do
		echo "*\c"
	done
	echo
done
```

<a id="break - continue"></a>

#### break - continue

```bash
#! /bin/bash
while true; do
	echo "*************************"
	echo "please select your operation"
	echo "1 Copy"
	echo "2 Delete"
	echo "3 Backup"
	echo "4 Quit"
	read op
	case $op in
		C )
		echo "Copy"
		;;
		D )
		echo "Delete"
		;;
		B )
		echo "Backup"
		;;
		Q )
		echo "Quit"
		break
		;;
		* )
		echo "invalide selection"
		continue
	esac
done
```

<a id="EOF"></a>

### EOF

* EOF(end of file)结尾标识符
* 通常配合cat来输出用

```bash
#! /bin/bash
cat <<EOF
  *
  ***
  ********
EOF
```

<a id="Shift参数左移指令"></a>

### Shift参数左移指令

* 每执行一次,参数序列属性左移一个位置,`$#`的值减1,移出去的参数不可再用

	```bash
	#! /bin/bash
	if [ $# -le 0 ]; then
		echo "err!: not enough parameters"
		exit 124
	fi
	sum=0
	while [ $# -gt 0 ]; do
		sum=`expr $sum + $1`
		shift
	done
	echo $sum
	```
	
<a id="shell 函数使用方法"></a>
	
### shell 函数使用方法

* 语法

	```bash
	# function 可以省略不写.
	function 函数名() {
	
	}
	
	# 函数调用不带()
	# 函数调用
	函数名 参数1 参数2 ...
	
	# 函数中的变量均为全局变量,没有局部变量.
	# 调用函数时,可以传递参数.在函数中用$1,$2..来引用传递参数
	```
	
* 例子

	```bash
	#! /bin/bash
	abc=123
	example (){
		abc=456
		echo $1
		echo $2
	}
	example aaa bbb
	echo $abc
	
	输出:
	aaa
	bbb
	456
	```


<a id="正则"></a>

### 正则

* grep
	* -v 不匹配
	* -n 显示行号
	* --color 显示颜色
* 简单常用

	```bash
	grep ^root file  #过滤file中root开头的
	grep bash$ file
	grep -n --color \' file # 显示file中含有'的 \去掉特殊符号含义
	grep spoo* file
	grep g[ao] file
	grep ^[^#] file # 不以#开头的
	grep [3-5] file # 搜索含有3-5数字的
	grep ^[a-z] file # 以a-z开头的
	grep -n ^$ file  # 显示空白行
	grep r..t file #.表示任意字符,以r开头t结尾,长度为4
	grep ^g.*g file # g开头 g结尾
	```
	
	```bash
	将COMMIT_MSG_Standard中的元素转字符串匹配MSG_AHEAD
	=~表示正则匹配
	if [[ ${COMMIT_MSG_Standard[@]} =~ "$MSG_AHEAD:" ]]; then
	
	&>/dev/null等价/dev/null 2>&1. 将输出结果定向到/dev/null就是将结果丢弃,
	-w的意思就按word匹配
	if echo "${COMMIT_MSG_Standard[@]}" | grep -w "$MSG_AHEAD" &>/dev/null; then
	```
	
### sed

* stream editor 流编辑器

<a id="输出到文件"></a>

### 输出到文件

举个例子：ls test.sh test1.sh >success.txt 2>&1

将前面执行结果的标准输出流写入success.txt文件，省略了1，全句为：`ls test.sh test1.sh 1>success.txt 2>&1`

将编译日志输出到文件
`xcodebuild -project yourproject.xcodeproj -scheme YourBuildScheme -arch arm64 -sdk iphoneos > build-log.txt 2>&1`


<a id="判断安装"></a>

### 判断安装

* 判断安装XXX

	```bash
	if which oclint 2>/dev/null; then
		echo 'oclint exist'
	else
		echo 'oclint not exist'
		echo 'install oclint'
		brew tap oclint/formulae
	    brew install oclint
	fi
	
	if which xcpretty 2>/dev/null; then
		echo 'xcpretty exist'
	else
		echo 'xcpretty not exist'
		brew install xcpretty
	fi
	```

<a id="githook hook commit"></a>

### githook hook commit

* 提交规范化

	```bash
	# 获取左后一次提交
	COMMIT_EDITMSG=$1
	COMMIT_MSG=`cat $COMMIT_EDITMSG`
	# 将COMMIT_MSG以:分割去第一部分  如echo "a/b/c" |cut -d '/' -f 1输出的为a
	MSG_AHEAD=`echo $COMMIT_MSG | cut -d ':' -f 1`
	
	MSG_TYPE=$2
	
	COMMIT_MSG_Standard=("add:" "change:" "del:" "fix:")
	
	# 查看是否是add: change: del: fix:开头
	function arr_contain(){
		# 局部变量
		local arr=`echo "$1"`
		local tmp
		for tmp in ${arr[*]}; do
			if [ "$2" == "$tmp" ]; then
				echo true
				return
			fi
		done
		echo false
	}
	
	
	function hookMessage() {
	
		case $MSG_TYPE in
			message )
			
			local configUserName=`git config user.name`
			local errorLog=`echo "\033[31m 你的提交信息不规范❌ \033[0m"`
			local colorErrorUserName=`echo "\033[41;36m $configUserName \033[0m"`
			local colorSuccessUserName=`echo "\033[42;37m $configUserName \033[0m"`
	
	
			# if [[ ${COMMIT_MSG_Standard[@]} =~ "$MSG_AHEAD:" ]]; then
			# 	contain="YES"
			# else
			# 	contain="NO"
			# fi
	
			# if echo "${COMMIT_MSG_Standard[@]}" | grep -w "$MSG_AHEAD" &>/dev/null; then
			# 	contain="YES"
			# else
			# 	contain="NO"
			# fi
	
			commit_arr=`echo ${COMMIT_MSG_Standard[*]}`
			arr_contain_result=`arr_contain "$commit_arr" "$MSG_AHEAD:"`
			contain=$arr_contain_result
	
			if $contain; then
				echo
				echo
				echo "$colorSuccessUserName ✅"
				echo
				exit 0
			else
				echo
				echo Hi $colorErrorUserName $errorLog
				echo
	
	cat << EOF
	================= 请务必遵循下面规范 ================
	   ${COMMIT_MSG_Standard[0]}            ✅
	   ${COMMIT_MSG_Standard[1]}         ✅
	   ${COMMIT_MSG_Standard[2]}            ✅
	   ${COMMIT_MSG_Standard[3]}            ✅
	====================================================
	EOF
				echo
				exit 1
				fi
			;;
	
			* )
			echo "$MSGTYPE"
		 	;;
		esac
	}
	
	hookMessage
	```

	
