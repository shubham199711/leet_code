number_lookup_table = {
'I':1,
'V':5,
'X':10,
'L':50,
'C':100,
'D':500,
'M':1000
}
class Solution:
    def romanToInt(self, s: str) -> int:
       total,prev = 0, float('inf')
       for index, item in enumerate(s):
           current_val = number_lookup_table.get(item)
           total += current_val
           if(prev < current_val):
               total -= prev * 2
           prev = current_val
       return total