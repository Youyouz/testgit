#һ����վ��������"discuss.leetcode.com"�������˶������������Ϊ����������
#���õ���"com"����һ������"leetcode.com"����͵�һ��Ϊ"discuss.leetcode.com"��
#�����Ƿ�������"discuss.leetcode.com"ʱ��Ҳͬʱ�������丸����"leetcode.com"�Լ���������?"com"��

#����һ�������ʴ�������������ϣ�Ҫ��ֱ����ÿ�����������ʵĴ�����
#���ʽΪ���ʴ���+�ո�+��ַ�����磺"9001 discuss.leetcode.com"��

#��Դ�����ۣ�LeetCode��
#���ӣ�https://leetcode-cn.com/problems/subdomain-visit-count



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