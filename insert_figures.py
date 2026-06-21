#!/usr/bin/env python3
"""Insert figure images into the Word document at placeholder positions."""

from docx import Document
from docx.shared import Cm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

doc = Document('/home/user/Skill/final_submission_PM_Bengaluru_v2.docx')

figures = {
    '[INSERT FIGURE 1': '/home/user/Skill/figure1_map.png',
    '[INSERT FIGURE 2': '/home/user/Skill/figure2_combined.png',
    '[INSERT FIGURE 3': '/home/user/Skill/figure3_combined.png',
    '[INSERT FIGURE 4': '/home/user/Skill/figure4_combined.png',
}

# Find placeholder paragraphs and note their indices
body = doc.element.body
paras = doc.paragraphs

for fig_key, img_path in figures.items():
    for i, para in enumerate(paras):
        if para.text.startswith(fig_key):
            print(f"Found placeholder for {fig_key} at para {i}: {para.text[:60]}")

            # Create a new centered paragraph with the image
            new_p = OxmlElement('w:p')
            pPr = OxmlElement('w:pPr')
            jc = OxmlElement('w:jc')
            jc.set(qn('w:val'), 'center')
            pPr.append(jc)
            new_p.append(pPr)

            # Insert new image paragraph before the placeholder
            idx = list(body).index(para._element)

            # We'll use a temporary doc to get the run with image, then move it
            tmp_doc = Document()
            tmp_para = tmp_doc.add_paragraph()
            tmp_para.alignment = 1  # center
            run = tmp_para.add_run()

            # Width: Figure 1 (portrait map) narrower; combined figures wider
            if 'FIGURE 1' in fig_key:
                width = Cm(10)
            else:
                width = Cm(15.5)

            run.add_picture(img_path, width=width)

            # Copy the run element into our new paragraph
            new_p.append(run._r)
            body.insert(idx, new_p)

            # Clear the placeholder text (keep paragraph for spacing)
            para.clear()
            for run in para.runs:
                run.text = ''
            print(f"  -> Image inserted.")
            break
    else:
        print(f"WARNING: placeholder not found for {fig_key}")

out = '/home/user/Skill/final_submission_PM_Bengaluru_v2.docx'
doc.save(out)
print(f"\nSaved: {out}")
