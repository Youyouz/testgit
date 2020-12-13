#一个网站域名，如"discuss.leetcode.com"，包含了多个子域名。作为顶级域名，
#常用的有"com"，下一级则有"leetcode.com"，最低的一级为"discuss.leetcode.com"。
#当我们访问域名"discuss.leetcode.com"时，也同时访问了其父域名"leetcode.com"以及顶级域名?"com"。

#给定一个带访问次数和域名的组合，要求分别计算每个域名被访问的次数。
#其格式为访问次数+空格+地址，例如："9001 discuss.leetcode.com"。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/subdomain-visit-count



class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        for strs in cpdomains:
            times, domain = strs.split()
            times = int(times)
            frags = domain.split('.')
            for i in range(len(frags)):
                ans['.'.join(frags[i:])] += times
        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]