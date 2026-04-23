import streamlit as st

st.set_page_config(
    page_title="DC Dashboard | Jose Lopez",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado
st.markdown("""
    <style>
        .main { background-color: #0f1117; }
        [data-testid="stSidebar"] { background-color: #1a1d2e; }
        h1, h2, h3 { color: #4fc3f7; }
        .metric-card {
            background-color: #1e2130;
            border-radius: 10px;
            padding: 20px;
            border-left: 4px solid #4fc3f7;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🏢 Data Center Dashboard")
st.subheader("Administración y Tendencias de Mercado — Mexico & LATAM")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Uptime Global", "99.98%", "+0.02%")
with col2:
    st.metric("PUE Promedio", "1.42", "-0.08")
with col3:
    st.metric("Incidentes Activos", "2", "-1")
with col4:
    st.metric("Capacidad Usada", "78%", "+3%")

st.markdown("---")
st.markdown("""
### 📋 Navegación
Usa el menú lateral para explorar las secciones del dashboard:
- **01 · Operations** — Uptime, SLAs e incidentes
- **02 · Energy** — PUE y consumo energético
- **03 · Security** — Cumplimiento TIA-942 / ISO 27001
- **04 · Market Intelligence** — Mercado DC en México
- **05 · Emerging Technologies** — Radar tecnológico 2024–2030
""")

st.caption("Desarrollado por Jose Lopez · UPY 2026 · Datos basados en reportes Gartner, CBRE y Statista")