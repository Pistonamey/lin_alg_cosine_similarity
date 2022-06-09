import matplotlib.pyplot as plt
import numpy as np

#a) function to generate cosine similarity matrix
def self_similarity(matrix):
    M,N = matrix.shape #Dimensions of the matrix

    sim_mat = np.zeros((M,M)) # Fill the matrix with zeroes

    for i in range(M): #row
        for j in range(M): #column
            u=matrix[i,:]
            v=matrix[j,:]

            sim_mat[i,j] = np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v)) #compute cosine similarity between the vectors

    return sim_mat

#b) generate a matrix and pass it to the funciton
#A = np.array(
#    [[0, 1, 0, 0, 1],
#     [0, 0, 1, 1, 1],
#     [1, 1, 0, 1, 0]])

A=np.random.randint(4,size=(3,5))

result_matrix=self_similarity(A)

print(result_matrix)

#c) matplot
plt.matshow(result_matrix)
plt.show()
