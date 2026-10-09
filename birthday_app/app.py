import base64
import random
from pathlib import Path

import streamlit as st

# ----------------------------------------------------------------------------
# CONFIG – edit these to personalise
# ----------------------------------------------------------------------------
HER_NAME = "Roshibina"
HIS_NAME = "Harsh"
AGE = 22

WISH_MESSAGE = f"""
Happy 22nd Birthday, my love! 🎂

Today the world got the most beautiful soul, and I got the luckiest
chance to love her. You make my ordinary days feel like little celebrations,
and my heart feels like home whenever you smile.

I wish this year gives you everything your heart quietly asks for –
endless laughter, big dreams coming true, peaceful nights and
sweet mornings. And whatever comes, I'll always be right beside you.
"""

CLOSING_MESSAGE = f"""
Every picture shows only a little of how beautiful you are, {HER_NAME},
inside and out. The best days of your life are still waiting for you,
and I can't wait to see you shine through every one of them.
Thank you for being you – my person, my happiness, my forever. 💖

Once again, happy birthday, my princess! 🎀

<b>Always yours,<br>{HIS_NAME}</b> 🎀
"""

CUTE_LINES = [
    "Meow! You're the cutest person ever 🐱",
    "Someone special turns 22 today! 🎉",
    "Kitty says: you deserve all the cake 🍰",
    "Harsh loves you SO much 💕",
    "Make a wish, birthday girl ✨",
    "You're my favourite human 🎀",
    "Purr-fect day for a purr-fect girl 😽",
]

PHOTO_TITLE = "Beautiful Moments of You 📸"
PHOTO_CAPTIONS = ["That beautiful smile 💕", "Cutie pie 🌸", "Pretty as ever ✨",
                  "Pure happiness 🎈", "Princess vibes 👑", "Simply gorgeous 🎀"]

BASE = Path(__file__).parent
PHOTO_DIR = BASE / "photos"
ASSET_DIR = BASE / "assets"

st.set_page_config(
    page_title=f"Happy Birthday {HER_NAME}! 🎀",
    page_icon="🎀",
    layout="centered",
)

# ----------------------------------------------------------------------------
# CSS
# ----------------------------------------------------------------------------
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Fredoka:wght@400;500;600;700&family=Dancing+Script:wght@500;600;700&family=Sacramento&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Fredoka', sans-serif;
}
.stApp {
    background: linear-gradient(135deg, #ffe3ef 0%, #ffd1e8 40%, #ffeaf4 100%);
    overflow-x: hidden;
}
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 2rem; max-width: 760px;}

