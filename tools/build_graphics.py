#!/usr/bin/env python3
"""Build the profile's original SVG graphics. Standard library only.

Run from the repository root: python3 tools/build_graphics.py
Technology icons are vendored separately; see assets/icons/README.md.
"""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
LIGHT = dict(bg="#FCFCFB", panel="#F5F7F5", text="#202722", muted="#747C76",
             accent="#819889", soft="#A8B9AC", border="#E5EAE5", ink="#52685A")
DARK = dict(bg="#161C18", panel="#202923", text="#E6ECE7", muted="#A4AEA6",
            accent="#819889", soft="#6F8476", border="#303B33", ink="#B7C8BC")


def svg(width, height, title, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">Original, restrained geometric branding for Sharon Davasia. Decorative illustration, not a project screenshot.</desc>
{body}
</svg>
'''


def header(p):
    dots = "\n".join(
        f'      <circle cx="{x}" cy="{y}" r="1.15" fill="{p["soft"]}" opacity=".48"/>'
        for y in range(58, 245, 22) for x in range(846, 1130, 22)
    )
    nodes = [(898, 104), (898, 196), (984, 70), (984, 230), (1070, 104), (1070, 196)]
    edges = [(898,104,984,70),(898,104,984,150),(898,196,984,150),(898,196,984,230),
             (984,70,1070,104),(984,150,1070,104),(984,150,1070,196),(984,230,1070,196)]
    lines = "\n".join(f'    <path d="M{a} {b} L{c} {d}" stroke="{p["accent"]}" stroke-width="1.2" opacity=".65"/>' for a,b,c,d in edges)
    circles = "\n".join(f'    <circle cx="{x}" cy="{y}" r="5" fill="{p["bg"]}" stroke="{p["accent"]}" stroke-width="1.5"/>' for x,y in nodes)
    body = f'''  <rect x=".5" y=".5" width="1199" height="279" rx="12" fill="{p['bg']}" stroke="{p['border']}"/>
  <rect x="56" y="44" width="48" height="48" rx="9" fill="{p['panel']}" stroke="{p['border']}"/>
  <text x="80" y="75" text-anchor="middle" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="20" font-weight="600" letter-spacing="-1" fill="{p['ink']}">SD</text>
  <text x="54" y="164" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="56" font-weight="600" letter-spacing="-2.4" fill="{p['text']}">Sharon Davasia</text>
  <text x="58" y="204" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="18" fill="{p['muted']}">Curiosity, made practical.</text>
  <path d="M58 236h38" stroke="{p['accent']}" stroke-width="3" stroke-linecap="round"/>
  <g>
{dots}
    <circle cx="984" cy="150" r="91" fill="none" stroke="{p['border']}"/>
    <rect x="922" y="88" width="124" height="124" rx="20" fill="none" stroke="{p['border']}" transform="rotate(12 984 150)"/>
{lines}
{circles}
    <rect x="965" y="131" width="38" height="38" rx="10" fill="{p['panel']}" stroke="{p['accent']}" stroke-width="1.5"/>
    <path d="M977 150h14M984 143v14" stroke="{p['ink']}" stroke-width="1.6" stroke-linecap="round"/>
    <path d="M824 46h12m-6-6v12M1130 254h12m-6-6v12" stroke="{p['soft']}" stroke-width="1"/>
  </g>'''
    return svg(1200, 280, "Sharon Davasia — Curiosity, made practical.", body)


def frame(p, body, title):
    return svg(720, 240, title, f'''  <rect width="720" height="240" rx="8" fill="{p['bg']}"/>
  <path d="M24 24h16m-8-8v16M680 216h16m-8-8v16" stroke="{p['soft']}" stroke-width="1"/>
{body}''')


def recallpad(p):
    body = f'''  <g fill="none" stroke="{p['border']}" stroke-width="1.5">
    <rect x="104" y="48" width="218" height="146" rx="9" fill="{p['panel']}"/>
    <path d="M104 78h218"/>
    <rect x="446" y="54" width="164" height="38" rx="6" fill="{p['panel']}"/>
    <rect x="446" y="102" width="164" height="38" rx="6" fill="{p['panel']}"/>
    <rect x="446" y="150" width="164" height="38" rx="6" fill="{p['panel']}"/>
  </g>
  <g fill="{p['soft']}"><circle cx="120" cy="63" r="2.5"/><circle cx="131" cy="63" r="2.5"/><circle cx="142" cy="63" r="2.5"/></g>
  <path d="M128 98h124M128 116h164M128 134h145M128 152h94" stroke="{p['soft']}" stroke-width="4" stroke-linecap="round" opacity=".65"/>
  <path d="M278 92v36l-10-7-10 7V92z" fill="{p['accent']}" opacity=".8"/>
  <path d="M338 121h88m-8-7 8 7-8 7" fill="none" stroke="{p['accent']}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  <g fill="{p['accent']}"><circle cx="360" cy="103" r="2"/><circle cx="375" cy="96" r="2"/><circle cx="390" cy="103" r="2"/></g>
  <g stroke="{p['soft']}" stroke-width="3" stroke-linecap="round"><path d="M462 68h70M462 79h108M462 116h92M462 127h62M462 164h78M462 175h100"/></g>
  <g fill="{p['accent']}"><rect x="584" y="66" width="10" height="14" rx="2"/><rect x="584" y="114" width="10" height="14" rx="2"/><rect x="584" y="162" width="10" height="14" rx="2"/></g>'''
    return frame(p, body, "RecallPad — capture and retrieval illustration")


def ideaforge(p):
    satellites = [(226,62),(454,62),(226,150),(454,150)]
    paths = "\n".join(f'  <path d="M360 120 L{x+20} {y+14}" stroke="{p["accent"]}" stroke-width="1.4" fill="none" opacity=".7"/>' for x,y in satellites)
    boxes = "\n".join(f'  <rect x="{x}" y="{y}" width="40" height="28" rx="6" fill="{p["panel"]}" stroke="{p["border"]}"/>' for x,y in satellites)
    body = f'''  <g fill="none" stroke="{p['border']}"><circle cx="360" cy="120" r="87"/><circle cx="360" cy="120" r="103" stroke-dasharray="2 9"/></g>
{paths}
{boxes}
  <rect x="329" y="89" width="62" height="62" rx="14" fill="{p['panel']}" stroke="{p['accent']}" stroke-width="1.5"/>
  <path d="M347 120h26M360 107v26" stroke="{p['ink']}" stroke-width="2" stroke-linecap="round"/>
  <g fill="{p['accent']}"><circle cx="246" cy="76" r="3"/><circle cx="474" cy="76" r="3"/><circle cx="246" cy="164" r="3"/><circle cx="474" cy="164" r="3"/></g>
  <path d="M166 120h28m-14-14v28M526 120h28m-14-14v28" stroke="{p['soft']}" stroke-width="1"/>'''
    return frame(p, body, "IdeaForge — multi-agent orchestration illustration")


def certifypro(p):
    body = f'''  <rect x="238" y="43" width="244" height="154" rx="8" fill="{p['panel']}" stroke="{p['border']}" transform="rotate(-5 360 120)"/>
  <rect x="228" y="51" width="244" height="154" rx="8" fill="{p['bg']}" stroke="{p['accent']}" stroke-width="1.4"/>
  <rect x="244" y="67" width="212" height="122" rx="3" fill="none" stroke="{p['border']}"/>
  <path d="M264 92h116M264 111h164M264 126h142M264 141h98" stroke="{p['soft']}" stroke-width="3" stroke-linecap="round" opacity=".7"/>
  <path d="M264 169h62" stroke="{p['accent']}" stroke-width="1.5"/>
  <path d="M405 163l-7 28 15-8 13 8-5-28" fill="{p['soft']}" opacity=".65"/>
  <circle cx="413" cy="153" r="20" fill="{p['panel']}" stroke="{p['accent']}" stroke-width="1.5"/>
  <path d="M404 153l6 6 12-13" fill="none" stroke="{p['ink']}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <g fill="{p['soft']}"><circle cx="184" cy="88" r="2"/><circle cx="530" cy="153" r="2"/></g>
  <path d="M174 152h20m-10-10v20M516 82h20m-10-10v20" stroke="{p['border']}"/>'''
    return frame(p, body, "CertifyPro — digital certificate illustration")


def vision(p):
    body = f'''  <g fill="none" stroke="{p['border']}"><rect x="180" y="38" width="360" height="164" rx="8"/><path d="M180 160h360M270 38v164M450 38v164" stroke-dasharray="3 7"/></g>
  <path d="M202 76V58h18M498 58h18v18M202 164v18h18M498 182h18v-18" fill="none" stroke="{p['accent']}" stroke-width="2" stroke-linecap="round"/>
  <rect x="291" y="62" width="132" height="119" rx="4" fill="{p['panel']}" fill-opacity=".65" stroke="{p['accent']}" stroke-width="1.4"/>
  <g fill="none" stroke="{p['ink']}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="355" cy="84" r="9"/><path d="M355 95l-4 37m-17-23 21-10 22 17M351 132l-18 30m18-30 24 27"/>
  </g>
  <g fill="{p['accent']}"><circle cx="355" cy="99" r="3"/><circle cx="334" cy="109" r="3"/><circle cx="377" cy="116" r="3"/><circle cx="351" cy="132" r="3"/><circle cx="333" cy="162" r="3"/><circle cx="375" cy="159" r="3"/></g>
  <path d="M146 120h16m-8-8v16M558 120h16m-8-8v16" stroke="{p['soft']}"/>'''
    return frame(p, body, "Computer vision — detection frame and pose keypoints illustration")


def contact_badge(label, width, icon, p):
    """Small, local, theme-aware alternative to a remote badge service."""
    if icon in ("github", "linkedin"):
        root = ET.parse(ASSETS / "icons" / f"{icon}.svg").getroot()
        box = [float(v) for v in root.get("viewBox", "0 0 128 128").split()]
        scale = 16 / max(box[2], box[3])
        inner = "".join(ET.tostring(child, encoding="unicode") for child in root
                        if not child.tag.endswith("title"))
        mark = f'<g transform="translate(10 6) scale({scale:.6f})" fill="{p["accent"]}">{inner}</g>'
    elif icon == "email":
        mark = f'''<g transform="translate(10 7)" fill="none" stroke="{p['accent']}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><rect x="0" y="0" width="16" height="13" rx="2"/><path d="m1 2 7 5 7-5"/></g>'''
    else:
        mark = f'''<g transform="translate(10 6)" fill="none" stroke="{p['accent']}" stroke-width="1.3"><circle cx="8" cy="8" r="7"/><ellipse cx="8" cy="8" rx="3" ry="7"/><path d="M1 8h14"/></g>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="28" viewBox="0 0 {width} 28" role="img" aria-label="{label}">
  <rect x=".5" y=".5" width="{width-1}" height="27" rx="4" fill="{p['panel']}" stroke="{p['border']}"/>
  {mark}
  <text x="34" y="18" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif" font-size="12" font-weight="500" fill="{p['text']}">{label}</text>
</svg>
'''


def divider():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="16" viewBox="0 0 1200 16" aria-hidden="true">
  <path d="M16 8h1184" stroke="#819889" stroke-opacity=".3"/>
  <rect x="3" y="3" width="10" height="10" rx="2" transform="rotate(45 8 8)" fill="#819889" fill-opacity=".65"/>
</svg>
'''


def main():
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "projects").mkdir(exist_ok=True)
    (ASSETS / "contact").mkdir(exist_ok=True)
    for name, palette in [("light", LIGHT), ("dark", DARK)]:
        (ASSETS / f"header-{name}.svg").write_text(header(palette))
        for fn in (recallpad, ideaforge, certifypro, vision):
            (ASSETS / "projects" / f"{fn.__name__}-{name}.svg").write_text(fn(palette))
        for label, width, icon in [("GitHub", 92, "github"), ("LinkedIn", 106, "linkedin"),
                                   ("Email", 88, "email"), ("Portfolio", 114, "portfolio")]:
            (ASSETS / "contact" / f"{icon}-{name}.svg").write_text(contact_badge(label, width, icon, palette))
    (ASSETS / "divider.svg").write_text(divider())
    print("Built 19 original SVG graphics.")


if __name__ == "__main__":
    main()
