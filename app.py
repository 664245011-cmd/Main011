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

/* Main App Layout - Cyberpunk / Neon Violet Theme */
.stApp {
    background-color: #080711;
    background-image: 
        radial-gradient(circle at 20% 15%, rgba(168, 85, 247, 0.22) 0%, transparent 45%),
        radial-gradient(circle at 80% 85%, rgba(14, 165, 233, 0.18) 0%, transparent 45%),
        radial-gradient(circle at 50% 50%, rgba(236, 72, 153, 0.08) 0%, transparent 60%);
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
    padding: 6px 18px;
    border-radius: 30px;
    background: rgba(168, 85, 247, 0.12);
    border: 1px solid rgba(168, 85, 247, 0.4);
    color: #C084FC;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 16px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    box-shadow: 0 0 15px rgba(168, 85, 247, 0.2);
}

.hero h1 {
    font-family: 'Outfit', 'Prompt', sans-serif;
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FFFFFF 10%, #F472B6 45%, #C084FC 75%, #38BDF8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 14px;
    letter-spacing: -0.5px;
    filter: drop-shadow(0 0 35px rgba(168, 85, 247, 0.35));
}

.hero p {
    color: #A1A1AA;
    font-size: 1.15rem;
    letter-spacing: 0.3px;
    margin-top: 0;
    font-weight: 300;
}

/* Glassmorphism Cards */
.card {
    background: linear-gradient(145deg, rgba(24, 20, 42, 0.75), rgba(12, 10, 24, 0.85));
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 22px;
    padding: 30px 24px;
    height: 280px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    margin-bottom: 24px;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.6);
    position: relative;
    overflow: hidden;
}

.card::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 22px;
    border: 1px solid rgba(192, 132, 252, 0);
    transition: border-color 0.4s ease;
    pointer-events: none;
}

.card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0 20px 45px -12px rgba(168, 85, 247, 0.4);
    background: linear-gradient(145deg, rgba(35, 28, 62, 0.85), rgba(18, 14, 36, 0.95));
}

.card:hover::after {
    border-color: rgba(192, 132, 252, 0.5);
}

.card-top {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 12px;
}

.card .icon {
    font-size: 2.1rem;
    padding: 12px;
    background: rgba(168, 85, 247, 0.1);
    border-radius: 16px;
    border: 1px solid rgba(168, 85, 247, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: inset 0 0 12px rgba(168, 85, 247, 0.15);
}

.card h3 {
    color: #F4F4F5;
    font-family: 'Outfit', 'Prompt', sans-serif;
    margin: 0;
    font-size: 1.18rem;
    font-weight: 700;
    line-height: 1.4;
}

.card p {
    color: #A1A1AA;
    font-size: 0.92rem;
    line-height: 1.6;
    margin: 0;
    font-weight: 300;
}

/* Neon Glow Button */
.btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    text-align: center;
    text-decoration: none !important;
    padding: 13px 20px;
    border-radius: 14px;
    font-weight: 600;
    font-size: 0.95rem;
    color: #FFFFFF !important;
    background: linear-gradient(135deg, #EC4899 0%, #8B5CF6 50%, #06B6D4 100%);
    background-size: 200% auto;
    transition: all 0.4s ease;
    box-shadow: 0 4px 20px rgba(139, 92, 246, 0.35);
    border: 1px solid rgba(255, 255, 255, 0.15);
}

.btn:hover {
    background-position: right center;
    box-shadow: 0 6px 28px rgba(236, 72, 153, 0.55);
    transform: translateY(-2px);
}

.section-divider {
    display: flex;
    align-items: center;
    text-align: center;
    color: #71717A;
    font-size: 0.88rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    margin: 20px 0 35px 0;
    text-transform: uppercase;
}

.section-divider::before, .section-divider::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.section-divider::before { margin-right: 18px; }
.section-divider::after { margin-left: 18px; }

.custom-footer {
    text-align: center;
    color: #71717A;
    margin-top: 60px;
    padding: 30px 20px;
    font-size: 0.85rem;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
}

footer, #MainMenu { visibility: hidden; }

[data-testid="stSidebar"] {
    background: #0C0A18 !important;
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