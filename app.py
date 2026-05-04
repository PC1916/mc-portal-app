import streamlit as st
import math

# Page Config
st.set_page_config(page_title="MC Bedrock Portal Master", page_icon="⛏️")

# Sidebar for extra tips
with st.sidebar:
    st.header("Bedrock Tips")
    st.write("• **Ratio:** 8:1 (OW:Nether)")
    st.write("• **Safety:** 16 blocks in Nether")
    st.write("• **Height:** Y-coordinates are 1:1")
    st.divider()
    st.caption("Created for Nether Tunneling")

st.title("🧱 Minecraft Portal & Tunnel Master")

# --- SECTION 1: COORDINATE CONVERTER ---
st.header("1. Coordinate Converter")
st.info("Input your current coordinates to find the matching link.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("🌍 Overworld → 🌌 Nether")
    ow_x = st.number_input("Overworld X", value=0, key="ow_x")
    ow_z = st.number_input("Overworld Z", value=0, key="ow_z")
    st.success(f"Build Nether Portal at:\n**X: {ow_x//8} | Z: {ow_z//8}**")

with col2:
    st.subheader("🌌 Nether → 🌍 Overworld")
    n_x_in = st.number_input("Nether X", value=0, key="n_x")
    n_z_in = st.number_input("Nether Z", value=0, key="n_z")
    st.info(f"Build Overworld Portal at:\n**X: {n_x_in*8} | Z: {n_z_in*8}**")

st.divider()

# --- SECTION 2: SAFETY BUFFER ---
st.header("2. Anti-Overlap Safety Check")
st.write("Check if your next portal is far enough away to avoid 'bleeding' into the previous one.")

scol1, scol2 = st.columns(2)
with scol1:
    last_x = st.number_input("Last Portal Nether X", value=0)
with scol2:
    last_z = st.number_input("Last Portal Nether Z", value=0)

safe_x = last_x + 16
safe_z = last_z + 16

st.warning(f"🚀 **Safe Zone:** For a clean link, your next portal should be at least at **X: {safe_x}** or **Z: {safe_z}**.")

st.divider()

# --- SECTION 3: TUNNEL PLANNER ---
st.header("3. Tunnel Logistics")
st.write("Calculate the distance between two Nether points.")

tcol1, tcol2 = st.columns(2)
with tcol1:
    p1_x = st.number_input("Start X", value=0, key="ax")
    p1_z = st.number_input("Start Z", value=0, key="az")
with tcol2:
    p2_x = st.number_input("End X", value=0, key="bx")
    p2_z = st.number_input("End Z", value=0, key="bz")

# Math
dist_n = math.sqrt((p2_x - p1_x)**2 + (p2_z - p1_z)**2)
dist_ow = dist_n * 8

if dist_n > 0:
    st.metric("Nether Tunnel Length", f"{round(dist_n, 1)} Blocks")
    st.write(f"This tunnel bypasses **{round(dist_ow, 1)}** Overworld blocks!")
    
    # Tool Estimation
    picks = math.ceil(dist_n / 60)
    st.caption(f"📦 Estimated iron pickaxes needed for a 1x2 tunnel: ~{picks}")
