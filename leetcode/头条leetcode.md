## 头条leetcode

* <a href="#15. 三数之和">15. 三数之和</a>
* <a href="#321. 拼接最大数">321. 拼接最大数</a>
* <a href="#1101. 彼此熟识的最早时间">1101. 彼此熟识的最早时间</a>



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