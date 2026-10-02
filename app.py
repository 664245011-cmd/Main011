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
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700;800&family=Prompt:wght@300;400;500;600;700&display=swap');

/* Dynamic Holographic Background */
.stApp {
    background: #020617;
    background-image: 
        radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.15) 0px, transparent 50%),
        radial-gradient(at 100% 0%, rgba(236, 72, 153, 0.15) 0px, transparent 50%),
        radial-gradient(at 50% 100%, rgba(129, 140, 248, 0.12) 0px, transparent 50%);
    background-attachment: fixed;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', 'Prompt', sans-serif;
    color: #F8FAFC;
}

/* Header & Hero Area */
.hero-wrapper {
    text-align: center;
    padding: 60px 20px 40px 20px;
    position: relative;
}

.hero-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 20px;
    border-radius: 9999px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(10px);
    color: #38BDF8;
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    box-shadow: 0 0 20px rgba(56, 189, 248, 0.2);
    margin-bottom: 20px;
}

.hero-pill span {
    width: 8px;
    height: 8px;
    background: #38BDF8;
    border-radius: 50%;
    box-shadow: 0 0 10px #38BDF8;
}

.main-title {
    font-size: 3.8rem;
    font-weight: 800;
    line-height: 1.1;
    background: linear-gradient(180deg, #FFFFFF 30%, #94A3B8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 16px;
    letter-spacing: -1.5px;
}

.main-title .highlight {
    background: linear-gradient(135deg, #38BDF8 0%, #818CF8 50%, #F472B6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.sub-title {
    color: #94A3B8;
    font-size: 1.2rem;
    max-width: 650px;
    margin: 0 auto;
    font-weight: 400;
    line-height: 1.6;
}

/* Ultra Modern Glass Cards */
.card-grid {
    padding: 10px 0;
}

.ultra-card {
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 28px;
    padding: 32px 28px;
    height: 320px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    backdrop-filter: blur(20px);
    position: relative;
    overflow: hidden;
    transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
    margin-bottom: 24px;
}

/* Light beam effect on top of card */
.ultra-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.8), transparent);
    transition: 0.7s;
}

.ultra-card:hover::before {
    left: 100%;
}

.ultra-card:hover {
    transform: translateY(-12px);
    border-color: rgba(56, 189, 248, 0.3);
    background: rgba(30, 41, 59, 0.7);
    box-shadow: 
        0 20px 40px -15px rgba(0, 0, 0, 0.7),
        0 0 30px rgba(56, 189, 248, 0.15);
}

.card-header {
    display: flex;
    align-items: flex-start;
    gap: 18px;
}

.card-icon {
    width: 54px;
    height: 54px;
    min-width: 54px;
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.01));
    border: 1px solid rgba(255, 255, 255, 0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.2);
}

.card-body h3 {
    color: #F8FAFC;
    font-size: 1.3rem;
    font-weight: 700;
    margin: 0 0 8px 0;
    line-height: 1.3;
}

.card-body p {
    color: #64748B;
    font-size: 0.95rem;
    line-height: 1.6;
    margin: 0;
}

/* High-Contrast Action Button with Shimmer */
.action-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    padding: 14px 24px;
    border-radius: 16px;
    font-weight: 700;
    font-size: 0.95rem;
    color: #020617 !important;
    background: #F8FAFC;
    text-decoration: none !important;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(255, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
}

.action-btn:hover {
    background: #38BDF8;
    color: #020617 !important;
    box-shadow: 0 0 25px rgba(56, 189, 248, 0.6);
    transform: scale(1.02);
}

/* Section Divider */
.divider-container {
    text-align: center;
    margin: 40px 0 50px 0;
    position: relative;
}

.divider-line {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    width: 100%;
}

.divider-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: #020617;
    padding: 0 20px;
    color: #475569;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* Footer */
.footer {
    text-align: center;
    padding: 40px 0;
    color: #475569;
    font-size: 0.85rem;
}

footer, #MainMenu { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
</style>

<div class="hero-wrapper">
    <div class="hero-pill"><span></span> NEXT-GEN RECOMMENDATION Engine</div>
    <div class="main-title">ANIME <span class="highlight">HUB</span></div>
    <div class="sub-title">ปลดล็อกการค้นพบอนิเมะด้วยพลังแห่ง Neo4j Graph Database เชื่อมโยงทุกมิติความสัมพันธ์ของผู้ใช้และอนิเมะ</div>
</div>

<div class="divider-container">
    <div class="divider-line"></div>
    <div class="divider-text">EXPLORE SYSTEMS</div>
</div>
""",
    unsafe_allow_html=True,
)

APPS = [
    (
        "🎌",
        "โครงสร้างข้อมูล Anime & User",
        "เข้าถึงข้อมูลเชิงลึก บริหารจัดการโหนด User และ Anime บนฐานข้อมูลกราฟ Neo4j",
        "https://colab.research.google.com/drive/1KMFRz3LPGn4fD5jBG-ZwCuxoh_yIozvE?usp=sharing",
        "เปิดโปรเจกต์ใน Colab ↗",
    ),
    (
        "👥",
        "วิเคราะห์ความสัมพันธ์ User",
        "สำรวจเครือข่ายความสัมพันธ์ FRIEND_OF และพฤติกรรมการรับชมอนิเมะของผู้ใช้งาน",
        "https://colab.research.google.com/drive/1UYPIwMs_xU9LFInJJ1FPOMk_e7nA3_Pt?usp=sharing",
        "เปิดโปรเจกต์ใน Colab ↗",
    ),
    (
        "🎯",
        "ระบบแนะนำ Anime อัจฉริยะ",
        "ประมวลผลคำแนะนำอนิเมะแบบเรียลไทม์ โดยอ้างอิงจากรสนิยมของกลุ่มเพื่อนคุณ",
        "https://9suvavqbzjuffsung5rryh.streamlit.app/",
        "เข้าสู่ระบบคำแนะนำ 🚀",
    ),
]

# Layout Display
cols = st.columns(3)
for i, (icon, title, desc, url, btn_text) in enumerate(APPS):
    with cols[i]:
        st.markdown(
            f"""
            <div class="ultra-card">
                <div>
                    <div class="card-header">
                        <div class="card-icon">{icon}</div>
                        <div class="card-body">
                            <h3>{title}</h3>
                            <p>{desc}</p>
                        </div>
                    </div>
                </div>
                <a class="action-btn" href="{url}" target="_blank">{btn_text}</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="footer">
        Anime Recommendation System &bull; Powered by Streamlit & Neo4j
    </div>
    """,
    unsafe_allow_html=True,
)