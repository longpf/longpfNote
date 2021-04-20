* <a href="#394. 字符串解码">394. 字符串解码</a>
* <a href="#8. 字符串转换整数 (atoi)">8. 字符串转换整数 (atoi)</a>



<a id="394. 字符串解码"></a>

### 394. 字符串解码

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: `k[encoded_string]`，表示其中方括号内部的 
`encoded_string` 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
 
```
示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
``` 

```cpp
class Solution {
    string src;
    size_t ptr;
    
    int getDigits() {
        int ret = 0;
        while (ptr < src.size() && isdigit(src[ptr])) {
            ret = ret * 10 + src[ptr++] - '0';
        }
        return ret;
    }
    string getString() {
        if (ptr == src.size() || src[ptr] == ']') {
            return "";
        }
        char cur = src[ptr];
        int repTime = 1;
        string ret;
        if (isdigit(cur)) {
            repTime = getDigits();
            ptr++; // 跳过 [
            string str = getString();
            ptr++; // 跳过 ]
            while (repTime--) { // 构造字符串
                ret += str;
            }
        }
        else if (isalpha(cur) || cur == '[') {
            ret += cur;
            ptr++;
        }
        return ret + getString();
    }
public:
    string decodeString(string s) {
        src = s;
        ptr = 0;
        return getString();
    }
};
```

<a id="8. 字符串转换整数 (atoi)"></a>
### 8. 字符串转换整数 (atoi)

函数 myAtoi(string s) 的算法如下：

读入字符串并丢弃无用的前导空格

检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 

确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。

将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。

如果整数数超过 32 位有符号整数范围 `[−2^31,  2^31 − 1]` ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 `−2^31` 的整数应该被固定为 `−2^31` ，大于 `2^31 − 1` 的整数应该被固定为 `2^31 − 1` 。

 
 ```cpp
 int myAtoi(string s) {
    if (s.size() == 0) return 0;
    int index = 0;
    while (index < s.size() && s[index] == ' ') index++;
    bool isNeg = false;
    long res = 0;
    for (int i=index; i < s.size(); i++) {
        char c = s[i];
        if (c == '+' && i == index) {
            continue;
        }
        else if (c == '-' && i== index) {
            isNeg = true;
        }
        else if ( c >= '0' && c <= '9') {
            res = res * 10 + c - '0';
            if ((!isNeg && res >= INT_MAX) || (isNeg && -res <= INT_MIN)){
                return isNeg ? INT_MIN : INT_MAX;
            }
        }
        else {
            break;
        }
    }
    return isNeg ? (-static_cast<int>(res)) : static_cast<int>(res);
}
 ```
 
 
 
 
 
 
 