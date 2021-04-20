<a href="#394. 字符串解码">394. 字符串解码</a>



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

 
 
 
 
 
 
 
 
 
 