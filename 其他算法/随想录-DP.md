
* <a href="#动规五部曲">动规五部曲</a>
* <a href="#跳台阶">跳台阶</a>
* <a href="#746. 使⽤最⼩花费爬楼梯">746. 使⽤最⼩花费爬楼梯</a>
* <a href="#62. 不同路径">62. 不同路径</a>
* <a href="#63. 不同路径 II">63. 不同路径 II</a>
* <a href="#343. 整数拆分">343. 整数拆分</a>
* <a href="#96. 不同的二叉搜索树">96. 不同的二叉搜索树</a>
* <a href="#01背包">01背包</a>
	* <a href="#01背包二维dp">01背包二维dp</a>
	* <a href="#01背包一维dp">01背包一维dp</a>
* <a href="#416. 分割等和⼦集">416. 分割等和⼦集</a>
* <a href="#1049. 最后⼀块⽯头的重量 II">1049. 最后⼀块⽯头的重量 II</a>
* <a href="#494. ⽬标和">494. ⽬标和</a>
* <a href="#股票问题">股票问题</a>
	* <a href="#121. 买卖股票的最佳时机">121. 买卖股票的最佳时机</a>
	* <a href="#122. 买卖股票的最佳时机 II">122. 买卖股票的最佳时机 II</a>
	* <a href="#123. 买卖股票的最佳时机 III">123. 买卖股票的最佳时机 III</a>
	* <a href="#188. 买卖股票的最佳时机 IV">188. 买卖股票的最佳时机 IV</a>
	* <a href="#309.最佳买卖股票时机含冷冻期">309.最佳买卖股票时机含冷冻期</a>
	* <a href="#714.买卖股票的最佳时机含⼿续费">714.买卖股票的最佳时机含⼿续费</a>
* <a href="#子序列问题">子序列问题</a>
	* <a href="#300.最⻓递增⼦序列">300.最⻓递增⼦序列</a>
	* <a href="#674. 最⻓连续递增序列">674. 最⻓连续递增序列</a>
	* <a href="#718. 最⻓重复⼦数组">718. 最⻓重复⼦数组</a>
	* <a href="#1143.最⻓公共⼦序列">1143.最⻓公共⼦序列</a>
	* <a href="#53. 最⼤⼦序和">53. 最⼤⼦序和</a>
	* <a href="#1035.不相交的线">1035.不相交的线</a>
	* <a href="#392.判断⼦序列">392.判断⼦序列</a>
	* <a href="#115.不同的⼦序列">115.不同的⼦序列</a>
	* <a href="#72. 编辑距离">72. 编辑距离</a>

<a id="动规五部曲"></a>
动规五部曲: 

1. 确定dp[i]数组已经下标的定义
2. 确定递推公式
3. dp数组初始化
4. 确定遍历顺序
5. 举例推到dp数组


<a id="跳台阶"></a>
### 跳台阶

⼀步⼀个台阶，两个台阶，三个台阶，直到 m个台阶

`dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-m]`

```cpp
int climbstairs(int n) {
	vector<int> dp(n+1,0);
	dp[0] = 1;
	for(int i = 1;i <=n;i++){
		for(int j = 1;j <= m;j++){
			if (i-j >= 0) dp[i] += dp[i-j];
		}
	}
	return dp[n];
}
```

<a id="746. 使⽤最⼩花费爬楼梯"></a>
### 746. 使⽤最⼩花费爬楼梯

* 每个台阶对应一个非负体力话费
* 可以一次爬一个,或者两个
* 开始从下标或者1开始
* 求爬到顶最小花费

```cpp
// dp[i] 表示在i位置的最小花费
int minCostClimbingStairs(vector<int>& cost) {
    size_t n = cost.size();
    vector<int> dp(n,0);
    dp[0] = cost[0];
    dp[1] = cost[1];
    for (int i = 2; i < n; i++) {
        dp[i] = min(dp[i-1],dp[i-2]) + cost[i];
        cout << "cost[" << i << "] = " << cost[i] << "      dp[" << i << "] = " << dp[i] << endl;
    }
    return min(dp[n-1],dp[n-2]);
}

// 空间O(1)
int minCostClimbingStairs2(vector<int>& cost) {
    size_t n = cost.size();
    int dp0 = cost[0];
    int dp1 = cost[1];
    int dpi = 0;
    for (int i = 2; i < n; i++) {
        dpi = min(dp0,dp1) + cost[i];
        dp0 = dp1;
        dp1 = dpi;
    }
    return min(dp0,dp1);
}
```

