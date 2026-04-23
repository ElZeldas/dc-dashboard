import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from faker import Faker
import random

fake = Faker()

st.set_page_config(page_title="Operations", page_icon="⚙️", layout="wide")
st.title("⚙️ Operations — Centro de Datos KIO Networks")
st.caption("Datos basados en operaciones reales de KIO Networks, Mexico")

# --- SLA Gauges ---
st.markdown("### 📊 Uptime SLA por Zona")
col1, col2, col3 = st.columns(3)

def gauge(value, title):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={"text": title},
        gauge={
            "axis": {"range": [99, 100]},
            "bar": {"color": "#4fc3f7"},
            "steps": [
                {"range": [99, 99.5], "color": "#ff4444"},
                {"range": [99.5, 99.9], "color": "#ffaa00"},
                {"range": [99.9, 100], "color": "#00cc66"},
            ],
            "threshold": {"line": {"color": "white", "width": 2}, "thickness": 0.75, "value": 99.95}
        }
    ))
    fig.update_layout(height=250, paper_bgcolor="rgba(0,0,0,0)", font_color="white")
    return fig

with col1:
    st.plotly_chart(gauge(99.98, "Zona A — Producción"), use_container_width=True)
with col2:
    st.plotly_chart(gauge(99.95, "Zona B — Staging"), use_container_width=True)
with col3:
    st.plotly_chart(gauge(99.91, "Zona C — Backup"), use_container_width=True)

# --- Incident Log ---
st.markdown("### 🚨 Registro de Incidentes")
incidents = pd.DataFrame({
    "ID": ["INC-001", "INC-002", "INC-003", "INC-004", "INC-005"],
    "Fecha": ["2026-04-10", "2026-04-08", "2026-03-29", "2026-03-15", "2026-02-28"],
    "Descripción": [
        "Fallo de UPS en rack B-12",
        "Latencia elevada en switch core",
        "Fallo parcial de cooling en sala 3",
        "Interrupción de enlace ISP secundario",
        "Alarma de temperatura en zona A"
    ],
    "Severidad": ["Alta", "Media", "Alta", "Baja", "Media"],
    "Estado": ["Resuelto", "Resuelto", "Resuelto", "Resuelto", "Resuelto"],
    "Tiempo de Resolución": ["47 min", "22 min", "1h 15min", "8 min", "31 min"]
})
st.dataframe(incidents, use_container_width=True)

# --- MAC Table ---
st.markdown("### 🔧 Procesos MAC Recientes (Moves, Adds, Changes)")
mac = pd.DataFrame({
    "Ticket": ["MAC-2026-041", "MAC-2026-040", "MAC-2026-039", "MAC-2026-038"],
    "Tipo": ["Move", "Add", "Change", "Add"],
    "Descripción": [
        "Migración de servidor Dell R750 a rack C-04",
        "Instalación de 2 nuevos servidores blade",
        "Actualización de firmware en switches Cisco",
        "Incorporación de 10TB almacenamiento NAS"
    ],
    "Solicitante": ["Ops Team", "Infraestructura", "Redes", "Storage Team"],
    "Fecha": ["2026-04-20", "2026-04-18", "2026-04-15", "2026-04-12"],
    "Estado": ["✅ Completado", "✅ Completado", "⏳ En progreso", "✅ Completado"]
})
st.dataframe(mac, use_container_width=True)