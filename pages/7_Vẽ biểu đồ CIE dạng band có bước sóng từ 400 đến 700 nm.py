import streamlit as st
import colour
import numpy as np
import matplotlib.pyplot as plt

# 1. Tiêu đề
st.set_page_config(page_title="CIE band 400-700 nm", layout="wide")
st.title("Biểu đồ CIE dạng band (400–700 nm)")
st.write("Hàm phối màu CIE 1931 – quan sát viên tiêu chuẩn 2°.")

# 2. Lấy dữ liệu CIE từ 400 đến 700 nm, mỗi 10 nm
khoang_pho = colour.SpectralShape(400, 700, 10)
cie = colour.MSDS_CMFS["CIE 1931 2 Degree Standard Observer"].copy()
cie = cie.align(khoang_pho)

buoc_song = cie.wavelengths
x_bar = cie.values[:, 0]
y_bar = cie.values[:, 1]
z_bar = cie.values[:, 2]

# 3. Tạo dải màu phổ để minh họa từ 400 đến 700 nm
song_mau = np.arange(400, 701, 1)
XYZ = colour.wavelength_to_XYZ(song_mau)
XYZ = XYZ / np.maximum(np.max(XYZ, axis=1, keepdims=True), 1e-9)
RGB = np.clip(colour.XYZ_to_sRGB(XYZ), 0, 1)
dai_mau = RGB[np.newaxis, :, :]

# 4. Vẽ biểu đồ
hinh, truc = plt.subplots(figsize=(10, 5))
truc.plot(buoc_song, x_bar, "r", label="x̄(λ)", linewidth=2)
truc.plot(buoc_song, y_bar, "g", label="ȳ(λ)", linewidth=2)
truc.plot(buoc_song, z_bar, "b", label="z̄(λ)", linewidth=2)

# Dải màu chỉ minh họa màu sắc màn hình, không phải số liệu đo
truc.imshow(dai_mau, extent=[400, 700, -0.20, -0.06], aspect="auto")
truc.axhline(0, color="gray", linewidth=0.8)
truc.set_xlim(400, 700)
truc.set_ylim(-0.22, 2.0)
truc.set_xticks(np.arange(400, 701, 20))
truc.set_xlabel("Bước sóng (nm)")
truc.set_ylabel("Giá trị hàm phối màu")
truc.set_title("CIE 1931 – Dải bước sóng 400–700 nm")
truc.legend()
truc.grid(alpha=0.25)
hinh.tight_layout()

st.pyplot(hinh)
plt.close(hinh)

# 5. Ghi chú
st.write("**Phạm vi dữ liệu:** 400–700 nm, bước lấy mẫu 10 nm (31 điểm).")
st.caption("Dải màu phía dưới là màu sRGB mô phỏng trên màn hình, không phải dữ liệu đo màu hay giá trị hàm phối màu.")
