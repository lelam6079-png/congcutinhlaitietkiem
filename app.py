import streamlit as st

# ==============================
# CẤU HÌNH TRANG
# ==============================
st.set_page_config(
    page_title="Công cụ tính lãi tiền gửi tiết kiệm_Lê Quang Lâm"
    page_icon="🏦",
    layout="centered"
)

# ==============================
# TIÊU ĐỀ
# ==============================
st.title("🏦 TÍNH LÃI TIỀN GỬI TIẾT KIỆM")
st.write("Nhập thông tin tiền gửi để tính toán tiền lãi.")

st.divider()

# ==============================
# NHẬP THÔNG TIN
# ==============================

so_tien_gui = st.number_input(
    "💰 Số tiền gửi (VNĐ)",
    min_value=0,
    value=100_000_000,
    step=1_000_000,
    format="%d"
)

ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.01,
    format="%.2f"
)

hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

# ==============================
# NÚT TÍNH TOÁN
# ==============================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Kiểm tra dữ liệu
    if so_tien_gui <= 0:
        st.error("Vui lòng nhập số tiền gửi lớn hơn 0.")
    elif lai_suat < 0:
        st.error("Lãi suất không được nhỏ hơn 0.")
    else:

        # Chuyển lãi suất % sang dạng thập phân
        lai_suat_nam = lai_suat / 100

        # ==============================
        # TÍNH LÃI THEO KỲ HẠN
        # ==============================

        # Tổng tiền lãi đơn trong toàn bộ kỳ hạn
        tong_lai = (
            so_tien_gui
            * lai_suat_nam
            * ky_han
            / 12
        )

        # ------------------------------
        # NHẬN LÃI CUỐI KỲ
        # ------------------------------
        if hinh_thuc == "Cuối kỳ":

            so_ky = 1

            lai_dinh_ky = tong_lai

            tong_tien = so_tien_gui + tong_lai

            ten_ky = "Cuối kỳ"

        # ------------------------------
        # NHẬN LÃI HÀNG THÁNG
        # ------------------------------
        elif hinh_thuc == "Hàng tháng":

            so_ky = ky_han

            lai_dinh_ky = (
                so_tien_gui
                * lai_suat_nam
                / 12
            )

            tong_tien = so_tien_gui + tong_lai

            ten_ky = "Mỗi tháng"

        # ------------------------------
        # NHẬN LÃI HÀNG QUÝ
        # ------------------------------
        else:

            # Số tháng không chia hết cho 3
            # vẫn tính tổng lãi theo số tháng thực tế
            so_ky = ky_han / 3

            lai_dinh_ky = (
                so_tien_gui
                * lai_suat_nam
                / 4
            )

            tong_tien = so_tien_gui + tong_lai

            ten_ky = "Mỗi quý"

        # ==============================
        # HIỂN THỊ KẾT QUẢ
        # ==============================

        st.success("✅ Tính toán thành công!")

        st.subheader("📊 KẾT QUẢ")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Tiền lãi định kỳ",
                f"{lai_dinh_ky:,.0f} VNĐ"
            )

            st.metric(
                "Tổng tiền lãi",
                f"{tong_lai:,.0f} VNĐ"
            )

        with col2:
            st.metric(
                "Tiền gốc",
                f"{so_tien_gui:,.0f} VNĐ"
            )

            st.metric(
                "Tổng gốc + lãi",
                f"{tong_tien:,.0f} VNĐ"
            )

        st.divider()

        # ==============================
        # THÔNG TIN CHI TIẾT
        # ==============================

        st.subheader("📋 Thông tin khoản gửi")

        st.write(f"**Số tiền gửi:** {so_tien_gui:,.0f} VNĐ")
        st.write(f"**Kỳ hạn:** {ky_han} tháng")
        st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
        st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")
        st.write(f"**Kỳ nhận lãi:** {ten_ky}")

        # ==============================
        # CÔNG THỨC
        # ==============================

        st.info(
            "Cách tính được sử dụng: "
            "Tiền lãi = Tiền gốc × Lãi suất năm × Số tháng / 12. "
            "Khoản tính trên giả định lãi suất cố định và không nhập lãi vào gốc "
            "(lãi đơn)."
        )
