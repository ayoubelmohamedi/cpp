
def combine(n, k):
    def backtrack(start, path):
        if len(path) == k:
            result.append(path.copy())
            return
        for i in range(start, n+1):
            path.append(i)
            print(path) 
            backtrack(i+1, path)
            path.pop()
        resutl = []
        backtrack(1,[])
        return res