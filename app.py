import streamlit as st

st.set_page_config(
    page_title="Anime Recommendation Hub",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');

/* Cyberpunk Dark Terminal Theme */
.stApp {
    background-color: #020617;
    background-image: 
        linear-gradient(rgba(15, 23, 42, 0.4) 1px, transparent 1px),
        linear-gradient(90deg, rgba(15, 23, 42, 0.4) 1px, transparent 1px),
        radial-gradient(circle at 50% 0%, rgba(16, 185, 129, 0.1) 0%, transparent 50%);
    background-size: 24px 24px, 24px 24px, 100% 100%;
    background-attachment: fixed;
}

html, body, [class*="css"] {
    font-family: 'Prompt', 'JetBrains Mono', sans-serif;
    color: #E2E8F0;
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 50px 20px 20px 20px;
}

.hero-tag {
    font-family: 'JetBrains Mono', monospace;
    display: inline-block;
    padding: 4px 12px;
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: #34D399;
    font-size: 0.8rem;
    font-weight: 700;
    border-radius: 4px;
    margin-bottom: 15px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.hero h1 {
    font-family: 'JetBrains Mono', 'Prompt', sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #34D399 0%, #38BDF8 50%, #818CF8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
    letter-spacing: -1px;
    filter: drop-shadow(0 0 25px rgba(52, 211, 153, 0.2));
}

.hero p {
    color: #94A3B8;
    font-size: 1.1rem;
    letter-spacing: 0.5px;
    margin-top: 0;
    font-weight: 300;
}

/* Neon Cyber Cards */
.card {
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(52, 211, 153, 0.15);
    border-radius: 12px;
    padding: 28px 24px;
    height: 280px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    backdrop-filter: blur(12px);
    transition: all 0.3s ease;
    margin-bottom: 24px;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    position: relative;
}

.card:hover {
    transform: translateY(-5px);
    border-color: rgba(52, 211, 153, 0.6);
    box-shadow: 0 0 25px rgba(52, 211, 153, 0.2), inset 0 0 15px rgba(52, 211, 153, 0.05);
    background: rgba(15, 23, 42, 0.95);
}

.card-top {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 10px;
}

.card .icon {
    font-size: 1.8rem;
    padding: 10px;
    background: rgba(52, 211, 153, 0.08);
    border: 1px solid rgba(52, 211, 153, 0.2);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.card h3 {
    color: #F8FAFC;
    font-family: 'Prompt', sans-serif;
    margin: 0;
    font-size: 1.15rem;
    font-weight: 700;
}

.card p {
    color: #94A3B8;
    font-size: 0.9rem;
    line-height: 1.6;
    margin: 0;
}

/* Cyber Neon Button */
.btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    text-align: center;
    text-decoration: none !important;
    padding: 11px 20px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 0.9rem;
    font-family: 'JetBrains Mono', sans-serif;
    color: #020617 !important;
    background: #34D399;
    transition: all 0.25s ease;
    box-shadow: 0 4px 15px rgba(52, 211, 153, 0.3);
}

.btn:hover {
    background: #6EE7B7;
    box-shadow: 0 0 20px rgba(110, 231, 183, 0.6);
    transform: translateY(-2px);
}

.section-title {
    text-align: center;
    color: #64748B;
    font-size: 0.95rem;
    font-family: 'JetBrains Mono', monospace;
    margin: 15px 0 30px 0;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.custom-footer {
    text-align: center;
    color: #64748B;
    margin-top: 50px;
    padding: 30px 20px;
    font-size: 0.85rem;
    font-family: 'JetBrains Mono', monospace;
    border-top: 1px solid rgba(52, 211, 153, 0.1);
}

footer, #MainMenu { visibility: hidden; }

[data-testid="stSidebar"] {
    background: #020617 !important;
    border-right: 1px solid rgba(52, 211, 153, 0.1) !important;
}
</style>

<div class="hero">
    <div class="hero-tag">// SYSTEM_ONLINE_v2.6</div>
    <h1>ANIME RECOMMENDATION</h1>
    <p>ระบบแนะนำอนิเมะอัจฉริยะด้วยฐานข้อมูลกราฟความสัมพันธ์ User & Anime</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">// AVAILABLE MODULES & LINKS</div>',
    unsafe_allow_html=True,
)

APPS = [
    (
        "🎌",
        "โครงสร้างข้อมูล Anime & User",
        "จัดการข้อมูล User และ Anime ด้วยฐานข้อมูลกราฟ Neo4j",
        "https://colab.research.google.com/drive/1KMFRz3LPGn4fD5jBG-ZwCuxoh_yIozvE?usp=sharing",
        "ACCESS_COLAB",
    ),
    (
        "👥",
        "วิเคราะห์ความสัมพันธ์ User",
        "วิเคราะห์ความสัมพันธ์ FRIEND_OF และประวัติการดู Anime",
        "https://colab.research.google.com/drive/1UYPIwMs_xU9LFInJJ1FPOMk_e7nA3_Pt?usp=sharing",
        "ACCESS_COLAB",
    ),
    (
        "🎯",
        "ระบบแนะนำ Anime",
        "แนะนำ Anime จากความสัมพันธ์และ Anime ที่เพื่อนเคยดู",
        "https://9suvavqbzjuffsung5rryh.streamlit.app/",
        "LAUNCH_APP",
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
                <a class="btn" href="{url}" target="_blank">[{btn_text}] →</a>
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
                <a class="btn" href="{url}" target="_blank">[{btn_text}] →</a>
            </div>
            """,
          unsafe_allow_html=True,
      )

st.markdown(
    """
    <div class="custom-footer">
        [ ROOT@ANIME-REC-SYSTEM:~# ] &bull; 2026 ALL RIGHTS RESERVED
    </div>
    """,
    unsafe_allow_html=True,
)