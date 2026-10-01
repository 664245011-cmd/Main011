import base64
from pathlib import Path

import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ผู้พัฒนา | Anime Recommendation",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Orbitron:wght@500;600;700;800&display=swap');


    /* =========================
       GLOBAL
    ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(124, 58, 237, 0.22),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 15%,
                rgba(236, 72, 153, 0.18),
                transparent 25%
            ),
            radial-gradient(
                circle at 50% 100%,
                rgba(6, 182, 212, 0.12),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #070914 0%,
                #0b1020 50%,
                #080b17 100%
            );

        background-attachment: fixed;
        min-height: 100vh;
    }

    html,
    body,
    [class*="css"] {
        font-family: 'Prompt', sans-serif;
        color: #E5E7EB;
    }


    /* =========================
       HIDE STREAMLIT
    ========================= */

    footer,
    #MainMenu {
        visibility: hidden;
    }


    /* =========================
       MAIN CONTAINER
    ========================= */

    .block-container {
        max-width: 1100px !important;
        padding-top: 25px !important;
        padding-bottom: 60px !important;
    }


    /* =========================
       SIDEBAR
    ========================= */

    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                rgba(12, 15, 32, 0.98),
                rgba(8, 11, 23, 0.98)
            ) !important;

        border-right:
            1px solid rgba(139, 92, 246, 0.18) !important;
    }

    [data-testid="stSidebarNav"] {
        padding-top: 25px;
    }

    [data-testid="stSidebarNav"]::before {
        content: "✦ ANIME RECOMMENDATION";

        display: block;

        margin: 0 20px 22px 20px;
        padding-bottom: 18px;

        border-bottom:
            1px solid rgba(139, 92, 246, 0.2);

        font-family: 'Orbitron', sans-serif;
        font-size: 0.7rem;
        font-weight: 600;

        letter-spacing: 1.5px;

        color: #A78BFA;
    }

    [data-testid="stSidebarNav"] a {
        margin: 6px 12px !important;
        padding: 13px 16px !important;

        border-radius: 12px;

        color: #94A3B8 !important;

        font-family: 'Prompt', sans-serif;
        font-weight: 500;

        transition: all 0.25s ease;
    }

    [data-testid="stSidebarNav"] a:hover {
        background:
            rgba(139, 92, 246, 0.12) !important;

        color: #E9D5FF !important;

        transform: translateX(4px);
    }

    [data-testid="stSidebarNav"]
    a[aria-current="page"] {
        background:
            linear-gradient(
                90deg,
                rgba(139, 92, 246, 0.25),
                rgba(59, 130, 246, 0.08)
            ) !important;

        color: #C4B5FD !important;

        border-left:
            3px solid #A78BFA;
    }


    /* =========================
       SIDEBAR MENU TEXT
    ========================= */

    [data-testid="stSidebarNav"] li:nth-child(1) a * {
        font-size: 0 !important;
    }

    [data-testid="stSidebarNav"] li:nth-child(1) a::after {
        content: "🏠  หน้าหลัก";
        font-size: 0.95rem !important;
    }

    [data-testid="stSidebarNav"] li:nth-child(2) a * {
        font-size: 0 !important;
    }

    [data-testid="stSidebarNav"] li:nth-child(2) a::after {
        content: "👤  ผู้พัฒนา";
        font-size: 0.95rem !important;
    }


    /* =========================
       HERO
    ========================= */

    .hero {
        text-align: center;
        padding: 35px 20px 15px;
    }

    .hero-badge {
        display: inline-block;

        padding: 7px 18px;

        border-radius: 50px;

        background:
            rgba(139, 92, 246, 0.10);

        border:
            1px solid rgba(167, 139, 250, 0.25);

        color: #C4B5FD;

        font-size: 0.8rem;

        letter-spacing: 1.5px;

        margin-bottom: 18px;

        box-shadow:
            0 0 25px rgba(139, 92, 246, 0.12);
    }

    .hero h1 {
        margin: 0;

        font-family:
            'Orbitron',
            'Prompt',
            sans-serif;

        font-size: 3.3rem;
        font-weight: 800;

        background:
            linear-gradient(
                90deg,
                #C4B5FD,
                #A78BFA,
                #67E8F9,
                #F0ABFC
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        filter:
            drop-shadow(
                0 0 18px
                rgba(167, 139, 250, 0.25)
            );
    }

    .hero p {
        color: #94A3B8;

        font-size: 1rem;

        margin-top: 12px;

        letter-spacing: 0.5px;
    }


    /* =========================
       PROFILE IMAGE
    ========================= */

    .profile-section {
        display: flex;
        justify-content: center;

        margin-top: 25px;
        margin-bottom: 30px;
    }

    .profile-ring {
        width: 230px;
        height: 230px;

        border-radius: 50%;

        padding: 5px;

        background:
            conic-gradient(
                #8B5CF6,
                #22D3EE,
                #EC4899,
                #8B5CF6
            );

        box-shadow:
            0 0 30px rgba(139, 92, 246, 0.25),
            0 0 70px rgba(34, 211, 238, 0.08);

        animation:
            glow 4s ease-in-out infinite;
    }

    .profile-ring img {
        width: 100%;
        height: 100%;

        border-radius: 50%;

        object-fit: cover;

        display: block;

        border:
            6px solid #0B1020;
    }

    @keyframes glow {

        0%,
        100% {
            box-shadow:
                0 0 30px
                rgba(139, 92, 246, 0.25),

                0 0 70px
                rgba(34, 211, 238, 0.08);
        }

        50% {
            box-shadow:
                0 0 45px
                rgba(139, 92, 246, 0.45),

                0 0 90px
                rgba(34, 211, 238, 0.15);
        }
    }


    /* =========================
       PROFILE CARD
    ========================= */

    .profile-card {
        max-width: 650px;

        margin: 0 auto;

        padding: 35px;

        border-radius: 24px;

        background:
            linear-gradient(
                145deg,
                rgba(30, 41, 59, 0.72),
                rgba(15, 23, 42, 0.65)
            );

        border:
            1px solid rgba(167, 139, 250, 0.16);

        backdrop-filter: blur(20px);

        -webkit-backdrop-filter:
            blur(20px);

        box-shadow:
            0 20px 60px
            rgba(0, 0, 0, 0.35),

            inset 0 1px 0
            rgba(255, 255, 255, 0.04);

        position: relative;

        overflow: hidden;
    }

    .profile-card::before {
        content: "";

        position: absolute;

        width: 180px;
        height: 180px;

        top: -100px;
        right: -70px;

        background: #8B5CF6;

        filter: blur(80px);

        opacity: 0.15;
    }

    .profile-card h2 {
        text-align: center;

        margin: 0 0 8px;

        color: #F8FAFC;

        font-size: 1.8rem;

        font-weight: 700;
    }

    .profile-role {
        text-align: center;

        color: #A78BFA;

        font-size: 0.9rem;

        margin-bottom: 30px;

        letter-spacing: 1px;
    }


    /* =========================
       INFO GRID
    ========================= */

    .info-grid {
        display: grid;

        grid-template-columns:
            1fr 1fr;

        gap: 15px;
    }

    .info-box {
        padding: 18px 20px;

        border-radius: 16px;

        background:
            rgba(15, 23, 42, 0.65);

        border:
            1px solid
            rgba(148, 163, 184, 0.10);

        transition:
            all 0.25s ease;
    }

    .info-box:hover {
        transform:
            translateY(-3px);

        border-color:
            rgba(167, 139, 250, 0.35);

        background:
            rgba(30, 41, 59, 0.75);

        box-shadow:
            0 10px 25px
            rgba(0, 0, 0, 0.2);
    }

    .info-label {
        color: #64748B;

        font-size: 0.8rem;

        margin-bottom: 5px;
    }

    .info-value {
        color: #E2E8F0;

        font-size: 1rem;

        font-weight: 600;
    }

    .info-value.highlight {
        color: #A5B4FC;
    }


    /* =========================
       PROJECT BOX
    ========================= */

    .project-box {
        max-width: 650px;

        margin: 18px auto 0;

        padding: 18px 22px;

        border-radius: 16px;

        background:
            linear-gradient(
                90deg,
                rgba(139, 92, 246, 0.10),
                rgba(34, 211, 238, 0.06)
            );

        border:
            1px solid
            rgba(139, 92, 246, 0.15);

        text-align: center;
    }

    .project-title {
        color: #64748B;

        font-size: 0.78rem;

        letter-spacing: 1px;

        margin-bottom: 5px;
    }

    .project-name {
        color: #C4B5FD;

        font-size: 1rem;

        font-weight: 600;
    }


    /* =========================
       FOOTER
    ========================= */

    .custom-footer {
        text-align: center;

        color: #475569;

        margin-top: 55px;

        padding-top: 25px;

        border-top:
            1px solid
            rgba(148, 163, 184, 0.08);

        font-size: 0.8rem;

        letter-spacing: 0.5px;
    }


    /* =========================
       MOBILE
    ========================= */

    @media (max-width: 700px) {

        .hero h1 {
            font-size: 2.3rem;
        }

        .profile-ring {
            width: 190px;
            height: 190px;
        }

        .profile-card {
            padding: 25px 18px;
        }

        .info-grid {
            grid-template-columns: 1fr;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-badge">
            ✦ DEVELOPER PROFILE ✦
        </div>

        <h1>ผู้พัฒนา</h1>

        <p>
            ข้อมูลผู้จัดทำโปรเจค Anime Recommendation
        </p>

    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# PROFILE IMAGE
# =========================================================

photo_path = (
    Path(__file__).resolve().parent.parent
    / "assets"
    / "1.jpg"
)

try:

    photo_b64 = base64.b64encode(
        photo_path.read_bytes()
    ).decode()

    st.markdown(
        f"""
        <div class="profile-section">

            <div class="profile-ring">

                <img
                    src="data:image/jpeg;base64,{photo_b64}"
                    alt="Developer Profile"
                >

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

except FileNotFoundError:

    st.markdown(
        """
        <div class="profile-section">

            <div class="profile-ring">

                <div style="
                    width:100%;
                    height:100%;
                    border-radius:50%;
                    background:#111827;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:4rem;
                ">
                    🧑‍💻
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# PROFILE CARD
# =========================================================

st.markdown(
    """
    <div class="profile-card">

        <h2>
            ทินภัทร ช้อยสามนาค
        </h2>

        <div class="profile-role">
            COMPUTER SCIENCE • DEVELOPER
        </div>

        <div class="info-grid">

            <div class="info-box">

                <div class="info-label">
                    🪪 รหัสนักศึกษา
                </div>

                <div class="info-value highlight">
                    664245011
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    🎓 หมู่เรียน
                </div>

                <div class="info-value highlight">
                    Sec. 66/43
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    💻 Project
                </div>

                <div class="info-value">
                    Anime Recommendation
                </div>

            </div>


            <div class="info-box">

                <div class="info-label">
                    🚀 Project Year
                </div>

                <div class="info-value">
                    2026
                </div>

            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# PROJECT
# =========================================================

st.markdown(
    """
    <div class="project-box">

        <div class="project-title">
            CURRENT PROJECT
        </div>

        <div class="project-name">
            🌸 Anime Recommendation System
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="custom-footer">
        ✦ Anime Recommendation Projects 2026 ✦
    </div>
    """,
    unsafe_allow_html=True,
)