<a id="62. 不同路径"></a>
### 62. 不同路径

从`(0,0)`到`(m,n)`的网格,有多少路径

```cpp
int uniquePaths(int m,int n){
    // 1. 定于dp[i][j]  (0,0) ->(i,j)的数量
    vector<vector<int>>dp(m,vector<int>(n,0));
    // 2. 初始化
    for(int i=0;i<m;i++)dp[i][0]=1;
    for(int j=0;j<n;j++)dp[0][j]=1;
    // 3.4. 动归方程 & 遍历
    for(int i=1;i<m;i++){
        for(int j=1;j<n;j++){
            dp[i][j]=dp[i-1][j]+dp[i][j-1];
        }
    }
    return dp[m-1][n-1];
}

// 优化
int uniquePaths(int m, int n) {
    vector<int> dp(n, 0);
    for(int i = 0; i < m; ++i){
        for(int j = 0; j < n; ++j){
            dp[j] = (i > 0 && j >0 ) ? dp[j] = dp[j-1] + dp[j] : 1;
        }
    }
    return dp[n-1];
}
```

<a id="63. 不同路径 II"></a>
### 63. 不同路径 II

网格中有障碍物,障碍物的坐标在obstacleGrid中

```cpp
int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
    size_t m = obstacleGrid.size();
    size_t n = obstacleGrid[0].size();
    vector<vector<int>> dp(m,vector<int>(n,0));
    for (int i=0;i<m&&obstacleGrid[i][0]==0;i++) dp[i][0] = 1;
    for (int j=0;j<n&&obstacleGrid[0][j]==0;j++) dp[0][j] = 1;
    for (int i=1; i < m; i++) {
        for (int j=1; j < n; j++) {
            dp[i][j] = obstacleGrid[i][j] == 1 ? 0 : (dp[i-1][j] + dp[i][j-1]);
        }
    }
    return dp[m-1][n-1];
}
```

<a id="343. 整数拆分"></a>
### 343. 整数拆分

给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积

```cpp
int integerBreak(int n) {
    // dp[i] 标识拆分i后得到的最大乘积
    vector<int> dp(n+1,0);
    // dp[0],dp[1]没有意义
    dp[2] = 1;
    for (int i = 3; i <= n; i++) {
        for (int j = 1; j < i; j++) {
            // dp[i] 为j*(i-j)和dp[i-j]*j的最大值
            dp[i] = max(dp[i],max(j*(i-j),dp[i-j]*j));
        }
    }
    return dp[n];
}
```
    
<a id="96. 不同的二叉搜索树"></a>
### 96. 不同的二叉搜索树
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

https://leetcode-cn.com/problems/unique-binary-search-trees/

```cpp
/*
 这道题为中等偏难, 可忽略
 当n=3时,
 dp[3] 等于以1为root的数量 + 以2为root的数量 + 以3为root的数量
 以1为root = dp[0]*dp[2]
 以2为root = dp[1]*dp[1]
 以3为root = dp[2]*dp[0]
 */
int numTrees(int n) {
    // dp[i]标识1到i为根节点组成的二叉搜索树的个数
    vector<int> dp(n+1,0);
    // 当root为null的时候,也可以看做是一个二叉搜索树
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            dp[i] += dp[j-1]*dp[i-j];
        }
    }
    return dp[n];
}
```

<a id="01背包"></a>

### 01背包

<a id="01背包二维dp"></a>

#### 01背包二维dp

```cpp
void test_2_wei_bag_problem1() {
    vector<int> weight = {1,3,4};
    vector<int> value = {15,20,30};
    int bagWeight = 4;
    // 1. dp[i][j]表示从小标[0,1]取任意个物品,放进容量为j的背包,所产生的价值
    vector<vector<int>> dp(weight.size(),vector<int>(bagWeight+1,0));
    // 2. dp[i][j] 由:
    //      a: dp[i-1][j], 背包中不放i
    //      b: dp[i-1][j-weight[i]] + value[i],背包中存放i的价值
    // => dp[i][j] = max(a,b)
    // 3. 初始化,dp[i][0] = 0,dp[0][j] = vlaue[0] (当j>=weight[0])
    for (int j=weight[0]; j<=bagWeight; j++) {
        dp[0][j] = value[0];
    }
    // 4. 遍历
    for (int i = 1; i < weight.size(); i++) { // 遍历物品
        for (int j = 1; j <= bagWeight; j++) { // 遍历背包容量
            if (j < weight[i]) {
                dp[i][j] = dp[i-1][j];
            } else {
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i]);
            }
        }
    }
    int res = dp[weight.size()-1][bagWeight];
    cout <<"test_2_wei_bag_problem1 = " << res << endl;
}
```

