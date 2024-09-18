class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orders = {c:i for i,c in enumerate(order)}
        print(orders)
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if orders[w1[j]]>orders[w2[j]]:
                        return False
                    break
        return True