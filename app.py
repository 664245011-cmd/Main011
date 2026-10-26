
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

<!-- Header: logo only (navigation links removed) -->
<div class="major-navbar">
    <div class="major-logo">
        <span style="font-size: 1.8rem;">🍿</span>
        <span class="brand">ANIME</span>
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
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDyBXS1JbKttxnxaeSKQkdqdZkZRPf2qYA1goKOn_iug&s=10",
    ),
    (
        "⛅️️",
        "Canva Presentation",
        "งานนำเสนอสไลด์โปรเจกต์ Anime Recommendation บน Canva",
        "https://canva.link/3u8r9s574edov6g",
        "เข้าชม Canva 🎬",
        "https://logos-world.net/wp-content/uploads/2021/11/Canva-Logo.png",
    ),
    (
        "⛅️",
        "แบบฝึกหัด",
        "แบบฝึกหัดสไลด์ บน Canva",
        "https://canva.link/n0t7yuf9venb98p",
        "เข้าชม Canva 🎬",
        "https://cdn-icons-png.flaticon.com/512/2991/2991108.png",
    ),
    (
        "⛅️",
        "GitHub",
        "เข้าเว็บ GitHub",
        "https://github.com/664245011-cmd",
        "เข้าเว็บ GitHub 🎬",
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
                    <a class="btn-book" href="{url}" target="_blank" rel="noopener noreferrer">{btn_text}</a>
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
