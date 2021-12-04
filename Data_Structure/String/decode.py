"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string
inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

# Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

def decodeString(s):
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] !="[":
                    substr = stack.pop() + substr
                stack.pop()
                    
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                    
                stack.append(int(k) * substr)
                
        return "".join(stack)

s = "3[a]2[bc]"
print(decodeString(s))