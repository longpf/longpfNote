
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