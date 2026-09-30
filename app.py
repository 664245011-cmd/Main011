import streamlit as st

st.set_page_config(
    page_title="ML Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Inter:wght@400;600;800&display=swap');

/* Main App Layout - Modern Dark Theme */
.stApp {
    background-color: #0B0F19;
    background-image: 
        radial-gradient(circle at 15% 50%, rgba(99, 102, 241, 0.15) 0%, transparent 25%),
        radial-gradient(circle at 85% 30%, rgba(139, 92, 246, 0.15) 0%, transparent 25%),
        radial-gradient(circle at 50% 80%, rgba(6, 182, 212, 0.1) 0%, transparent 30%);
    background-attachment: fixed;
}

html, body, [class*="css"] { 
    font-family: 'Prompt', 'Inter', sans-serif; 
    color: #E2E8F0;
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 50px 20px 30px 20px;
}
.hero h1 {
    font-family: 'Inter', 'Prompt', sans-serif;
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #818CF8 0%, #A78BFA 50%, #22D3EE 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 12px;
    letter-spacing: -1px;
    line-height: 1.2;
}
.hero p { 
    color: #94A3B8; 
    font-size: 1.15rem; 
    letter-spacing: 0.5px; 
    margin-top: 0; 
    font-weight: 300;
}

/* Cards */
.card {
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: 20px;
    padding: 28px;
    height: 260px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    margin-bottom: 24px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    position: relative;
    overflow: hidden;
}

.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(167, 139, 250, 0.6), transparent);
    opacity: 0;
    transition: opacity 0.4s ease;
}

.card:hover {
    transform: translateY(-8px);
    border-color: rgba(167, 139, 250, 0.4);
    box-shadow: 0 20px 40px -5px rgba(99, 102, 241, 0.25), 0 10px 20px -5px rgba(0, 0, 0, 0.3);
    background: rgba(30, 41, 59, 0.8);
}

.card:hover::before {
    opacity: 1;
}

.card .icon { 
    font-size: 2.5rem; 
    margin-bottom: 12px;
    display: inline-block;
    filter: drop-shadow(0 0 8px rgba(167, 139, 250, 0.4));
}
.card h3 { 
    color: #F1F5F9; 
    margin: 0 0 8px 0; 
    font-size: 1.25rem; 
    font-weight: 600; 
}
.card p { 
    color: #94A3B8; 
    font-size: 0.9rem; 
    line-height: 1.6; 
    margin: 0;
}

/* Buttons */
.btn {
    display: block;
    text-align: center;
    text-decoration: none !important;
    padding: 12px 20px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 0.95rem;
    color: #FFFFFF !important;
    background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%);
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.1);
}
.btn:hover {
    background: linear-gradient(135deg, #818CF8 0%, #A78BFA 100%);
    box-shadow: 0 8px 25px rgba(139, 92, 246, 0.45);
    transform: translateY(-2px);
}

/* Hide default Streamlit elements */
footer, #MainMenu { visibility: hidden; }
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { visibility: visible !important; }

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background: #0F1525 !important;
    border-right: 1px solid rgba(148, 163, 184, 0.1) !important;
}
[data-testid="stSidebarNav"] {
    padding-top: 20px;
}
[data-testid="stSidebarNav"]::before {
    content: "ML HUB NAVIGATION";
    display: block;
    margin: 0 20px 20px 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(148, 163, 184, 0.15);
    font-family: 'Inter', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: #64748B;
}
[data-testid="stSidebarNav"] a {
    margin: 4px 12px !important;
    padding: 12px 16px !important;
    border-radius: 10px;
    color: #94A3B8 !important;
    font-family: 'Prompt', sans-serif;
    font-weight: 500;
    font-size: 0.95rem;
    transition: all 0.2s ease;
    background: transparent !important;
}
[data-testid="stSidebarNav"] a:hover {
    background: rgba(99, 102, 241, 0.1) !important;
    color: #C7D2FE !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: linear-gradient(90deg, rgba(99, 102, 241, 0.2) 0%, transparent 100%) !important;
    color: #A5B4FC !important;
    border-left: 3px solid #818CF8;
    font-weight: 600;
}

/* เปลี่ยนข้อความเมนู: app -> หน้าหลัก, about -> ผู้พัฒนา */
[data-testid="stSidebarNav"] li:nth-child(1) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(1) a::after { content: "🏠 หน้าหลัก"; font-size: 0.95rem !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a * { font-size: 0 !important; }
[data-testid="stSidebarNav"] li:nth-child(2) a::after { content: "👨‍💻 ผู้พัฒนา"; font-size: 0.95rem !important; }

/* Footer */
.custom-footer {
    text-align: center;
    color: #64748B;
    margin-top: 40px;
    padding: 30px 20px;
    font-size: 0.85rem;
    border-top: 1px solid rgba(148, 163, 184, 0.1);
}
</style>

<div class="hero">
    <h1>MACHINE LEARNING HUB</h1>
    <p>ศูนย์รวมเว็บแอปพลิเคชัน Machine Learning และ AI อัจฉริยะ</p>
</div>
""", unsafe_allow_html=True)

st.write("")

APPS = [
    ("🌳", "งานที่ 1", "relationships", "https://colab.research.google.com/drive/1KMFRz3LPGn4fD5jBG-ZwCuxoh_yIozvE?authuser=1"),
    ("🛡️", "งานที่ 2", "relationships", "https://colab.research.google.com/drive/1KMFRz3LPGn4fD5jBG-ZwCuxoh_yIozvE?authuser=1"),
    ("🎯", "งานที่ 3", "relationships", "https://9suvavqbzjuffsung5rryh.streamlit.app/"),
]

cols = st.columns(3)
for i, (icon, title, desc, url) in enumerate(APPS):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card">
            <div>
                <div class="icon">{icon}</div>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            <a class="btn" href="{url}" target="_blank">เปิดแอปพลิเคชัน →</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="custom-footer">
    Made with ❤️ using Streamlit · Machine Learning Projects 2026
</div>
""", unsafe_allow_html=True)