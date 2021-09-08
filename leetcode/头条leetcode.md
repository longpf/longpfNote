## 头条leetcode

* <a href="#1. 两数之和">1. 两数之和</a>
* <a href="#2. 两数相加">2. 两数相加</a>
* <a href="#3. 无重复字符的最长子串">3. 无重复字符的最长子串</a>
* <a href="#4. 寻找两个正序数组的中位数">4. 寻找两个正序数组的中位数</a>
* <a href="#5. 最长回文子串">5. 最长回文子串</a>
* <a href="#7. 整数反转">7. 整数反转</a>
* <a href="#11. 盛最多水的容器">11. 盛最多水的容器</a>
* <a href="#15. 三数之和">15. 三数之和</a>
* <a href="#20. 有效的括号">20. 有效的括号</a>
* <a href="#21. 合并两个有序链表">21. 合并两个有序链表</a>
* <a href="#42. 接雨水">42. 接雨水</a>
* <a href="#46. 全排列">46. 全排列</a>
* <a href="#53. 最大子序和">53. 最大子序和</a>
* <a href="#93. 复原IP地址">93. 复原IP地址</a>
* <a href="#141. 环形链表">141. 环形链表</a>
* <a href="#146. LRU缓存机制">146. LRU缓存机制</a>
* <a href="#206. 反转链表">206. 反转链表</a>
* <a href="#321. 拼接最大数">321. 拼接最大数</a>
* <a href="#1101. 彼此熟识的最早时间">1101. 彼此熟识的最早时间</a>
* <a href="#199. 二叉树的右视图">199. 二叉树的右视图</a>
* <a href="#25. K 个一组翻转链表">25. K 个一组翻转链表</a>
* <a href="#9. 回文数">9. 回文数</a>
* <a href="#31. 下一个排列">31. 下一个排列</a>
* <a href="#200. 岛屿数量">200. 岛屿数量</a>
* <a href="#56. 合并区间">56. 合并区间</a>
* <a href="#70. 爬楼梯">70. 爬楼梯</a>
* <a href="#121. 买卖股票的最佳时机">121. 买卖股票的最佳时机</a>
* <a href="#33. 搜索旋转排序数组">33. 搜索旋转排序数组</a>
* <a href="#62. 不同路径">62. 不同路径</a>
* <a href="#92. 反转链表 II">92. 反转链表 II</a>
* <a href="#165. 比较版本号">165. 比较版本号</a>
* <a href="#322. 零钱兑换">322. 零钱兑换</a>
* <a href="#124. 二叉树中的最大路径和"> 124. 二叉树中的最大路径和</a>
* <a href="#215. 数组中的第K个最大元素">215. 数组中的第K个最大元素</a>
* <a href="#54. 螺旋矩阵">54. 螺旋矩阵</a>
* <a href="#102. 二叉树的层序遍历">102. 二叉树的层序遍历</a>
* <a href="#105. 从前序与中序遍历序列构造二叉树">105. 从前序与中序遍历序列构造二叉树</a>
* <a href="#103. 二叉树的锯齿形层序遍历">103. 二叉树的锯齿形层序遍历</a>
* <a href="#23. 合并K个升序链表">23. 合并K个升序链表</a>
* <a href="#440. 字典序的第K小数字">440. 字典序的第K小数字</a>
* <a href="#字母组合">字母组合</a>


<a id="1. 两数之和"></a>
### 1. 两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

```
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```

easy, 数组是无序的.

```cpp
解 : 
vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> res{};
    map<int,int> hash{};
    int size = nums.size();
    for (int i=0;i<size;i++) {
        hash[nums[i]] = i;
    }
    for (int i=0;i<size;i++) {
        int value = target-nums[i];
        if(hash.find(value) != hash.end() && hash[value]!=i) {
            res.push_back(i);
            res.push_back(hash[value]);
            sort(res.begin(),res.end());
            return res;
        }
    }
    return res;
}
```


<a id="2. 两数相加"></a>
### 2. 两数相加

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

```
示例
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
```

解题 :

```cpp
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    if (!l1) return l2;
    if (!l2) return l1;
    int sum = 0;
    int carry = 0;
    ListNode *res = NULL;
    ListNode *n = NULL;
    while (l1 || l2 || carry != 0) {
        int v1 = 0,v2 = 0;
        if (l1) {
           v1 = l1->val;
           l1 = l1->next;
        }
        if (l2) {
           v2 = l2->val;
           l2 = l2->next;
        }
       int sum = v1+v2+carry;
       carry = sum/10;
       ListNode *tmp = new ListNode (sum%10);
       if (!res) {
           res = tmp;
           n = tmp;
       }else{
           n->next = tmp;
           n = tmp;
       }
    }
    return res;
}
```

<a id="3. 无重复字符的最长子串"></a>

### 3. 无重复字符的最长子串

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

```cpp
输入: "abcabcbb"   输出: 3 
输入: "bbbbb" 	 输出: 1
输入: "pwwkew" 	 输出: 3
输入 "tmmzuxt"  	 输出: 5
```

滑动窗口,窗户每次向右滑动都要维护left

