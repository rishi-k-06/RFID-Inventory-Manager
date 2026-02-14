import streamlit as st
import pandas as pd
import time
from datetime import datetime

st.set_page_config(page_title="Warehouse Manager", page_icon="📦", layout="wide")

st.title("📦 RFID Inventory Control Center")

# Simulated Product Database
if 'inventory' not in st.session_state:
    st.session_state.inventory = pd.DataFrame([
        {'ID': 'A123', 'Product': 'Servo Motors', 'Stock': 45, 'Min': 10},
        {'ID': 'B456', 'Product': 'Li-ion Cells', 'Stock': 8, 'Min': 20},
        {'ID': 'C789', 'Product': 'Aluminum Rails', 'Stock': 102, 'Min': 50}
    ])

placeholder = st.empty()

for _ in range(100):
    # Simulating a "Scan" event from NodeMCU
    if _ % 5 == 0:
        st.session_state.inventory.loc[1, 'Stock'] -= 1 # Simulate B456 being checked out
    
    with placeholder.container():
        st.subheader("Current Stock Status")
        
        # Highlight Low Stock
        def highlight_low(s):
            return ['background-color: #ffcccc' if s.Stock < s.Min else '' for _ in s]
        
        st.table(st.session_state.inventory.style.apply(highlight_low, axis=1))

        # Alert Section
        low_items = st.session_state.inventory[st.session_state.inventory['Stock'] < st.session_state.inventory['Min']]
        if not low_items.empty:
            for _, item in low_items.iterrows():
                st.error(f"⚠️ REORDER ALERT: {item['Product']} is below safety threshold!")

    time.sleep(3)