<a id="01背包一维dp"></a>
#### 01背包一维dp

```cpp
/*
 二维递推公式dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
 中,dp[i-1]可以拷贝存储到dp[i]中  =>
 
 1. dp[j], 容量为j,的最大价值
 2. 递推公式 dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);
 3. 初始化dp[j] 价值都是非0的, 推导中一直取最大值.则初始化为0可以
 4. 需要倒序遍历, 这样才能保证每一个物品i值被放入一次.
    如果是正序, i=0时,
    dp[1] = dp[1 - weight[0]] + value[0] = 15
    dp[2] = dp[2 - weight[0]] + value[0] = 30
    这样物品0就被使用了两次
 */
void test_1_wei_bag_problem() {
    vector<int> weight = {1,3,4};
    vector<int> value = {15,20,30};
    int bagWeight = 4;
    vector<int> dp(bagWeight+1,0);
    for (int i=0; i < weight.size(); i++) {
        for (int j = bagWeight; j>=weight[i]; j--) {
            dp[j] = max(dp[j],dp[j-weight[i]]+value[i]);
        }
    }
    cout << dp[bagWeight] << endl;
}
```

<a id="416. 分割等和⼦集"></a>
### 416. 分割等和⼦集

给定⼀个只包含正整数的⾮空数组。是否可以将这个数组分割成两个⼦集，使得两个⼦集的元素和相
等。
注意:
每个数组中的元素不会超过 100
数组的⼤⼩不会超过 200
示例 1:
输⼊: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
 
01背包问题

* 背包的体积sum/2
* 背包要放入的元素,重量为元素数值,价值也是元素数值
* 背包如果正好装满,说明找到了sum/2
* 背包中每一个元素是不可重复放入
 
1. dp[i],背包的总量为i,最大可以凑成i的子集和
2. dp[j] = max(dp[j],dp[j-num[i]]+num[i])
3. 这里价值是非负整数,所以初始化为0,如果可能有负数则初始化为INT_MIN
每个元素不会超过100,数组大小不超过200.那总和不超过20000,背包最大为10000
4. 遍历顺序,跟01背包一样,
 
```cpp
bool canPartition(vector<int>& nums) {
    int sum = 0;
    for (int i = 0; i < nums.size(); i++) {
        sum += nums[i];
    }
    if (sum % 2 == 1) return false;
    int target = sum/2;
    vector<int> dp(10001,0);
    for (int i = 0; i < nums.size(); i++) {
        for (int j = target; j >= nums[i]; j--) {
            dp[j] = max(dp[j],dp[j-nums[i]]+nums[i]);
        }
    }
    if (dp[target] == target) return true;
    return false;
}
```

<a id="1049. 最后⼀块⽯头的重量 II"></a>
### 1049. 最后⼀块⽯头的重量 II

```
有⼀堆⽯头，每块⽯头的重量都是正整数。
每⼀回合，从中选出任意两块⽯头，然后将它们⼀起粉碎。假设⽯头的重量分别为 x 和 y，且 x <= y。
那么粉碎的可能结果如下：
如果 x == y，那么两块⽯头都会被完全粉碎；
如果 x != y，那么重量为 x 的⽯头将会完全粉碎，⽽重量为 y 的⽯头新重量为 y-x。
最后，最多只会剩下⼀块⽯头。返回此⽯头最⼩的可能重量。如果没有⽯头剩下，就返回 0。
示例：
输⼊：[2,7,4,1,8,1]
输出：1
 
本题其实就是尽量让⽯头分成重量相同的两堆，相撞之后剩下的⽯头最⼩，这样就化解成01背包问题
了。
这里跟416很像,01背包问题
```

```cpp
int lastStoneWeightII(vector<int>& stones) {
    int sum = 0;
    for (int i = 0; i < stones.size(); i++) {
        sum += stones[i];
    }
    int target = sum/2;
    vector<int> dp(15001,0);
    for (int i = 0; i < stones.size(); i++) {
        for (int j = target; j >= stones[i]; j--) {
            dp[j] = max(dp[j],dp[j-stones[i]]+stones[i]);
        }
    }
    return sum-dp[target]-dp[target];
}
```


