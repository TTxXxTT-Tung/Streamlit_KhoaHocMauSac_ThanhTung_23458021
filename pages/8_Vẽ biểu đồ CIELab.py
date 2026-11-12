import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Tiêu đề
st.set_page_config(page_title="Biểu đồ CIELAB", layout="wide")
st.title("Biểu đồ chuyển dịch màu CIELAB")
st.write("Nhập hai màu Lab1 và Lab2 để biểu diễn và nhận xét sự chuyển dịch màu.")

# 2. Nhập giá trị màu
cot1, cot2 = st.columns(2)

with cot1:
    st.subheader("Màu Lab1")
    L1 = st.number_input("L*1", min_value=0.0, max_value=100.0, value=55.0)
    a1 = st.number_input("a*1", min_value=-150.0, max_value=150.0, value=20.0)
    b1 = st.number_input("b*1", min_value=-150.0, max_value=150.0, value=25.0)

with cot2:
    st.subheader("Màu Lab2")
    L2 = st.number_input("L*2", min_value=0.0, max_value=100.0, value=65.0)
    a2 = st.number_input("a*2", min_value=-150.0, max_value=150.0, value=10.0)
    b2 = st.number_input("b*2", min_value=-150.0, max_value=150.0, value=5.0)

# 3. Tính mức độ chuyển dịch
DL = L2 - L1
Da = a2 - a1
Db = b2 - b1
DeltaE = np.sqrt(DL**2 + Da**2 + Db**2)

# 4. Vẽ hai điểm trong không gian CIELAB
hinh = plt.figure(figsize=(8, 6))
truc = hinh.add_subplot(111, projection="3d")
truc.scatter(a1, b1, L1, color="blue", s=70, label="Lab1")
truc.scatter(a2, b2, L2, color="red", s=70, label="Lab2")
truc.plot([a1, a2], [b1, b2], [L1, L2], "k--", linewidth=1)
truc.quiver(a1, b1, L1, Da, Db, DL, color="black", arrow_length_ratio=0.15)
truc.set_xlabel("a* (lục ↔ đỏ)")
truc.set_ylabel("b* (lam ↔ vàng)")
truc.set_zlabel("L* (độ sáng)")
truc.set_xlim(-150, 150)
truc.set_ylim(-150, 150)
truc.set_zlim(0, 100)
truc.set_title("Chuyển dịch màu từ Lab1 sang Lab2")
truc.legend()
hinh.tight_layout()

st.pyplot(hinh)
plt.close(hinh)

# 5. Hiển thị kết quả
st.subheader("Kết quả so sánh")
st.write(f"ΔL* = {DL:.2f}  |  Δa* = {Da:.2f}  |  Δb* = {Db:.2f}")
st.write(f"Chênh lệch màu ΔE*ab (CIE 1976) = **{DeltaE:.2f}**")

# 6. Nhận xét theo chiều biến thiên của từng trục
if DL > 0:
    st.write("- Màu Lab2 **sáng hơn** màu Lab1.")
elif DL < 0:
    st.write("- Màu Lab2 **tối hơn** màu Lab1.")
else:
    st.write("- Hai màu có **cùng độ sáng L***.")

if Da > 0:
    st.write("- Lab2 chuyển dịch theo hướng **đỏ** (+a*).")
elif Da < 0:
    st.write("- Lab2 chuyển dịch theo hướng **lục** (−a*).")
else:
    st.write("- Không có thay đổi theo trục a*.")

if Db > 0:
    st.write("- Lab2 chuyển dịch theo hướng **vàng** (+b*).")
elif Db < 0:
    st.write("- Lab2 chuyển dịch theo hướng **lam** (−b*).")
else:
    st.write("- Không có thay đổi theo trục b*.")

st.caption("Đồ thị biểu diễn tọa độ CIELAB, không phải màu RGB thực tế trên màn hình. Chỉ số ΔE*ab không tự xác định đạt/không đạt nếu chưa có dung sai.")
