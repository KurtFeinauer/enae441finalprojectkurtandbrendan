import numpy as np

# Load the matrix
data = np.load('Project-Measurements-Easy.npy', allow_pickle=True)


# Function to split the matrix based on the condition t2 - t1 > 5.5
def split_by_time_jump(matrix, threshold=5.5):
    # Initialize a list to store the resulting sub-matrices
    sub_matrices = []

    # Start with the first row as the initial sub-matrix
    sub_matrix = [matrix[0]]

    # Iterate through the matrix and check the time difference between consecutive rows
    for i in range(1, len(matrix)):
        # Calculate the delta time (difference between the first column values)
        delta_t = matrix[i, 0] - matrix[i - 1, 0]

        if delta_t > threshold:
            # If the time jump exceeds the threshold, split here
            print(f"Delta t jump: {delta_t} (rows {i - 1} to {i})")
            sub_matrices.append(np.array(sub_matrix))
            sub_matrix = [matrix[i]]  # Start a new sub-matrix with the current row
        else:
            sub_matrix.append(matrix[i])

    # Append the last sub-matrix
    sub_matrices.append(np.array(sub_matrix))

    return sub_matrices


# Apply the function to the data
split_matrices = split_by_time_jump(data)

# Show the resulting splits
print("\nFinal Splits:")
for idx, sub_matrix in enumerate(split_matrices):
    print(f"Sub-matrix {idx + 1}:\n", sub_matrix)

