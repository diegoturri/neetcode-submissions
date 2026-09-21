class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            operation = operations[i]

            if operation == "+":
                res.append(res[-1]+res[-2])
            elif operation == "D":
                res.append(res[-1] * 2)
            elif operation == "C":
                res.pop()
            else:
                res.append(int(operation))
        
        return sum(res)