class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        hand.sort()

        comb_index = [[-1, 0] for _ in  range(len(hand) // groupSize)]

        for i in range(len(hand)):
            for j in range(len(comb_index)):
                index, comb_len = comb_index[j]
                if index != -1 and comb_len < groupSize:
                    if hand[i] - hand[index] > 1:
                        return False
                    elif hand[i] == hand[index]:
                        continue
                    else:
                        comb_index[j][0] = i
                        comb_index[j][1] = comb_len + 1
                        break
                elif index == -1:
                    comb_index[j][0] = i
                    comb_index[j][1] = comb_len + 1
                    break
                elif index != -1 and comb_len == groupSize:
                    continue
                if j == len(comb_index) - 1 and hand[i] == hand[index]:
                    return False
        
        check = 0
        for index, comb_len in comb_index:
            if index != -1 and comb_len == groupSize:
                    check += 1

        return True if check == len(comb_index) else False

