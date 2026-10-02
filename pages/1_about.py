import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="ผู้พัฒนา | Anime Recommendation",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700;800&family=Prompt:wght@300;400;500;600;700&display=swap');

/* Main App Layout - Cyberpunk Cyber Glow */
.stApp {
    background: #060713;
    background-image: 
        radial-gradient(circle at 15% 15%, rgba(139, 92, 246, 0.22) 0%, transparent 45%),
        radial-gradient(circle at 85% 85%, rgba(6, 182, 212, 0.18) 0%, transparent 45%),
        radial-gradient(circle at 50% 50%, rgba(236, 72, 153, 0.12) 0%, transparent 55%);
    background-attachment: fixed;
}

html, body, [class*="css"] { 
    font-family: 'Plus Jakarta Sans', 'Prompt', sans-serif; 
    color: #F8FAFC;
}

/* Hero Section with Glowing Accent */
.hero { 
    text-align: center; 
    padding: 45px 20px 10px 20px; 
}
.hero h1 {
    font-family: 'Plus Jakarta Sans', 'Prompt', sans-serif;
    font-size: 3.3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FFFFFF 10%, #F472B6 45%, #C084FC 75%, #38BDF8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 6px;
    filter: drop-shadow(0 0 30px rgba(139, 92, 246, 0.35));
}
.hero p { 
    color: #94A3B8; 
    font-size: 1.15rem; 
    letter-spacing: 0.5px; 
    margin-top: 0; 
    font-weight: 300;
}

/* Profile Photo Wrap with Cyber Ring */
.profile-photo-wrap {
    display: flex;
    justify-content: center;
    margin-top: 25px;
}
.profile-photo-wrap img {
    width: 195px;
    height: 195px;
    border-radius: 50%;
    border: 4px solid transparent;
    background:
        linear-gradient(#0A0817, #0A0817) padding-box,
        linear-gradient(135deg, #EC4899, #8B5CF6, #06B6D4) border-box;
    box-shadow: 0 0 35px rgba(139, 92, 246, 0.45), inset 0 0 15px rgba(236, 72, 153, 0.3);
    object-fit: cover;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.profile-photo-wrap img:hover {
    transform: scale(1.05) rotate(2deg);
    box-shadow: 0 0 50px rgba(236, 72, 153, 0.65), inset 0 0 20px rgba(6, 182, 212, 0.5);
}

/* Glassmorphism Profile Card */
.profile-card {
    max-width: 480px;
    margin: 30px auto 0 auto;
    background: linear-gradient(145deg, rgba(20, 16, 41, 0.8), rgba(10, 8, 22, 0.9));
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 26px;
    padding: 35px 40px;
    text-align: center;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    box-shadow: 0 20px 45px -15px rgba(0, 0, 0, 0.6), 0 0 25px rgba(139, 92, 246, 0.15);
    position: relative;
    overflow: hidden;
}
.profile-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #EC4899, #8B5CF6, #06B6D4);
}
.profile-card h2 {
    color: #FFFFFF;
    font-family: 'Plus Jakarta Sans', 'Prompt', sans-serif;
    font-size: 1.65rem;
    font-weight: 700;
    margin: 0 0 24px 0;
    letter-spacing: 0.5px;
}
.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 8px;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
    color: #CBD5E1;
    font-size: 1.05rem;
}
.info-row:first-of-type { border-top: none; }
.info-row span.label { 
    color: #94A3B8; 
    font-weight: 400; 
    display: flex;
    align-items: center;
    gap: 8px;
}
.info-row span.value { 
    font-weight: 600; 
    color: #F472B6; 
    background: rgba(244, 114, 182, 0.12);
    padding: 5px 14px;
    border-radius: 10px;
    border: 1px solid rgba(244, 114, 182, 0.25);
    letter-spacing: 0.5px; 
}

/* Sidebar Styling */
footer, #MainMenu { visibility: hidden; }
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { visibility: visible !important; }

[data-testid="stSidebar"] {
    background: #0A0817 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
}
[data-testid="stSidebarNav"] { padding-top: 20px; }
[data-testid="stSidebarNav"]::before {
    content: "ANIME HUB MENU";
    display: block;
    margin: 0 20px 20px 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: #64748B;
}
[data-testid="stSidebarNav"] a {
    margin: 4px 12px !important;
    padding: 12px 16px !important;
    border-radius: 12px;
    color: #94A3B8 !important;
    font-family: 'Prompt', sans-serif;
    font-weight: 500;
    font-size: 0.95rem;
    transition: all 0.25s ease;
    background: transparent !important;
}
[data-testid="stSidebarNav"] a:hover {
    background: rgba(139, 92, 246, 0.12) !important;
    color: #C084FC !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: linear-gradient(90deg, rgba(139, 92, 246, 0.2) 0%, transparent 100%) !important;
    color: #C084FC !important;
    border-left: 3px solid #8B5CF6;
    font-weight: 600;
}

/* Menu label overrides */
[data-testid="stSidebarNav"] li:nth-child(1) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(1) a::after { content: "🏠 หน้าหลัก"; font-size: 0.95rem !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a::after { content: "🧑‍💻 ผู้พัฒนา"; font-size: 0.95rem !important; }

/* Footer */
.custom-footer {
    text-align: center;
    color: #64748B;
    margin-top: 60px;
    padding: 30px 20px;
    font-size: 0.85rem;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero">
    <h1>ผู้พัฒนา</h1>
    <p>✨ ข้อมูลผู้จัดทำโปรเจกต์ Anime Recommendation ✨</p>
</div>
""",
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
        '<div class="profile-photo-wrap"><div style="width:195px;height:195px;border-radius:50%;background:#0A0817;border:4px solid #8B5CF6;display:flex;align-items:center;justify-content:center;font-size:4rem;">🧑‍💻</div></div>',
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
    Anime Recommendation System &bull; Powered by Streamlit &copy; 2026
</div>
""",
    unsafe_allow_html=True,
)