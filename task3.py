import streamlit as st
import time

# Configure the page layout and title
st.set_page_config(
    page_title="Sign Up | Portal",
    page_icon="✨",
    layout="centered"
)

# Custom CSS styling for gorgeous modern visual effects, gradients, and card containers
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .signup-card {
        background: white;
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.8);
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        opacity: 0.9;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# App Container
st.markdown("<div class='signup-card'>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #333;'>Create Account 🚀</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Join our community today! Please fill in your details.</p>", unsafe_allow_html=True)

with st.form("signup_form"):
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name", placeholder="John")
    with col2:
        last_name = st.text_init = st.text_input("Last Name", placeholder="Doe")
        
    email = st.text_input("Email Address", placeholder="john.doe@example.com")
    password = st.text_input("Password", type="password", placeholder="••••••••")
    confirm_password = st.text_input("Confirm Password", type="password", placeholder="••••••••")
    
    terms = st.checkbox("I agree to the Terms of Service and Privacy Policy")
    
    submitted = st.form_submit_button("Sign Up")

if submitted:
    # Validation logic
    if not first_name or not email or not password:
        st.error("⚠️ Please fill in all required fields.")
    elif password != confirm_password:
        st.error("❌ Passwords do not match.")
    elif not terms:
        st.error("📜 You must agree to the terms and conditions.")
    else:
        # Success visual effects sequence
        with st.spinner("Creating your account and setting up your workspace..."):
            time.sleep(1.5) # Simulate backend request delay
            
        st.balloons() # Triggers celebratory screen balloons effect!
        st.success(f"🎉 Welcome aboard, {first_name}! Your account has been created successfully.")
        st.info("💡 Check your email for a verification link to activate your dashboard.")

st.markdown("</div>", unsafe_allow_html=True)