def root(adj, s, sa, node = 0, par = -1):
    ra = 0
    ba = 0

   
    for it in adj[node]:
        if it == par:
            continue

        root(adj, s, sa, it, node)

      
        ra = max(ra, sa[it][0])
        ra = max(ra, sa[it][1])

        
        ba = max(ba, sa[it][1])


    if s[node] == 'R':
        sa[node][0] = ra + 1
        sa[node][1] = 0
    else:
        sa[node][0] = ba + 1
        sa[node][1] = ba + 1


def reroot(adj, s, ans, sa, node = 0, par = -1, red_par = 0, blue_par = 0):
    
    if s[node] == 'R':
        ans[node][0] = max(sa[node][0], 1 + red_par)
        ans[node][1] = 0
    else:
        ans[node][0] = max(sa[node][0], 1 + blue_par)
        ans[node][1] = max(sa[node][1], 1 + blue_par)

  
    fr = red_par
    sr = red_par
    fb = blue_par
    sb = blue_par

    for it in adj[node]:
        if it == par:
            continue

        
        if sa[it][0] > fr:
            sr = fr
            fr = sa[it][0]
        elif sa[it][0] > sr:
            sr = sa[it][0]

        
        if sa[it][1] > fb:
            sb = fb
            fb = sa[it][1]
        elif sa[it][1] > sb:
            sb = sa[it][1]

   
    for it in adj[node]:
        if it == par:
            continue

        new_red = 0
        new_blue = 0

        if s[node] == 'R':
           
            new_red = 1
            if sa[it][0] == fr:
                new_red += sr
            else:
                new_red += fr
            new_blue = 0
        else:

            new_red = 1
            if sa[it][1] == fb:
                new_red += sb
            else:
                new_red += fb
            new_blue = new_red

        
        reroot(adj, s, ans, sa, it, node, new_red, new_blue)

class Solution:
    def longestPath(self, s, edges):
        # code here
        n = len(s)

            
        adj = [[] for _ in range(n)]

        for e in edges:
            adj[e[0] - 1].append(e[1] - 1)
            adj[e[1] - 1].append(e[0] - 1)

            
        subTreeAns = [[0, 0] for _ in range(n)]

            
        root(adj, s, subTreeAns)

        ans = [[0, 0] for _ in range(n)]

            
        reroot(adj, s, ans, subTreeAns)

        res = 0

           
        for i in range(n):
            res = max(res, ans[i][0], ans[i][1])

        return res

        