/* polka dots overlay */
.stApp::before {
    content: "";
    position: fixed; inset: 0; pointer-events: none;
    background-image: radial-gradient(#ffffff88 12%, transparent 13%);
    background-size: 36px 36px;
    z-index: 0;
}

.title {
    font-family: 'Pacifico', cursive;
    color: #e0457b;
    text-align: center;
    font-size: 2.6rem;
    line-height: 1.25;
    text-shadow: 3px 3px 0 #fff, 5px 5px 0 #ffb6d2;
    margin: 0.2rem 0 0.4rem 0;
}
.subtitle {
    text-align: center; color: #b3446f;
    font-size: 1.2rem; font-weight: 500; margin-bottom: 0.6rem;
}
.hint {
    text-align:center; color:#b3446f; font-size:1.15rem; font-weight:600; margin: .2rem 0 .8rem 0;
}
.music-note {text-align:center; color:#b3446f; font-size:.95rem; margin-top:-.4rem;}
.speech {
    background: #fff; border: 3px solid #ff8fb8; border-radius: 22px;
    padding: 0.7rem 1.1rem; color: #b3446f; font-weight: 600;
    text-align: center; margin: 0.5rem auto 0.2rem auto; max-width: 420px;
    position: relative; animation: pop 0.5s ease both;
}
.kitty-wrap {text-align:center; animation: bounce 2.4s ease-in-out infinite;}
.cake {font-size: 4rem; text-align:center; animation: bounce 1.8s ease-in-out infinite;}

/* ---------- birthday letter card ---------- */
.card {
    position: relative;
    background:
        radial-gradient(#ffd6e7 18%, transparent 20%) 0 0 / 22px 22px,
        #fffafc;
    border: 5px solid #ff8fb8;
    border-radius: 30px;
    padding: 0 1.8rem 1.4rem 1.8rem;
    margin-top: 1.6rem;
    box-shadow: 0 0 0 5px #fff, 0 0 0 8px #ffc2dc, 0 14px 30px rgba(224, 69, 123, 0.25);
    color: #7a1f47;
    text-align: center;
    animation: pop 0.8s ease both;
}
.card .bunting {display:block; width: calc(100% + 3.6rem); margin: -2px -1.8rem 0 -1.8rem; height: 56px;}
.card .dear {
    font-family: 'Pacifico', cursive; color: #e0457b; font-size: 1.9rem; margin: .4rem 0 .2rem 0;
}
.card p {
    font-family: 'Dancing Script', cursive; font-weight: 600;
    font-size: 1.6rem; line-height: 1.55; margin: .55rem 0;
}
.card p.dear {font-family: 'Pacifico', cursive; font-weight: 400; font-size: 1.9rem;}
.card b {font-family: 'Pacifico', cursive; font-weight: 400; color: #e0457b; font-size: 1.5rem; line-height: 1.7;}

/* buttons */
div.stButton {text-align: center;}
div.stButton > button {
    background: linear-gradient(135deg, #ff6fa5, #ff9ec4);
    color: #fff; border: 3px solid #fff;
    border-radius: 999px; padding: 0.7rem 2.2rem;
    font-family: 'Fredoka', sans-serif; font-size: 1.25rem; font-weight: 600;
    box-shadow: 0 8px 20px rgba(255, 111, 165, 0.5);
    transition: transform .2s ease, box-shadow .2s ease;
    animation: pulse 1.8s infinite;
}
div.stButton > button:hover {
    transform: scale(1.08) rotate(-2deg); color: #fff; border-color: #fff;
    box-shadow: 0 12px 26px rgba(255, 111, 165, 0.7);
}
div.stButton > button:focus:not(:active) {color:#fff; border-color:#fff;}

/* audio player */
div[data-testid="stAudio"] {max-width: 340px; margin: 0 auto;}
div[data-testid="stAudio"] audio {width: 100%; height: 38px; border-radius: 999px;}

/* floating doodles */
.floaters {position: fixed; inset: 0; pointer-events: none; z-index: 1; overflow: hidden;}
.floaters span {
    position: absolute; bottom: -60px; opacity: .85;
    animation: floatUp linear infinite;
}

/* decorated photo frames */
.polaroid-grid {display:flex; flex-wrap:wrap; justify-content:center; gap: 44px 30px; margin: 1.6rem 0 1.8rem 0;}
.polaroid {
    position: relative;
    width: 240px; padding: 16px 16px 12px 16px;
    background:
        radial-gradient(#ffc2dc 22%, transparent 24%) 0 0 / 14px 14px,
        #fff0f7;
    border: 5px solid #ff8fb8;
    border-radius: 26px;
    box-shadow: 0 0 0 5px #fff, 0 0 0 8px #ffb6d2, 0 14px 26px rgba(224, 69, 123, .30);
    transition: transform .3s ease; animation: pop .8s ease both;
    text-align: center;
}
.polaroid:hover {transform: scale(1.07) rotate(0deg) !important; z-index: 5;}
.polaroid img {
    width: 100%; display:block; border-radius: 14px;
    border: 4px solid #fff; outline: 3px dashed #ff8fb8; outline-offset: 0;
}
.polaroid .cap {font-family:'Pacifico',cursive; color:#e0457b; margin-top:12px; font-size:1.05rem;}
.polaroid .tape {
    position:absolute; top:-18px; left:50%; width:90px; height:26px;
    transform: translateX(-50%) rotate(-3deg);
    background: repeating-linear-gradient(45deg, #ffd6e7, #ffd6e7 8px, #fff 8px, #fff 16px);
    opacity:.92; border-radius:4px; box-shadow: 0 2px 5px rgba(0,0,0,.15);
}
.polaroid .doodle {position:absolute; z-index:3; line-height:1; pointer-events:none;}
.polaroid .d-bow   {top:-22px; left:-20px; font-size:40px; transform: rotate(-20deg); animation: wiggle 2.6s ease-in-out infinite;}
.polaroid .d-star  {top:34px; right:-22px; font-size:30px; animation: twinkle 1.8s ease-in-out infinite;}
.polaroid .d-heart {bottom:48px; left:-24px; font-size:30px; animation: bounce 2.2s ease-in-out infinite;}
.polaroid .d-flower{bottom:-18px; right:34px; font-size:28px; animation: wiggle 3s ease-in-out infinite;}
.polaroid .d-kitty {bottom:-30px; right:-26px; width:74px; height:68px; transform: rotate(10deg); animation: bounce 2.4s ease-in-out infinite;}
.polaroid.alt .d-kitty {right:auto; left:-26px; transform: rotate(-10deg);}
.polaroid.alt .d-bow {left:auto; right:-20px; transform: rotate(20deg) scaleX(-1);}
.polaroid.alt .d-star {right:auto; left:-22px;}
.polaroid.alt .d-heart {left:auto; right:-24px;}

/* cake scene */
.cake-scene {text-align:center; margin: .4rem auto; animation: pop .7s ease both;}
.cake-scene svg {width: 100%; max-width: 430px; height: auto; overflow: visible;}
.flame-in {transform-box: fill-box; transform-origin: 50% 90%; animation: flicker .35s ease-in-out infinite alternate;}
.glow {animation: glowPulse 1s ease-in-out infinite alternate;}
.smoke {fill: none; stroke: #bdbdbd; stroke-width: 3; stroke-linecap: round; opacity: 0; animation: smokeUp 2.4s ease-out forwards;}
.slice {transform-origin: 340px 290px; animation: sliceOut 1s ease .9s forwards;}
.knife {animation: knifeCut 1.7s ease forwards;}
.crumb {animation: floatCrumb 1.2s ease-out 1.4s both;}

@keyframes floatUp {
    0%   {transform: translateY(0) rotate(0deg); opacity: 0;}
    10%  {opacity: .9;}
    100% {transform: translateY(-115vh) rotate(360deg); opacity: 0;}
}
@keyframes wiggle {0%,100% {transform: rotate(-12deg);} 50% {transform: rotate(12deg);}}
@keyframes twinkle {0%,100% {transform: scale(.8); opacity:.6;} 50% {transform: scale(1.25); opacity:1;}}
@keyframes bounce {0%,100% {transform: translateY(0);} 50% {transform: translateY(-14px);}}
@keyframes flicker {0% {transform: scale(1, 1) rotate(-3deg);} 100% {transform: scale(.92, 1.1) rotate(3deg);}}
@keyframes glowPulse {0% {opacity:.35;} 100% {opacity:.8;}}
@keyframes smokeUp {0% {opacity:.9; transform: translateY(0);} 100% {opacity:0; transform: translateY(-46px);}}
@keyframes sliceOut {0% {transform: translate(0,0) rotate(0);} 100% {transform: translate(36px, 12px) rotate(9deg);}}
@keyframes knifeCut {
    0% {transform: translateY(-90px); opacity: 1;}
    45% {transform: translateY(0); opacity: 1;}
    75% {transform: translateY(0); opacity: 1;}
    100% {transform: translateY(-10px); opacity: 0;}
}
@keyframes floatCrumb {0% {opacity:0; transform: translateY(-14px);} 100% {opacity:1; transform: translateY(0);}}
@keyframes pulse {
    0% {box-shadow: 0 0 0 0 rgba(255,111,165,.6);}
    70% {box-shadow: 0 0 0 16px rgba(255,111,165,0);}
    100% {box-shadow: 0 0 0 0 rgba(255,111,165,0);}
}
@keyframes pop {0% {transform: scale(.85); opacity: 0;} 100% {transform: scale(1); opacity: 1;}}

@media (max-width: 600px) {
    .title {font-size: 2rem;}
    .card p {font-size: 1.4rem;}
    .polaroid {width: 150px; padding: 10px 10px 8px 10px;}
    .polaroid .d-kitty {width:52px; height:48px;}
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# Doodles & SVG pieces
# ----------------------------------------------------------------------------
def floaters(emojis=("🎀", "🌸", "💖", "⭐", "🎈", "🍰", "🐱", "✨", "🧁")):
    rnd = random.Random(7)
    items = []
    for _ in range(18):
        left = rnd.randint(2, 96)
        size = rnd.randint(22, 44)
        dur = rnd.randint(9, 18)
        delay = rnd.randint(0, 12)
        e = rnd.choice(emojis)
        items.append(
            f'<span style="left:{left}%;font-size:{size}px;'
            f'animation-duration:{dur}s;animation-delay:{delay}s">{e}</span>'
        )
    st.markdown(f'<div class="floaters">{"".join(items)}</div>', unsafe_allow_html=True)


KITTY_SVG = """
<div class="kitty-wrap">
<svg width="210" height="190" viewBox="0 0 210 190" xmlns="http://www.w3.org/2000/svg">
  <!-- ears -->
  <polygon points="35,70 40,18 85,45" fill="#fff" stroke="#3b2b33" stroke-width="4" stroke-linejoin="round"/>
  <polygon points="175,70 170,18 125,45" fill="#fff" stroke="#3b2b33" stroke-width="4" stroke-linejoin="round"/>
  <!-- head -->
  <ellipse cx="105" cy="110" rx="82" ry="64" fill="#fff" stroke="#3b2b33" stroke-width="4"/>
  <!-- eyes -->
  <ellipse cx="72" cy="108" rx="7" ry="9" fill="#3b2b33"/>
  <ellipse cx="138" cy="108" rx="7" ry="9" fill="#3b2b33"/>
  <!-- nose -->
  <ellipse cx="105" cy="124" rx="9" ry="6" fill="#ffc107" stroke="#3b2b33" stroke-width="2.5"/>
  <!-- whiskers -->
  <g stroke="#3b2b33" stroke-width="3" stroke-linecap="round">
    <line x1="14" y1="104" x2="50" y2="112"/><line x1="12" y1="124" x2="50" y2="124"/><line x1="16" y1="144" x2="52" y2="134"/>
    <line x1="196" y1="104" x2="160" y2="112"/><line x1="198" y1="124" x2="160" y2="124"/><line x1="194" y1="144" x2="158" y2="134"/>
  </g>
  <!-- cheeks -->
  <ellipse cx="52" cy="134" rx="9" ry="5" fill="#ffb6d2" opacity=".7"/>
  <ellipse cx="158" cy="134" rx="9" ry="5" fill="#ffb6d2" opacity=".7"/>
  <!-- bow -->
  <g stroke="#3b2b33" stroke-width="3.5" stroke-linejoin="round">
    <polygon points="140,50 172,28 176,70" fill="#ff4f8b"/>
    <polygon points="140,50 112,32 104,70" fill="#ff4f8b"/>
    <circle cx="140" cy="50" r="10" fill="#ff7aa8"/>
  </g>
</svg>
</div>
"""

KITTY_MINI = (
    '<svg class="doodle d-kitty" viewBox="0 0 110 100" xmlns="http://www.w3.org/2000/svg">'
    '<g stroke="#3b2b33" stroke-width="3.5" stroke-linejoin="round">'
    '<polygon points="12,38 16,6 44,24" fill="#fff"/><polygon points="98,38 94,6 66,24" fill="#fff"/>'
    '<ellipse cx="55" cy="58" rx="44" ry="34" fill="#fff"/>'
    '<polygon points="74,28 94,14 96,40" fill="#ff4f8b"/><polygon points="74,28 58,16 54,40" fill="#ff4f8b"/>'
    '<circle cx="74" cy="28" r="6" fill="#ff7aa8"/></g>'
    '<ellipse cx="38" cy="58" rx="4" ry="5.5" fill="#3b2b33"/><ellipse cx="72" cy="58" rx="4" ry="5.5" fill="#3b2b33"/>'
    '<ellipse cx="55" cy="68" rx="5.5" ry="3.5" fill="#ffc107" stroke="#3b2b33" stroke-width="2"/>'
    '<g stroke="#3b2b33" stroke-width="2.5" stroke-linecap="round">'
    '<line x1="6" y1="56" x2="26" y2="62"/><line x1="5" y1="70" x2="26" y2="68"/>'
    '<line x1="104" y1="56" x2="84" y2="62"/><line x1="105" y1="70" x2="84" y2="68"/></g>'
    '<ellipse cx="28" cy="72" rx="5" ry="3" fill="#ffb6d2" opacity=".7"/><ellipse cx="82" cy="72" rx="5" ry="3" fill="#ffb6d2" opacity=".7"/>'
    '</svg>'
)

CAKE_SVG_ROW = '<div class="cake">🎂🎈🎁🎈🎂</div>'


def bunting_svg() -> str:
    """Party flags that hang across the top of the letter cards."""
    colors = ["#ff6fa5", "#ffd166", "#7bdff2", "#b794f4", "#ff9ec4", "#95e1a3"]
    flags = []
    n = 12
    w = 600 / n
    for i in range(n):
        x = i * w + 4
        # follow a gentle curve
        y = 8 + 10 * (1 - ((i + .5) / n * 2 - 1) ** 2) * 0.0 + 6 * abs(((i + .5) / n * 2 - 1)) * -1 + 6
        flags.append(
            f'<polygon points="{x:.1f},{y:.1f} {x + w - 8:.1f},{y:.1f} {x + (w - 8) / 2:.1f},{y + 34:.1f}" '
            f'fill="{colors[i % len(colors)]}" stroke="#fff" stroke-width="2"/>'
        )
    return (
        '<svg class="bunting" viewBox="0 0 600 56" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">'
        '<path d="M0,6 Q300,18 600,6" stroke="#e0457b" stroke-width="3" fill="none"/>'
        + "".join(flags) + '</svg>'
    )


def candle_flame(cx: float, cy: float, scale: float) -> str:
    if scale <= 0:
        return ""
    return (
        f'<g transform="translate({cx},{cy})">'
        f'<circle class="glow" cx="0" cy="-6" r="{30 * scale:.1f}" fill="#ffe27a"/>'
        f'<g transform="scale({scale})"><g class="flame-in">'
        '<path d="M0,-24 C11,-9 11,6 0,9 C-11,6 -11,-9 0,-24Z" fill="#ffb300"/>'
        '<path d="M0,-12 C5,-4 5,3 0,5 C-5,3 -5,-4 0,-12Z" fill="#fff6c9"/>'
        '</g></g></g>'
    )


def smoke(cx: float, cy: float) -> str:
    out = []
    for k, dx in enumerate((-6, 0, 6)):
        out.append(
            f'<path class="smoke" style="animation-delay:{k * .25}s" '
            f'd="M{cx + dx},{cy} q-7,-10 0,-20 q7,-10 0,-20"/>'
        )
    return "".join(out)


SLICE_X = 284  # where the knife cuts


def cake_body(x0: float, x1: float, with_text: bool) -> str:
    """Cake pieces restricted to the x-range [x0, x1]."""
    def rect(xa, xb, y, h, fill, extra=""):
        a, b = max(xa, x0), min(xb, x1)
        if b <= a:
            return ""
        return f'<rect x="{a}" y="{y}" width="{b - a}" height="{h}" fill="{fill}" {extra}/>'

    out = []
    # bottom tier
    out.append(rect(60, 340, 205, 85, "#ffd1e8", 'stroke="#e0457b" stroke-width="0"'))
    out.append(rect(60, 340, 238, 7, "#fff"))
    out.append(rect(60, 340, 264, 7, "#fff"))
    out.append(rect(60, 340, 205, 16, "#ff8fb8"))
    for cx in range(69, 332, 18):
        if x0 <= cx <= x1:
            out.append(f'<circle cx="{cx}" cy="221" r="9" fill="#ff8fb8"/>')
    # top tier
    out.append(rect(100, 300, 140, 65, "#fff0f7"))
    out.append(rect(100, 300, 168, 6, "#ffc2dc"))
    out.append(rect(100, 300, 190, 6, "#ffc2dc"))
    out.append(rect(100, 300, 140, 14, "#ff6fa5"))
    for cx in range(108, 293, 16):
        if x0 <= cx <= x1:
            out.append(f'<circle cx="{cx}" cy="154" r="8" fill="#ff6fa5"/>')
    # top tier sits on the bottom tier
    out.append(rect(100, 300, 205, 0.1, "#fff0f7"))
    # strawberries
    for sx in (118, 200, 270):
        if x0 <= sx <= x1:
            out.append(f'<text x="{sx}" y="138" font-size="24" text-anchor="middle">🍓</text>')
    if with_text:
        out.append(
            '<text x="180" y="233" font-family="Pacifico, cursive" font-size="22" '
            'fill="#e0457b" text-anchor="middle" stroke="#fff" stroke-width="3" paint-order="stroke">'
            f'{HER_NAME}</text>'
        )
    return "".join(out)


def cake_svg(level: int, cut: bool) -> str:
    """level: 3..0 = how strong the candle flames still are. cut: cake already sliced."""
    scale = {3: 1.0, 2: 0.8, 1: 0.5, 0: 0.0}[level]
    parts = ['<svg viewBox="0 0 400 330" xmlns="http://www.w3.org/2000/svg">']
    # plate
    parts.append('<ellipse cx="200" cy="294" rx="192" ry="24" fill="#fff" stroke="#ffb6d2" stroke-width="5"/>')
    parts.append('<ellipse cx="200" cy="294" rx="150" ry="14" fill="#ffe3ef"/>')
    if cut:
        parts.append(cake_body(0, SLICE_X, True))
        parts.append('<g class="slice">' + cake_body(SLICE_X, 1000, False) + '</g>')
    else:
        parts.append(cake_body(0, 1000, True))
    # number candles "2" "2"
    for cx, col in ((165, "#4cc3ff"), (235, "#ffb347")):
        parts.append(
            f'<text x="{cx}" y="140" font-family="Fredoka, sans-serif" font-weight="700" font-size="92" '
            f'text-anchor="middle" fill="{col}" stroke="#fff" stroke-width="5" paint-order="stroke">2</text>'
        )
    for cx in (165, 235):
        parts.append(f'<line x1="{cx}" y1="74" x2="{cx}" y2="82" stroke="#5b3a29" stroke-width="3" stroke-linecap="round"/>')
        parts.append(candle_flame(cx, 62, scale))
        if level == 0 and not cut:
            parts.append(smoke(cx, 66))
    if cut:
        # knife slicing down on the cut line
        parts.append(
            f'<g class="knife"><rect x="{SLICE_X - 4}" y="118" width="8" height="150" fill="#dfe6ee" stroke="#8795a3" stroke-width="2"/>'
            f'<polygon points="{SLICE_X - 4},268 {SLICE_X + 4},268 {SLICE_X},282" fill="#dfe6ee" stroke="#8795a3" stroke-width="2"/>'
            f'<rect x="{SLICE_X - 7}" y="70" width="14" height="48" rx="6" fill="#ff6fa5" stroke="#fff" stroke-width="3"/></g>'
        )
        parts.append('<g class="crumb"><text x="352" y="268" font-size="22">✨</text><text x="40" y="270" font-size="20">💖</text></g>')
    parts.append('</svg>')
    return '<div class="cake-scene">' + "".join(parts) + '</div>'


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
def to_html(text: str, dear: bool = False) -> str:
    """Turn a message into <p> paragraphs (blank lines would break Streamlit's HTML block)."""
    paras = [" ".join(par.split()) for par in text.strip().split("\n\n")]
    html = "".join(f"<p>{x}</p>" for x in paras)
    if dear:
        html = f'<p class="dear">Dear {HER_NAME},</p>' + html
    return html


def letter(text: str, dear: bool = False):
    st.markdown(
        f'<div class="card">{bunting_svg()}{to_html(text, dear)}</div>',
        unsafe_allow_html=True,
    )


def img_to_b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def load_photos():
    exts = {".jpg", ".jpeg", ".png", ".webp"}
    return sorted(p for p in PHOTO_DIR.glob("*") if p.suffix.lower() in exts)


def play_song():
    """Autoplays the birthday song. Keep this the FIRST element on every page that
    has music, so the song keeps playing smoothly when she moves between pages."""
    custom = ASSET_DIR / "birthday_song.mp3"
    default = ASSET_DIR / "happy_birthday.wav"
    if custom.exists():
        st.audio(custom.read_bytes(), format="audio/mp3", loop=True, autoplay=True)
    elif default.exists():
        st.audio(default.read_bytes(), format="audio/wav", loop=True, autoplay=True)


def reset_cake():
    st.session_state.flame = 3
    st.session_state.cut = False
    st.session_state.cake_fx = False


def go(page: str):
    st.session_state.page = page
    if page == "home":
        st.session_state.line_idx = -1
        st.session_state.balloons_done = False
        st.session_state.snow_done = False
        reset_cake()


def blow():
    st.session_state.flame = max(0, st.session_state.flame - 1)


def cut_cake():
    st.session_state.cut = True


for key, val in (("page", "home"), ("line_idx", -1), ("balloons_done", False),
                 ("snow_done", False), ("flame", 3), ("cut", False), ("cake_fx", False)):
    if key not in st.session_state:
        st.session_state[key] = val

page = st.session_state.page

# ----------------------------------------------------------------------------
# PAGE 1 – landing with interactive kitty
# ----------------------------------------------------------------------------
if page == "home":
    floaters()
    st.markdown('<div class="subtitle">🎀 A little surprise for someone special 🎀</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="title">Hello, {HER_NAME}!</div>', unsafe_allow_html=True)
    st.markdown(KITTY_SVG, unsafe_allow_html=True)

    if st.session_state.line_idx >= 0:
        line = CUTE_LINES[st.session_state.line_idx % len(CUTE_LINES)]
        st.markdown(f'<div class="speech">{line}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="speech">Psst… tap the button below to talk to kitty 🐾</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("😽 Pet the kitty", use_container_width=True):
            st.session_state.line_idx = random.randint(0, len(CUTE_LINES) - 1)
            st.rerun()

    st.write("")
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.button("🎁 Click here, there's a surprise!", on_click=go, args=("wish",), use_container_width=True)

# ----------------------------------------------------------------------------
# PAGE 2 – birthday wish (music starts here)
# ----------------------------------------------------------------------------
elif page == "wish":
    play_song()
    st.markdown('<div class="music-note">🎵 Press ▶️ if the song doesn\'t start</div>', unsafe_allow_html=True)
    floaters(("🎈", "🎉", "🎂", "💖", "🌸", "✨", "🎀"))
    if not st.session_state.balloons_done:
        st.balloons()
        st.session_state.balloons_done = True

    st.markdown(f'<div class="title">Happy {AGE}th Birthday<br>{HER_NAME}! 🎂</div>', unsafe_allow_html=True)
    st.markdown(CAKE_SVG_ROW, unsafe_allow_html=True)
    letter(WISH_MESSAGE, dear=True)
    st.write("")
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.button("📸 See your beautiful moments", on_click=go, args=("photos",), use_container_width=True)

# ----------------------------------------------------------------------------
# PAGE 3 – photos
# ----------------------------------------------------------------------------
elif page == "photos":
    play_song()
    st.markdown('<div class="music-note">🎵 Press ▶️ if the song doesn\'t start</div>', unsafe_allow_html=True)
    floaters(("💖", "🌸", "⭐", "🎀", "✨"))
    if not st.session_state.snow_done:
        st.snow()
        st.session_state.snow_done = True

    st.markdown(f'<div class="title">{PHOTO_TITLE}</div>', unsafe_allow_html=True)

    photos = load_photos()
    tilts = [-4, 3, -2, 4, -3, 2]
    if photos:
        cards = []
        extras = ["🌸", "🍓", "🌷", "🧁", "🍭", "🦋"]
        for i, p in enumerate(photos):
            mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"
            alt = " alt" if i % 2 else ""
            cards.append(
                f'<div class="polaroid{alt}" style="transform: rotate({tilts[i % len(tilts)]}deg)">'
                f'<div class="tape"></div>'
                f'<div class="doodle d-bow">🎀</div>'
                f'<div class="doodle d-star">⭐</div>'
                f'<div class="doodle d-heart">💖</div>'
                f'<div class="doodle d-flower">{extras[i % len(extras)]}</div>'
                f'{KITTY_MINI}'
                f'<img src="data:{mime};base64,{img_to_b64(p)}"/>'
                f'<div class="cap">{PHOTO_CAPTIONS[i % len(PHOTO_CAPTIONS)]}</div></div>'
            )
        st.markdown(f'<div class="polaroid-grid">{"".join(cards)}</div>', unsafe_allow_html=True)
    else:
        st.info("Add photos to the 'photos' folder next to app.py")

    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.button("🕯️ Time to make a wish!", on_click=go, args=("cake",), use_container_width=True)

# ----------------------------------------------------------------------------
# PAGE 4 – candles (tap to blow) + cake cutting
# ----------------------------------------------------------------------------
elif page == "cake":
    play_song()
    st.markdown('<div class="music-note">🎵 Press ▶️ if the song doesn\'t start</div>', unsafe_allow_html=True)
    floaters(("🎈", "🎉", "🍰", "💖", "✨", "🎀"))

    level = st.session_state.flame
    cut = st.session_state.cut

    if cut:
        st.markdown('<div class="title">Yummy! 🍰</div>', unsafe_allow_html=True)
    elif level == 0:
        st.markdown('<div class="title">Candles Out!<br>Make a Wish 🌠</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="title">Blow the Candles! 🕯️</div>', unsafe_allow_html=True)

    st.markdown(cake_svg(level, cut), unsafe_allow_html=True)

    if cut:
        if not st.session_state.cake_fx:
            st.balloons()
            st.session_state.cake_fx = True
        st.markdown(f'<div class="hint">Happy birthday, {HER_NAME}! May every wish come true 💖</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1, 3, 1])
        with c2:
            st.button("💌 Open my letter", on_click=go, args=("final",), use_container_width=True)
    elif level == 0:
        st.markdown('<div class="hint">Close your eyes, make a wish… now cut the cake! 🔪</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1, 3, 1])
        with c2:
            st.button("🔪 Cut the cake!", on_click=cut_cake, use_container_width=True)
    else:
        st.markdown(f'<div class="hint">Keep tapping! {level} more {"tap" if level == 1 else "taps"} 💨</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1, 3, 1])
        with c2:
            st.button("💨 Tap to blow!", on_click=blow, use_container_width=True)

# ----------------------------------------------------------------------------
# PAGE 5 – closing letter
# ----------------------------------------------------------------------------
else:
    play_song()
    st.markdown('<div class="music-note">🎵 Press ▶️ if the song doesn\'t start</div>', unsafe_allow_html=True)
    floaters(("💖", "🌸", "⭐", "🎀", "🎈", "✨"))
    st.markdown(f'<div class="title">With All My Love 💖</div>', unsafe_allow_html=True)
    letter(CLOSING_MESSAGE)
    st.markdown('<div class="cake">💖🎀💖</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.button("🔁 Watch again", on_click=go, args=("home",), use_container_width=True)
