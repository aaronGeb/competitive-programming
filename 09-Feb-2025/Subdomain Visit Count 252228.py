# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
      
        counts = defaultdict(int)  
        
        for entry in cpdomains:
            count, domain = entry.split() 
            count = int(count)  
            subdomains = domain.split('.')  
            
            # Generate all possible subdomains
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])  
                counts[subdomain] += count
      
        return [f"{count} {subdomain}" for subdomain, count in counts.items()]