### 494. ⽬标和

<a id="494. ⽬标和"></a>

```
给定⼀个⾮负整数数组，a1, a2, ..., an, 和⼀个⽬标数，S。现在你有两个符号 + 和 -。对于数组中的任意
⼀个整数，你都可以从 + 或 -中选择⼀个符号添加在前⾯。
返回可以使最终数组和为⽬标数 S 的所有添加符号的⽅法数。
示例：
输⼊：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
⼀共有5种⽅法让最终⽬标和为3。
 
转化成01背包问题
假设加法的总和为x, 那么减法总和为sum-x
所以  x-(sum-x) = S
x = (S + sum)/2
如果 (S + sum)%2是奇数,则无解, 例如:sum=5,S=2,那x=3,不合理
 
1. dp[j] 表示装满j, 有dp[j]种方法
2. 递推公式
不考虑nums[i]的情况下,
dp[j] = dp[j-nums[i]],
将每个nums[i] 叠加起来就是dp[j]
3. 初始化, dp[0] = 1,装满容量为0的背包有一种方法
```
 
```cpp
int findTargetSumWays(vector<int>& nums, int S) {
    int sum = 0;
    for (int i=0; i < nums.size(); i++) {
        sum+=nums[i];
    }
    if (S > sum) return 0;
    if ((S+sum)%2==1) return 0;
    int bagSize = (S+sum)/2;
    vector<int> dp(bagSize+1,0);
    dp[0] = 1;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = bagSize; j >= nums[i]; j--) {
            dp[j] += dp[j-nums[i]];
        }
    }
    return dp[bagSize];
}
```

<a id="股票问题"></a>
<a id="121. 买卖股票的最佳时机"></a>
### 121. 买卖股票的最佳时机

```
给定⼀个数组 prices ，它的第 i 个元素 prices[i] 表示⼀⽀给定股票第 i 天的价格。
你只能选择 某⼀天 买⼊这只股票，并选择在 未来的某⼀个不同的⽇⼦ 卖出该股票。设计⼀个算法来计
算你所能获取的最⼤利润。
返回你可以从这笔交易中获取的最⼤利润。如果你不能获取任何利润，返回 0 。
示例 1：
输⼊：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买⼊，在第 5 天（股票价格 = 6）的时候卖出，最⼤利润 = 6-1
= 5 。注意利润不能是 7-1 = 6, 因为卖出价格需要⼤于买⼊价格；同时，你不能在买⼊前卖出股票。
```

```cpp
// 贪心法
int maxProfit(vector<int>& prices) {
    int res = 0;
    if (prices.size() < 2) return res;
    int minPrice = prices[0];
    for (int i = 1; i < prices.size(); i++) {
        int price = prices[i];
        res = max(price-minPrice,res);
        minPrice = min(price,minPrice);
    }
    return res;
}
    
// dp
int maxProfit2(vector<int>& prices) {
    size_t len = prices.size();
    if (len == 0) return 0;
    // dp[i][0] 表示第i天持有的收益
    // dp[i][1] 表示第i天卖出的收益
    vector<vector<int>> dp(len,vector<int>(2));
    // 第0天持有收益
    dp[0][0] = -prices[0];
    // 第0天卖出
    dp[0][1] = 0;
    for (int i = 1; i < len; i++) {
        dp[i][0] = max(dp[i-1][0],-prices[i]); // max(前一天已经持有,第i天买入)
        dp[i][1] = max(dp[i-1][1],prices[i]+dp[i-1][0]); // max(前一天已经卖出,第i天卖出)
    }
    return dp[len-1][1];
}

/*
 dp  空间O(1)
 dp[i] 是邮dp[i-1]推导而来
 dp[i][0] = max(dp[i-1][0],-prices[i]); // max(前一天已经持有,第i天买入)
 dp[i][1] = max(dp[i-1][1],prices[i]+dp[i-1][0]); // max(前一天已经卖出,第i天卖出)
 */
int maxProfit3(vector<int>& prices) {
    size_t len = prices.size();
    vector<vector<int>> dp(2,vector<int>(2,0));
    dp[0][0] = -prices[0];
    dp[0][1] = 0;
    for (int i = 1; i<len; i++) {
        dp[i%2][0] = max(dp[(i-1)%2][0],-prices[i]);
        dp[i%2][1] = max(dp[(i-1)%2][1],dp[(i-1)%2][0]+prices[i]);
    }
    return dp[(len-1)%2][1];
}
```
<a id="122. 买卖股票的最佳时机 II"></a>
### 122. 买卖股票的最佳时机 II

