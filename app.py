import streamlit as st
from streamlit_player import st_player

# --- Page Configuration ---
st.set_page_config(page_title="Custom YouTube Player", layout="wide")

# --- Custom Dark Theme Styling ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #7d5fff; color: white; border-radius: 5px; border: none; }
    .stTextInput>div>div>input { background-color: #1a1c24; color: white; border: 1px solid #333; }
    div[data-testid="stExpander"] { background-color: #1a1c24; border: none; }
    /* Bottom Controls Container */
    .control-panel {
        background-color: #13151c;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Top Navigation Bar ---
t1, t2, _ = st.columns([1.5, 1.5, 7])
with t1:
    st.button("Add Another Video")
with t2:
    st.button("Load Videos", type="secondary")

# URL Input Field
video_url = st.text_input("YouTube URL", "https://youtu.be/t9BnLcx3Q0Y", label_visibility="collapsed")

# --- Main Video Display ---
# st_player handles embedding better than st.video for many YouTube links
player_event = st_player(video_url, height=500, key="youtube_player")

# --- Action Buttons ---
b1, b2, _ = st.columns([2, 2, 6])
with b1:
    st.button("📸 Take Screenshot (0)")
with b2:
    st.button("📄 Download PDF")

# --- Looping Segment Controls ---
st.markdown("---")
l1, l2, l3, l4, l5 = st.columns([1.5, 1, 0.5, 1, 2])
with l1:
    loop_on = st.toggle("Loop segment", value=True)
with l2:
    start_time = st.text_input("Start", value="0:00", label_visibility="collapsed")
with l3:
    st.write("to")
with l4:
    end_time = st.text_input("End", value="End time", label_visibility="collapsed")
with l5:
    st.button("Download Segment")

# --- Caption Customization Panel ---
st.markdown('<div class="control-panel">', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.write("**Caption Position**")
    pos = st.selectbox("Position", ["Bottom", "Top", "Center"], label_visibility="collapsed")
    st.write("**Background Color**")
    bg_color = st.color_picker("BG Color", "#000000", label_visibility="collapsed")

with c2:
    st.write("**Font Size**")
    f_size = st.number_input("Size", value=16, label_visibility="collapsed")
    st.write("**Background Opacity**")
    bg_opacity = st.slider("Opacity", 0.0, 1.0, 0.5, label_visibility="collapsed")

with c3:
    st.write("**Font Color**")
    f_color = st.color_picker("Font Color", "#ffffff", label_visibility="collapsed")
    st.write("**Font Family**")
    f_family = st.selectbox("Family", ["Arial", "Roboto", "Verdana", "Courier"], label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# --- The Visual Caption Overlay ---
# We use a mathematical helper to convert hex to RGBA for the background
def hex_to_rgba(hex, opacity):
    h = hex.lstrip('#')
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return f"rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, {opacity})"

rgba_bg = hex_to_rgba(bg_color, bg_opacity)

# This CSS positions the caption exactly over the video area
st.markdown(f"""
    <div style="
        position: absolute;
        top: 250px;
        left: 20%;
        width: 60%;
        background-color: {rgba_bg};
        color: {f_color};
        font-size: {f_size}px;
        font-family: {f_family};
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        z-index: 100;
        pointer-events: none;
    ">
        The fluffiest keyboard ever! ⌨️✨
    </div>
    """, unsafe_allow_html=True)