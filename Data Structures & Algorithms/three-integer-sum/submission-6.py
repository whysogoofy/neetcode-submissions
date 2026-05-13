class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        print(arr)

        output = []

        for i in range(len(arr) - 2):
            j, k = i+1, len(arr) - 1

            if i > 0 and arr[i] == arr[i-1]:
                continue
            if arr[i] > 0:
                break

            while j < k:
                # print("enter", arr[j] + arr[k] + arr[i], i, j, k, arr[i], arr[j], arr[k])
                if arr[j] + arr[k] + arr[i] > 0:
                    k -= 1
                elif arr[j] + arr[k] + arr[i] < 0:
                    j += 1
                else:
                    output.append([arr[i], arr[j], arr[k]])
                    # break
                    j += 1
                    while j < k and arr[j-1] == arr[j]:
                        j += 1

         
        # unique = []
        # for a in output:
        #     if a not in unique:
        #         unique.append(a)
        return output