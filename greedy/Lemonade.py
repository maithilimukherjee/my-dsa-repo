class Solution(object):
    def lemonadeChange(self, bills):
        """
        Determines if it's possible to give correct change to every customer.

        :param bills: List[int] - sequence of bills given by customers in order
        :return: bool - True if change can be given to all customers, False otherwise
        """
        c5 = 0   # count of $5 bills
        c10 = 0  # count of $10 bills
        
        for bill in bills:
            if bill == 5:
                c5 += 1
            elif bill == 10:
                if c5 == 0:
                    return False
                c5 -= 1
                c10 += 1
            else:  # bill == 20
                if c10 > 0 and c5 > 0:
                    c10 -= 1
                    c5 -= 1
                elif c5 >= 3:
                    c5 -= 3
                else:
                    return False
        return True


if __name__ == "__main__":
    # sample test cases
    sol = Solution()
    print(sol.lemonadeChange([5, 5, 5, 10, 20]))  # True
    print(sol.lemonadeChange([5, 5, 10, 10, 20])) # False
