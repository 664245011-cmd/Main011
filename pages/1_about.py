import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="ผู้พัฒนา | Anime Recommendation",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;800&display=swap');

/* Main App Layout - Cinema Black & Gold */
.stApp {
    background-color: #08070A;
    background-image: 
        radial-gradient(circle at 10% 20%, rgba(229, 9, 20, 0.2) 0%, transparent 40%),
        radial-gradient(circle at 90% 80%, rgba(212, 175, 55, 0.2) 0%, transparent 40%);
    background-attachment: fixed;
}

html, body, [class*="css"] { 
    font-family: 'Prompt', 'Outfit', sans-serif; 
    color: #F5F5F7;
}

/* Hero Section */
.hero { 
    text-align: center; 
    padding: 40px 20px 10px 20px; 
}
.hero h1 {
    font-family: 'Outfit', 'Prompt', sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FFFFFF 0%, #F3C623 50%, #E50914 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 6px;
    filter: drop-shadow(0 0 20px rgba(229, 9, 20, 0.4));
}
.hero p { 
    color: #A1A1AA; 
    font-size: 1.15rem; 
    letter-spacing: 0.5px; 
    margin-top: 0; 
    font-weight: 300;
}

/* Profile Photo Wrap with Gold Cinema Frame */
.profile-photo-wrap {
    display: flex;
    justify-content: center;
    margin-top: 25px;
}
.profile-photo-wrap img {
    width: 190px;
    height: 190px;
    border-radius: 50%;
    border: 4px solid #F3C623;
    box-shadow: 0 0 30px rgba(212, 175, 55, 0.4), 0 0 15px rgba(229, 9, 20, 0.5);
    object-fit: cover;
    transition: all 0.4s ease;
}
.profile-photo-wrap img:hover {
    transform: scale(1.05);
    box-shadow: 0 0 45px rgba(243, 198, 35, 0.7), 0 0 25px rgba(229, 9, 20, 0.8);
}

/* Movie VIP Pass Card Style */
.profile-card {
    max-width: 480px;
    margin: 30px auto 0 auto;
    background: linear-gradient(145deg, #121016, #1A1721);
    border: 1px solid #D4AF37;
    border-radius: 20px;
    padding: 35px 40px;
    text-align: center;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.8), 0 0 15px rgba(212, 175, 55, 0.2);
    position: relative;
    overflow: hidden;
}
.profile-card::before {
    content: 'VIP MOVIE PASS';
    position: absolute;
    top: 12px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 0.65rem;
    font-weight: 800;
    letter-spacing: 3px;
    color: #D4AF37;
    background: rgba(212, 175, 55, 0.1);
    padding: 2px 14px;
    border-radius: 10px;
    border: 1px solid rgba(212, 175, 55, 0.3);
}
.profile-card h2 {
    color: #FFFFFF;
    font-family: 'Outfit', 'Prompt', sans-serif;
    font-size: 1.7rem;
    font-weight: 700;
    margin: 15px 0 20px 0;
    letter-spacing: 0.5px;
}
.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 8px;
    border-top: 1px dashed rgba(212, 175, 55, 0.25);
    color: #E4E4E7;
    font-size: 1.05rem;
}
.info-row:first-of-type { border-top: 1px dashed rgba(212, 175, 55, 0.25); }
.info-row span.label { 
    color: #A1A1AA; 
    font-weight: 400; 
    display: flex;
    align-items: center;
    gap: 8px;
}
.info-row span.value { 
    font-weight: 700; 
    color: #F3C623; 
    background: rgba(229, 9, 20, 0.2);
    padding: 4px 14px;
    border-radius: 8px;
    border: 1px solid rgba(229, 9, 20, 0.5);
    letter-spacing: 0.5px; 
}

/* Hide default Streamlit elements */
footer, #MainMenu { visibility: hidden; }
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { visibility: visible !important; }

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background: #0F0E13 !important;
    border-right: 1px solid rgba(212, 175, 55, 0.2) !important;
}
[data-testid="stSidebarNav"] { padding-top: 20px; }
[data-testid="stSidebarNav"]::before {
    content: "MAJOR CINEMA MENU";
    display: block;
    margin: 0 20px 20px 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(212, 175, 55, 0.2);
    font-family: 'Outfit', sans-serif;
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 2px;
    color: #D4AF37;
}
[data-testid="stSidebarNav"] a {
    margin: 4px 12px !important;
    padding: 12px 16px !important;
    border-radius: 10px;
    color: #A1A1AA !important;
    font-family: 'Prompt', sans-serif;
    font-weight: 500;
    font-size: 0.95rem;
    transition: all 0.25s ease;
    background: transparent !important;
}
[data-testid="stSidebarNav"] a:hover {
    background: rgba(229, 9, 20, 0.15) !important;
    color: #F3C623 !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: linear-gradient(90deg, rgba(229, 9, 20, 0.25) 0%, transparent 100%) !important;
    color: #F3C623 !important;
    border-left: 3px solid #E50914;
    font-weight: 700;
}

/* Menu label overrides */
[data-testid="stSidebarNav"] li:nth-child(1) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(1) a::after { content: "🏠 หน้าหลัก (Home)"; font-size: 0.95rem !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a::after { content: "🎬 ผู้พัฒนา (Developer)"; font-size: 0.95rem !important; }

/* Footer */
.custom-footer {
    text-align: center;
    color: #71717A;
    margin-top: 60px;
    padding: 30px 20px;
    font-size: 0.85rem;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero">
    <h1>ผู้พัฒนา</h1>
    <p>🍿 ข้อมูลผู้จัดทำโปรเจค Anime Recommendation 🎬</p>
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
      ' style="width:190px;height:190px;border-radius:50%;background:#121016;border:4px'
      ' solid'
      ' #F3C623;display:flex;align-items:center;justify-content:center;font-size:4rem;">🧑‍💻</div></div>',
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
    Anime Recommendation System &bull; Cinema Edition Built with Streamlit &copy; 2026
</div>
""",
    unsafe_allow_html=True,
)
