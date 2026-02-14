class Solution:
    def distMoney(self, money: int, children: int) -> int:

        if children > money:
            return -1
        if money > 8 * children: return children - 1
        remaining_money = money - children

        max_eight = remaining_money// 7
        if max_eight and remaining_money%7 ==3:
            if not children-max_eight>1:
                return max_eight-1
        return max_eight
        