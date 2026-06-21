#!/usr/bin/env python3
"""
Updates figure citations and inserts captions for the combined figure pairs:
  2&3 → Figure 2 (a & b)
  4&5 → Figure 3 (a & b)
  6&7 → Figure 4 (a & b)
"""

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import copy

doc = Document('/home/user/Skill/final_submission_PM_Bengaluru.docx')

# ── Step 1: update all in-text figure citations ───────────────────────────────
# Order matters — replace more specific strings first
replacements = [
    # old citation      → new citation
    ("(Figure 2a)",     "(Figure 2a)"),   # already correct if present
    ("Figure 2a",       "Figure 2a"),
    ("(Figure 2)",      "(Figure 2a)"),   # Mann-Kendall trend
    ("(Figure 3)",      "(Figure 2b)"),   # exceedance frequency
    ("Figure 3)",       "Figure 2b)"),
    ("(Figure 4)",      "(Figure 3a)"),   # COD matrix
    ("Figure 4)",       "Figure 3a)"),
    ("(Figure 5)",      "(Figure 3b)"),   # MDS
    ("Figure 5)",       "Figure 3b)"),
    ("Figure 6 ",       "Figure 4a "),    # diurnal profiles
    ("Figure 6\n",      "Figure 4a\n"),
    ("Figure 6.",       "Figure 4a."),
    ("(Figure 7)",      "(Figure 4b)"),   # weekend effect
    ("Figure 7,",       "Figure 4b,"),
    ("Figure 7.",       "Figure 4b."),
]

def replace_in_para(para, old, new):
    """Replace text in a paragraph preserving runs."""
    full = para.text
    if old not in full:
        return False
    # Simple: rebuild as single run (safe for citation-only paragraphs)
    for run in para.runs:
        if old in run.text:
            run.text = run.text.replace(old, new)
            return True
    # Fallback: stitch across runs
    new_full = full.replace(old, new)
    for run in para.runs:
        run.text = ""
    if para.runs:
        para.runs[0].text = new_full
    return True

for para in doc.paragraphs:
    for old, new in replacements:
        replace_in_para(para, old, new)

# Also fix conclusion para that says "Figure 4" (COD value)
for para in doc.paragraphs:
    if "COD value of 0.42 (Figure 4)" in para.text:
        replace_in_para(para, "(Figure 4)", "(Figure 3a)")

# ── Step 2: helper to insert a caption paragraph after a given paragraph ──────
def insert_caption_after(para, caption_text, placeholder_text):
    """Insert a figure placeholder line + italic caption after `para`."""
    body = doc.element.body
    idx = list(body).index(para._element)

    def make_para(text, italic=False, bold=False, centre=True, size=10):
        p = OxmlElement('w:p')
        pPr = OxmlElement('w:pPr')
        jc = OxmlElement('w:jc')
        jc.set(qn('w:val'), 'center' if centre else 'both')
        pPr.append(jc)
        p.append(pPr)
        r = OxmlElement('w:r')
        rPr = OxmlElement('w:rPr')
        if italic:
            i = OxmlElement('w:i'); rPr.append(i)
        if bold:
            b = OxmlElement('w:b'); rPr.append(b)
        sz = OxmlElement('w:sz')
        sz.set(qn('w:val'), str(size * 2))
        rPr.append(sz)
        r.append(rPr)
        t = OxmlElement('w:t')
        t.text = text
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        r.append(t)
        p.append(r)
        return p

    # blank line before figure
    body.insert(idx + 1, make_para(""))
    # placeholder box line
    body.insert(idx + 2, make_para(placeholder_text, bold=True, size=11))
    # caption line
    body.insert(idx + 3, make_para(caption_text, italic=True, size=10))
    # blank line after
    body.insert(idx + 4, make_para(""))


# ── Step 3: locate the right paragraphs and insert captions ──────────────────

# Figure 2 caption → insert after the "Urban Sprawl Effect" section paragraph
# (the paragraph that ends with "Rengarajan et al., 2011; Tiwari et al., 2009).")
fig2_para = None
for p in doc.paragraphs:
    if "Rengarajan et al., 2011" in p.text and "Tiwari et al., 2009" in p.text:
        fig2_para = p
        break

