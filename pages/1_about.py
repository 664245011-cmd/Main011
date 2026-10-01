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
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;800&display=swap');

/* Main App Layout - Anime Cyberpunk Theme */
.stApp {
    background-color: #050811;
    background-image: 
        radial-gradient(circle at 10% 20%, rgba(236, 72, 153, 0.12) 0%, transparent 30%),
        radial-gradient(circle at 90% 80%, rgba(59, 130, 246, 0.15) 0%, transparent 35%),
        radial-gradient(circle at 50% 50%, rgba(139, 92, 246, 0.08) 0%, transparent 40%);
    background-attachment: fixed;
}

html, body, [class*="css"] { 
    font-family: 'Prompt', 'Outfit', sans-serif; 
    color: #F1F5F9;
}

/* Hero Section with Glowing Accent */
.hero { 
    text-align: center; 
    padding: 40px 20px 10px 20px; 
}
.hero h1 {
    font-family: 'Outfit', 'Prompt', sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FF758C 0%, #FF7EB3 50%, #7928CA 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 6px;
    filter: drop-shadow(0 0 25px rgba(255, 117, 140, 0.3));
}
.hero p { 
    color: #94A3B8; 
    font-size: 1.15rem; 
    letter-spacing: 0.5px; 
    margin-top: 0; 
    font-weight: 300;
}

/* Profile Photo Wrap with Anime Ring */
.profile-photo-wrap {
    display: flex;
    justify-content: center;
    margin-top: 25px;
}
.profile-photo-wrap img {
    width: 190px;
    height: 190px;
    border-radius: 50%;
    border: 4px solid transparent;
    background:
        linear-gradient(#0F172A, #0F172A) padding-box,
        linear-gradient(135deg, #FF758C, #8B5CF6, #3B82F6) border-box;
    box-shadow: 0 0 35px rgba(139, 92, 246, 0.4), inset 0 0 15px rgba(255, 117, 140, 0.3);
    object-fit: cover;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.profile-photo-wrap img:hover {
    transform: scale(1.05) rotate(2deg);
    box-shadow: 0 0 50px rgba(255, 117, 140, 0.6), inset 0 0 20px rgba(59, 130, 246, 0.5);
}

/* Glassmorphism Profile Card */
.profile-card {
    max-width: 480px;
    margin: 30px auto 0 auto;
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 35px 40px;
    text-align: center;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5), 0 0 20px rgba(139, 92, 246, 0.1);
    position: relative;
    overflow: hidden;
}
.profile-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #FF758C, #8B5CF6, #3B82F6);
}
.profile-card h2 {
    color: #FFFFFF;
    font-family: 'Outfit', 'Prompt', sans-serif;
    font-size: 1.65rem;
    font-weight: 700;
    margin: 0 0 24px 0;
    letter-spacing: 0.5px;
}
.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 8px;
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
    background: rgba(244, 114, 182, 0.1);
    padding: 4px 12px;
    border-radius: 8px;
    border: 1px solid rgba(244, 114, 182, 0.2);
    letter-spacing: 0.5px; 
}

/* Hide default Streamlit elements */
footer, #MainMenu { visibility: hidden; }
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { visibility: visible !important; }

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background: #090D16 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
}
[data-testid="stSidebarNav"] { padding-top: 20px; }
[data-testid="stSidebarNav"]::before {
    content: "ANIME HUB MENU";
    display: block;
    margin: 0 20px 20px 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    font-family: 'Outfit', sans-serif;
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
    background: rgba(255, 117, 140, 0.1) !important;
    color: #FF758C !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: linear-gradient(90deg, rgba(255, 117, 140, 0.15) 0%, transparent 100%) !important;
    color: #FF758C !important;
    border-left: 3px solid #FF758C;
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
    <p>✨ ข้อมูลผู้จัดทำโปรเจค Anime Recommendation ✨</p>
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
      '<div class="profile-photo-wrap"><div'
      ' style="width:190px;height:190px;border-radius:50%;background:#0F172A;border:4px'
      ' solid'
      ' #FF758C;display:flex;align-items:center;justify-content:center;font-size:4rem;">🧑‍💻</div></div>',
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