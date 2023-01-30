import numpy as np

def matriceBloc(A,i,j):
    return A[(i-1)2:((i-1)2)+2,(j-1)2:((j-1)2)+2]


def produitBlocs(A,B):
    return np.array([[np.dot(matriceBloc(A,1,1),matriceBloc(B,1,1)) + np.dot(matriceBloc(A,1,2), matriceBloc(B,2,1)), np.dot(matriceBloc(A,1,1),matriceBloc(B,1,2)) + np.dot(matriceBloc(A,1,2), matriceBloc(B,2,2))],
                  [np.dot(matriceBloc(A,2,1),matriceBloc(B,1,1)) + np.dot(matriceBloc(A,2,2), matriceBloc(B,2,1)), np.dot(matriceBloc(A,2,1),matriceBloc(B,1,2)) + np.dot(matriceBloc(A,2,2), matriceBloc(B,2,2))]])

A = np.array([[6,2,2,1],[4,-2,3,1],[2,8,5,3],[3,-1,4,2]])

print(produitBlocs(A, A))