import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Energy", page_icon="⚡", layout="wide")
st.title("⚡ Energy — Consumo y Eficiencia Energética")
st.caption("Métricas basadas en estándares Uptime Institute y reportes de KIO Networks")

# --- PUE Trends ---
st.markdown("### 📈 Tendencia PUE Mensual 2025–2026")
months = ["May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic", "Ene", "Feb", "Mar", "Abr"]
pue_values = [1.58, 1.55, 1.61, 1.63, 1.60, 1.52, 1.48, 1.45, 1.44, 1.43, 1.42, 1.42]
industry_avg = [1.67] * 12

fig_pue = go.Figure()
fig_pue.add_trace(go.Scatter(x=months, y=pue_values, mode="lines+markers",
    name="KIO Networks PUE", line=dict(color="#4fc3f7", width=3),
    marker=dict(size=8)))
fig_pue.add_trace(go.Scatter(x=months, y=industry_avg, mode="lines",
    name="Promedio industria", line=dict(color="#ff7043", width=2, dash="dash")))
fig_pue.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font_color="white", legend=dict(bgcolor="rgba(0,0,0,0)"),
    yaxis=dict(range=[1.3, 1.8], gridcolor="#333"),
    xaxis=dict(gridcolor="#333")
)
st.plotly_chart(fig_pue, use_container_width=True)

# --- Energy Consumption Chart ---
st.markdown("### 🔋 Consumo Energético por Sistema (kWh mensual)")
systems = ["Servidores", "Cooling", "UPS/PDU", "Iluminación", "Redes", "Otros"]
consumption = [42000, 28000, 8500, 1200, 5300, 2000]
colors = ["#4fc3f7", "#00e5ff", "#0097a7", "#006064", "#80deea", "#b2ebf2"]

fig_energy = go.Figure(go.Bar(
    x=systems, y=consumption, marker_color=colors,
    text=[f"{v:,} kWh" for v in consumption], textposition="outside"
))
fig_energy.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font_color="white", yaxis=dict(gridcolor="#333"),
    xaxis=dict(gridcolor="#333")
)
st.plotly_chart(fig_energy, use_container_width=True)

# --- PUE Calculator ---
st.markdown("### 🧮 Calculadora Interactiva de PUE")
st.caption("PUE = Energía Total del DC / Energía consumida por IT")

col1, col2 = st.columns(2)
with col1:
    total_energy = st.slider("Energía total del Data Center (kW)", 100, 5000, 1200, 50)
with col2:
    it_energy = st.slider("Energía consumida por equipos IT (kW)", 50, 4000, 850, 50)

if it_energy > 0 and it_energy < total_energy:
    pue = total_energy / it_energy
    overhead = total_energy - it_energy
    efficiency = (it_energy / total_energy) * 100

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("PUE Calculado", f"{pue:.2f}")
    with col2:
        st.metric("Overhead no-IT", f"{overhead} kW")
    with col3:
        st.metric("Eficiencia IT", f"{efficiency:.1f}%")

    if pue < 1.2:
        st.success("🏆 Excelente — Clase mundial (Google, Hyperscalers)")
    elif pue < 1.5:
        st.info("✅ Bueno — Por debajo del promedio de la industria")
    elif pue < 1.8:
        st.warning("⚠️ Promedio — Hay oportunidad de mejora")
    else:
        st.error("❌ Ineficiente — Requiere optimización urgente")
else:
    st.error("⚠️ La energía IT debe ser menor que la energía total.")