可以多次买卖

```cpp
int maxProfit_mul(vector<int>& prices) {
    size_t len = prices.size();
    if (len == 0) return 0;
    vector<vector<int>> dp(len,vector<int>(2,0));
    dp[0][0] = -prices[0];
    dp[0][1] = 0;
    for (int i = 1; i < len; i++) {
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]-prices[i]);
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i]);
    }
    return dp[len-1][1];
}
    
int maxProfit_mul2(vector<int>& prices) {
    size_t len = prices.size();
    vector<vector<int>> dp(2,vector<int>(2,0));
    dp[0][0] = -prices[0];
    dp[0][1] = 0;
    for (int i = 1; i<len; i++) {
    	  // 第i天的可以由 第i-1天已经持有,或者 第i-1天卖出,第i天持有 取最大,, 这是与 一次买卖不同点
        dp[i%2][0] = max(dp[(i-1)%2][0],dp[(i-1)%2][1]-prices[i]);
        dp[i%2][1] = max(dp[(i-1)%2][1],dp[(i-1)%2][0]+prices[i]);
    }
    return dp[(len-1)%2][1];
}
```

<a id="123. 买卖股票的最佳时机 III"></a>
### 123. 买卖股票的最佳时机 III

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 **两笔** 交易

```cpp
/*
 dp定义
 ⼀天⼀共就有五个状态，
 0. 没有操作
 1. 第⼀次买⼊
 2. 第⼀次卖出
 3. 第⼆次买⼊
 4. 第⼆次卖出
 dp[i][j]中 i表示第i天，j为 [0 - 4] 五个状态，dp[i][j]表示第i天状态j所剩最⼤现⾦
 */
int maxProfit_2times_2(vector<int>& prices) {
    if (prices.size() == 0) return 0;
    vector<int> dp(5, 0);
    dp[1] = -prices[0];
    dp[3] = -prices[0];
    for (int i = 1; i < prices.size(); i++) {
        dp[1] = max(dp[1], dp[0] - prices[i]);
        dp[2] = max(dp[2], dp[1] + prices[i]);
        dp[3] = max(dp[3], dp[2] - prices[i]);
        dp[4] = max(dp[4], dp[3] + prices[i]);
    }
    return dp[4];
}

// 上面dp[i] dp[i-1]推导而来,可以用滚动数组
int maxProfit_2times_2_2(vector<int>& prices) {
    int len = prices.size();
    if (len == 0) return 0;
    vector<int> dp(5,0);
    dp[1] = -prices[0];
    dp[3] = -prices[0];
    for (int i = 1; i < len; i++) {
        dp[1] = max(dp[1],dp[0]-prices[i]);
        dp[2] = max(dp[2],dp[1]+prices[i]);
        dp[3] = max(dp[3],dp[2]-prices[i]);
        dp[4] = max(dp[4],dp[3]+prices[i]);
    }
    return dp[4];
}
```

<a id="188. 买卖股票的最佳时机 IV"></a>

### 188. 买卖股票的最佳时机 IV

困难

```cpp
// 股票问题,买卖 k 次
int maxProfit(int k, vector<int>& prices) {
    int len = prices.size();
    if (len == 0) return 0;
    /*
     dp[i][j]
     0 不操作
     1 第一次买入
     2 第一次卖出
     3 第二次买入
     4 第二次卖出
     ...
     共有 2 * k + 1个状态
     */
    vector<vector<int>> dp(len,vector<int>(2*k+1,0));
    for (int j = 1; j < 2 * k; j += 2) {
        dp[0][j] = -prices[0];
    }
    for (int i = 1; i < len; i++) {
        for (int j = 0; j < 2 * k - 1; j+=2) {
            dp[i][j+1] = max(dp[i-1][j+1],dp[i-1][j]-prices[i]);
            dp[i][j+2] = max(dp[i-1][j+2],dp[i-1][j+1]+prices[i]);
        }
    }
    return dp[len-1][2*k];
}
```

<a id="309.最佳买卖股票时机含冷冻期"></a>
### 309.最佳买卖股票时机含冷冻期

