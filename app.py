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

.movie-poster {
    width: 100%;
    height: 200px;
    background-size: contain;
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
        "https://logos-world.net/wp-content/uploads/2021/11/Canva-Logo.png",
    ),
    (
        "⛅️",
        "แบบฝีกหัด",
        "แบบฝีกหัดสไลด์ บน Canva",
        "https://canva.link/n0t7yuf9venb98p",
        "เข้าชม Canva 🎬",
        "data:image/png;base64,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",
    ),
    (
        "⛅️",
        "github",
        "เข้าเว็บ github",
        "https://github.com/664245011-cmd",
        "เข้าเว็บ github 🎬",
        "https://upload.wikimedia.org/wikipedia/commons/c/c2/GitHub_Invertocat_Logo.svg",
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
