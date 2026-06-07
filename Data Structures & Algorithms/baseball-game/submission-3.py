class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_list = []

        for op in operations:
            if op == "+":
                score_list.append(score_list[-1] + score_list[-2])
            elif op == "D":
                score_list.append(2 * score_list[-1])
            elif op == "C":
                score_list.pop()
            else:
                score_list.append(int(op))

        return sum(score_list)