```cpp
// 多次买卖, 卖出后冻结一天的时间
int maxProfit_lengDong(vector<int>& prices) {
    int len = prices.size();
    /*
     状态一    持有股票状态
     状态二    两天前卖出状态,度过冷冻期,
     状态三    今天卖出
     状态四    今天冷冻期,冷冻期为1天
     */
    vector<vector<int>> dp(len,vector<int>(4,0));
    dp[0][0] = -prices[0];
    dp[0][1] = 0;
    dp[0][2] = 0;
    dp[0][3] = 0;
    for (int i = 1; i < len; i++) {
        /*
         持有状态由两种情况推到:
         1.前一天已经持有
         2.当天(第i天)买入, 可买入的情况如下
            2.1 前一天是冷冻期
            2.2 前一天就已经是未持有状态(状态二)
         */
        dp[i][0] = max(dp[i-1][0],max(dp[i-1][3]-prices[i],dp[i-1][1]-prices[i]));
        /*
         状态二由下面两种情况推导:
         1. 前一天已经是状态二
         2. 前一天是冷冻状态
         */
        dp[i][1] = max(dp[i-1][1],dp[i-1][3]);
        /*
         状态三 只能由前一天为持有状态下推导
         */
        dp[i][2] = dp[i-1][0]+prices[i];
        /*
         状态四 只能是前一天卖出
         */
        dp[i][3] = dp[i-1][2];
    }
    return max(dp[len-1][3],max(dp[len-1][1],dp[len-1][2]));
}
```

<a id="714.买卖股票的最佳时机含⼿续费"></a>
### 714.买卖股票的最佳时机含⼿续费

```cpp
// 多次买卖, 每次卖出时需要交一笔手续费fee
int maxProfitWithFee(vector<int>& prices, int fee){
    int len = prices.size();
    if (len == 0) return 0;
    vector<vector<int>> dp(len,vector<int>(2,0));
    dp[0][0] = -prices[0];
    for (int i = 1; i < len; i++) {
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]-prices[i]);
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i]-fee);
    }
    return max(dp[len-1][1],dp[len-1][0]);
}
```

<a id="子序列问题"></a>
### 子序列问题

<a id="300.最⻓递增⼦序列"></a>

### 300.最⻓递增⼦序列

```cpp
给你⼀个整数数组 nums ，找到其中最⻓严格递增⼦序列的⻓度。
⼦序列是由数组派⽣⽽来的序列，删除（或不删除）数组中的元素⽽不改变其余元素的顺序。例如，
[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的⼦序列。
示例 1：
输⼊：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最⻓递增⼦序列是 [2,3,7,101]，因此⻓度为 4 。
```

```cpp
int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    // dp[i] : [0,i]的最大子序列长度
    vector<int> dp(n,0);
    int res = 0;
    for (int i=0; i<n; i++) {
        // dp[i] 起始大小至少为1
        dp[i] = 1;
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) dp[i] = max(dp[i],dp[j]+1);
        }
        if (dp[i] > res) res = dp[i];
    }
    return res;
}
```

<a id="674. 最⻓连续递增序列"></a>
### 674. 最⻓连续递增序列

```cpp
int findLengthOfLCIS(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;
    // dp[i] 以i为结尾的最大连续子序列长度
    vector<int> dp(n,1);
    int res = 1;
    for (int i = 0; i < n-1; i++) {
        if(nums[i+1] > nums[i]) dp[i+1] = dp[i] + 1;
        if (dp[i+1] > res) res = dp[i+1];
    }
    return res;
}
```

<a id="718. 最⻓重复⼦数组"></a>
### 718. 最⻓重复⼦数组

```
/*
 给两个整数数组 A 和 B ，返回两个数组中公共的、⻓度最⻓的⼦数组的⻓度。
 示例：
 输⼊：
 A: [1,2,3,2,1]
 B: [3,2,1,4,7]
 输出：3
 解释：
 ⻓度最⻓的公共⼦数组是 [3, 2, 1] 。
 */
```

