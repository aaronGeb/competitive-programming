# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices =  prices
        self.product_price_map = {products[i]:prices[i] for i in range(len(self.products))}
        self.coustomer_count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.coustomer_count += 1
        total = 0
        for i in range(len(product)):
            total += self.product_price_map[product[i]] * amount[i]
        if self.coustomer_count % self.n == 0:
            total *=(100 - self.discount)/100
        return total



        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)