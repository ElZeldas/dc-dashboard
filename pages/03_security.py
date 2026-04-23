import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Security", page_icon="🔒", layout="wide")
st.title("🔒 Security — Cumplimiento y Controles de Seguridad")
st.caption("Basado en estándares TIA-942, ISO 27001 e NFPA 75")

# --- Compliance Overview ---
st.markdown("### 📋 Checklist de Cumplimiento TIA-942 / ISO 27001")

col1, col2 = st.columns(2)

tia_items = [
    ("Redundancia eléctrica N+1", True),
    ("Generadores de respaldo", True),
    ("UPS con autonomía mínima 15 min", True),
    ("Cooling redundante", True),
    ("Cableado estructurado categoría 6A", True),
    ("Rutas de fibra redundantes", True),
    ("Separación de zonas críticas", True),
    ("Monitoreo ambiental 24/7", True),
    ("Supresión de incendios VESDA", True),
    ("Piso falso antistático", False),
]

iso_items = [
    ("Política de seguridad de la información", True),
    ("Gestión de riesgos documentada", True),
    ("Control de acceso físico biométrico", True),
    ("CCTV con retención 90 días", True),
    ("Gestión de incidentes formalizada", True),
    ("BCP / DRP documentado y probado", True),
    ("Auditorías internas anuales", True),
    ("Capacitación al personal", True),
    ("Clasificación de activos de información", False),
    ("Cifrado de datos en tránsito y reposo", True),
]

with col1:
    st.markdown("#### 🏗️ TIA-942 — Infraestructura")
    for item, status in tia_items:
        icon = "✅" if status else "❌"
        st.markdown(f"{icon} {item}")

with col2:
    st.markdown("#### 🔐 ISO 27001 — Seguridad de la Información")
    for item, status in iso_items:
        icon = "✅" if status else "❌"
        st.markdown(f"{icon} {item}")

# --- Compliance Score Gauges ---
st.markdown("### 🎯 Score de Cumplimiento")
col1, col2, col3 = st.columns(3)

def compliance_gauge(value, title, color):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        number={"suffix": "%"},
        title={"text": title},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": color},
            "steps": [
                {"range": [0, 60], "color": "#ff4444"},
                {"range": [60, 80], "color": "#ffaa00"},
                {"range": [80, 100], "color": "#1a2a1a"},
            ],
        }
    ))
    fig.update_layout(height=250, paper_bgcolor="rgba(0,0,0,0)", font_color="white")
    return fig

with col1:
    st.plotly_chart(compliance_gauge(90, "TIA-942", "#4fc3f7"), use_container_width=True)
with col2:
    st.plotly_chart(compliance_gauge(90, "ISO 27001", "#00e5ff"), use_container_width=True)
with col3:
    st.plotly_chart(compliance_gauge(95, "NFPA 75", "#80deea"), use_container_width=True)

# --- Physical Security Controls ---
st.markdown("### 🛡️ Controles de Seguridad Física")

controls = {
    "Control de Acceso": [
        ("Autenticación biométrica (huella + iris)", "Activo", "🟢"),
        ("Torniquetes de doble factor en entrada principal", "Activo", "🟢"),
        ("Man-trap en sala de servidores", "Activo", "🟢"),
        ("Tarjetas RFID por zona con logs de acceso", "Activo", "🟢"),
    ],
    "Vigilancia": [
        ("CCTV HD en todas las zonas (128 cámaras)", "Activo", "🟢"),
        ("Monitoreo NOC 24/7/365", "Activo", "🟢"),
        ("Guardias de seguridad en puntos críticos", "Activo", "🟢"),
        ("Detección de movimiento perimetral", "Activo", "🟢"),
    ],
    "Protección contra Desastres": [
        ("Sistema VESDA detección temprana de humo", "Activo", "🟢"),
        ("Supresión FM-200 en salas críticas", "Activo", "🟢"),
        ("Sensores de inundación bajo piso falso", "En revisión", "🟡"),
        ("Jaulas de Faraday en zonas EMI", "Activo", "🟢"),
    ]
}

for category, items in controls.items():
    st.markdown(f"#### {category}")
    cols = st.columns(2)
    for i, (control, status, icon) in enumerate(items):
        with cols[i % 2]:
            st.markdown(f"{icon} **{control}** — *{status}*")