```cpp
int findLength(vector<int>& A, vector<int>& B) {
    int res = 0;
    /*
     dp[i][j]表示 A的小标[0,i-1]和B的下标[0,j-1]的最大重复个数
     i-1,j-1这种表示是为了更方便初始化,和递推
     */
    vector<vector<int>> dp(A.size()+1,vector<int>(B.size()+1,0));
    for (int i = 1; i <= A.size(); i++) {
        for (int j = 1; j <= B.size(); j++) {
            if (A[i-1] == B[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            }
            if (dp[i][j] > res) res = dp[i][j];
        }
    }
    return res;
}
// 不好理解 会上面的就行
// 滚动数组解法, 因为dp[i][j] 都是由dp[i-1][j-1] 可以压缩为 dp[j]由dp[j-1],为了避免重复B从后遍历
int findLength2(vector<int>& A, vector<int>& B) {
    int res = 0;
    vector<int> dp(B.size()+1,0);
    for (int i = 1; i <= A.size(); i++) {
        for (int j = B.size();j > 0;j--) {
            if (A[i-1] == B[j-1]) {
                dp[j] = dp[j-1] + 1;
            } else {
                dp[j] = 0;
            }
            if (dp[j] > res) {
                res = dp[j];
            }
        }
    }
    return res;
}
```

<a id="1143.最⻓公共⼦序列"></a>
### 1143.最⻓公共⼦序列

```cpp
/*
 给定两个字符串 text1 和 text2，返回这两个字符串的最⻓公共⼦序列的⻓度。
 ⼀个字符串的 ⼦序列 是指这样⼀个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除
 某些字符（也可以不删除任何字符）后组成的新字符串。
 例如，"ace" 是 "abcde" 的⼦序列，但 "aec" 不是 "abcde" 的⼦序列。两个字符串的「公共⼦序列」是
 这两个字符串所共同拥有的⼦序列。
 若这两个字符串没有公共⼦序列，则返回 0。
 示例 1:
 输⼊：text1 = "abcde", text2 = "ace"
 输出：3
 解释：最⻓公共⼦序列是 "ace"，它的⻓度为 3。
 */
int longestCommonSubsequence(string text1, string text2) {
    // dp[i][j] 表示text1的[0,i-1]范围 和 text2的[0,j-1] 的公共子序列长度为dp[i][j].  为啥不是dp[i][j]表示i,j范围?  为了方便书写, 方便初始换dp
    vector<vector<int>> dp(text1.size()+1,vector<int>(text2.size()+1,0));
    int res = 0;
    for (int i = 1; i <= text1.size(); i++) {
        for (int j = 1; j <= text2.size(); j++) {
            if (text1[i-1] == text2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
            }
            if (dp[i][j] > res) {
                res = dp[i][j];
            }
        }
    }
    return res;
}
```

<a id="53. 最⼤⼦序和"></a>
### 53. 最⼤⼦序和

```cpp
/*
 给定⼀个整数数组 nums ，找到⼀个具有最⼤和的连续⼦数组（⼦数组最少包含⼀个元素），返回其最
 ⼤和。
 示例:
 输⼊: [-2,1,-3,4,-1,2,1,-5,4]
 输出: 6
 解释: 连续⼦数组 [4,-1,2,1] 的和最⼤，为 6
 */
int maxSubArray(vector<int>& nums) {
    // dp[i] 表示下标[0,i]的最大和
    vector<int> dp(nums.size(),0);
    dp[0] = nums[0];
    int res = dp[0];
    for (int i = 1; i < nums.size(); i++) {
        dp[i] = max(dp[i-1]+nums[i],nums[i]);
        if (dp[i] > res) {
            res = dp[i];
        }
    }
    return res;
}
// 贪心写法
int maxSubArray2(vector<int>& nums) {
    int sum = 0, res = INT_MIN;
    for (int i=0; i<nums.size(); i++) {
        if (sum < 0) {
            sum = nums[i];
        } else {
            sum += nums[i];
        }
        if (sum > res) {
            res = sum;
        }
    }
    return res;
}
```


<a id="1035.不相交的线"></a>
### 1035.不相交的线

```cpp
/*
 我们在两条独⽴的⽔平线上按给定的顺序写下 A 和 B 中的整数。
 现在，我们可以绘制⼀些连接两个数字 A[i] 和 B[j] 的直线，只要 A[i] == B[j]，且我们绘制的直线不与任
 何其他连线（⾮⽔平线）相交。以这种⽅法绘制线条，并返回我们可以绘制的最⼤连线数。
 
 就是求两个字符串的公共子序列
 */
int maxUncrossedLines(vector<int>& A, vector<int>& B) {
    vector<vector<int>> dp(A.size()+1,vector<int>(B.size()+1,0));
    for (int i = 1; i <= A.size(); i++) {
        for (int j = 1; j <= B.size(); j++) {
            if (A[i-1] == B[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
            }
        }
    }
    return dp[A.size()][B.size()];
}
```

