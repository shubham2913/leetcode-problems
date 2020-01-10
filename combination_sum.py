class Solution:
    def combinationSum(self, candidates, target):
        n=len(candidates)
        dp=[[ [] for j in range(target+1)] for i in range(n+1)]
        for i in range(n+1) :
            for j in range(target+1) :
                if i==0 :
                    dp[i][j]=[]
                elif j==0 :
                    dp[i][j]=[[0]]
                else :
                    if len(dp[i-1][j])!=0 :
                        dp[i][j]+=(dp[i-1][j])
                    if candidates[i-1] <= j :
                        if len(dp[i][j-candidates[i-1]])!=0 :
                            l1=[]
                            for l in dp[i][j-candidates[i-1]] :
                                l2=[x for x in l]
                                l2.append(candidates[i-1])
                                if l2[0]==0 :
                                    l2.pop(0)
                                l1.append(l2)
                            dp[i][j]+=l1
                    # print(i,j)
                    # print(dp[1][1])
        return dp[n][target]