class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ages = []

        for ch in details:
            ages.append(int(ch[11:13]))

        count = 0
        for age in ages:
            if age > 60:
                count += 1

        return count