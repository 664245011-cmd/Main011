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
    justify-content: flex-start;
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
