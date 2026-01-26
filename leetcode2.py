class Listnode:
    def solution(self, l1, l2):
        result = []

        l1 = list(reversed(l1))
        l2 = list(reversed(l2))

        A = 0
        B = 0

        for x in range(len(l1)):
            A = A * 10 + l1[x]
            B = B * 10 + l2[x]

        total = A + B

        while total > 0:
            result.append(total % 10)
            total //= 10

        return result


sl = Listnode()
print(sl.solution([2,4,3], [5,6,4]))
