* <a href="#394. 字符串解码">394. 字符串解码</a>
* <a href="#8. 字符串转换整数 (atoi)">8. 字符串转换整数 (atoi)</a>
* <a href="#72. 编辑距离">72. 编辑距离</a>
* <a href="#43. 字符串相乘">43. 字符串相乘</a>
* <a href="#136. 只出现一次的数字">136. 只出现一次的数字</a>
* <a href="#169. 多数元素">169. 多数元素</a>
* <a href="#344. 反转字符串">344. 反转字符串</a>



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
        else if (isalpha(cur)) {
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
 

<a id="72. 编辑距离"></a> 
### 72. 编辑距离

**困难**

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

```
你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
``` 

```cpp
/*
 // dp[i][j] 表示word1的前i个字符 和 word2的前j个的最小编辑次数
 状态转移方程
 if word1[i-1]==word2[j-1]  -> dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1])
 else ->  dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
 */
int minDistance(string word1, string word2) {
    int m = word1.size(),n = word2.size();
    if (m == 0 || n == 0) return m + n;
    
    int dp[m+1][n+1];
    // 边界情况
    for (int i = 0; i < m+1; i++) {
        dp[i][0] = i;
    }
    for (int j = 0; j < n+1; j++) {
        dp[0][j] = j;
    }
    for (int i = 1; i < m + 1; i++) {
        for (int j = 1; j < n + 1; j++) {
            int left = dp[i-1][j];
            int down = dp[i][j-1];
            int left_down = dp[i-1][j-1];
            dp[i][j] = (word1[i-1] == word2[j-1]) ? min(min(left+1,down+1),left_down) : min(min(left+1,down+1),left_down+1);
        }
    }
    return dp[m][n];
}
```

<a id="43. 字符串相乘"></a>

### 43. 字符串相乘

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

```
 示例 1:

 输入: num1 = "2", num2 = "3"
 输出: "6"
 示例 2:

 输入: num1 = "123", num2 = "456"
 输出: "56088"
 说明：

 num1 和 num2 的长度小于110。
 num1 和 num2 只包含数字 0-9。
 num1 和 num2 均不以零开头，除非是数字 0 本身。
```

```cpp
string multiply(string num1, string num2) {
    int m = num1.size(), n = num2.size();
    vector<int> pos(m+n,0);
    for (int i = m-1; i>=0; i--) {
        for (int j = n-1; j>=0; j--) {
            int n1 = (num1[i] - '0');
            int n2 = (num2[j] - '0');
            int p1 = i + j;
            int p2 = i + j + 1;
            int sum = pos[p2] + n1 * n2;
            pos[p2] = sum % 10;
            pos[p1] += sum / 10;
        }
    }
    string res = "";
    for (int i = 0; i < pos.size(); i++) {
        if (pos[i] == 0 && res.size() == 0) continue;
        else res += to_string(pos[i]);
    }
    return res.size() == 0 ? "0" : res;
}
```

<a id="136. 只出现一次的数字"></a>

### 136. 只出现一次的数字

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

```
 说明：
 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

 示例 1:

 输入: [2,2,1]
 输出: 1
 示例 2:

 输入: [4,1,2,1,2]
 输出: 4
```

```cpp
int singleNumber(vector<int>& nums) {
    int res = 0;
    for (int i = 0; i < nums.size(); i++) {
        res ^= nums[i];
    }
    return res;
}
```

<a id="### 169. 多数元素"></a>
 
### 169. 多数元素

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 `⌊ n/2 ⌋` 的元素。

```
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1：
输入：[3,2,3]
输出：3
示例 2：
输入：[2,2,1,1,1,2,2]
输出：2
```

```cpp
int majorityElement(vector<int>& nums) {
    int count = 0;
    int cur = 0;
    for (int i=0; i < nums.size(); i++) {
        if (nums[i] == cur) {
            count++;
        }
        else if (count == 0) {
            cur = nums[i];
            count = 1;
        }
        else {
            count --;
        }
    }
    return cur;
}
```

<a id="344. 反转字符串"></a>

### 344. 反转字符串

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
	
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

```
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
```

```cpp
void reverseString(vector<char>& s) {
//        reverse(s.begin(),s.end());
    int size = s.size();
    for (int i=0; i< size/2; i++) {
        char tmp = s[i];
        s[i] = s[size-1-i];
        s[size-1-i] = tmp;
    }
}
```