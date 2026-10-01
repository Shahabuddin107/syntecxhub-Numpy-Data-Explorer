import numpy as np
import time

def print_separator(title):
    print("\n" + "=" * 50)
    print(f"  {title.upper()}")
    print("=" * 50)


# -------------------------------------------------------------
# TASK 1: NumPy Fundamentals - Creation, Indexing, and Slicing
# -------------------------------------------------------------
print_separator("Task 1: Fundamentals (Creation, Indexing, Slicing)")

# 1D Array
arr1d = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1d)
print("First Element (Index 0):", arr1d[0])
print("Slice [1 to 4]:", arr1d[1:4])

# 2D Array (Matrix)
arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("\n2D Array:\n", arr2d)
print("Element at Row 1, Column 2:", arr2d[1, 2])
print("First 2 Rows and Columns:\n", arr2d[:2, :2])


# -------------------------------------------------------------
# TASK 2: Mathematical, Axis-wise & Statistical Operations
# -------------------------------------------------------------
print_separator("Task 2: Math, Axis-wise & Statistics")

# Random dataset: 4 students ke 3 subjects ke marks (out of 100)
np.random.seed(42)  # Output same rakhne ke liye
dataset = np.random.randint(50, 100, size=(4, 3))
print("Student Marks Dataset (4 Students, 3 Subjects):\n", dataset)

# Basic statistics
print("\nDataset Statistics:")
print(f"- Overall Mean (Average): {np.mean(dataset):.2f}")
print(f"- Standard Deviation:     {np.std(dataset):.2f}")
print(f"- Maximum Mark:           {np.max(dataset)}")
print(f"- Minimum Mark:           {np.min(dataset)}")

# Axis-wise operations:
# axis=0 -> Column-wise (Subject-wise average)
# axis=1 -> Row-wise (Har student ka total)
print("\nAxis-wise Analysis:")
print("Subject Average (Column-wise):", np.mean(dataset, axis=0))
print("Total Marks per Student (Row-wise):", np.sum(dataset, axis=1))


# -------------------------------------------------------------
# TASK 3: Reshaping and Broadcasting
# -------------------------------------------------------------
print_separator("Task 3: Reshaping and Broadcasting")

# 1D array banakar usko 2D mein reshape karna
linear_arr = np.arange(1, 13)  # 1 se 12 tak
print("Original 1D array (Length 12):", linear_arr)

matrix_3x4 = linear_arr.reshape(3, 4)
print("\nReshaped to 3x4 Matrix:\n", matrix_3x4)

# Broadcasting: Ek single row ko poore matrix mein add karna
bonus = np.array([10, 20, 30, 40])
result_broadcast = matrix_3x4 + bonus

print("\nRow Array to add:", bonus)
print("Result after Broadcasting:\n", result_broadcast)


# -------------------------------------------------------------
# TASK 4: Save and Load Operations
# -------------------------------------------------------------
print_separator("Task 4: Save & Load Array")

file_name = "saved_marks_data.npy"

# Data save karna
np.save(file_name, dataset)
print(f"Data saved successfully as '{file_name}'.")

# Data load karna
loaded_data = np.load(file_name)
print("Loaded Data from Disk:\n", loaded_data)


# -------------------------------------------------------------
# TASK 5: Performance Comparison (NumPy vs Python List)
# -------------------------------------------------------------
print_separator("Task 5: Performance - NumPy vs Python List")

size = 5_000_000  # 50 Lakh numbers

# 1. Standard Python List
list1 = list(range(size))
list2 = list(range(size))

start_py = time.time()
list_result = [x + y for x, y in zip(list1, list2)]
time_py = time.time() - start_py
print(f"Python List Time:  {time_py:.4f} seconds")

# 2. NumPy Array
nparr1 = np.arange(size)
nparr2 = np.arange(size)

start_np = time.time()
np_result = nparr1 + nparr2
time_np = time.time() - start_np
print(f"NumPy Vector Time: {time_np:.4f} seconds")

# Speedup factor
speedup = time_py / time_np
print(f"\nResult: NumPy is approx {speedup:.1f}x FASTER than Python Lists!")