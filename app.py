import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="NumPy Data Explorer", layout="wide")

st.title("📊 NumPy Data Explorer Dashboard")
st.write("Hands-on interactive demonstration of core NumPy capabilities.")

# Sidebar options
st.sidebar.header("Navigation")
task = st.sidebar.radio("Select Module:", [
    "1. Array Fundamentals",
    "2. Math & Statistics",
    "3. Reshaping & Broadcasting",
    "4. Save & Load Operations",
    "5. Performance Benchmark"
])

# TASK 1
if task == "1. Array Fundamentals":
    st.subheader("1. Array Creation, Indexing & Slicing")
    arr1d = np.array([10, 20, 30, 40, 50])
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**1D Array:**")
        st.write(arr1d)
        st.write("Element at Index 2:", arr1d[2])
        st.write("Slice [1:4]:", arr1d[1:4])
    with col2:
        st.markdown("**2D Array (3x3 Matrix):**")
        st.write(arr2d)
        st.write("Element at Row 1, Col 2:", arr2d[1, 2])

# TASK 2
elif task == "2. Math & Statistics":
    st.subheader("2. Mathematical & Statistical Operations")
    np.random.seed(42)
    dataset = np.random.randint(50, 100, size=(5, 3))
    
    st.write("**Student Marks Dataset (5 Students, 3 Subjects):**")
    st.dataframe(dataset)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Overall Average", f"{np.mean(dataset):.2f}")
    col2.metric("Highest Mark", int(np.max(dataset)))
    col3.metric("Lowest Mark", int(np.min(dataset)))
    
    st.write("**Subject-wise Average (Column-wise):**", np.mean(dataset, axis=0))
    st.write("**Total Marks per Student (Row-wise):**", np.sum(dataset, axis=1))

# TASK 3
elif task == "3. Reshaping & Broadcasting":
    st.subheader("3. Reshaping & Broadcasting")
    linear_arr = np.arange(1, 13)
    matrix_3x4 = linear_arr.reshape(3, 4)
    bonus = np.array([10, 20, 30, 40])
    broadcast_res = matrix_3x4 + bonus
    
    st.write("**Original 1D Array:**", linear_arr)
    st.write("**Reshaped to 3x4 Matrix:**")
    st.write(matrix_3x4)
    st.write("**Row Array added via Broadcasting:**", bonus)
    st.write("**Final Result:**")
    st.write(broadcast_res)

# TASK 4
elif task == "4. Save & Load Operations":
    st.subheader("4. Array Save & Load (.npy)")
    sample_arr = np.random.randint(10, 99, size=(3, 3))
    
    if st.button("Save Array to Disk"):
        np.save("web_marks_data.npy", sample_arr)
        st.success("Array successfully saved as 'web_marks_data.npy'!")
        
    if st.button("Load Array from Disk"):
        try:
            loaded_data = np.load("web_marks_data.npy")
            st.info("Loaded Data from Disk:")
            st.write(loaded_data)
        except Exception:
            st.warning("Pehle 'Save Array to Disk' button dabayein.")

# TASK 5
elif task == "5. Performance Benchmark":
    st.subheader("5. Performance: NumPy vs Python Lists")
    size = st.slider("Array Size (Elements):", 1_000_000, 10_000_000, 3_000_000, step=1_000_000)
    
    if st.button("Run Benchmark Test"):
        with st.spinner("Benchmark chal raha hai..."):
            # Python List
            l1, l2 = list(range(size)), list(range(size))
            t0 = time.time()
            _ = [x + y for x, y in zip(l1, l2)]
            time_py = time.time() - t0
            
            # NumPy
            a1, a2 = np.arange(size), np.arange(size)
            t0 = time.time()
            _ = a1 + a2
            time_np = time.time() - t0
            
            speedup = time_py / time_np
            
            st.success(f"NumPy is approx **{speedup:.1f}x FASTER** than standard Python lists!")
            col1, col2 = st.columns(2)
            col1.metric("Python List Duration", f"{time_py:.4f} s")
            col2.metric("NumPy Vector Duration", f"{time_np:.4f} s")