```cpp
int lengthOfLongestSubstring(string s) {
    vector<int> m(256,0);
    int res = 0,left = 0; // left滑动窗口左侧
    for (int i=0;i<s.size();i++) {
        char c = s[i];
        // left>m[c], 说明在left到i之间没有字符c,如果存在c,则left比m[c]小
        if (m[c]==0 || left > m[c]) {
            res = max(res,i-left+1);
        }else {
            left = m[c];
        }
        m[c] = i+1;
    }
    return res;
}
```

<a id="4. 寻找两个正序数组的中位数"></a>
### 4. 寻找两个正序数组的中位数

给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

```
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
```

**hard 困难**

```cpp
// 折半删除
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    int m = nums1.size(), n = nums2.size();
    int k = (m+n)/2;
    if ((m+n)%2==0){
        return (findKth(nums1,nums2,0,0,m,n,k)+findKth(nums1,nums2,0,0,m,n,k+1))/2.0;
    } else {
        return findKth(nums1,nums2,0,0,m,n,k+1);
    }
}
    
double findKth(vector<int> &arr1,vector<int> &arr2,int start1,int start2,int len1,int len2,int k){
    // 保证数组1的长度小于数组2
    if (len1 > len2) {
        return findKth(arr2,arr1,start2,start1,len2,len1,k);
    }
    if (len1==0) {
        return arr2[start2+k-1];
    }
    if (k==1) {
        return min(arr1[start1],arr2[start2]);
    }
    // 防止越界, nums1=[1]  nums2=[2,3,4,5,6]
    int p1 = min(k/2,len1);
    int p2 = k-p1;
    if (arr1[start1+p1-1] < arr2[start2+p2-1]) {
        // arr1的前p1个元素不在搜索范围内
        return findKth(arr1,arr2,start1+p1,start2,len1-p1,len2,k-p1);
    }
    else if (arr1[start1+p1-1] > arr2[start2+p2-1]) {
        return findKth(arr1,arr2,start1,start2+p2,len1,len2-p2,k-p2);
    }
    else {
        // 相等说明找到第k个元素
        return arr1[start1+p1-1];
    }
}
```

<a id="5. 最长回文子串"></a>
### 5. 最长回文子串

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

[https://github.com/longpf/longpfNote/blob/master/其他算法/随想录-DP.md#回文子串问题](https://github.com/longpf/longpfNote/blob/master/其他算法/随想录-DP.md#回文子串问题)

```
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

输入: "cbbd"
输出: "bb"
```

解:

```cpp
string longestPalindrome(string s) {
    int startIndex = 0,len = 0,left = 0,right = 0;
    for (int i = 0; i < (int)s.size() - 1 ;i++) {
        if (s[i]==s[i+1]){
            left = i;
            right = i+1;
            searchPalindrome(s,startIndex,len,left,right);
        }
        left = i;
        right = i;
        searchPalindrome(s,startIndex,len,left,right);
    }
    if (len==0) {
        len = s.size();
    }
    return s.substr(startIndex,len);
}
    
void searchPalindrome(string &s,int &startIndex,int &len,int left,int right) {
    int step = 1;
    while (left-step>=0 && right+step < s.size()) {
        if (s[left-step] != s[right+step])
            break;
        step++;
    }
    int length = right-left+2*step-1;
    if (length > len) {
        startIndex = left-step+1;
        len = length;
    }
}

// 动态规划解法
dp[j][i]表示字符区间[j,i]是否为回文串
i=j, 为回文串
i=j+1 && s[i]=s[j] 相邻情况为回文串
i-j>=2 && dp[j+1][i-1] 为回文串

string longestPalindrome(string s) {
    int size = s.size();
    if (size<2) return s;
    int dp[size][size];
    int left = 0,right = 0,len = 0;
    for (int i=0;i<size;i++) {
        for (int j = 0;j<i;j++) {
            dp[j][i] = (s[j]==s[i] && (i-j<2||dp[j+1][i-1]));
            if (dp[j][i] && len < i-j+1) {
                len=i-j+1;
                left=j;
                right=i;
            }
        }
        dp[i][i] = 1;
    }
    return s.substr(left,right-left+1);
}
```


<a id="7. 整数反转"></a>
### 7. 整数反转

```cpp
int reverse(int x) {
    long long res = 0;
    while (x != 0) {
        res = res * 10 + x % 10;
        x /= 10;
    }
    if (res < INT_MIN || res > INT_MAX) {
        return 0;
    }
    return  res;
}
```

<a id="11. 盛最多水的容器"></a>
### 11. 盛最多水的容器

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

```cpp
int maxArea(vector<int>& height) {
    int size = (int)height.size();
    int res = 0;
    int i = 0, j = size - 1;
    while (i < j) {
        int h = min(height[j],height[i]);
        int water = (j-i)*h;
        res = max(res,water);
        while (i<j && height[i]==h) i++;
        while (i<j && height[j]==h) j--;
    }
    return res;
}
```

<a id="15. 三数之和"></a>
### 15. 三数之和

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

**先排列,使用双指针 [解题](https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-cshi-xian-shuang-zhi-zhen-fa-tu-shi/)**

```cpp
vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res{};
        sort(nums.begin(),nums.end());
        int size = nums.size();
        int low = 0,high = 0;
        int maxIndex = size-2;
        for (int index = 0;index < size; index++) {
            int now = nums[index];
            if (now > 0) break;
            low = index+1;
            high = size-1;
            while(low < high) {
                if (nums[low]+nums[high] == -now) {
                    vector<int> sol{now,nums[low],nums[high]};
                    res.push_back(sol);
                    int key = nums[low];
                    while (low < high && nums[low] == key) {low++;}
                    key = nums[high];
                    while (low < high && nums[high] == key) { high --;}
                }
                else if (nums[low]+nums[high] > -now) { high--; } 
                else {low ++; }
            }
            while (index+1 < maxIndex && now==nums[index+1]) {  index++; }
        }
        return res;
    }
```

<a id="20. 有效的括号"></a>
### 20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

```cpp
bool isValid(string s) {
    stack<char> st{};
    for (int i=0;i<s.length();i++) {
        char c= s[i];
        if (c=='('||c=='['||c=='{') {
            st.push(c);
        }
        else {
            if (st.empty()) return false;
            if (c==')'&&st.top()!='(') return false;
            if (c==']'&&st.top()!='[') return false;
            if (c=='}'&&st.top()!='{') return false;
            st.pop();
        }
    }
    return st.empty();
}
```

<a id="21. 合并两个有序链表"></a>

### 21. 合并两个有序链表

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

解:

```cpp
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode *dummy = new ListNode(-1), *cur = dummy;
    while (l1 && l2) {
        if (l1->val < l2->val) {
            cur->next = l1;
            l1 = l1->next;
        }else {
            cur->next = l2;
            l2 = l2->next;
        }
        cur = cur->next;
    }
    cur->next = l1?l1:l2;
    ListNode *res = dummy->next;
    delete dummy;
    dummy = NULL;
    return res;
}
```

<a id="42. 接雨水"></a>
### 42. 接雨水

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png)

