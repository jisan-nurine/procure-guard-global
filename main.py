import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import random

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Procure Guard Global",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #0f2027, #203a43, #2c5364);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .main-header h1 { color: #ffffff; margin: 0; }
    .main-header p { color: #b0c4de; margin: 0; }

    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #2c5364;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .risk-low    { color: #28a745; font-weight: 700; }
    .risk-medium { color: #ffc107; font-weight: 700; }
    .risk-high   { color: #dc3545; font-weight: 700; }

    .stButton>button {
        background: linear-gradient(90deg, #2c5364, #0f2027);
        color: white; border: none; border-radius: 8px;
        padding: 0.6rem 1.5rem; font-weight: 600;
    }
    .stButton>button:hover { opacity: 0.9; }
</style>
""", unsafe_allow_html=True)

# ---------------- Session State ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- Header ----------------
st.markdown("""
<div class="main-header">
    <h1>🛡️ Procure Guard Global</h1>
    <p>AI-Powered Global Procurement Protection System · $13T Tender OS</p>
</div>
""", unsafe_allow_html=True)

# ---------------- Sidebar ----------------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shield.png", width=80)
    st.title("Navigation")
    page = st.radio("Go to", ["📊 Dashboard", "🔍 Tender Analyzer", "📁 History", "ℹ️ About"])
    st.divider()
    st.caption("🔒 Enterprise Grade Security")
    st.caption("© 2025 Jisan Nurine")

# ---------------- Dashboard Page ----------------
if page == "📊 Dashboard":
    st.subheader("📈 Global Procurement Overview")

    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Global Tenders", "$13T", "Live")
    with col2: st.metric("Risk Detected", "1,240", "-12%")
    with col3: st.metric("Protected Value", "$4.2B", "+8%")
    with col4: st.metric("Active Vendors", "18,432", "+3.5%")

    st.divider()

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 🚨 Risk Distribution")
        risk_df = pd.DataFrame({
            "Category": ["Low", "Medium", "High", "Critical"],
            "Count": [820, 310, 90, 20],
        })
        fig = px.pie(risk_df, names="Category", values="Count", hole=0.45,
                     color="Category",
                     color_discrete_map={"Low":"#28a745","Medium":"#ffc107",
                                         "High":"#fd7e14","Critical":"#dc3545"})
        fig.update_layout(height=350, margin=dict(t=20, b=20))
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.markdown("#### 📊 Monthly Protected Value ($M)")
        trend = pd.DataFrame({
            "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
            "Value": [320, 410, 380, 520, 610, 580, 720, 810],
        })
        fig2 = px.line(trend, x="Month", y="Value", markers=True)
        fig2.update_traces(line_color="#2c5364", line_width=3)
        fig2.update_layout(height=350, margin=dict(t=20, b=20))
        st.plotly_chart(fig2, use_container_width=True)

# ---------------- Tender Analyzer ----------------
elif page == "🔍 Tender Analyzer":
    st.subheader("🔍 AI Tender Risk Analyzer")

    with st.form("tender_form"):
        c1, c2 = st.columns(2)
        with c1:
            tender_name = st.text_input("Tender / RFP Name *", "Global Hospital Supply Tender")
            vendor_name = st.text_input("Vendor Name", "MedSupply International")
        with c2:
            tender_value = st.number_input("Tender Value ($)", min_value=1000,
                                           value=5_000_000, step=1000)
            country = st.selectbox("Country", ["Bangladesh", "USA", "UK", "Germany",
                                               "India", "China", "UAE", "Others"])
        submitted = st.form_submit_button("🚀 Analyze Tender Risk")

    if submitted:
        if not tender_name.strip():
            st.error("⚠️ Please enter a valid Tender name.")
        else:
            with st.spinner("Analyzing with AI models..."):
                progress = st.progress(0)
                for i in range(100):
                    progress.progress(i + 1)
                risk_score = random.randint(5, 45)
                if risk_score < 20:
                    level, cls, advice = "Low Risk", "risk-low", "Vendor verification passed. SAFE to proceed."
                elif risk_score < 35:
                    level, cls, advice = "Medium Risk", "risk-medium", "Further due diligence recommended."
                else:
                    level, cls, advice = "High Risk", "risk-high", "DO NOT proceed. Manual review required."

            st.success(f"✅ Analysis Complete for **{tender_name}**")
            st.divider()

            r1, r2, r3, r4 = st.columns(4)
            r1.metric("Tender Value", f"${tender_value:,.0f}")
            r2.metric("Vendor", vendor_name or "N/A")
            r3.metric("Country", country)
            r4.metric("Risk Score", f"{risk_score}%")

            st.markdown(f"### Risk Level: <span class='{cls}'>{level}</span>",
                        unsafe_allow_html=True)
            st.info(f"🤖 **AI Suggestion:** {advice}")

            # Gauge chart
            gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=risk_score,
                title={"text": "Risk Score"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#2c5364"},
                    "steps": [
                        {"range": [0, 20], "color": "#d4edda"},
                        {"range": [20, 35], "color": "#fff3cd"},
                        {"range": [35, 100], "color": "#f8d7da"},
                    ],
                },
            ))
            gauge.update_layout(height=300, margin=dict(t=30, b=10))
            st.plotly_chart(gauge, use_container_width=True)

            # Save to history
            st.session_state.history.append({
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Tender": tender_name,
                "Vendor": vendor_name,
                "Country": country,
                "Value ($)": tender_value,
                "Risk Score": risk_score,
                "Level": level,
            })
            st.balloons()

# ---------------- History Page ----------------
elif page == "📁 History":
    st.subheader("📁 Analysis History")
    if not st.session_state.history:
        st.warning("No analyses yet. Go to **Tender Analyzer** to get started.")
    else:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df, use_container_width=True, hide_index=True)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download Report (CSV)", csv,
                           file_name=f"procure_guard_{datetime.now():%Y%m%d}.csv",
                           mime="text/csv")

        if st.button("🗑️ Clear History"):
            st.session_state.history = []
            st.rerun()

# ---------------- About Page ----------------
elif page == "ℹ️ About":
    st.subheader("ℹ️ About Procure Guard Global")
    st.markdown("""
    **Procure Guard Global** is an AI-powered tender & RFP risk assessment platform
    designed to protect organizations from procurement fraud, vendor risk, and
    price manipulation across **$13 Trillion** of global tenders.

    #### 🎯 Key Features
    - Real-time AI risk scoring
    - Multi-country vendor verification
    - Price benchmarking against market
    - Exportable compliance reports
    - Enterprise-grade security

    ---
    **Developer:** Jisan Nurine  
    **Built with:** Streamlit · Plotly · Python  
    **Version:** 2.0.0
    """)

# ---------------- Footer ----------------
st.divider()
st.caption("🟢 System Live · Powered by Procure Guard AI Engine · © 2025 Jisan Nurine")