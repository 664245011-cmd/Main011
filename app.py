import streamlit as st

st.set_page_config(
    page_title="Anime Recommendation Hub",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;800&display=swap');

/* Main App Layout - Major Cinema Theme (Black, Gold & Red) */
.stApp {
    background-color: #08070A;
    background-image: 
        radial-gradient(circle at 50% 0%, rgba(229, 9, 20, 0.25) 0%, transparent 50%),
        radial-gradient(circle at 85% 90%, rgba(212, 175, 55, 0.15) 0%, transparent 40%);
    background-attachment: fixed;
}

html, body, [class*="css"] {
    font-family: 'Prompt', 'Outfit', sans-serif;
    color: #F5F5F7;
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
    background: linear-gradient(135deg, rgba(229, 9, 20, 0.2), rgba(212, 175, 55, 0.2));
    border: 1px solid #D4AF37;
    color: #F3C623;
    font-size: 0.85rem;
    font-weight: 700;
    margin-bottom: 15px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
}

.hero h1 {
    font-family: 'Outfit', 'Prompt', sans-serif;
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FFFFFF 20%, #F3C623 60%, #E50914 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 12px;
    letter-spacing: -0.5px;
    filter: drop-shadow(0 0 25px rgba(229, 9, 20, 0.4));
}

.hero p {
    color: #A1A1AA;
    font-size: 1.15rem;
    letter-spacing: 0.3px;
    margin-top: 0;
    font-weight: 300;
}

/* Movie Ticket Style Card */
.card {
    background: linear-gradient(145deg, #121016, #1A1721);
    border: 1px solid rgba(212, 175, 55, 0.3);
    border-radius: 16px;
    padding: 28px 24px;
    height: 290px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1);
    margin-bottom: 24px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
    position: relative;
    overflow: hidden;
}

/* Ticket Side Notches (รอยเจาะตั๋วหนัง) */
.card::before {
    content: '';
    position: absolute;
    left: -10px;
    top: 50%;
    transform: translateY(-50%);
    width: 20px;
    height: 20px;
    background-color: #08070A;
    border-radius: 50%;
    box-shadow: inset -2px 0 3px rgba(212, 175, 55, 0.3);
}

.card::after {
    content: '';
    position: absolute;
    right: -10px;
    top: 50%;
    transform: translateY(-50%);
    width: 20px;
    height: 20px;
    background-color: #08070A;
    border-radius: 50%;
    box-shadow: inset 2px 0 3px rgba(212, 175, 55, 0.3);
}

.card:hover {
    transform: translateY(-8px) scale(1.02);
    border-color: #F3C623;
    box-shadow: 0 15px 35px rgba(229, 9, 20, 0.35), 0 0 15px rgba(212, 175, 55, 0.2);
}

.card-top {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 12px;
}

.card .icon {
    font-size: 2rem;
    padding: 10px 14px;
    background: rgba(229, 9, 20, 0.15);
    border-radius: 12px;
    border: 1px solid rgba(229, 9, 20, 0.4);
    display: flex;
    align-items: center;
    justify-content: center;
}

.card h3 {
    color: #FFFFFF;
    font-family: 'Outfit', 'Prompt', sans-serif;
    margin: 0;
    font-size: 1.2rem;
    font-weight: 700;
    line-height: 1.3;
}

.card p {
    color: #A1A1AA;
    font-size: 0.9rem;
    line-height: 1.6;
    margin: 0;
    font-weight: 300;
}

/* Major Cinema Red/Gold Button */
.btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    text-align: center;
    text-decoration: none !important;
    padding: 12px 20px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 0.95rem;
    color: #FFFFFF !important;
    background: linear-gradient(135deg, #E50914 0%, #B81D24 100%);
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(229, 9, 20, 0.4);
    border: 1px solid #FF3B30;
    letter-spacing: 0.5px;
}

.btn:hover {
    background: linear-gradient(135deg, #FF1E27 0%, #E50914 100%);
    box-shadow: 0 6px 25px rgba(229, 9, 20, 0.7);
    color: #FFF275 !important;
    transform: translateY(-2px);
}

.section-divider {
    display: flex;
    align-items: center;
    text-align: center;
    color: #D4AF37;
    font-size: 0.9rem;
    font-weight: 700;
    letter-spacing: 2px;
    margin: 25px 0 35px 0;
    text-transform: uppercase;
}

.section-divider::before, .section-divider::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid rgba(212, 175, 55, 0.3);
}

.section-divider::before { margin-right: 15px; }
.section-divider::after { margin-left: 15px; }

.custom-footer {
    text-align: center;
    color: #71717A;
    margin-top: 60px;
    padding: 30px 20px;
    font-size: 0.85rem;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
}

footer, #MainMenu { visibility: hidden; }

[data-testid="stSidebar"] {
    background: #0F0E13 !important;
    border-right: 1px solid rgba(212, 175, 55, 0.2) !important;
}
</style>

<div class="hero">
    <div class="hero-badge">🎟️ CINEMA GRAPH SYSTEM</div>
    <h1>ANIME RECOMMENDATION</h1>
    <p>ระบบแนะนำอนิเมะอัจฉริยะ คัดสรรจากความสัมพันธ์ User & Anime</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-divider">🎬 เลือกบริการกดรับตั๋ว / ข้อมูลระบบ</div>',
    unsafe_allow_html=True,
)

APPS = [
    (
        "🎌",
        "โครงสร้างข้อมูล Anime & User",
        "จัดการข้อมูล User และ Anime ด้วยฐานข้อมูลกราฟ Neo4j",
        "https://colab.research.google.com/drive/1KMFRz3LPGn4fD5jBG-ZwCuxoh_yIozvE?usp=sharing",
        "เปิดใน Colab 🎟️",
    ),
    (
        "👥",
        "วิเคราะห์ความสัมพันธ์ User",
        "วิเคราะห์ความสัมพันธ์ FRIEND_OF และประวัติการดู Anime",
        "https://colab.research.google.com/drive/1UYPIwMs_xU9LFInJJ1FPOMk_e7nA3_Pt?usp=sharing",
        "เปิดใน Colab 🎟️",
    ),
    (
        "🎯",
        "ระบบแนะนำ Anime",
        "แนะนำ Anime จากความสัมพันธ์และ Anime ที่เพื่อนเคยดู",
        "https://9suvavqbzjuffsung5rryh.streamlit.app/",
        "จองตั๋ว / ใช้งานระบบ 🍿",
    ),
   (
        "⛅️",
        "Canva Presentation",
        "งานนำเสนอโปรเจค Anime Recommendation บน Canva",
        "https://canva.link/3u8r9s574edov6g",
        "เปิด Canva 🎬",
    ),
]

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
        Anime Recommendation System &bull; Cinema Edition Built with Streamlit & Neo4j &copy; 2026
    </div>
    """,
    unsafe_allow_html=True,
)