if fig2_para:
    insert_caption_after(
        fig2_para,
        caption_text=(
            "Figure 2. (a) Mann-Kendall trend analysis of PM₂.₅ concentrations "
            "across 13 CAAQMS stations in Bengaluru (2018–2024), illustrating the "
            "divergent two-speed air quality trajectory between the Peenya industrial cluster "
            "(Sen’s Slope = −2.75 μg·m⁻³·year⁻¹; "
            "p < 0.01) and residential/mixed-use zones. "
            "(b) Exceedance frequency analysis showing the percentage of monitored days on which "
            "PM₁₀ concentrations exceeded the NAAQS threshold (>60 μg/m³) "
            "at each station, identifying RVCE-Mailasandra as the primary non-compliance hotspot "
            "(89.9% violation days). Data source: CPCB CAAQMS network (2018–2024)."
        ),
        placeholder_text="[INSERT FIGURE 2 HERE — Combined panels 2a (trend) and 2b (exceedance frequency)]"
    )
    print("Figure 2 caption inserted.")
else:
    print("WARNING: Figure 2 anchor paragraph not found.")

# Figure 3 caption → insert after the MDS bullet list (last bullet ends with "densifying the core.")
fig3_para = None
for p in doc.paragraphs:
    if "densifying the core" in p.text:
        fig3_para = p
        break

if fig3_para:
    insert_caption_after(
        fig3_para,
        caption_text=(
            "Figure 3. (a) Pairwise Coefficient of Divergence (COD) matrix for all 13 CAAQMS "
            "station combinations, with values exceeding 0.20 indicating spatially heterogeneous "
            "environments (Wilson et al., 2005). The Peenya–Jayanagar pair yields the "
            "highest COD (0.42), confirming chemical decoupling of the industrial north from the "
            "residential south. "
            "(b) Non-Metric Multidimensional Scaling (MDS) ordination of the 13 CAAQMS stations "
            "in two-dimensional Euclidean chemical space, resolving three structurally distinct "
            "airshed regimes: Industrial (red), Kerbside (orange), and Residential/Background "
            "(green). Data source: CPCB CAAQMS network (2018–2024)."
        ),
        placeholder_text="[INSERT FIGURE 3 HERE — Combined panels 3a (COD matrix) and 3b (MDS ordination)]"
    )
    print("Figure 3 caption inserted.")
else:
    print("WARNING: Figure 3 anchor paragraph not found.")

# Figure 4 caption → insert after weekend effect paragraph
# (paragraph containing "Guttikunda et al., 2014" and "<3%")
fig4_para = None
for p in doc.paragraphs:
    if "transient mobility" in p.text and "Guttikunda" in p.text:
        fig4_para = p
        break

if fig4_para:
    insert_caption_after(
        fig4_para,
        caption_text=(
            "Figure 4. (a) Diurnal (24-hour) PM₁₀ concentration profiles for "
            "representative stations across the three identified airshed regimes: "
            "Silk Board (Kerbside, bimodal peaks at 09:00 and 19:00, r² > 0.85), "
            "Peenya (Industrial, sustained daytime baseline with nocturnal boundary-layer "
            "compression peak), and Jayanagar (Residential, flat profile indicating passive "
            "pollution receipt). "
            "(b) Weekend effect analysis showing the percentage reduction in mean NO₂ "
            "concentrations on Sundays relative to weekdays across all 13 CAAQMS stations. "
            "Silk Board junction records an 18.4% reduction (traffic proxy), while Peenya "
            "records <3% (continuous industrial emissions). "
            "Data source: CPCB CAAQMS network (2018–2024)."
        ),
        placeholder_text="[INSERT FIGURE 4 HERE — Combined panels 4a (diurnal profiles) and 4b (weekend NO₂ effect)]"
    )
    print("Figure 4 caption inserted.")
else:
    print("WARNING: Figure 4 anchor paragraph not found.")

# ── Step 4: update Figure 1 caption to use italic style ──────────────────────
for p in doc.paragraphs:
    if p.text.startswith("Figure 1. Location map"):
        for run in p.runs:
            run.italic = True
            run.font.size = Pt(10)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        break

# ── Save ─────────────────────────────────────────────────────────────────────
out = '/home/user/Skill/final_submission_PM_Bengaluru_v2.docx'
doc.save(out)
print(f"\nSaved: {out}")