```
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
```

hard.  

双指针,第i个元素对总水量的贡献为R(i),设它左边的最大高度maxLeft,右侧最大高度maxRight,则1R(i)=min(maxLeft,maxRight)-height[i]`

解:

```cpp
int trap(vector<int>& height) {
    int l = 0, r = height.size()-1;
    // 左侧和右侧 可用的最大值. 第i个元素左侧可用最大值,和右侧可用最大值的存储
    int level = 0; 
    int water = 0;
    while (l < r) {
        int lower = height[height[l] < height[r] ? l++ : r--];
        level = max(level, lower);
        water += level-lower;
    }
    return water;
}
// 比上面的解法更好理解
int trap(vector<int>& height) {
    int l = 0,r = height.size()-1;
    int water = 0;
    int l_max = 0,r_max = 0;
    while (l < r) {
        if (height[l] < height[r]) {
            height[l] >= l_max ? (l_max = height[l]) : water += (l_max-height[l]);
            l++;
        }
        else {
            height[r] >= r_max ? (r_max = height[r]) : water += (r_max-height[r]);
            r--;
        }
    }
    return water;
}
```

<a id="46. 全排列"></a>
### 46. 全排列

给定一个 没有重复 数字的序列，返回其所有可能的全排列

```
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

```cpp
vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> res{};
    if (nums.size()==0) return res;
    sort(nums.begin(),nums.end());
    permuteCore(res,nums,0,nums.size());
    return res;
}

void permuteCore(vector<vector<int>> &res,vector<int> &nums,int k,int n) {
    if (k == n) {
        res.push_back(nums);
        return ;
    }
    for (int i = k;i < n; i ++ ) {
        if (nums[i]==nums[k] && i != k) {
            continue;
        }
        swap(nums[i],nums[k]);
        permuteCore(res,nums,k+1,n);
        swap(nums[i],nums[k]);
    }
}
```

<a id="53. 最大子序和"></a>
### 53. 最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

```cpp
int maxSubArray(vector<int>& nums) {
    int size = (int)nums.size();
    int max = INT_MIN, sum = 0;
    for (int i=0;i<size;i++) {
        if (sum <= 0) {
            sum = nums[i];
        } else {
            sum += nums[i];
        }
        if(sum > max) {
            max = sum;
        }
    }
    return max;
}
```

<a id="93. 复原IP地址"></a>
### 93. 复原IP地址

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

```
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
```

```cpp
class Solution {
    vector<string> res;
public:
    vector<string> restoreIpAddresses(string s) {
        string ip = "";
        dfs(s,0,ip);
        return res;
    }
    void dfs(string s,int n,string ip) {
        if (n == 4) {
            if (s.empty()) res.push_back(ip);
        } else {
            for (int k = 1; k < 4;k++) {
                if (s.size() < k) break;
                int val = stoi(s.substr(0,k));
                // 大于255 或 以0开始 剪枝
                if (val > 255 || to_string(val).size() != k) continue;
                dfs(s.substr(k),n+1,ip+s.substr(0,k)+(n==3?"":"."));
            }
        }
    }
};
```

<a id="141. 环形链表"></a>
### 141. 环形链表

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环

```cpp
bool hasCycle(ListNode *head) {
    if (!head) return false;
    ListNode *fast = head, *slow = head;
    fast = fast->next;
    if (fast) fast = fast->next;
    while(fast && fast!=slow) {
        slow = slow->next;
        fast = fast->next;
        if (fast) fast = fast->next;
    }
    if (fast!=slow) return false;
    return true;
}
```

<a id="146. LRU缓存机制"></a>
### 146. LRU缓存机制

运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

