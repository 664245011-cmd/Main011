import streamlit as st

st.set_page_config(
    page_title="Anime Recommendation",
    page_icon="🎌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Outfit:wght@400;600;800&display=swap');

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

.hero {
    text-align: center;
    padding: 45px 20px 20px 20px;
}

.hero h1 {
    font-family: 'Outfit', 'Prompt', sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FF758C 0%, #FF7EB3 50%, #7928CA 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
    letter-spacing: -0.5px;
    filter: drop-shadow(0 0 25px rgba(255, 117, 140, 0.3));
}

.hero p {
    color: #94A3B8;
    font-size: 1.15rem;
    letter-spacing: 0.5px;
    margin-top: 0;
    font-weight: 300;
}

/* Glassmorphism Card */
.card {
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 28px;
    height: 270px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    margin-bottom: 24px;
    box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.5);
    position: relative;
    overflow: hidden;
}

.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #FF758C, #8B5CF6, #3B82F6);
    opacity: 0.7;
    transition: opacity 0.3s ease;
}

.card:hover {
    transform: translateY(-8px);
    border-color: rgba(255, 117, 140, 0.4);
    box-shadow: 0 20px 40px -10px rgba(255, 117, 140, 0.25), 0 0 20px rgba(139, 92, 246, 0.2);
    background: rgba(15, 23, 42, 0.9);
}

.card:hover::before {
    opacity: 1;
}

.card .icon {
    font-size: 2.3rem;
    margin-bottom: 10px;
    display: inline-block;
    filter: drop-shadow(0 0 10px rgba(255, 117, 140, 0.4));
}

.card h3 {
    color: #FFFFFF;
    font-family: 'Outfit', 'Prompt', sans-serif;
    margin: 0 0 8px 0;
    font-size: 1.2rem;
    font-weight: 700;
}

.card p {
    color: #94A3B8;
    font-size: 0.90rem;
    line-height: 1.6;
    margin: 0;
}

/* Modern Gradient Button */
.btn {
    display: block;
    text-align: center;
    text-decoration: none !important;
    padding: 11px 20px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 0.95rem;
    color: #FFFFFF !important;
    background: linear-gradient(135deg, #FF758C 0%, #8B5CF6 100%);
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(255, 117, 140, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.15);
}

.btn:hover {
    background: linear-gradient(135deg, #FF8DA1 0%, #9D75F8 100%);
    box-shadow: 0 6px 22px rgba(255, 117, 140, 0.5);
    transform: translateY(-2px);
}

.section-title {
    text-align: center;
    color: #CBD5E1;
    font-size: 1.15rem;
    margin: 10px 0 30px 0;
    font-weight: 400;
}

.custom-footer {
    text-align: center;
    color: #64748B;
    margin-top: 50px;
    padding: 30px 20px;
    font-size: 0.85rem;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
}

footer, #MainMenu { visibility: hidden; }

[data-testid="stSidebar"] {
    background: #090D16 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
}
</style>

<div class="hero">
    <h1>ANIME RECOMMENDATION</h1>
    <p>ระบบแนะนำอนิเมะด้วยกราฟความสัมพันธ์ระหว่าง User และ Anime</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-title">✨ รวมโปรเจกต์ระบบ Anime Recommendation ของเรา</div>',
    unsafe_allow_html=True,
)

APPS = [
    (
        "🎌",
        "โครงสร้างข้อมูล Anime & User",
        "จัดการข้อมูล User และ Anime ด้วยฐานข้อมูลกราฟ Neo4j",
        "https://colab.research.google.com/drive/1KMFRz3LPGn4fD5jBG-ZwCuxoh_yIozvE?usp=sharing",
    ),
    (
        "👥",
        "วิเคราะห์ความสัมพันธ์ User",
        "วิเคราะห์ความสัมพันธ์ FRIEND_OF และประวัติการดู Anime",
        "https://colab.research.google.com/drive/1UYPIwMs_xU9LFInJJ1FPOMk_e7nA3_Pt?usp=sharing",
    ),
    (
        "🎯",
        "ระบบแนะนำ Anime",
        "แนะนำ Anime จากความสัมพันธ์และ Anime ที่เพื่อนเคยดู",
        "https://9suvavqbzjuffsung5rryh.streamlit.app/",
    ),
    (
        "🗄️",
        "Neo4j Database",
        "ฐานข้อมูลกราฟที่ใช้จัดเก็บ User, Anime และความสัมพันธ์",
        "https://neo4j.com/",
    ),
]

# การจัดเลย์เอาต์การ์ด: แถวแรก 3 ใบ และแถวที่ 4 วางตรงกลาง
cols = st.columns(3)
for i, (icon, title, desc, url) in enumerate(APPS):
  if i < 3:
    with cols[i]:
      st.markdown(
          f"""
            <div class="card">
                <div>
                    <div class="icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>
                <a class="btn" href="{url}" target="_blank">เปิดระบบ →</a>
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
                    <div class="icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>
                <a class="btn" href="{url}" target="_blank">เปิดเว็บไซต์ →</a>
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