* <a href="#394. 字符串解码">394. 字符串解码</a>
* <a href="#8. 字符串转换整数 (atoi)">8. 字符串转换整数 (atoi)</a>
* <a href="#72. 编辑距离">72. 编辑距离</a>
* <a href="#43. 字符串相乘">43. 字符串相乘</a>
* <a href="#136. 只出现一次的数字">136. 只出现一次的数字</a>
* <a href="#169. 多数元素">169. 多数元素</a>
* <a href="#344. 反转字符串">344. 反转字符串</a>
* <a href="#148. 排序链表">148. 排序链表</a>
* <a href="#887. 鸡蛋掉落">887. 鸡蛋掉落</a>
* <a href="#104. 二叉树的最大深度">104. 二叉树的最大深度</a>
* <a href="#300. 最长递增子序列">300. 最长递增子序列</a>
* <a href="#19. 删除链表的倒数第 N 个结点">19. 删除链表的倒数第 N 个结点</a>
* <a href="#88. 合并两个有序数组">88. 合并两个有序数组</a>
* <a href="#292. Nim 游戏">292. Nim 游戏</a>
* <a href="#415. 字符串相加">415. 字符串相加</a>
* <a href="#160. 相交链表">160. 相交链表</a>
* <a href="#用两个栈实现队列">用两个栈实现队列</a>
* <a href="#236. 二叉树的最近公共祖先">236. 二叉树的最近公共祖先</a>



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

