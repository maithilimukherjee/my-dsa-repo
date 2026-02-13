class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        
        # 1. if students are more than books → impossible
        if k > n:
            return -1
        
        # 2. define search space
        # minimum possible max pages = largest single book
        low = max(arr)
        
        # maximum possible max pages = sum of all books
        high = sum(arr)
        
        # helper function to check feasibility
        def is_possible(max_pages):
            students_used = 1   # start with first student
            current_sum = 0     # pages assigned to current student
            
            for pages in arr:
                # if adding this book exceeds allowed max_pages
                if current_sum + pages > max_pages:
                    students_used += 1
                    current_sum = pages   # assign book to new student
                    
                    # if students exceed k → not feasible
                    if students_used > k:
                        return False
                else:
                    current_sum += pages
            
            return True  # allocation possible within k students
        
        # 3. binary search on answer space
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if is_possible(mid):
                result = mid      # mid works, try smaller
                high = mid - 1
            else:
                low = mid + 1     # mid too small, increase
        
        return result
