class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flattern = []
        for i in mat:
            flattern += i
        if r*c!=len(flattern):
            return mat
        mat = []
        for j in range(0,len(flattern), c):
            mat.append(flattern[j:j+c])
        return mat
