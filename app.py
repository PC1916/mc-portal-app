import streamlit as st
import math

st.set_page_config(page_title="MC Portal & Tunnel Calc", page_icon="⛏️")

st.title("⛏️ Minecraft Tunnel & Portal Tools")

# --- SECTION 1: PORTAL CALCULATOR ---
st.header("1. Portal Coordinator")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Overworld → Nether")
    ow_x = st.number_input("Overworld X", value=0)
    ow_z = st.number_input("Overworld Z", value=0)
    st.success(f"Nether: **X: {ow_x//8} | Z: {ow_z//8}**")

with col2:
    st.subheader("Nether → Overworld")
    n_x_in = st.number_input("Nether X", value=0)
    n_z_in = st.number_input("Nether Z", value=0)
    st.info(f"Overworld: **X: {n_x_in*8} | Z: {n_z_in*8}**")

st.divider()

# --- SECTION 2: TUNNEL PLANNER ---
st.header("2. Tunnel Distance Planner")
st.write("Enter two points in the Nether to see how long your tunnel will be.")

tcol1, tcol2 = st.columns(2)
with tcol1:
    p1_x = st.number_input("Point A: X", value=0, key="ax")
    p1_z = st.number_input("Point A: Z", value=0, key="az")
with tcol2:
    p2_x = st.number_input("Point B: X", value=0, key="bx")
    p2_z = st.number_input("Point B: Z", value=0, key="bz")

# Distance Math
dist_nether = math.sqrt((p2_x - p1_x)**2 + (p2_z - p1_z)**2)
dist_overworld = dist_nether * 8

st.metric("Nether Tunnel Length", f"{round(dist_nether, 1)} blocks")
st.write(f"🌍 This tunnel covers **{round(dist_overworld, 1)}** blocks in the Overworld!")

if dist_nether > 0:
    st.warning(f"💡 You will need approximately **{math.ceil(dist_nether/60)}** iron pickaxes (without Unbreaking) to dig this 1x2 tunnel.")
