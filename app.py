import streamlit as st
from message_detector import message_detector_ui # Linking your code
from image_detector import image_detector_ui

# --- 1. HOME PAGE STYLING ---
def apply_home_styles():
    st.markdown("""
        <style>
        /* CodeChef Grid Background */
        .stApp {
            background-color: #ffffff;
            background-image: 
                linear-gradient(to right, #e2e8f0 1px, transparent 1px),
                linear-gradient(to bottom, #e2e8f0 1px, transparent 1px);
            background-size: 40px 40px;
        }

        /* Top Navbar */
        .navbar {
            display: flex; justify-content: space-between; align-items: center;
            padding: 15px 60px; background-color: rgba(255, 255, 255, 0.9);
            position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
            border-bottom: 1px solid #e2e8f0;
        }
        .nav-left { font-size: 26px; font-weight: 800; color: #2D3748; }
        .nav-right { display: flex; gap: 15px; }

        /* Login Button - Changed to Grey */
        .login-btn { 
            background-color: #F0F2F6 !important; 
            color: #000000 !important; 
            border: 1px solid #cbd5e0 !important;
            padding: 8px 22px; border-radius: 8px; font-weight: 600;
        }

        /* Sign Up Button */
        .signup-btn { 
            background-color: #3182ce; color: white; border: none;
            padding: 8px 22px; border-radius: 8px; font-weight: 600;
        }

        /* Hero Section Styling */
        .hero { text-align: center; padding: 160px 20px 60px 20px; }
        .hero h1 { font-size: 64px; font-weight: 850; color: #2b6cb0; line-height: 1.1; }
        
        /* Hero Sub-text - Changed Font Color to BLACK */
        .hero p { 
            font-size: 22px; 
            color: #000000 !important; 
            max-width: 800px; margin: 0 auto; font-weight: 500; 
        }

        /* Action Cards */
        .action-card {
            background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 24px;
            padding: 40px; text-align: center;
        }

        #MainMenu, footer, header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

# --- 2. PAGE COMPONENTS ---
def home_page():
    apply_home_styles()
    # Navbar
    st.markdown("""
        <div class="navbar">
            <div class="nav-left">FraudGuard</div>
            <div class="nav-right">
                <button class="login-btn">Login</button>
                <button class="signup-btn">Sign Up</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown("""
        <div class="hero">
            <h1>Suspicious Link? Unknown Image?<br>Let's Secure it for Real.</h1>
            <p>Going to protect thousands of users from phishing, deepfakes, and scammers with our real-time AI engine.</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")
    
    # Action Cards
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="action-card"><h1 style="font-size:60px;"></h1><h3>AI Message Detector</h3></div>', unsafe_allow_html=True)
        if st.button("Open Message Scanner", use_container_width=True):
            st.session_state.page = "message"
            st.rerun()
    with col2:
        st.markdown('<div class="action-card"><h1 style="font-size:60px;"></h1><h3>AI Image Detector</h3></div>', unsafe_allow_html=True)
        if st.button("Open Image Scanner", use_container_width=True):
            st.session_state.page = "image"
            st.rerun()

    # How it Works Section (Scroll down part)
    st.markdown("""
        <div style="background: white; padding: 60px; margin-top: 50px; border-radius: 30px; border: 1px solid #e2e8f0;">
            <h2 style='text-align: center; color: #2D3748;'>How FraudGuard Works</h2>
            <div style='display: flex; gap: 30px; margin-top: 30px;'>
                <div style='flex: 1;'>
                    <h4 style='color: #2b6cb0;'>1. Detection</h4>
                    <p style='color: black;'>Our AI scans text for 'Urgency' and 'Threats' and images for 'Pixel manipulation'.</p>
                </div>
                <div style='flex: 1;'>
                    <h4 style='color: #2b6cb0;'>2. Analysis</h4>
                    <p style='color: black;'>Links are cross-referenced with global phishing databases in milliseconds.</p>
                </div>
                <div style='flex: 1;'>
                    <h4 style='color: #2b6cb0;'>3. Protection</h4>
                    <p style='color: black;'>You receive a clear verdict and a voice explanation to stay safe.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- 3. MAIN NAVIGATION ---
def main():
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "message":
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if st.sidebar.button("Back to Home"):
            st.session_state.page = "home"
            st.rerun()
        message_detector_ui()
    elif st.session_state.page == "image": # <--- UPDATED THIS SECTION
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if st.sidebar.button("Back to Home"):
            st.session_state.page = "home"
            st.rerun()
        image_detector_ui() # <--- CALLS THE NEW GEMINI CODE

if __name__ == "__main__":
    main()