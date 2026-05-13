class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = [0, 0], [m-1, n-1]
        # count = 0
        # print(m, n)

        while l[0]*n + l[1] <= r[0]*n + r[1]:
            total = 0
            if r[0] == l[0]:
                total = r[1] - l[1] + 1
            else:
                total = (r[0] - l[0] - 1)*n + n - l[1] + r[1] + 1
                
            md = [l[0] + (l[1] + total//2) // n, (l[1] + total//2) % n]
            # print(l, r, total, md, matrix[md[0]][md[1]])
            if matrix[md[0]][md[1]] == target:
                return True
            elif matrix[md[0]][md[1]] < target:
                l = [md[0] + (md[1] + 1) // n, (md[1] + 1) % n]
            elif matrix[md[0]][md[1]] > target:
                if md[1] == 0:  
                    r = [md[0] - 1, n - 1]
                else:
                    r = [md[0], md[1] - 1]
            # print(l, r)
            # count += 1
            # if count == 4:
            #     return False

        return False