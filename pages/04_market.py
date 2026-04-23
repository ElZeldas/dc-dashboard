import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Market Intelligence", page_icon="📈", layout="wide")
st.title("📈 Market Intelligence — Mercado DC en México")
st.caption("Fuentes: CBRE Data Center Market Report 2024, Statista, Gartner, SE Latam")

# --- KPIs de Mercado ---
st.markdown("### 🌎 Panorama del Mercado Mexicano 2024–2026")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Capacidad Total (MW)", "412 MW", "+68 MW vs 2023")
with col2:
    st.metric("Tasa de Crecimiento", "18.4%", "+3.2% YoY")
with col3:
    st.metric("Inversión 2024", "$2.8B USD", "+22% vs 2023")
with col4:
    st.metric("Ocupación Promedio", "87%", "+5%")

st.markdown("---")

# --- Mercado por Ciudad ---
st.markdown("### 🏙️ Capacidad por Ciudad (MW instalados)")
cities = ["CDMX", "Querétaro", "Guadalajara", "Monterrey", "Mérida", "Tijuana"]
capacity = [210, 85, 52, 38, 18, 9]
growth = [12, 34, 18, 22, 45, 15]

fig_cities = go.Figure()
fig_cities.add_trace(go.Bar(
    name="Capacidad (MW)", x=cities, y=capacity,
    marker_color="#4fc3f7",
    text=[f"{v} MW" for v in capacity], textposition="outside"
))
fig_cities.add_trace(go.Scatter(
    name="Crecimiento YoY (%)", x=cities, y=growth,
    mode="lines+markers", yaxis="y2",
    line=dict(color="#ff7043", width=3),
    marker=dict(size=10)
))
fig_cities.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font_color="white", legend=dict(bgcolor="rgba(0,0,0,0)"),
    yaxis=dict(title="Capacidad (MW)", gridcolor="#333"),
    yaxis2=dict(title="Crecimiento (%)", overlaying="y", side="right", gridcolor="#333"),
    xaxis=dict(gridcolor="#333")
)
st.plotly_chart(fig_cities, use_container_width=True)

# --- Modelos de Despliegue ---
st.markdown("### 🗂️ Modelos de Despliegue en México")
col1, col2 = st.columns(2)

with col1:
    labels = ["Colocation", "Hiperescala", "On-Premise", "Edge Computing", "Managed Services"]
    values = [42, 28, 18, 7, 5]
    fig_pie = go.Figure(go.Pie(
        labels=labels, values=values, hole=0.4,
        marker_colors=["#4fc3f7", "#00e5ff", "#0097a7", "#80deea", "#006064"]
    ))
    fig_pie.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", font_color="white",
        legend=dict(bgcolor="rgba(0,0,0,0)"),
        title="Distribución por modelo (%)"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.markdown("#### 🏢 Principales Operadores en México")
    operators = pd.DataFrame({
        "Operador": ["KIO Networks", "Telmex/TELNOC", "Equinix", "CyrusOne", "Axtel", "QTS"],
        "HQ": ["CDMX", "CDMX", "EUA", "EUA", "Monterrey", "EUA"],
        "MW Operados": [85, 72, 48, 35, 28, 22],
        "Tier": ["III+", "III", "IV", "III+", "III", "IV"],
        "Presencia": ["Nacional", "Nacional", "CDMX/QRO", "CDMX", "Norte", "CDMX"]
    })
    st.dataframe(operators, use_container_width=True, hide_index=True)

# --- Hotspots Regionales ---
st.markdown("### 📍 Hotspots Regionales — ¿Por qué estas ciudades?")

hotspots = {
    "🏆 CDMX": "Mayor concentración de demanda empresarial. Hub financiero y corporativo. Infraestructura de fibra más densa del país. Riesgo sísmico mitigado con construcción especializada.",
    "🚀 Querétaro": "Crecimiento más acelerado del país (+34% YoY). Zona industrial consolidada. Menor riesgo sísmico. Incentivos fiscales estatales. Conectividad a CDMX < 3ms latencia.",
    "🌊 Mérida": "Mercado emergente con mayor potencial 2025–2030. Hub para cable submarino hacia EUA y Caribe. Zona libre de huracanes histórica. Gobierno estatal pro-inversión tecnológica.",
    "🏔️ Monterrey": "Gateway al mercado nearshoring. Proximidad a frontera con EUA. Alta demanda industrial y manufactura 4.0. Segundo hub financiero del país."
}

for city, description in hotspots.items():
    with st.expander(city):
        st.write(description)