```cpp
class LRUCache {
private:
    int cap;
    list<pair<int,int>> l;
    unordered_map<int,list<pair<int,int>>::iterator> m;
public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        auto it = m.find(key);
        if (it == m.end()) return -1;
        l.splice(l.begin(),l,it->second);
        m[key] = l.begin();
        return it->second->second;
    }
    
    void put(int key, int value) {
        auto it = m.find(key);
        if (it != m.end()) {
            l.erase(it->second);
        }
        l.push_front(make_pair(key,value));
        m[key] = l.begin();
        if (m.size() > cap) {
            int k = l.rbegin()->first;
            l.pop_back();
            m.erase(k);
        }
    }
};
```

<a id="206. 反转链表"></a>
### 206. 反转链表

反转一个单链表。

```cpp
ListNode* reverseList(ListNode* head) {
    if (!head) return NULL;
    ListNode *p = head;
    ListNode *pre = NULL;
    ListNode *n = NULL;
    while (p) {
        n = p->next;
        p->next = pre;
        pre = p;
        p = n;
    }
    return pre;
}
```

<a id="321. 拼接最大数"></a>
### 321. 拼接最大数

给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

```
示例 1:
输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]

示例 2:
输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]

示例 3:
输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]
```

hard

[题解](https://leetcode-cn.com/problems/create-maximum-number/solution/cshou-xian-qiu-jie-zi-wen-ti-zai-he-bing-zi-wen-ti/)

假设最大子序列中,包含nums1的s个元素和nums2的k-s个元素.

那么可以通过反证法证明，来自nums1的s个元素，构成了nums1的长度为s的最大子序列；来自nums2的k-s个元素，构成了nums2的长度为k-s的最大子序列。

因此，可以首先分别求出nums1中长度为s的最大子序列，和nums2中长度为k-s的最大子序列，然后求它们归并起来的最大子序列的长度，最后对一切可能的s求最大值。


```cpp
vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
    vector<int> res(k,0);
    // 假设最大子序列中有s个元素来自nums1,对所有可能的s值遍历
    int n = nums1.size(),m = nums2.size();
    for (int s=max(0,k-m);s <= min(n,k);s++) {
        vector<int> tmp{};
        // nums1中长度为s的最大子序列
        vector<int> tmp1 = maxKsequence(nums1,s);
        vector<int> tmp2 = maxKsequence(nums2,k-s);
        auto iter1 = tmp1.begin(), iter2 = tmp2.begin();
        while (iter1 != tmp1.end() || iter2 != tmp2.end()) {
            // 对两个子序列进行归并
            // lexicographical_compare：比较两个序列的字典序大小
            tmp.push_back(lexicographical_compare(iter1,tmp1.end(),iter2,tmp2.end()) ? *iter2++ : *iter1++);
        }
        // 如果归并后的最大子序列大于目前已找到的最大子序列，则更新解
        res = lexicographical_compare(res.begin(),res.end(),tmp.begin(),tmp.end()) ? tmp : res;
    }
    return res;
}

vector<int> maxKsequence(vector<int> v,int k) {
    int n = v.size();
    if (k >= n) return v;
    int pop = n-k;
    vector<int> res{};
    for (int i=0;i<n;i++){
        while(!res.empty() && v[i]>res.back() && pop-->0) {
            res.pop_back();
        }
        res.push_back(v[i]);
    }
    // 截取钱k个元素
    res.resize(k);
    return res;
}
```

<a id="1101. 彼此熟识的最早时间"></a>
### 1101. 彼此熟识的最早时间

在一个社交圈子当中，有 N 个人。每个人都有一个从 0 到 N-1 唯一的 id 编号。

我们有一份日志列表 logs，其中每条记录都包含一个非负整数的时间戳，以及分属两个人的不同 id，logs[i] = [timestamp, id_A, id_B]。

每条日志标识出两个人成为好友的时间，友谊是相互的：如果 A 和 B 是好友，那么 B 和 A 也是好友。

如果 A 是 B 的好友，或者 A 是 B 的好友的好友，那么就可以认为 A 也与 B 熟识。

返回圈子里所有人之间都熟识的最早时间。如果找不到最早时间，就返回 -1 。

```
示例
输入：logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], N = 6
输出：20190301
解释：
第一次结交发生在 timestamp = 20190101，0 和 1 成为好友，社交朋友圈如下 [0,1], [2], [3], [4], [5]。
第二次结交发生在 timestamp = 20190104，3 和 4 成为好友，社交朋友圈如下 [0,1], [2], [3,4], [5].
第三次结交发生在 timestamp = 20190107，2 和 3 成为好友，社交朋友圈如下 [0,1], [2,3,4], [5].
第四次结交发生在 timestamp = 20190211，1 和 5 成为好友，社交朋友圈如下 [0,1,5], [2,3,4].
第五次结交发生在 timestamp = 20190224，2 和 4 已经是好友了。
第六次结交发生在 timestamp = 20190301，0 和 3 成为好友，大家都互相熟识了。
```

medium  

并查集: [https://zhuanlan.zhihu.com/p/93647900](https://zhuanlan.zhihu.com/p/93647900)

最基本的**并查集**，无非就是要判断什么时候所有元素都在一个集合里了。
那么**每次merge之后， N减去1， 如果N变成1了，则可以认为所有元素都在一个集合中。**

[题解](https://leetcode-cn.com/problems/the-earliest-moment-when-everyone-become-friends/solution/c-bing-cha-ji-by-klaxxi/)

```cpp
class Solution {
public:
    int earliestAcq(vector<vector<int>>& logs, int N) {
        sort(logs.begin(), logs.end());
        record.resize(N);
        for (int i = 0; i < record.size(); i++) {
            record[i] = i;
        }
        for (const auto& log : logs) {
            int x = find(log[1]);
            int y = find(log[2]);
            if (x != y) {
                record[x] = y;
                if (--N == 1) {
                    return log[0];
                }
            }
        }
        return -1;
    }
private:
    vector<int> record;
    int find(int x) {
        return record[x] == x ? x : record[x] = find(record[x]);
    }
};
```

<a id="199. 二叉树的右视图"></a>
### 199. 二叉树的右视图

给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

```
输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

```cpp
vector<int> rightSideView(TreeNode* root) {
    vector<int> res{};
    if (!root) return res;
    queue<TreeNode *> q{};
    q.push(root);
    while (!q.empty()) {
        int size = q.size();
        for (int i=0;i<size;i++) {
            TreeNode *n = q.front();
            q.pop();
            if (i == size-1) {
                res.push_back(n->val);
            }
            if (n->left) {
                q.push(n->left);
            }
            if (n->right) {
                q.push(n->right);
            }
        }
    }       
    return res;
}

//bfs
vector<int> rightSideView(TreeNode* root) {
    vector<int> res{};
    if (!root) return res;
    queue<TreeNode *> q{};
    q.push(root);
    TreeNode *last = root;
    TreeNode *nlast = NULL;
    while (!q.empty()) {
        TreeNode *n = q.front();
        q.pop();
        if (n->left) {
            q.push(n->left);
            nlast = n->left;
        }
        if (n->right) {
            q.push(n->right);
            nlast = n->right;
        }
        if (n == last) {
            res.push_back(n->val);
            last = nlast;
        }
    }       
    return res;
}
```

<a id="25. K 个一组翻转链表"></a>
### 25. K 个一组翻转链表

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

```
给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
```

**困难**

<div align="left">
<img src="https://pic.leetcode-cn.com/866b404c6b0b52fa02385e301ee907fc015742c3766c80c02e24ef3a8613e5ad-k个一组翻转链表.png" width="300" height="600">
</div>


```cpp
ListNode* reverseKGroup(ListNode* head, int k) {
    ListNode *dummy = new ListNode(0);
    dummy->next = head;
    ListNode *pre = dummy;
    ListNode *end = dummy;
    while (end->next) {
        for (int i=0;i<k && end!=NULL;i++) end = end->next;
        if (end == NULL) break;
        ListNode *start = pre->next;
        ListNode *next = end->next;
        end->next = NULL;
        pre->next = reverse(start);
        start->next = next;
        pre = start;
        end = pre;
    }
    ListNode *res = dummy->next;
    delete dummy;
    return res;
}
ListNode *reverse(ListNode *head) {
    ListNode *pre = NULL;
    ListNode *n = NULL;
    while (head) {
        n = head->next;
        head->next = pre;
        pre = head;
        head = n;
    }
    return pre;
}
```

<a id="9. 回文数"></a>
### 9. 回文数

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

```
输入: 121
输出: true

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
```

```cpp
bool isPalindrome(int x) {
    if (x < 0) return false;
    int n1 = x;
    long n2 = 0;
    while (n1 > 0) {
        n2 = (n2*10)+(n1%10);
        n1 /= 10;
    }
    return x == n2;
}
//解法2
bool isPalindrome(int x) {
    if (x<0) return false;
    int div = 1;
    while (x / div >= 10) div *= 10;
    while (x > 0)
    {
        int left = x / div;
        int right = x % 10;
        if (left != right) return false;
        //更新x
        x = (x % div) / 10;
        //更新div
        div /= 100;
    }
    //如果为0的话
    return true;
}
```

<a id="31. 下一个排列"></a>

### 31. 下一个排列

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

[http://blog.longpengfei.com/post/31-next-permutation-%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%8E%92%E5%88%97/](http://blog.longpengfei.com/post/31-next-permutation-%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%8E%92%E5%88%97/)

```
1 2 7 4 3 1  ->  1 3 1 2 4 7
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```

```cpp
void nextPermutation(vector<int>& nums) {
    int n = nums.size(),i = n - 2, j = n - 1;
    while (i >= 0 && nums[i]>=nums[i+1]) --i;
    if (i >= 0) {
        while (nums[j]<=nums[i]) j--;
        swap(nums[i],nums[j]);
    }
    reverse(nums.begin()+i+1,nums.end());
}
```

<a id="200. 岛屿数量"></a>
### 200. 岛屿数量

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

```
输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1

输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
```

```cpp
void dfs(vector<vector<char>> &grid,int r, int c){
    int rows = grid.size();
    int cols = grid[0].size();
    grid[r][c] = '0';
    if (r-1>=0 && grid[r-1][c] == '1') dfs(grid,r-1,c);
    if (r+1<rows && grid[r+1][c] == '1') dfs(grid,r+1,c);
    if (c-1>=0 && grid[r][c-1] == '1') dfs(grid,r,c-1);
    if (c+1<cols && grid[r][c+1] == '1') dfs(grid,r,c+1);
}
int numIslands(vector<vector<char>>& grid) {
    int rows = grid.size();
    if (!rows) return 0;
    int cols = grid[0].size();
    int res = 0;
    for (int r = 0;r < rows;r++) {
        for (int c = 0;c < cols;c++) {
            if (grid[r][c] == '1') {
                res++;
                dfs(grid,r,c);
            }
        }
    }
    return res;
}
```

<a id="56. 合并区间"></a>
### 56. 合并区间

给出一个区间的集合，请合并所有重叠的区间。

```
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
```

```cpp
vector<vector<int>> merge(vector<vector<int>>& intervals) {
    vector<vector<int>> res{};
    if (intervals.size()==0) return res;
    sort(intervals.begin(),intervals.end());
    vector<int> vec = intervals[0];
    for (int i = 1;i < intervals.size();i++){
        vector<int> v = intervals[i];
        if (v[0] <= vec[1]) {
            vec[1] = max(vec[1],v[1]);
        } else {
            res.push_back(vec);
            vec = v;
        }
    }
    res.push_back(vec);
    return res;
}
```

<a id="70. 爬楼梯"></a>
### 70. 爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

斐波那契,f(n)=f(n-1)+f(n-2)

```cpp
int climbStairs(int n) {
    if (n < 3) return n;
    int a = 1, b = 2;
    int c = 0;
    for (int i = 3; i <= n;i++){
        c = a+b;
        a = b;
        b = c;
    }
    return c;
}
```

<a id="121. 买卖股票的最佳时机"></a>
### 121. 买卖股票的最佳时机

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

```
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

```cpp
int maxProfit(vector<int>& prices) {
    int res = 0;
    if (prices.size() < 2) return res;
    int minPrice = prices[0];
    for (int i=1;i<prices.size();i++) {
        int price = prices[i];
        res = max(res,price-minPrice);
        minPrice = min(minPrice,price);
    }
    return res;
}
```

<a id="33. 搜索旋转排序数组"></a>
### 33. 搜索旋转排序数组

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别

```
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
```

```cpp
int search(vector<int>& nums, int target) {
    int n = nums.size();
    int i = 0,j = n-1;
    while(i <= j) {
        int mid = (i+j)/2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < nums[j]) {
            if (nums[mid] < target && nums[j] >= target) {
                i = mid + 1;
            } else {
                j = mid - 1;
            }
        }
        else {
            if (nums[i] <= target && nums[mid] > target) {
                j = mid - 1;
            } else {
                i = mid + 1;
            }
        }
    }
    return -1;
}
```

<a id="62. 不同路径"></a>
### 62. 不同路径

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

![](../leetcode_pic/robot_maze.png)

```
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

输入: m = 7, n = 3
输出: 28
```

![动态规划](../leetcode_pic/robot_maze_sol.png)

```cpp
// 回溯法 时间过长通不过
void dfs(int m,int n,int r,int c,int &res) {
    if (r == m-1 && c == n-1) {
        res ++;
        return;
    }
    if (r < m-1) dfs(m,n,r+1,c,res);
    if (c < n-1) dfs(m,n,r,c+1,res);
}
int uniquePaths(int m, int n) {
    int res = 0;
    dfs(m,n,0,0,res);
    return res;
}
// 动态规划
int uniquePaths(int m, int n) {
     vector<vector<int>> dp(m, vector<int>(n, 0));
     for(int i = 0; i < m; ++i){
         for(int j = 0; j < n; ++j){
             dp[i][j] = (i > 0 && j >0 ) ? dp[i][j-1] + dp[i-1][j] : 1;
         }
     }
     return dp[m-1][n-1];
 }
//优化
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n, 0);
        for(int i = 0; i < m; ++i){
            for(int j = 0; j < n; ++j){
                dp[j] = (i > 0 && j >0 ) ? dp[j] = dp[j-1] + dp[j] : 1;
            }
        }
        return dp[n-1];
    }
};
```

<a id="92. 反转链表 II"></a>
### 92. 反转链表 II

反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

```
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
```

```cpp
ListNode* reverseBetween(ListNode* head, int m, int n) {
    ListNode *pre = NULL, *cur = head;
    while (m>1) {
        pre = cur;
        cur = cur->next;
        m--;
        n--;
    }
    ListNode *con = pre,*tail = cur, *third = NULL;
    while (n > 0) {
        third = cur->next;
        cur->next = pre;
        pre = cur;
        cur = third;
        n--;
    }
    if (con) {
        con->next = pre;
    } else {
        head = pre;
    }
    tail->next = cur;
    return head;
}
```

<a id="165. 比较版本号"></a>

### 165. 比较版本号

比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

```
输入: version1 = "0.1", version2 = "1.1"
输出: -1

输入: version1 = "1.0.1", version2 = "1"
输出: 1

输入: version1 = "7.5.2.4", version2 = "7.5.3"
输出: -1

输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，“01” 和 “001” 表示相同的数字 “1”。

输入：version1 = "1.0", version2 = "1.0.0"
输出：0
解释：version1 没有第三级修订号，这意味着它的第三级修订号默认为 “0”。
```

```cpp
int compareVersion(string version1, string version2) {
    int i = 0,j = 0;
    while (i < version1.size()||j<version2.size()) {
        int x=i,y=j;
        while(x<version1.size()&&version1[x]!='.') x++;
        while(y<version2.size()&&version2[y]!='.') y++;
        int a = (i==x)?0:stoi(version1.substr(i,x-i));
        int b = (j==y)?0:stoi(version2.substr(j,y-j));
        if (a>b) {
            return 1;
        } else if (a<b){
            return -1;
        } else {
            i = x+1;
            j = y+1;
        }
    }
    return 0;
}

int compareVersion(string version1, string version2) {
    vector<int> v1{};
    vector<int> v2{};
    string str;
    istringstream is(version1);
    while (getline(is, str, '.')) {
        v1.push_back(stoi(str));
    }
    istringstream is2(version2);
    while (getline(is2, str, '.')) {
        v2.push_back(stoi(str));
    }
    int i = 0;
    for (; i<min(v1.size(),v2.size());) {
        if (v1[i]==v2[i]) {
            i++;
        } else if(v1[i] > v2[i]){
            return 1;
        } else {
            return -1;
        }
    }
    int j = i;
    while (j < v1.size()) {
        if (v1[j++] != 0) return 1;
    }
    j = i;
    while (j < v2.size()) {
        if (v2[j++] != 0) return -1;
    }
    return 0;
}
```

<a id="322. 零钱兑换"></a>

### 322. 零钱兑换

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

贪心算法

```cpp
int coinChange(vector<int>&coins, int amount) {
    if (amount == 0) return 0;
    sort(coins.rbegin(), coins.rend());
    int ans = INT_MAX;
    coinChangeCore(coins, 0, amount, 0, ans);
    return ans==INT_MAX?-1:ans;
}
    
void coinChangeCore(vector<int>&coins,int index,int amount,int count, int &ans) {
    if (amount == 0) {
        ans = min(ans,count);
        return;
    }
    if (index == coins.size()) return;
    for (int k=amount/coins[index]; k>=0&&count+k<ans; k--) {
        coinChangeCore(coins, index+1, amount-k*coins[index], count+k, ans);
    }
}
```

<a id="124. 二叉树中的最大路径和"></a>


### 124. 二叉树中的最大路径和

路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

     给你一个二叉树的根节点 root ，返回其 最大路径和 。
     
     输入：root = [1,2,3]
     输出：6
     解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
     
     输入：root = [-10,9,20,null,null,15,7]
     输出：42
     解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42


```cpp
int maxGain(TreeNode *root,int &res) {
    if (root == NULL) {
        return 0;
    }
    int left = max(maxGain(root->left, res),0);
    int right = max(maxGain(root->right, res),0);
    int sum = root->val + left + right;
    if (sum > res) {
        res = sum;
    }
    return root->val + max(left,right);
}
    
int maxPathSum(TreeNode* root) {
    int res = INT_MIN;
    maxGain(root, res);
    return res;
}
```

<a id = "215. 数组中的第K个最大元素"></a>

### 215. 数组中的第K个最大元素

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
 
 ```
 输入: [3,2,1,5,6,4] 和 k = 2
 输出: 5
 
 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
 输出: 4
 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
 ```
 
 ```cpp
 int findKthLargest(vector<int>& nums, int k) {
    if (nums.size() == 0 || k < 1 || k > nums.size()) return 0;
    priority_queue<int,vector<int>,greater<int>> q{};
    for (int i = 0; i<nums.size(); i++) {
        q.push(nums[i]);
        if (q.size() > k) {
            q.pop();
        }
    }
    return q.top();
}
 ```
 
<a id="54. 螺旋矩阵"></a>
 
### 54. 螺旋矩阵


给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。


```cpp
vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> res{};
    int rows = matrix.size();
    if (rows == 0) return res;
    int cols = matrix[0].size();
    if (cols == 0) return res;
    int top = 0,bottom = rows-1,left = 0,right = cols-1;
    while (top <= bottom && left <= right) {
        for (int j = left ; j <= right; j++) {
            res.push_back(matrix[top][j]);
        }
        for (int i = top + 1; i <= bottom; i++) {
            res.push_back(matrix[i][right]);
        }
        if (top < bottom) {
            for (int j = right-1; j > left; j--) {
                res.push_back(matrix[bottom][j]);
            }
        }
        if (left < right) {
            for (int i = bottom; i > top; i--) {
                res.push_back(matrix[i][left]);
            }
        }
        top++;
        bottom--;
        left++;
        right--;
    }
    return res;
}
``` 

<a id="102. 二叉树的层序遍历"></a>

### 102. 二叉树的层序遍历

 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

```
 示例：
 二叉树：[3,9,20,null,null,15,7],

     3
    / \
   9  20
     /  \
    15   7
 返回其层序遍历结果：

 [
   [3],
   [9,20],
   [15,7]
 ]
```


```cpp
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> res{};
    if (root==NULL) return res;
    queue<TreeNode *> q{};
    q.push(root);
    int toBePrint = 1;
    int nextLevel = 0;
    vector<int> nums;
    while (!q.empty()) {
        TreeNode *pNode = q.front();
        nums.push_back(pNode->val);
        if (pNode->left) {
            q.push(pNode->left);
            nextLevel++;
        }
        if (pNode->right) {
            q.push(pNode->right);
            nextLevel++;
        }
        q.pop();
        toBePrint--;
        if (toBePrint==0) {
            toBePrint = nextLevel;
            nextLevel = 0;
            res.push_back(nums);
            nums.clear();
        }
    }
    return res;
}
```

<a id="105. 从前序与中序遍历序列构造二叉树"></a>

### 105. 从前序与中序遍历序列构造二叉树

```cpp
TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    if (preorder.size()==0 || inorder.size()==0) return NULL;
    return buildTreeCore(preorder, 0, preorder.size()-1, inorder, 0, inorder.size()-1);
}
    
TreeNode *buildTreeCore(vector<int> &pre,int s1,int e1,vector<int> &in,int s2,int e2) {
    int i = s2;
    for (; i < e2; i++) {
        if (pre[s1] == in[i]) {
            break;
        }
    }
    if (i > e2) return NULL;
    TreeNode *root = new TreeNode(pre[s1]);
    root->left = buildTreeCore(pre, s1+1, s1+i-s2, in, s2, i-1);
    root->right = buildTreeCore(pre, s1+i-s2+1, e1, in, i+1, e2);
    return root;
}
```

<a id="103. 二叉树的锯齿形层序遍历"></a>

### 103. 二叉树的锯齿形层序遍历

之字型打印二叉树

```cpp
vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
    vector<vector<int>> res{};
    if (!root) return res;
    stack<TreeNode *> odd{};
    stack<TreeNode *> even{};
    odd.push(root);
    vector<int> arr{};
    while (!odd.empty() || !even.empty()) {
        while (!odd.empty()) {
            TreeNode *top= odd.top();
            arr.push_back(top->val);
            odd.pop();
            if (top->left) {
                even.push(top->left);
            }
            if (top->right) {
                even.push(top->right);
            }
        }
        if (arr.size()) {
            res.push_back(arr);
            arr.clear();
        }
        while (!even.empty()) {
            TreeNode *top = even.top();
            even.pop();
            arr.push_back(top->val);
            if (top->right) {
                odd.push(top->right);
            }
            if (top->left) {
                odd.push(top->left);
            }
        }
        if (arr.size()) {
            res.push_back(arr);
            arr.clear();
        }
    }
    return res;
}
```

### 22. 括号生成

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

```
 示例 1：
 输入：n = 3
 输出：["((()))","(()())","(())()","()(())","()()()"]
 
 示例 2：
 输入：n = 1
 输出：["()"]
```


```cpp
vector<string> generateParenthesis(int n) {
    vector<string> res{};
    generateParenthesisCore(n, n, "", res);
    return res;
}
    // left左括号剩余的个数,right右括号剩余的个数
void generateParenthesisCore(int left,int right,string out,vector<string> &res) {
    if (left > right) return; // 说明out中右括号比左括号多
    if (left == 0 && right == 0) {
        res.push_back(out);
    }
    else {
        if (left > 0) {
            generateParenthesisCore(left-1, right, out+'(', res);
        }
        if (right > 0) {
            generateParenthesisCore(left, right-1, out+')', res);
        }
    }
}
```

<a id="23. 合并K个升序链表"></a>

### 23. 合并K个升序链表

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

```cpp
// 小顶堆比较
struct cmp {
    bool operator () (ListNode *n1,ListNode *n2){
        return n1->val > n2->val;
    }
};
ListNode* mergeKLists(vector<ListNode*>& lists) {
    priority_queue<ListNode*,vector<ListNode*>,cmp> q;
    for (int i = 0; i < lists.size();i++)
    {
        if (lists[i]) q.push(lists[i]);
    }
    ListNode *head = NULL,*pre = NULL,*top = NULL;
    while (!q.empty()) {
        top = q.top();
        q.pop();
        if (!head) head = top;
        else pre->next = top;
        pre = top;
        if (top->next) q.push(top->next);
    }
    return head;
}
```

<a id="440. 字典序的第K小数字"></a>

### 440. 字典序的第K小数字

给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。

**Hard 困难**

```
注意：1 ≤ k ≤ n ≤ 109。

示例 :

输入:
n: 13   k: 2

输出:
10

解释:
字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
```

这道题如果使用大顶堆,优先级队列的方式求解, 如果n,k很大的时候, 算法用时过长,不通过

```cpp
// 获取该前缀下有多少个数
long getCount(long prefix,long n) {
    long cur = prefix;
    // 如果不是long, next可能溢出
    long next = cur+1; // 下一个前缀
    long count = 0;
    while (cur <= n) { // 当前的前缀不能大于上界
        count += min(next,n+1)-cur;
        cur *= 10;
        next *= 10;
    }
    return count;
}
    
int findKthNumber(int n, int k) {
    long p = 1; // 当前所在的位置, 当p==k时,也就是第k个数
    long prefix = 1;
    while (p < k) {
        long count = getCount(prefix, n);
        if (p + count > k) { // 说明第k个在这个范围
            p++;
            prefix *= 10;
        } else { // 扩大前缀
            prefix++;
            p += count;
        }
    }
    return static_cast<int>(prefix);
}
```

<a id="字母组合"></a>
### 字母组合

```
A:1, B:2 , C:3 ... Z:26
AB : 12
AC : 13
AD : 14
AZ : 126
126 对应的组合有  AZ/ABF/LF 
问112113114115116有多少组合
```

```cpp
void findAll(string numStr) {
    int len = numStr.length();
    vector<int> dp(len,0);
    dp[0] = 1;
    
    for (int i = 1; i < len; i++) {
        string s = "";
        s += numStr[i-1];
        s += numStr[i];
        dp[i] = dp[i-1]+(stoi(s)<27?1:0);
    }
    cout << "findAll = " << dp[len-1] << endl;
}
```
