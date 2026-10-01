import streamlit as st

st.set_page_config(
    page_title="Anime Recommendation Hub",
    page_icon="🎌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;800&display=swap');

/* Main App Layout - Premium Dark Anime Theme */
.stApp {
    background-color: #030712;
    background-image: 
        radial-gradient(circle at 15% 10%, rgba(225, 29, 72, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 90%, rgba(79, 70, 229, 0.15) 0%, transparent 40%);
    background-attachment: fixed;
}

html, body, [class*="css"] {
    font-family: 'Prompt', 'Outfit', sans-serif;
    color: #F8FAFC;
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 50px 20px 25px 20px;
}

.hero-badge {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 30px;
    background: rgba(225, 29, 72, 0.1);
    border: 1px solid rgba(225, 29, 72, 0.3);
    color: #FB7185;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 15px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.hero h1 {
    font-family: 'Outfit', 'Prompt', sans-serif;
    font-size: 3.4rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FFFFFF 20%, #FB7185 60%, #818CF8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 12px;
    letter-spacing: -0.5px;
    filter: drop-shadow(0 0 30px rgba(225, 29, 72, 0.2));
}

.hero p {
    color: #94A3B8;
    font-size: 1.15rem;
    letter-spacing: 0.3px;
    margin-top: 0;
    font-weight: 300;
}

/* Modern Glass Cards */
.card {
    background: linear-gradient(145deg, rgba(17, 24, 39, 0.7), rgba(11, 15, 25, 0.8));
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 20px;
    padding: 30px 24px;
    height: 280px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    margin-bottom: 24px;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    position: relative;
    overflow: hidden;
}

.card::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 20px;
    border: 1px solid rgba(251, 113, 133, 0);
    transition: border-color 0.4s ease;
    pointer-events: none;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px -15px rgba(225, 29, 72, 0.3);
    background: linear-gradient(145deg, rgba(22, 30, 49, 0.8), rgba(15, 23, 42, 0.9));
}

.card:hover::after {
    border-color: rgba(251, 113, 133, 0.4);
}

.card-top {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 12px;
}

.card .icon {
    font-size: 2rem;
    padding: 12px;
    background: rgba(255, 255, 255, 0.03);
    border-radius: 14px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    display: flex;
    align-items: center;
    justify-content: center;
}

.card h3 {
    color: #F8FAFC;
    font-family: 'Outfit', 'Prompt', sans-serif;
    margin: 0;
    font-size: 1.15rem;
    font-weight: 700;
    line-height: 1.4;
}

.card p {
    color: #94A3B8;
    font-size: 0.9rem;
    line-height: 1.6;
    margin: 0;
    font-weight: 300;
}

/* Premium Button */
.btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    text-align: center;
    text-decoration: none !important;
    padding: 12px 20px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 0.95rem;
    color: #FFFFFF !important;
    background: linear-gradient(135deg, #E11D48 0%, #4F46E5 100%);
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(225, 29, 72, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.btn:hover {
    background: linear-gradient(135deg, #F43F5E 0%, #6366F1 100%);
    box-shadow: 0 6px 25px rgba(225, 29, 72, 0.5);
    transform: translateY(-2px);
}

.section-divider {
    display: flex;
    align-items: center;
    text-align: center;
    color: #64748B;
    font-size: 0.9rem;
    font-weight: 500;
    letter-spacing: 1px;
    margin: 20px 0 35px 0;
    text-transform: uppercase;
}

.section-divider::before, .section-divider::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.section-divider::before { margin-right: 15px; }
.section-divider::after { margin-left: 15px; }

.custom-footer {
    text-align: center;
    color: #64748B;
    margin-top: 60px;
    padding: 30px 20px;
    font-size: 0.85rem;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
}

footer, #MainMenu { visibility: hidden; }

[data-testid="stSidebar"] {
    background: #0B0F19 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
}
</style>

<div class="hero">
    <div class="hero-badge">⚡ GRAPH-POWERED RECOMMENDATION</div>
    <h1>ANIME RECOMMENDATION</h1>
    <p>ระบบแนะนำอนิเมะอัจฉริยะด้วยฐานข้อมูลกราฟความสัมพันธ์ User & Anime</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-divider">ระบบและเครื่องมือทั้งหมด</div>',
    unsafe_allow_html=True,
)

APPS = [
    (
        "🎌",
        "โครงสร้างข้อมูล Anime & User",
        "จัดการข้อมูล User และ Anime ด้วยฐานข้อมูลกราฟ Neo4j",
        "https://colab.research.google.com/drive/1KMFRz3LPGn4fD5jBG-ZwCuxoh_yIozvE?usp=sharing",
        "เปิดใน Colab →",
    ),
    (
        "👥",
        "วิเคราะห์ความสัมพันธ์ User",
        "วิเคราะห์ความสัมพันธ์ FRIEND_OF และประวัติการดู Anime",
        "https://colab.research.google.com/drive/1UYPIwMs_xU9LFInJJ1FPOMk_e7nA3_Pt?usp=sharing",
        "เปิดใน Colab →",
    ),
    (
        "🎯",
        "ระบบแนะนำ Anime",
        "แนะนำ Anime จากความสัมพันธ์และ Anime ที่เพื่อนเคยดู",
        "https://9suvavqbzjuffsung5rryh.streamlit.app/",
        "ใช้งานระบบ →",
    ),
    (
        "🗄️",
        "Neo4j Database",
        "ฐานข้อมูลกราฟที่ใช้จัดเก็บ User, Anime และความสัมพันธ์",
        "https://neo4j.com/",
        "เยี่ยมชมเว็บไซต์ →",
    ),
]

# จัดเลย์เอาต์การ์ด: แถวแรก 3 ใบ และแถวที่ 4 วางตรงกลาง
cols = st.columns(3)
for i, (icon, title, desc, url, btn_text) in enumerate(APPS):
  if i < 3:
    with cols[i]:
      st.markdown(
          f"""
            <div class="card">
                <div>
                    <div class="card-top">
                        <div class="icon">{icon}</div>
                        <h3>{title}</h3>
                    </div>
                    <p>{desc}</p>
                </div>
                <a class="btn" href="{url}" target="_blank">{btn_text}</a>
            </div>
            """,
          unsafe_allow_html=True,
      )
  else:
    left, center, right = st.columns([1, 1.0, 1])
    with center:
      st.markdown(
          f"""
            <div class="card">
                <div>
                    <div class="card-top">
                        <div class="icon">{icon}</div>
                        <h3>{title}</h3>
                    </div>
                    <p>{desc}</p>
                </div>
                <a class="btn" href="{url}" target="_blank">{btn_text}</a>
            </div>
            """,
          unsafe_allow_html=True,
      )

st.markdown(
    """
    <div class="custom-footer">
        Anime Recommendation System &bull; Built with Streamlit & Neo4j &copy; 2026
    </div>
    """,
    unsafe_allow_html=True,
)