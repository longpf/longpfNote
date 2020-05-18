## 头条leetcode

* <a href="#1. 两数之和">1. 两数之和</a>
* <a href="#2. 两数相加">2. 两数相加</a>
* <a href="#3. 无重复字符的最长子串">3. 无重复字符的最长子串</a>
* <a href="#4. 寻找两个正序数组的中位数">4. 寻找两个正序数组的中位数</a>
* <a href="#5. 最长回文子串">5. 最长回文子串</a>
* <a href="#15. 三数之和">15. 三数之和</a>
* <a href="#21. 合并两个有序链表">21. 合并两个有序链表</a>
* <a href="#42. 接雨水">42. 接雨水</a>
* <a href="#53. 最大子序和">53. 最大子序和</a>
* <a href="#321. 拼接最大数">321. 拼接最大数</a>
* <a href="#1101. 彼此熟识的最早时间">1101. 彼此熟识的最早时间</a>



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
        // left>m[c], 说明在left到i之间没有字符c
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