import streamlit as st
import inspect
from abc import ABC, abstractmethod

# App configuration
st.set_page_config(
    page_title="Stress Tester",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)


