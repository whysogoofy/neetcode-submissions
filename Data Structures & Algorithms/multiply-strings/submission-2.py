class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        
        output = ["0"] * ((len(num2) + len(num1))*2)

        for i in range(len(num1)-1, -1, -1):
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                prod = int(num1[i])*int(num2[j])
                out_idx = len(output) - len(num1) - len(num2) + i + j + 1
                # print(out_idx, i, j)
                place_sum = int(output[out_idx]) + prod + carry
                # print("place_sum", place_sum)
                output[out_idx] = str(place_sum % 10)
                if place_sum > 9:
                    carry = place_sum // 10
                else:
                    carry = 0
            
            if carry:
                out_idx = len(output) - len(num1) - len(num2) + i
                outsum = int(output[out_idx]) + carry
                output[out_idx] = str(outsum % 10)

        trim_idx = 0
        # print(output)

        for i in range(len(output)):
            if output[i] == "0":
                trim_idx += 1
            else:
                break
        
        # print(trim_idx)

        return "".join(output[trim_idx:])