import streamlit as st
from PIL import Image
from pathlib import Path

# 1. Cấu hình trang
st.set_page_config(page_title="Khoa học Màu sắc", layout="wide")

thu_muc = Path(__file__).resolve().parent


# 2. Hàm hiển thị logo
def hien_logo(ten_file, ten_don_vi, kich_thuoc):
    anh = Image.open(thu_muc / ten_file).convert("RGBA")

    # Cắt phần trong suốt dư thừa
    vung = anh.getchannel("A").getbbox()
    if vung:
        anh = anh.crop(vung)

    # Thu nhỏ logo, giữ nguyên tỷ lệ
    anh.thumbnail(kich_thuoc, Image.Resampling.LANCZOS)

    # Tạo khung 480 x 220 và căn giữa logo
    khung = Image.new("RGBA", (480, 220), (255, 255, 255, 0))
    x = (480 - anh.width) // 2
    y = (220 - anh.height) // 2
    khung.alpha_composite(anh, (x, y))

    # Hiển thị logo và tên đơn vị
    st.image(khung, width="stretch")
    st.markdown(
        f"<p style='text-align:center;font-size:20px;font-weight:600;"
        f"line-height:1.5;min-height:50px'>{ten_don_vi}</p>",
        unsafe_allow_html=True
    )


# 3. Hiển thị 3 logo trên cùng một hàng
cot1, cot2, cot3 = st.columns(3)

with cot1:
    hien_logo(
        "logo_truong.png",
        "TRƯỜNG ĐẠI HỌC CÔNG NGHỆ KỸ THUẬT TP.HCM",
        (294, 154)
    )

with cot2:
    hien_logo(
        "logo_khoa.png",
        "KHOA MỸ THUẬT VÀ TRUYỀN THÔNG",
        (250, 132)
    )

with cot3:
    hien_logo(
        "logo_ict.png",
        "CTY CỔ PHẦN IN TỔNG HỢP CẦN THƠ",
        (294, 154)
    )


# 4. Tiêu đề project
st.divider()

st.markdown(
    "<h1 style='text-align:center;font-size:60px'>"
    "KHOA HỌC MÀU SẮC</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;font-size:30px'>"
    "Project quá trình môn: Ứng dụng MATLAB trong Công nghệ In</p>",
    unsafe_allow_html=True
)


# 5. Thông tin sinh viên
st.divider()

st.subheader("Thông tin sinh viên")
st.write("**Họ và tên:** Quách Thanh Tùng")
st.write("**Mã số sinh viên:** 23458021")
st.write("**Lớp:** 23VL58CT1")
