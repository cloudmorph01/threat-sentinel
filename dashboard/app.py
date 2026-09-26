import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
from pathlib import Path
# Ensure root directory is on Python path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
from core.db import (
    get_stats_summary,
    get_recent_events,
    get_top_attackers,
    get_top_credentials,
    get_mitre_stats,
    get_geo_map_data
)
import config
# Streamlit Page Configuration
st.set_page_config(
    page_title="ThreatSentinel | SOC Analyst Console",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Custom CSS for Cyber Security SOC look
st.markdown("""
<style>
    .metric-card {
        background-color: #1e293b;
        border-radius: 8px;
        padding: 18px;