<a id="392.判断⼦序列"></a>
### 392.判断⼦序列

```
给定字符串 s 和 t ，判断 s 是否为 t 的⼦序列。
字符串的⼀个⼦序列是原始字符串删除⼀些（也可以不删除）字符⽽不改变剩余字符相对位置形成的新
字符串。（例如，"ace"是"abcde"的⼀个⼦序列，⽽"aec"不是）。
示例 1：
输⼊：s = "abc", t = "ahbgdc"
输出：true
```

```cpp
bool isSubsequence(string s, string t){
    // dp[i][j] 表示,以下标i-1的为结尾的s,和以j-1为结尾的t,相同子序列长度为dp[i][j]
    vector<vector<int>> dp(s.size()+1,vector<int>(t.size()+1,0));
    for (int i = 1; i <= s.size(); i++) {
        for (int j = 1; j <= t.size(); j++) {
            if (s[i-1] == t[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                // 相当于删除t[j-1]
                dp[i][j] = dp[i][j-1];
            }
        }
    }
    if (dp[s.size()][t.size()] == t.size()) {
        return true;
    }
    return false;
}
```

<a id="115.不同的⼦序列"></a>
### 115.不同的⼦序列

```
/*
 给定⼀个字符串 s 和⼀个字符串 t ，计算在 s 的⼦序列中 t 出现的个数。
 字符串的⼀个 ⼦序列 是指，通过删除⼀些（也可以不删除）字符且不⼲扰剩余字符相对位置所组成的新
 字符串。（例如，"ACE" 是 "ABCDE" 的⼀个⼦序列，⽽ "AEC" 不是）
 题⽬数据保证答案符合 32 位带符号整数范围。
 
 输入：s = "rabbbit", t = "rabbit"
 输出：3
 输入：s = "babgbag", t = "bag"
 输出：5
 */
```

```cpp
/*
 1. dp[i][j] 表示 以s的i-1结尾的子序列中出现以j-1为结尾的t的个数
 2.
    s[i-1]==t[j-1]时 分为两部分
    1.用s[i-1]匹配:dp[i-1][j-1]
    2.不用s[i-1]匹配: => s[i-2]和t[j-1] => dp[i-1][j]
 
    s[i-1]!=t[j-1]时只能用s的i-2和之前的去匹配
    dp[i][j] = dp[i-1][j]
 */
int numDistinct(string s, string t) {
    vector<vector<uint64_t>> dp(s.size()+1,vector<uint64_t>(t.size()+1,0));
    for (int i=0;i<=s.size();i++) dp[i][0] = 1;
    for (int j=1;j<=t.size();j++) dp[0][j] = 0;
    for (int i=1; i <= s.size(); i++) {
        for (int j = 1; j <= t.size(); j++) {
            if (s[i-1] == t[j-1]) {
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
            } else {
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    return dp[s.size()][t.size()];
}
```

<a id="72. 编辑距离"></a>
### 72. 编辑距离

```
/*
 困难
 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
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
 */
```

```cpp
/*
 dp[i][j] 表示以word1的i-1为结尾和word2的j-1为结尾 操作次数
 如果 word1[i-1] = word2[j-1]时, dp[i][j] = dp[i-1][j-1]
 不等时
    1. word1[i-1]增加一个字符(一次操作) dp[i-1][j] + 1
    2. word2[j-1]增加一个字符(相当于word1删除一个) dp[i][j-1] + 1
    3. 将word1[i-1]改成word2[j-1] => dp[i-1][j-1] + 1
 初始化: dp[i][0]表示word2为空字符串, dp[i][0] = i
        dp[0][j]同理 = j
 遍历: 从前到后遍历
 */
int minDistance(string word1, string word2) {
    vector<vector<int>> dp(word1.size()+1,vector<int>(word2.size()+1,0));
    for (int i=0; i<=word1.size(); i++) {
        dp[i][0] = i;
    }
    for (int j = 0; j <=word2.size(); j++) {
        dp[0][j] = j;
    }
    for (int i = 1; i <= word1.size(); i++) {
        for (int j = 1; j <= word2.size();j++) {
            if (word1[i-1] == word2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = min(dp[i-1][j]+1,min(dp[i][j-1]+1,dp[i-1][j-1]+1));
            }
        }
    }
    return dp[word1.size()][word2.size()];
}
```