# Problem: Text Justification - https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)
        
        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            line_words = words[i:j]
            spaces_needed = maxWidth - sum(len(word) for word in line_words)
            number_of_gaps = len(line_words) - 1
            
            
            if j == n or number_of_gaps == 0:
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
             
                space, extra = divmod(spaces_needed, number_of_gaps)
                line = ''
                for k in range(number_of_gaps):
                    line += line_words[k] + ' ' * (space + (1 if k < extra else 0))
                line += line_words[-1]
            
            res.append(line)
            i = j
        
        return res