**看这里:**
[https://github.com/longpf/longpfNote/blob/master/其他算法/随想录-DP.md#72.%20编辑距离](https://github.com/longpf/longpfNote/blob/master/其他算法/随想录-DP.md#72.%20编辑距离)

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

<a id="148. 排序链表"></a>

### 148. 排序链表

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

```
你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：
输入：head = []
输出：[]
```

```cpp
// 自底向上 
ListNode* sortList(ListNode* head) {
    if (!head) return NULL;
    int length = 0;
    ListNode *node = head;
    while (node) {
        length ++;
        node = node->next;
    }
    ListNode *dummy = new ListNode(0);
    dummy->next = head;
    for (int subLength = 1; subLength < length; subLength <<= 1) {
        ListNode *pre = dummy, *cur = dummy->next;
        while (cur) {
            ListNode *head1 = cur;
            for (int i = 1; i < subLength && cur->next; i++) {
                cur = cur->next;
            }
            ListNode *head2 = cur->next;
            cur->next = NULL;
            cur = head2;
            for (int i = 1; i < subLength && cur && cur->next; i++) {
                cur = cur->next;
            }
            ListNode *next = NULL;
            if (cur) {
                next = cur->next;
                cur->next = NULL;
            }
//            cur->next = NULL;
            ListNode *merged = merge(head1, head2);
            pre->next = merged;
            while (pre->next) {
                pre = pre->next;
            }
            cur = next;
        }
    }
    ListNode *res = dummy->next;
    delete dummy;
    return res;
}
    
ListNode *merge(ListNode *h1,ListNode *h2) {
    ListNode *dummy = new ListNode(0);
    ListNode *pre = dummy;
    while (h1 && h2) {
        if (h1->val < h2->val) {
            pre->next = h1;
            h1 = h1->next;
        } else {
            pre->next = h2;
            h2 = h2->next;
        }
        pre = pre->next;
    }
    if (h1) pre->next = h1;
    if (h2) pre->next = h2;
    ListNode *res = dummy->next;
    delete dummy;
    dummy = NULL;
    return res;
}
```



<a id="887. 鸡蛋掉落"></a>

### 887. 鸡蛋掉落

**困难 hard**

给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。

已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。

每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。

请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？

```
 示例 1：

 输入：k = 1, n = 2
 输出：2
 解释：
 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。
 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。
 如果它没碎，那么肯定能得出 f = 2 。
 因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。
 示例 2：

 输入：k = 2, n = 6
 输出：3
 示例 3：

 输入：k = 3, n = 14
 输出：4
```

二分法 + 动态规划, 

对于任意楼层x,存在两种情况,次数函数dp(k,n)

* 蛋碎了,接下来剩余k-1个蛋,来下面判断x-1个楼层
* 蛋没碎,接下来剩余k个蛋,来判断上面剩余的n-x个楼层

函数`T1=dp(k-1,x-1)`, `T2=dp(k,n-x)`,T1是关于x的递增函数,T2是关于x的递减函数.

求对于任意楼层x的`max(t1,t2)`,那交点即为所求的答案


![](https://raw.githubusercontent.com/longpf/Resource/master/img/rengjidan.png)

```cpp
unordered_map<int, int> memo;
int dp(int k, int n) {
    // n * 100 + k 为了避免键值冲突, n增加1,key增加100,对于任何k(k<=n)都不冲突,
    if (memo.find(n * 100 + k) == memo.end()) {
        int ans;
        if (n == 0) {
            ans = 0;
        } else if (k == 1) {
            ans = n;
        } else {
            int lo = 1, hi = n;
            while (lo + 1 < hi) {
                int x = (lo + hi) / 2;
                int t1 = dp(k - 1, x - 1);
                int t2 = dp(k, n - x);
                
                if (t1 < t2) {
                    lo = x;
                } else if (t1 > t2) {
                    hi = x;
                } else {
                    lo = hi = x;
                }
            }
            // 因为T1,T2是离散函数,不是连续函数, 交点左右相差1的时候,取最小值
            ans = 1 + min(max(dp(k - 1, lo - 1), dp(k, n - lo)),
                          max(dp(k - 1, hi - 1), dp(k, n - hi)));
        }
        
        memo[n * 100 + k] = ans;
    }
    
    return memo[n * 100 + k];
}
int superEggDrop(int k, int n) {
    return dp(k, n);
}
```

<a id="104. 二叉树的最大深度"></a>

### 104. 二叉树的最大深度

```cpp
int maxDepth(TreeNode* root) {
    if (!root) {
        return 0;
    }
    int left = maxDepth(root->left);
    int right = maxDepth(root->right);
    return 1 + max(left,right);
}
```

<a id="300. 最长递增子序列"></a>

### 300. 最长递增子序列

```cpp
int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    // dp[i] 是以第i个元素结尾的最长升序子序列长度
    vector<int> dp(n,0);
    for (int i = 0; i < n; i++) {
        dp[i] = 1;
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i],dp[j]+1);
            }
        }
    }
    int res = 0;
    for (int k = 0; k < n; k++) {
        if (dp[k] > res) {
            res = dp[k];
        }
    }
    return res;
}
```

<a id="19. 删除链表的倒数第 N 个结点"></a>

### 19. 删除链表的倒数第 N 个结点

```cpp
ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode *dummy = new ListNode(0);
    dummy->next = head;
    ListNode *fast = head, *slow = dummy;
    for (int i = 0; i < n; i++) {
        if (fast) {
            fast = fast->next;
        } else {
            return NULL;
        }
    }
    while (fast) {
        fast = fast->next;
        slow = slow->next;
    }
    slow->next = slow->next->next;
    ListNode *res = dummy->next;
    delete dummy;
    return res;
}
```

<a id="88. 合并两个有序数组"></a>

### 88. 合并两个有序数组

给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

```
示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
```

```cpp
/*
 双指针 反向排序
 p1 后面有m-1-p1个元素
 p2 后面有n-1-p2个元素
 num1在p1后面有m+n-1-p1个元素
 那么必须有 m-1-p1 + n-1-p2 <= m+n-1-p1
 ==> -1 <= p2 成立
 */
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int p1 = m - 1, p2 = n - 1;
    int tail = m + n - 1;
    int cur;
    while (p1 >= 0 || p2 >= 0) {
        if (p1 == -1) {
            cur = nums2[p2--];
        } else if (p2 == -1) {
            cur = nums1[p1--];
        } else if (nums1[p1] > nums2[p2]) {
            cur = nums1[p1--];
        } else {
            cur = nums2[p2--];
        }
        nums1[tail--] = cur;
    }
}
```

<a id="292. Nim 游戏"></a>

### 292. Nim 游戏

桌子上有一堆石头。

你们轮流进行自己的回合，你作为先手。

每一回合，轮到的人拿掉 1 - 3 块石头。

拿掉最后一块石头的人就是获胜者。

```
示例 1：
输入：n = 4
输出：false
解释：如果堆中有 4 块石头，那么你永远不会赢得比赛；
因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。
示例 2：
输入：n = 1
输出：true
示例 3：
输入：n = 2
输出：true
```

```cpp
n 不能被 4 整除，那么你总是可以赢得 Nim 游戏的胜利。
推理
让我们考虑一些小例子。显而易见的是，如果石头堆中只有一块、两块、或是三块石头，那么在你的回合，你就可以把全部石子拿走，从而在游戏中取胜。而如果就像题目描述那样，堆中恰好有四块石头，你就会失败。因为在这种情况下不管你取走多少石头，总会为你的对手留下几块，使得他可以在游戏中打败你。因此，要想获胜，在你的回合中，必须避免石头堆中的石子数为 4 的情况。
	
同样地，如果有五块、六块、或是七块石头，你可以控制自己拿取的石头数，总是恰好给你的对手留下四块石头，使他输掉这场比赛。但是如果石头堆里有八块石头，你就不可避免地会输掉，因为不管你从一堆石头中挑出一块、两块还是三块，你的对手都可以选择三块、两块或一块，以确保在再一次轮到你的时候，你会面对四块石头。

 显然，它以相同的模式不断重复
 n=4,8,12,16,…
bool canWinNim(int n) {
    return (n % 4 != 0);
}
```

<a id="415. 字符串相加"></a>

### 415. 字符串相加

给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

```cpp
string addStrings(string num1, string num2) {
     int i = num1.length() - 1, j = num2.length() - 1, add = 0;
     string ans = "";
     while (i >= 0 || j >= 0 || add != 0) {
         int x = i >= 0 ? num1[i] - '0' : 0;
         int y = j >= 0 ? num2[j] - '0' : 0;
         int result = x + y + add;
         ans.push_back('0' + result % 10);
         add = result / 10;
         i -= 1;
         j -= 1;
     }
     // 计算完以后的答案需要翻转过来
     reverse(ans.begin(), ans.end());
     return ans;
 }
 
 string addStrings(string num1, string num2) {
    int m = num1.size(),n = num2.size();
    vector<int> store(m+n,0);
    int i = m-1,j = n-1, index = store.size()-1;
    int carry = 0;
    while (i >= 0 || j >=0) {
        int n1 = 0, n2 = 0;
        if (i >= 0) n1 = num1[i--]-'0';
        if (j >=0 ) n2 = num2[j--]-'0';
        int sum = n1 + n2 + carry;
        store[index--] = sum%10;
        carry = sum/10;
    }
    if (carry > 0) {
        store[index] = carry;
    }
    string res = "";
    res.push_back('0'+1);
    for (int i=0; i < store.size(); i++) {
        if (store[i]==0 && res.size()==0) continue;
        res += to_string(store[i]);
    }
    return res.size() == 0 ? "0" : res;
}
```

<a id="160. 相交链表"></a>

### 160. 相交链表

```cpp
ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    if (!headA || !headB) return NULL;
    int len1 = getLength(headA);
    int len2 = getLength(headB);
    ListNode *longList = len1 > len2 ? headA : headB;
    ListNode *shortList = longList == headA ? headB : headA;
    int dis = abs(len1 - len2);
    for (int i = 0; i < dis; i++) {
        longList = longList->next;
    }
    while (longList && shortList) {
        if (longList == shortList) {
            return longList;
        }
        longList = longList->next;
        shortList = shortList->next;
    }
    return NULL;
}
    
int getLength(ListNode *node) {
    int len = 0;
    while (node) {
        len++;
        node = node->next;
    }
    return len;
}
```

<a id="用两个栈实现队列"></a>

### 用两个栈实现队列

```cpp
class Solution
{
public:
    void push(int node){
        stack1.push(node);
    }
    int pop(){
        if (stack2.empty()) {
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        int res = -1;
        if (!stack2.empty()) {
            res = stack2.top();
            stack2.pop();
        }
        return res;
    }
    
private:
    stack<int> stack1;
    stack<int> stack2;
};
```

<a id="236. 二叉树的最近公共祖先"></a>

### 236. 二叉树的最近公共祖先

```cpp

*
 1. 一个节点是另一个的子节点
 2. 两个节点在不同分支
 3. 递归left,right
 */
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root) return NULL;
    if (root == p || root == q) return root;
    TreeNode *left = lowestCommonAncestor(root->left, p, q);
    TreeNode *right = lowestCommonAncestor(root->right, p, q);
    if (left && right) {
        return root;
    }
    return right ? right : left;
}
```