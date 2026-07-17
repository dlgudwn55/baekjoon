def solution(sales, links):
    answer = 0
    adj_lst = [[] for _ in range(len(sales)+1)]
    for a, b in links:
        adj_lst[a].append(b)
    
    dp = [[0, 0] for _ in range(len(sales)+1)]
    
    def dfs(node):
        dp[node][1] = sales[node-1]
        is_occupied = False
        tmp = 10 ** 9
        
        for child in adj_lst[node]:
            dfs(child)
            
            mn = min(dp[child][0], dp[child][1])
            dp[node][0] += mn
            dp[node][1] += mn
            
            if dp[child][1] <= dp[child][0]:
                is_occupied = True
                
            tmp = min(tmp, dp[child][1] - dp[child][0])
            
        if not is_occupied and len(adj_lst[node]) > 0:
            dp[node][0] += tmp
        
    dfs(1)
    
    return min(dp[1][0], dp[1][1])