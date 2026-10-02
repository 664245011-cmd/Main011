import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="ผู้พัฒนา | Major Cineplex Anime",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;800&display=swap');

.stApp {
    background-color: #0B0B0E;
    background-image: linear-gradient(180deg, #050507 0%, #0B0B0E 100%);
    background-attachment: fixed;
}

html, body, [class*="css"] { 
    font-family: 'Prompt', sans-serif; 
    color: #FFFFFF;
}

/* Major Header Bar */
.major-navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 30px;
    background: #000000;
    border-bottom: 2px solid #E50914;
    margin: -60px -50px 20px -50px;
}

.major-logo {
    display: flex;
    align-items: center;
    gap: 12px;
}

.major-logo span.brand {
    font-family: 'Outfit', sans-serif;
    font-weight: 900;
    font-size: 1.6rem;
    color: #D4AF37;
    letter-spacing: 2px;
}

/* Profile Photo Wrap */
.profile-photo-wrap {
    display: flex;
    justify-content: center;
    margin-top: 30px;
}

.profile-photo-wrap img {
    width: 180px;
    height: 180px;
    border-radius: 50%;
    border: 3px solid #D4AF37;
    box-shadow: 0 0 25px rgba(212, 175, 55, 0.3), 0 0 15px rgba(229, 9, 20, 0.4);
    object-fit: cover;
}

/* Major Red Title Section */
.section-header-red {
    background: linear-gradient(90deg, #E50914 0%, #8B0000 40%, rgba(11, 11, 14, 0) 100%);
    padding: 10px 20px;
    border-radius: 6px;
    font-size: 1.2rem;
    font-weight: 700;
    color: #FFFFFF;
    margin: 20px auto 0 auto;
    max-width: 500px;
    text-align: center;
}

/* Movie VIP Card */
.profile-card {
    max-width: 500px;
    margin: 20px auto 0 auto;
    background: #141419;
    border: 1px solid rgba(212, 175, 55, 0.4);
    border-radius: 16px;
    padding: 30px 35px;
    text-align: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.8);
}

.profile-card h2 {
    color: #FFFFFF;
    font-size: 1.6rem;
    font-weight: 700;
    margin: 10px 0 20px 0;
}

.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 0;
    border-top: 1px dashed rgba(255, 255, 255, 0.1);
    color: #E4E4E7;
    font-size: 1.05rem;
}

.info-row span.label { 
    color: #A1A1AA; 
}

.info-row span.value { 
    font-weight: 700; 
    color: #D4AF37; 
    background: rgba(229, 9, 20, 0.25);
    padding: 4px 14px;
    border-radius: 6px;
    border: 1px solid rgba(229, 9, 20, 0.5);
}

footer, #MainMenu { visibility: hidden; }

[data-testid="stSidebar"] {
    background: #09090C !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(229, 9, 20, 0.2) !important;
    color: #D4AF37 !important;
    border-left: 3px solid #E50914;
}

.custom-footer {
    text-align: center;
    color: #71717A;
    margin-top: 60px;
    padding: 25px 20px;
    font-size: 0.85rem;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
}
</style>

<!-- Major Navbar -->
<div class="major-navbar">
    <div class="major-logo">
        <span style="font-size: 1.8rem;">🍿</span>
        <span class="brand">ANIME</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-header-red">🧑‍💻 ข้อมูลผู้จัดทำโปรเจกต์</div>',
    unsafe_allow_html=True,
)

# โหลดรูปภาพ
photo_path = Path(__file__).resolve().parent.parent / "assets" / "1.jpg"
try:
    photo_b64 = base64.b64encode(photo_path.read_bytes()).decode()
    st.markdown(
        f'<div class="profile-photo-wrap"><img src="data:image/jpeg;base64,{photo_b64}" alt="Profile Photo"></div>',
        unsafe_allow_html=True,
    )
except FileNotFoundError:
    st.markdown(
        '<div class="profile-photo-wrap"><div'
        ' style="width:180px;height:180px;border-radius:50%;background:#141419;border:3px'
        ' solid'
        ' #D4AF37;display:flex;align-items:center;justify-content:center;font-size:4rem;">🧑‍💻</div></div>',
        unsafe_allow_html=True,
    )

st.markdown(
    """
<div class="profile-card">
    <h2>ทินภัทร ช้อยสามนาค</h2>
    <div class="info-row">
        <span class="label">🆔 รหัสนักศึกษา</span>
        <span class="value">664245011</span>
    </div>
    <div class="info-row">
        <span class="label">🏫 หมู่เรียน</span>
        <span class="value">Sec. 66/43</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="custom-footer">
    Major Anime Recommendation System &bull; Powered by Streamlit &copy; 2026
</div>
""",
    unsafe_allow_html=True,
)
