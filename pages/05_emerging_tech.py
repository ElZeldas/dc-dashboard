import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Emerging Tech", page_icon="🚀", layout="wide")
st.title("🚀 Emerging Technologies — Radar Tecnológico 2024–2030")
st.caption("Fuentes: Gartner Hype Cycle 2024, Uptime Institute, IDC Latin America")

# --- KPIs ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Adopción IA en DCs", "67%", "+23% YoY")
with col2:
    st.metric("DCs con Liquid Cooling", "31%", "+12% YoY")
with col3:
    st.metric("Edge Nodes en LATAM", "1,240", "+340 en 2024")
with col4:
    st.metric("Inversión Green DC MX", "$480M USD", "+35% YoY")

st.markdown("---")

# --- Technology Radar ---
st.markdown("### 🎯 Technology Radar — Centros de Datos")

radar_data = pd.DataFrame({
    "Tecnología": [
        "Liquid Cooling", "AI Ops", "Green Energy", "Edge Computing",
        "Quantum Computing", "Silicon Photonics", "Modular DC",
        "5G Integration", "Autonomous DC", "Immersion Cooling"
    ],
    "Madurez (1-10)": [7, 8, 6, 7, 2, 3, 8, 6, 4, 5],
    "Impacto (1-10)": [9, 9, 8, 7, 10, 8, 7, 6, 9, 8],
    "Adopción México (%)": [25, 40, 30, 35, 2, 5, 45, 28, 8, 12],
    "Horizonte": [
        "Ahora", "Ahora", "Ahora", "Ahora",
        "2028+", "2027+", "Ahora", "2026", "2027+", "2026"
    ]
})

fig_radar = go.Figure()
colors = {"Ahora": "#00e676", "2026": "#4fc3f7", "2027+": "#ffaa00", "2028+": "#ff4444"}

for horizonte, color in colors.items():
    df_filtered = radar_data[radar_data["Horizonte"] == horizonte]
    fig_radar.add_trace(go.Scatter(
        x=df_filtered["Madurez (1-10)"],
        y=df_filtered["Impacto (1-10)"],
        mode="markers+text",
        name=horizonte,
        text=df_filtered["Tecnología"],
        textposition="top center",
        marker=dict(size=df_filtered["Adopción México (%)"] * 0.8 + 10, color=color, opacity=0.8),
    ))

fig_radar.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font_color="white", legend=dict(bgcolor="rgba(0,0,0,0)", title="Horizonte"),
    xaxis=dict(title="Madurez Tecnológica", range=[0, 11], gridcolor="#333"),
    yaxis=dict(title="Impacto en el Negocio", range=[0, 11], gridcolor="#333"),
    height=500
)
st.plotly_chart(fig_radar, use_container_width=True)
st.caption("💡 Tamaño de burbuja = % de adopción en México")

# --- Adoption Timeline ---
st.markdown("### 📅 Timeline de Adopción 2024–2030")

timeline = pd.DataFrame({
    "Tecnología": ["Modular DC", "AI Ops", "Liquid Cooling", "5G Integration",
                   "Immersion Cooling", "Autonomous DC", "Silicon Photonics", "Quantum Computing"],
    "Inicio": [2022, 2023, 2023, 2024, 2024, 2026, 2026, 2028],
    "Fin": [2026, 2027, 2028, 2026, 2027, 2030, 2029, 2032],
    "Categoría": ["Infraestructura", "Software", "Infraestructura", "Conectividad",
                  "Infraestructura", "Software", "Hardware", "Computación"]
})

color_map = {
    "Infraestructura": "#4fc3f7", "Software": "#00e676",
    "Conectividad": "#ffaa00", "Hardware": "#ff7043", "Computación": "#ce93d8"
}

fig_timeline = go.Figure()
for _, row in timeline.iterrows():
    fig_timeline.add_trace(go.Bar(
        x=[row["Fin"] - row["Inicio"]],
        y=[row["Tecnología"]],
        base=[row["Inicio"]],
        orientation="h",
        name=row["Categoría"],
        marker_color=color_map[row["Categoría"]],
        showlegend=row["Tecnología"] == timeline[timeline["Categoría"] == row["Categoría"]].iloc[0]["Tecnología"],
        text=f'{row["Inicio"]}–{row["Fin"]}',
        textposition="inside"
    ))

fig_timeline.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font_color="white", barmode="overlay",
    xaxis=dict(title="Año", range=[2022, 2033], gridcolor="#333",
               tickvals=list(range(2022, 2033))),
    yaxis=dict(gridcolor="#333"),
    legend=dict(bgcolor="rgba(0,0,0,0)"),
    height=400
)
st.plotly_chart(fig_timeline, use_container_width=True)

# --- Strategic Recommendations ---
st.markdown("### 💡 Recomendaciones Estratégicas")

recs = [
    ("🤖 Implementar AIOps en el corto plazo", "Alta",
     "Las herramientas de IA para operaciones de DC ya son maduras y tienen el mayor ROI en reducción de incidentes y optimización de recursos. Prioridad inmediata para KIO Networks."),
    ("❄️ Migrar a Liquid Cooling progresivamente", "Alta",
     "Con densidades de cómputo en aumento por GPU/AI workloads, el cooling tradicional se vuelve insuficiente. Iniciar con zonas de alta densidad y expandir gradualmente."),
    ("🌱 Certificar operaciones con energía renovable", "Media",
     "Los clientes enterprise y hiperescaladores exigen compromisos de carbono neutro. Invertir en PPAs de energía solar/eólica posiciona al DC en contratos de mayor valor."),
    ("📡 Desarrollar estrategia Edge para Mérida", "Media",
     "El sureste mexicano tiene baja latencia hacia cables submarinos del Caribe y EUA. Una estrategia Edge en Mérida puede capturar demanda de nearshoring y gaming latam."),
]

for title, priority, description in recs:
    color = "#ff4444" if priority == "Alta" else "#ffaa00"
    with st.expander(f"{title} — Prioridad: **{priority}**"):
        st.markdown(f"<span style='color:{color}'>●</span> {description}", unsafe_allow_html=True)