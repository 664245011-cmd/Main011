import streamlit as st

st.set_page_config(
    page_title="Major Cineplex | Anime Recommendation Hub",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;800&display=swap');

/* Overall Dark Background */
.stApp {
    background-color: #0B0B0E;
    background-image: linear-gradient(180deg, #050507 0%, #0B0B0E 100%);
    background-attachment: fixed;
}

html, body, [class*="css"] {
    font-family: 'Prompt', sans-serif;
    color: #FFFFFF;
}

/* Header Navbar - Major Style */
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

.major-nav-links {
    display: flex;
    gap: 20px;
    font-size: 0.85rem;
    color: #A1A1AA;
}

.major-nav-links span {
    cursor: pointer;
    transition: color 0.2s;
}

.major-nav-links span:hover {
    color: #E50914;
}

/* Banner Featured Hero Section with Anime Wallpaper Background */
.hero-banner {
    width: 100%;
    height: 230px;
    background: linear-gradient(90deg, rgba(5, 5, 7, 0.95) 0%, rgba(229, 9, 20, 0.65) 50%, rgba(5, 5, 7, 0.95) 100%), 
                url('https://images.unsplash.com/photo-1578632767115-351597cf2477?q=80&w=1200') center/cover;
    border-radius: 12px;
    padding: 35px 40px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    margin-bottom: 25px;
    border: 1px solid rgba(212, 175, 55, 0.3);
}

.hero-banner h1 {
    font-size: 2.2rem;
    font-weight: 800;
    margin: 0 0 8px 0;
    color: #FFFFFF;
    text-shadow: 0 2px 10px rgba(0,0,0,0.8);
}

.hero-banner p {
    color: #E4E4E7;
    font-size: 1.05rem;
    margin: 0;
    font-weight: 300;
}

/* Major Section Red Gradient Title Bar */
.section-header-red {
    background: linear-gradient(90deg, #E50914 0%, #8B0000 40%, rgba(11, 11, 14, 0) 100%);
    padding: 10px 20px;
    border-radius: 6px;
    font-size: 1.2rem;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
    letter-spacing: 0.5px;
}

/* Poster Card */
.movie-card {
    background: #141419;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.08);
    transition: all 0.3s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
    box-shadow: 0 8px 20px rgba(0,0,0,0.6);
    margin-bottom: 20px;
}

.movie-card:hover {
    transform: translateY(-8px);
    border-color: #E50914;
    box-shadow: 0 12px 28px rgba(229, 9, 20, 0.4);
}

/* ปรับปรุงการแสดงผลรูปโปสเตอร์การ์ดให้เต็มพื้นที่สมดุลกัน */
.movie-poster {
    width: 100%;
    height: 180px;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    position: relative;
    background-color: #1F1F28;
    display: flex;
    align-items: flex-end;
}

.poster-overlay {
    width: 100%;
    padding: 10px;
    background: linear-gradient(0deg, #141419 0%, transparent 100%);
}

.poster-badge {
    display: inline-block;
    padding: 3px 8px;
    background: #E50914;
    color: #FFFFFF;
    font-size: 0.7rem;
    font-weight: 700;
    border-radius: 4px;
    margin-bottom: 5px;
}

.movie-body {
    padding: 15px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    flex-grow: 1;
}

.movie-body h3 {
    font-size: 1.05rem;
    font-weight: 700;
    color: #FFFFFF;
    margin: 0 0 8px 0;
    line-height: 1.4;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.movie-body p {
    font-size: 0.82rem;
    color: #A1A1AA;
    line-height: 1.5;
    margin: 0 0 15px 0;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

/* Major Booking Button Style */
.btn-book {
    display: block;
    width: 100%;
    padding: 10px 0;
    text-align: center;
    background: linear-gradient(135deg, #E50914 0%, #B81D24 100%);
    color: #FFFFFF !important;
    font-weight: 700;
    font-size: 0.88rem;
    border-radius: 6px;
    text-decoration: none !important;
    transition: all 0.2s ease;
    border: 1px solid #FF3B30;
    box-shadow: 0 4px 12px rgba(229, 9, 20, 0.3);
}

.btn-book:hover {
    background: #FF1E27;
    box-shadow: 0 6px 18px rgba(229, 9, 20, 0.6);
    color: #FFF275 !important;
}

/* Footer */
.custom-footer {
    text-align: center;
    color: #71717A;
    margin-top: 50px;
    padding: 25px 20px;
    font-size: 0.85rem;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
}

footer, #MainMenu { visibility: hidden; }

[data-testid="stSidebar"] {
    background: #09090C !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
}
</style>

<!-- Major Top Bar Header -->
<div class="major-navbar">
    <div class="major-logo">
        <span style="font-size: 1.8rem;">🍿</span>
        <span class="brand">ANIME</span>
    </div>
    <div class="major-nav-links">
        <span>หน้าแรก</span>
        <span>ระบบแนะนำ</span>
        <span>ผู้พัฒนา</span>
    </div>
</div>

<!-- Major Feature Banner -->
<div class="hero-banner">
    <span class="poster-badge" style="width: fit-content; margin-bottom: 8px;">RECOMMENDED SYSTEM</span>
    <h1>ANIME RECOMMENDATION HUB</h1>
    <p>ระบบแนะนำอนิเมะอัจฉริยะ ประมวลผลจากฐานข้อมูลกราฟความสัมพันธ์ (Neo4j)</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-header-red">🎬 ระบบและเครื่องมือแนะนำทั้งหมด</div>',
    unsafe_allow_html=True,
)

# อัปเดตลิงก์รูปภาพให้เข้ากับธีมมืดและสไตล์เดียวกันทั้งหมด
APPS = [
    (
        "🎌",
        "โครงสร้างข้อมูล Anime & User",
        "จัดการข้อมูล User และ Anime ด้วยฐานข้อมูลกราฟ Neo4j",
        "https://colab.research.google.com/drive/1KMFRz3LPGn4fD5jBG-ZwCuxoh_yIozvE?usp=sharing",
        "เปิดใน Colab 🎟️",
        "https://upload.wikimedia.org/wikipedia/commons/d/d0/Google_Colaboratory_SVG_Logo.svg",
    ),
    (
        "👥",
        "วิเคราะห์ความสัมพันธ์ User",
        "วิเคราะห์ความสัมพันธ์ FRIEND_OF และประวัติการดู Anime",
        "https://colab.research.google.com/drive/1UYPIwMs_xU9LFInJJ1FPOMk_e7nA3_Pt?usp=sharing",
        "เปิดใน Colab 🎟️",
        "https://upload.wikimedia.org/wikipedia/commons/d/d0/Google_Colaboratory_SVG_Logo.svg",
    ),
    (
        "🎯",
        "ระบบแนะนำ Anime",
        "แนะนำ Anime จากความสัมพันธ์และ Anime ที่เพื่อนเคยดู",
        "https://9suvavqbzjuffsung5rryh.streamlit.app/",
        "เปิดใน streamlit 🎟️",
        "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?q=80&w=600",
    ),
    (
        "⛅️",
        "Canva Presentation",
        "งานนำเสนอสไลด์โปรเจกต์ Anime Recommendation บน Canva",
        "https://canva.link/3u8r9s574edov6g",
        "เข้าชม Canva 🎬",
        "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=600",
    ),
    (
        "⛅️",
        "แบบฝีกหัด",
        "แบบฝีกหัดสไลด์ บน Canva",
        "https://canva.link/n0t7yuf9venb98p",
        "เข้าชม Canva 🎬",
        "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=600",
    ),
    (
        "⛅️",
        "github",
        "เข้าเว็บ github",
        "https://github.com/664245011-cmd",
        "เข้าเว็บ github 🎬",
        "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?q=80&w=600",
    ),
]

cols = st.columns(4)
for i, (icon, title, desc, url, btn_text, img_url) in enumerate(APPS):
    with cols[i % 4]:
        st.markdown(
            f"""
            <div class="movie-card">
                <div class="movie-poster" style="background-image: url('{img_url}');">
                    <div class="poster-overlay">
                        <span class="poster-badge">{icon} FEATURE</span>
                    </div>
                </div>
                <div class="movie-body">
                    <div>
                        <h3>{title}</h3>
                        <p>{desc}</p>
                    </div>
                    <a class="btn-book" href="{url}" target="_blank">{btn_text}</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="custom-footer">
        Major Anime Recommendation System &bull; Powered by Streamlit & Neo4j &copy; 2026
    </div>
    """,
    unsafe_allow_html=True,
)
