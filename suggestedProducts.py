import bisect

class Solution:
    def suggestedProducts(self, products, searchWord: str):
        products.sort()
        cur, ans = '', []
        for char in searchWord:
            cur += char
            i = bisect.bisect_left(products, cur)
            ans.append([product for product in products[i : i + 3] if product.startswith(cur)])
        return ans