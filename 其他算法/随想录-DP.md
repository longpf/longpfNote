
* <a href="#动规五部曲">动规五部曲</a>
* <a href="#跳台阶">跳台阶</a>
* <a href="#746. 使⽤最⼩花费爬楼梯">746. 使⽤最⼩花费爬楼梯</a>
* <a href="#62. 不同路径">62. 不同路径</a>
* <a href="#63. 不同路径 II">63. 不同路径 II</a>
* <a href="#343. 整数拆分">343. 整数拆分</a>
* <a href="#96. 不同的二叉搜索树">96. 不同的二叉搜索树</a>


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