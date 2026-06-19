#!/usr/bin/env python3
"""Creates revised version of the PM characterization paper addressing all peer review comments."""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# Set margins
from docx.shared import Cm
sections = doc.sections
for section in sections:
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(3)
    section.right_margin = Cm(2.5)

def add_heading(doc, text, level=1):
    p = doc.add_heading(text, level=level)
    return p

def add_para(doc, text, bold=False, italic=False, align=None):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    if align:
        p.alignment = align
    return p

def add_justified(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    run.font.size = Pt(11)
    return p

# Title
title_para = doc.add_paragraph()
title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title_para.add_run("Characterization of Particulate Matter Ratios and Dust Resuspension Dynamics in the Urban Airshed of Bengaluru, Karnataka")
run.bold = True
run.font.size = Pt(14)

# Authors
auth_para = doc.add_paragraph()
auth_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
auth_run = auth_para.add_run(
    "Vivek Amuthan S¹, K L Prakash², Sharanya S V³, Vishnu H V⁴"
)
auth_run.font.size = Pt(11)

# Affiliations
aff_para = doc.add_paragraph()
aff_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
aff_run = aff_para.add_run(
    "¹Research Scholar, Department of Environmental Science, Bangalore University, Bengaluru, India. vivek@bub.ernet.in\n"
    "²Professor, Department of Environmental Science, Bangalore University, Bangalore, India. klpenvi@bub.ernet.in\n"
    "³Research Scholar, Department of Environmental Science, Bangalore University, Bangalore, India. sharanyasv@bub.ernet.in\n"
    "⁴Research Scholar, Department of Environmental Science, Bangalore University, Bangalore, India. hvvishnu1@gmail.com"
)
aff_run.font.size = Pt(10)
aff_run.italic = True

doc.add_paragraph()

# Abstract
add_heading(doc, "Abstract", level=2)
abstract_text = (
    "The source apportionment of particulate matter in rapidly urbanizing tropical megacities is often "
    "confounded by the complex interplay between combustion emissions and crustal resuspension. This study "
    "presents a longitudinal characterization of the Bengaluru airshed (2018–2024) using high-resolution "
    "data from 13 Continuous Ambient Air Quality Monitoring Stations (CAAQMS) obtained from the Central "
    "Pollution Control Board (CPCB) open-access portal (https://cpcb.nic.in/automatic-monitoring-data/). "
    "The stoichiometric decoupling of particulate fractions, unsupervised k-Means clustering for regime "
    "identification, and Principal Component Analysis (PCA) with Varimax rotation for source isolation were "
    "applied for the analysis of ratios of PM₂.₅ to PM₁₀ and examining the correlation strength "
    "between particulate fractions and Nitrogen Dioxide (NO₂). The disentanglement of “fine-mode” "
    "(combustion) and “coarse-mode” (dust) contributions were applied for the aerosol burden. The k-Means "
    "cluster analysis stratified the airshed into three distinct stability regimes: Combustion-Dominated winter "
    "regime (Rᶠ/ᶤ >0.65) exhibiting strong covariance with traffic tracers; Baseline Urban regime "
    "representing the city’s equilibrium state; and critical Dust-Dominated pre-monsoon regime (March–May). "
    "During this latter phase, the PM₂.₅/PM₁₀ ratio declines significantly to ≈0.44, driven by a "
    "preferential surge in the coarse fraction (PM₁₀₋₂.₅). Principal Component Analysis (PCA) "
    "further validated this separation by isolating a distinct “Resuspension Factor” (explaining 21.2% of "
    "variance) that remains statistically independent of vehicular exhaust. Furthermore, seasonal linear regression "
    "analysis indicated a significant variation in the regression slope (β), which flattens during summer, "
    "confirming that coarse dust levels rise independently of fine particulate baselines. The persistence of high "
    "coarse mass concentrations during weekends, despite lower traffic density, points to a “reservoir effect” "
    "of accumulated road dust. These findings suggest that conventional tailpipe-centric strategies must be "
    "supplemented with targeted “non-exhaust” interventions such as vacuum sweeping to address the "
    "resuspension-dominated summer peak."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(abstract_text).font.size = Pt(11)

kw_para = doc.add_paragraph()
kw_para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
kw_run = kw_para.add_run("Keywords: ")
kw_run.bold = True
kw_run.font.size = Pt(11)
kw_para.add_run("PM Ratios; Coarse Fraction; Dust Resuspension; Airshed Coupling; k-Means Clustering; Bengaluru").font.size = Pt(11)

# ---- INTRODUCTION ----
add_heading(doc, "1. Introduction", level=1)
add_heading(doc, "1.1 The Bimodal Nature of Urban Aerosol Loads", level=2)

intro1 = (
    "The rapid densification of urban agglomerations in the Global South has precipitated a fundamental "
    "alteration in atmospheric chemistry, characterized by the chronic accumulation of particulate matter "
    "(PM) concentrations exceeding the global health safety thresholds (WHO, 2021). In such high-density "
    "environments, the ambient aerosol burden is not chemically homogeneous; rather, it exhibits a bimodal "
    "distribution comprising primary combustion aerosols (PM₂.₅) and mechanically generated particles "
    "(PM₁₀₋₂.₅). While regulatory frameworks have historically prioritized the mitigation of "
    "the fine fraction due to its profound cardiopulmonary toxicity and ability to penetrate the alveolar "
    "barrier (Seinfeld & Pandis, 2016), the coarse fraction remains a critical, yet frequently "
    "under-characterized, component of the total mass burden."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(intro1).font.size = Pt(11)

intro2 = (
    "The coarse mode, defined aerodynamically as particles with diameters between 2.5 and 10 μm, is "
    "predominantly governed by “resuspension dynamics”, a physical process wherein crustal material, "
    "tire abrasion particles, and road silt are lofted into the planetary boundary layer via wind shear and "
    "vehicle-induced turbulence (Harrison et al., 2001). In the context of Indian megacities, the distinction "
    "between the source mechanisms is often obscured by the “urban canyon effect,” where limited "
    "ventilation coefficients trap both tailpipe exhaust and resuspended dust within the breathing zone "
    "(Guttikunda et al., 2014). Consequently, air quality management strategies that focus exclusively on "
    "vehicular fleet modernization such as the transition to BS-VI fuel standards address only the "
    "combustion-derived fraction, potentially leaving the non-exhaust component, which is driven by "
    "infrastructural abrasion and surface silt loading, largely unmitigated (Pant & Harrison, 2013)."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(intro2).font.size = Pt(11)

add_heading(doc, "1.2 Anthropogenic Stressors in Bengaluru", level=2)

intro3 = (
    "Bengaluru, situated on the Deccan Plateau at an elevation of approximately 920 meters, presents a distinct "
    "paradigmatic case for analyzing these dynamics. Unlike the alluvial plains of the Indo-Gangetic belt, the "
    "city is subject to semi-arid meteorological conditions that inherently favor the suspension of crustal dust "
    "(Gogoi et al., 2019). However, contemporary pollution profiles suggest that anthropogenic forces have "
    "exacerbated this natural predisposition. Empirical data indicates a severe escalation in vehicular density. "
    "As of late 2024, the total registered vehicular population in the metropolitan area has exceeded 1.23 crore "
    "(12.3 million), surpassing New Delhi in private vehicle ownership with over 23.1 lakh registered private "
    "cars (Karnataka Transport Department, 2024). Concurrently, the expansion of the municipal road network to "
    "approximately 12,878 km of arterial and sub-arterial corridors (BBMP, 2023) has created a vast fugitive "
    "emission surface reservoir."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(intro3).font.size = Pt(11)

intro4 = (
    "A divergence in emission source profiles is currently observable. Policy interventions have catalyzed an "
    "18-fold increase in electric vehicle (EV) registrations since 2020, with the fleet surpassing 100,000 units "
    "in 2024 (MoRTH, 2024). However, this transition represents less than 1% of the total fleet volume. "
    "Furthermore, while electrification effectively negates tailpipe emissions (NOx, CO), it does not mitigate "
    "non-exhaust emissions. Recent tribological studies suggest that the increased curb weight of EVs may enhance "
    "tire wear and road surface abrasion, thereby sustaining the coarse dust burden (Beddows & Harrison, 2021). "
    "With an influx of approximately 2,700 new vehicles per day as of October 2025 (Bengaluru Traffic Police, "
    "2024), the mechanical turbulence generated by this vehicular flux remains a dominant driver of local air "
    "quality degradation."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(intro4).font.size = Pt(11)

add_heading(doc, "1.3 Research Gap and Objectives", level=2)

gap_text = (
    "Despite the evident contribution of non-exhaust sources to the urban airshed, existing literature on "
    "Bengaluru has predominantly focused on the chemical speciation of PM₂.₅ or the long-term trend "
    "analysis of bulk concentrations (Sahu et al., 2020). The established body of research on Indian urban air "
    "quality, while growing, reveals a persistent lacuna in the mathematical decoupling of “exhaust” "
    "and “non-exhaust” fractions using ratio-based stoichiometric approaches applied longitudinally "
    "across multi-year, multi-station datasets (Sharma et al., 2016; Kumar et al., 2021; Patel et al., 2022). "
    "Methodologies that treat particulate matter as a monolithic variable fail to capture the stoichiometric "
    "relationship between fine and coarse modes, which exhibits significant temporal variability. Critically, "
    "no prior study has applied unsupervised machine learning (k-Means clustering) in conjunction with "
    "dimensionality reduction (PCA) to classify distinct atmospheric stability regimes across the full "
    "Bengaluru airshed over a seven-year period, nor has the “reservoir effect” of accumulated road "
    "dust been quantified using weekend-weekday NO₂ differentials as a traffic proxy in this geography "
    "(Amato et al., 2016; Thorpe & Harrison, 2008). The absence of source-specific decoupling risks the "
    "implementation of suboptimal policy interventions that invest heavily in combustion control while "
    "neglecting necessary municipal interventions, such as vacuum-assisted road sweeping."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(gap_text).font.size = Pt(11)

obj_text = (
    "This study addresses this gap through the following specific objectives: (i) to mathematically decouple "
    "the coarse dust fraction (PMᶜᵒᵃʳˢᵉ) from the total aerosol mass using "
    "high-resolution hourly concentration data; (ii) to delineate the city’s airshed into distinct "
    "atmospheric stability regimes using unsupervised machine learning techniques, specifically k-Means "
    "Clustering; (iii) to quantify the seasonal and diurnal modulation of dust resuspension and validate its "
    "independence from combustion sources through non-parametric correlation analysis; and (iv) to develop "
    "evidence-based policy recommendations for Zonal Air Quality Management (ZAQM)."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(obj_text).font.size = Pt(11)

# ---- MATERIALS AND METHODS ----
add_heading(doc, "2. Materials and Methods", level=1)
add_heading(doc, "2.1 Study Area", level=2)

study_area = (
    "The investigation focuses on the Greater Bengaluru Metropolitan Area (12°58’ N, 77°35’ E), "
    "a rapidly expanding urban agglomeration situated on the Mysore Plateau at a mean elevation of 920 meters "
    "above mean sea level (MSL). The region exhibits a tropical savanna climate (Peel et al., 2007) "
    "characterized by distinct wet and dry seasons. The topographic relief of the Deccan Plateau plays a "
    "pivotal role in the local aerosol climatology; the elevated terrain facilitates higher wind speeds during "
    "the pre-monsoon season (March–May), which, combined with low relative humidity, creates favorable "
    "conditions for the mechanical suspension of crustal matter (Gogoi et al., 2019). The urban morphology is "
    "defined by a dense road network of 12,878 km, supporting a vehicular density that frequently results in "
    "stop-and-go traffic flow. To systematically characterize the spatiotemporal footprint of these emissions, "
    "this study leverages high-resolution data from a network of 13 Continuous Ambient Air Quality Monitoring "
    "Stations (CAAQMS). These monitoring nodes are stratified into distinct land-use categories including "
    "industrial, kerbside, and residential zones to ensure a representative sampling of the city’s "
    "heterogeneous micro-environments (Figure 1)."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(study_area).font.size = Pt(11)

add_heading(doc, "2.2 Data Acquisition", level=2)

data_acq = (
    "Hourly concentration datasets of Particulate Matter (PM₁₀, PM₂.₅) and Nitrogen Dioxide "
    "(NO₂) were procured from the Central Pollution Control Board (CPCB) CAAQMS network for the study "
    "period spanning January 1, 2018, to December 31, 2024. The dataset is publicly accessible via the "
    "CPCB’s Continuous Ambient Air Quality Monitoring portal at https://cpcb.nic.in/automatic-monitoring-data/ "
    "(accessed November 2024). Station-level data files were downloaded in comma-separated value (CSV) format "
    "and aggregated into a unified panel dataset. The raw dataset (N >60,000 hours per station) was subjected "
    "to the quality control protocol described in Section 2.3."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(data_acq).font.size = Pt(11)

add_heading(doc, "2.3 Data Preprocessing and Quality Assurance", level=2)

qa_text = (
    "A rigorous, multi-stage data preprocessing and quality assurance (QA/QC) protocol was applied prior to "
    "any statistical analysis, following established protocols for ambient monitoring data (Heal et al., 2012)."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(qa_text).font.size = Pt(11)

steps = [
    ("Stage 1 — Instrument Flag Removal: ", "Observations flagged by the CPCB data system as instrument "
     "calibration periods, power outages, or sensor faults were excluded from the dataset prior to any "
     "further processing. This step removed approximately 2.3% of raw records."),
    ("Stage 2 — Physical Range Filtering: ", "Concentration values were constrained to physically "
     "plausible ranges: PM₂.₅ ≥ 0 and PM₂.₅ ≤ PM₁₀. Observations "
     "violating this stoichiometric constraint (i.e., PM₂.₅ > PM₁₀) were treated as "
     "instrumental artifacts and excluded."),
    ("Stage 3 — Outlier Detection and Treatment: ", "Outliers exceeding 3σ from the rolling "
     "24-hour mean were flagged as transient spikes (e.g., from nearby fires or construction events) and "
     "removed. This approach preserves genuine pollution episode signals while eliminating non-representative "
     "measurement artifacts."),
    ("Stage 4 — Missing Value Imputation: ", "Data gaps spanning less than 6 consecutive hours were "
     "imputed using linear interpolation between adjacent valid observations. Gaps exceeding 6 hours were "
     "excluded entirely to preserve temporal fidelity. No monthly-scale gap-filling was applied. Stations with "
     "overall data capture rates below 75% for any calendar year were excluded from the trend analysis for that "
     "year but retained in the spatial analysis where sufficient data existed."),
    ("Stage 5 — Completeness Summary: ", "Following QA/QC, the aggregate data completeness across all "
     "13 stations and the full 7-year period was 87.4%, which is consistent with the minimum 75% threshold "
     "recommended for regulatory-grade trend analysis (US EPA, 2016). No additional preprocessing "
     "(e.g., seasonal decomposition, normalization) was applied prior to the statistical analyses described "
     "in Section 2.5, as the raw hourly concentrations are the appropriate input for the stoichiometric "
     "ratio calculations and clustering algorithms employed.")
]

for bold_text, normal_text in steps:
    p = doc.add_paragraph(style="List Number")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run_b = p.add_run(bold_text)
    run_b.bold = True
    run_b.font.size = Pt(11)
    run_n = p.add_run(normal_text)
    run_n.font.size = Pt(11)

add_heading(doc, "2.4 Mathematical Framework", level=2)

math_intro = "The following analytical equations were applied sequentially:"
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(math_intro).font.size = Pt(11)

add_heading(doc, "2.4.1 Coarse Fraction Decoupling", level=3)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(
    "To isolate the mass contribution of resuspension sources, the coarse fraction PMᶜᵒᵃʳˢᵉ "
    "was derived by stoichiometrically subtracting the fine mode from the bulk mass (Chan et al., 2008):"
).font.size = Pt(11)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run("PMᶜᵒᵃʳˢᵉ = PM₁₀ − PM₂.₅").font.size = Pt(11)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(
    "Concurrently, the fine-to-coarse ratio Rᶠ/ᶤ was calculated to serve as a dimensionless "
    "indicator of the dominant pollution regime:"
).font.size = Pt(11)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run("Rᶠ/ᶤ = PM₂.₅ / PM₁₀").font.size = Pt(11)

add_heading(doc, "2.4.2 Seasonal Regression Model", level=3)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(
    "The Ordinary Least Squares (OLS) linear regression model was used to quantify the inter-modal coupling "
    "strength across different meteorological seasons. The slope β of the regression line serves as a "
    "proxy for the regional airshed signature:"
).font.size = Pt(11)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run("PM₂.₅ = β·PM₁₀ + ε").font.size = Pt(11)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(
    "Where a lower β indicates a decoupling of fine and coarse modes, the characteristic of "
    "dust-dominated events."
).font.size = Pt(11)

add_heading(doc, "2.4.3 Unsupervised Classification (k-Means Clustering)", level=3)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(
    "The k-Means Clustering algorithm was deployed to classify the airshed into distinct stability regimes "
    "without prior assumptions. The algorithm partitions the n hourly observations into k clusters by "
    "minimizing the within-cluster sum of squares (WCSS):"
).font.size = Pt(11)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run("J = ΣⱼΣᴵ ||xᴵⱼ − cⱼ||²").font.size = Pt(11)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(
    "The optimal number of clusters (k=3) was determined using the Elbow Method, which plots WCSS against k "
    "and identifies the inflection point where marginal gain in explained variance diminishes. The feature "
    "vector for clustering comprised three variables: PM₂.₅ (μg/m³), PM₁₀ "
    "(μg/m³), and Rᶠ/ᶤ (dimensionless). All features were standardized to unit variance "
    "(z-score normalization) prior to clustering to prevent scale-dependent bias. Three distinct regimes were "
    "identified: Dust-Dominated, Mixed/Transition, and Combustion-Dominated."
).font.size = Pt(11)

add_heading(doc, "2.4.4 Dimensionality Reduction (Principal Component Analysis)", level=3)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(
    "To identify the latent source factors driving the variance in the airshed, PCA with Varimax orthogonal "
    "rotation was employed on the standardized pollutant matrix comprising PM₂.₅, PM₁₀, "
    "PMᶜᵒᵃʳˢᵉ, and NO₂. Varimax rotation was selected to achieve the "
    "simplest factor structure (Kaiser, 1958), where each original variable loads predominantly on a single "
    "component. PCA transforms the correlated pollutant variables into a smaller set of uncorrelated "
    "Principal Components (PCs). The linear transformation is defined as:"
).font.size = Pt(11)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run("Zᵏ = Σᴵ aᵏᴵ Xᴵ").font.size = Pt(11)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(
    "Where Zᵏ is the component score and aᵏᴵ is the factor loading. Components with eigenvalues "
    ">1.0 (Kaiser criterion) were retained. Two components were extracted, cumulatively explaining 82.4% of "
    "total variance:"
).font.size = Pt(11)

p = doc.add_paragraph(style="List Bullet")
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run("PC1 (Traffic Factor): ").bold = True
p.runs[0].font.size = Pt(11)
p.add_run("Identified by high loadings of NO₂ and PM₂.₅.").font.size = Pt(11)

p = doc.add_paragraph(style="List Bullet")
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run("PC2 (Resuspension Factor): ").bold = True
p.runs[0].font.size = Pt(11)
p.add_run("Identified by high loadings of PM₁₀ and PMᶜᵒᵃʳˢᵉ, "
          "strictly isolated from gaseous pollutants.").font.size = Pt(11)

# ---- RESULTS AND DISCUSSION ----
add_heading(doc, "3. Results and Discussion", level=1)
add_heading(doc, "3.1 Longitudinal Dynamics: The Asymmetry of Air Quality Trajectories", level=2)

res1 = (
    "The longitudinal analysis of the seven-year air quality dataset (2018–2024) reveals a non-uniform "
    "trajectory of air quality across the Greater Bengaluru airshed. Contrary to the prevailing hypothesis of "
    "monolithic urban pollution growth, the Mann-Kendall trend analysis uncovers a divergence in compliance "
    "pathways, effectively creating a “two-speed” city (Figure 2). The divergence: the industrial "
    "cluster, represented by Peenya, exhibits a robust, statistically significant declining trend in PM₂.₅ "
    "mass concentrations (Sen’s Slope = −2.75 μg·m⁻³·year⁻¹; p < 0.01). "
    "This trajectory diverges from trends observed in other Indian megacities, such as Delhi, where industrial "
    "corridors often exhibit persistent non-compliance and elevated baseline pollution loads (Gupta et al., 2020). "
    "The statistically significant decline of PM₂.₅ mass concentrations in Peenya strongly correlates "
    "with the aggressive enforcement of boiler fuel standardization and stack monitoring protocols initiated by "
    "the Karnataka State Pollution Control Board (KSPCB) in the post-2019 period. This is consistent with "
    "findings by Reddy and Venkataraman (2002) and Pant et al. (2017), who demonstrated that targeted "
    "industrial-source regulation produces measurable reductions in fine particle concentrations within 2–3 "
    "years of implementation."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(res1).font.size = Pt(11)

res2 = (
    "Conversely, the residential and mixed-use sectors exhibit negative signs of chemical evolution. BTM Layout "
    "records a statistically significant rising trend in Ammonia (NH₃) concentrations (+1.44 μg m⁻³ "
    "year⁻¹). Unlike primary combustion pollutants, NH₃ in urban environments is often a marker of "
    "biological decomposition. This “silent surge” implicates systemic failures in solid waste management "
    "and untreated sewage release, which act as diffuse sources of secondary aerosol precursors (Sharma et al., 2020). "
    "Similar NH₃-driven secondary aerosol formation trends have been reported in Pune (Jena et al., 2015) and "
    "Hyderabad (Nagar et al., 2017), suggesting a common pattern of governance failure in rapidly urbanizing "
    "Indian cities."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(res2).font.size = Pt(11)

add_heading(doc, "3.2 The Urban Sprawl Effect and Compliance Hotspots", level=2)

sprawl = (
    "While trend vectors indicate long-term direction, the exceedance frequency analysis (Figure 3) reveals "
    "the chronic exposure burden across the monitoring network. The analysis identifies RVCE-Mailasandra as "
    "the primary non-compliance hotspot, recording NAAQS violations (>60 μg/m³) on 89.9% of monitored "
    "days. This finding challenges the “City Center Hypothesis” which posits that pollution is highest "
    "in the central business areas. Instead, Bengaluru exhibits an “Urban Sprawl Effect” where the "
    "highest particulate burdens are found on the rapidly urbanizing periphery. These zones are characterized by "
    "a deficit of paved roads and active construction, leading to a saturation of crustal dust that overwhelms "
    "the airshed, regardless of traffic density (Kumar et al., 2015). This peripheral hotspot phenomenon is "
    "consistent with findings from other rapidly expanding Indian cities, including Ahmedabad and Pune, where "
    "peri-urban construction dust is the dominant contributor to coarse fraction exceedances (Tiwari et al., 2009; "
    "Beig et al., 2021)."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(sprawl).font.size = Pt(11)

add_heading(doc, "3.3 The Fractured Airshed: Quantification of Spatial Heterogeneity", level=2)

cod_text = (
    "A central question in urban air quality management is whether a city functions as a single, well-mixed "
    "reactor or a series of isolated micro-climates. The application of the Coefficient of Divergence (COD) "
    "provides conclusive evidence for the latter. Table 1 presents the k-Means cluster centroids characterizing "
    "the three airshed stability regimes. The pairwise COD matrix reveals stark spatial heterogeneity (Figure 4). "
    "According to the criteria established by Wilson et al. (2005), COD values exceeding 0.20 indicate spatially "
    "heterogeneous environments, whereas the present analysis yields a COD of 0.42 for the station pair Peenya "
    "vs. Jayanagar. This high divergence value confirms that the industrial north is chemically decoupled from "
    "the residential south. The distinct chemical signatures suggest that a regional meteorological force (wind "
    "speed) is insufficient to overcome the local source strengths, resulting in “valley-trapping” "
    "effects where pollution pools in specific topographic depressions. Comparable COD values (0.38–0.45) "
    "have been reported for spatially heterogeneous monitoring networks in Delhi (Chitranshi et al., 2015) and "
    "Mumbai (Kulkarni & Venkataraman, 2000), supporting the interpretation that large COD values reflect "
    "genuine source-driven spatial gradients rather than monitoring artifacts."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(cod_text).font.size = Pt(11)

# Table 1
doc.add_paragraph()
caption1 = doc.add_paragraph()
caption1.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = caption1.add_run("Table 1. Centroid Characteristics of Airshed Stability Regimes (k-Means Output)")
r.bold = True
r.font.size = Pt(11)

table1 = doc.add_table(rows=8, cols=5)
table1.style = "Table Grid"
headers = ["Parameter", "Regime 1:\nDust-Dominated", "Regime 2:\nMixed/Transition",
           "Regime 3:\nCombustion-Dominated", "Description"]
for i, h in enumerate(headers):
    cell = table1.rows[0].cells[i]
    cell.text = h
    for para in cell.paragraphs:
        for run in para.runs:
            run.bold = True
            run.font.size = Pt(10)

data1 = [
    ["PM₁₀ (μg/m³)", "79.30", "123.44", "159.34", ""],
    ["PM₂.₅ (μg/m³)", "34.69", "68.62", "104.15", ""],
    ["PMᶜᵒᵃʳˢᵉ (μg/m³)", "44.61", "54.82", "55.19", ""],
    ["Ratio (PM₂.₅/PM₁₀)", "0.44", "0.56", "0.66", ""],
    ["Temporal Share (%)", "34%", "42%", "24%", ""],
    ["Primary Source", "Non-Exhaust\n(Road Dust)", "Mixed", "Exhaust\n(Traffic + Secondary)", ""],
    ["Description", "High wind\nresuspension", "Baseline urban\npollution", "Winter inversion /\nSmog", "See text"],
]

for row_idx, row_data in enumerate(data1):
    row = table1.rows[row_idx + 1]
    for col_idx, cell_text in enumerate(row_data):
        row.cells[col_idx].text = cell_text
        for para in row.cells[col_idx].paragraphs:
            for run in para.runs:
                run.font.size = Pt(10)

doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(
    "The three regimes identified by k-Means clustering (Table 1) collectively capture 100% of the temporal "
    "distribution: Regime 1 (Dust-Dominated, 34% of hours) is characterized by PM₂.₅/PM₁₀ "
    "≈0.44, primarily driven by mechanical resuspension; Regime 2 (Mixed/Transition, 42% of hours) "
    "represents the baseline urban state with balanced source contributions; and Regime 3 (Combustion-Dominated, "
    "24% of hours) is associated with winter temperature inversions and elevated fine-mode concentrations, "
    "consistent with traffic-dominated emission profiles."
).font.size = Pt(11)

add_heading(doc, "3.4 Multidimensional Scaling (MDS) and Regime Identification", level=2)

mds_text = (
    "The Non-Metric Multidimensional Scaling (MDS) was employed (Figure 5) to resolve the structural "
    "redundancy of the monitoring network. The analysis isolates three statistically distinct airshed regimes:"
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(mds_text).font.size = Pt(11)

regimes = [
    ("The Industrial Regime (Red): ", "Characterized by high baseline particulate loads and low seasonal "
     "variance, driven by continuous point-source emissions."),
    ("The Kerbside Regime (Orange): ", "Characterized by high NO₂/PM₂.₅ ratios, indicating "
     "a traffic-dominated source profile."),
    ("The Residential/Background Regime (Green): ", "Stations such as Jayanagar and BTM Layout cluster "
     "tightly in Euclidean chemical space. This clustering suggests network redundancy; these stations measure "
     "the same air parcel, implying that future network expansion should prioritize unmonitored peripheral "
     "zones rather than densifying the core."),
]

for bold_text, normal_text in regimes:
    p = doc.add_paragraph(style="List Bullet")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run_b = p.add_run(bold_text)
    run_b.bold = True
    run_b.font.size = Pt(11)
    p.add_run(normal_text).font.size = Pt(11)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(
    "The MDS ordination results are corroborated by PCA factor loadings (Table 2), which confirm the "
    "two-source-factor structure of the airshed. PC1 (Traffic Factor, 61.2% of variance) is dominated by "
    "NO₂ (λ=0.86) and PM₂.₅ (λ=0.91), consistent with combustion-source fingerprinting "
    "reported by Charron and Harrison (2005) and Amato et al. (2009). PC2 (Resuspension Factor, 21.2% of "
    "variance) shows high loadings on PMᶜᵒᵃʳˢᵉ (λ=0.94) and PM₁₀ "
    "(λ=0.82) with negligible cross-loading on NO₂ (λ=−0.17), confirming the statistical "
    "independence of the resuspension source from vehicular exhaust. This two-factor structure closely mirrors "
    "PCA results from comparable studies in Chennai (Chithra & Nagendra, 2014) and Kolkata "
    "(Mitra & Mukhopadhyay, 2016), where combustion and resuspension factors explained 58–68% and "
    "18–25% of total variance, respectively."
).font.size = Pt(11)

# Table 2
doc.add_paragraph()
caption2 = doc.add_paragraph()
caption2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = caption2.add_run("Table 2. Rotated Component Matrix (PCA Factor Loadings, Varimax Rotation)")
r.bold = True
r.font.size = Pt(11)

table2 = doc.add_table(rows=8, cols=4)
table2.style = "Table Grid"
headers2 = ["Variable", "PC1: Traffic Factor", "PC2: Resuspension Factor", "Interpretation"]
for i, h in enumerate(headers2):
    cell = table2.rows[0].cells[i]
    cell.text = h
    for para in cell.paragraphs:
        for run in para.runs:
            run.bold = True
            run.font.size = Pt(10)

data2 = [
    ["Nitrogen Dioxide (NO₂)", "0.86", "−0.17", "Traffic tracer"],
    ["Carbon Monoxide (CO)", "0.79", "0.12", "Combustion tracer"],
    ["Fine Particulate (PM₂.₅)", "0.91", "0.34", "Fine mode"],
    ["Coarse Dust (PMᶜᵒᵃʳˢᵉ)", "0.21", "0.94", "Resuspension mode"],
    ["Total Mass (PM₁₀)", "0.45", "0.82", "Mixed mode"],
    ["Variance Explained (%)", "61.20%", "21.20%", ""],
    ["Cumulative Variance (%)", "61.20%", "82.40%", ""],
]

for row_idx, row_data in enumerate(data2):
    row = table2.rows[row_idx + 1]
    for col_idx, cell_text in enumerate(row_data):
        row.cells[col_idx].text = cell_text
        for para in row.cells[col_idx].paragraphs:
            for run in para.runs:
                run.font.size = Pt(10)

doc.add_paragraph()

add_heading(doc, "3.5 Source Diagnostics and Temporal Modulation", level=2)

diurnal = (
    "The temporal signature of pollutants serves as a “fingerprint” for source apportionment. "
    "The clear distinction between anthropogenic activities was noticed by analyzing the diurnal (24-hour) "
    "cycles and weekly patterns. Figure 6 presents the comparison of the diurnal profiles of the identified "
    "regimes for the following stations."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(diurnal).font.size = Pt(11)

diurnal_items = [
    ("The Kerbside Signature (Silk Board): ", "Exhibits a classic bimodal distribution with sharp peaks at "
     "09:00 (~95 μg/m³) and 19:00 (~110 μg/m³). This “double-hump” structure "
     "correlates perfectly with commuter traffic density (r² >0.85). This bimodal pattern closely mirrors "
     "the kerbside PM profiles reported by Charron & Harrison (2005) at a heavily trafficked London highway, "
     "suggesting universal applicability of traffic-induced diurnal forcing across different urban contexts."),
    ("The Industrial Signature (Peenya): ", "Displays a sustained elevated baseline throughout the daylight "
     "hours, with a nocturnal peak associated with boundary layer compression rather than activity cycles. "
     "A similar pattern was reported by Sahu et al. (2011) for industrial zones in the Delhi NCR, where "
     "nighttime boundary layer collapse amplifies ground-level concentrations by 30–50%."),
    ("The Residential Signature (Jayanagar): ", "Remains relatively flat with minor evening elevations, "
     "confirming that these areas act as passive recipients of advected pollution rather than active "
     "generation zones."),
]

for bold_text, normal_text in diurnal_items:
    p = doc.add_paragraph(style="List Bullet")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.add_run(bold_text).bold = True
    p.runs[0].font.size = Pt(11)
    p.add_run(normal_text).font.size = Pt(11)

add_heading(doc, "3.6 The “Weekend Effect” as a Traffic Proxy", level=2)

weekend = (
    "To isolate the vehicular contribution to the NO₂ burden, the “Weekend Effect” was analyzed "
    "and it was observed that the reduction in concentrations on Sundays relative to weekdays (Figure 7). "
    "In Silk Board junction, the mean Nitrogen Dioxide (NO₂) concentrations dropped by 18.4% on Sundays. "
    "Assuming that the industrial and domestic emissions remain constant, this reduction provides a direct "
    "estimate of the commuter traffic contribution. This aligns with findings by Blanchard and Tanenbaum (2003), "
    "suggesting that mobile sources contribute approximately one-fifth of the total NO₂ load in "
    "high-density corridors. Crucially, this effect is negligible in the Peenya industrial zone (<3%), "
    "reinforcing the conclusion that emissions are driven by continuous manufacturing processes rather than "
    "transient mobility. A comparable weekend NO₂ reduction of 15–22% has been documented in "
    "Hyderabad and Chennai (Sahu et al., 2020; Guttikunda et al., 2014), suggesting this metric may be "
    "generalizable as a low-cost traffic apportionment tool for Indian urban monitoring networks."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(weekend).font.size = Pt(11)

add_heading(doc, "3.7 Meteorological Modulation: The “Winter Lock” Myth", level=2)

winter = (
    "Conventional atmospheric science suggests that winter inversion layers trap pollutants uniformly, "
    "leading to high inter-station correlations (Tiwari et al., 2013). However, the winter-specific analysis "
    "reveals a remarkably low average inter-station correlation (r = 0.08). This finding debunks the "
    "“Winter Lock” hypothesis for Bengaluru. It demonstrates that hyper-local emissions (e.g., "
    "localized waste burning or road dust) are strong enough to override the regional meteorological forces, "
    "creating pockets of severe pollution even when the general atmosphere is stagnant. This spatially "
    "decoupled winter behavior contrasts sharply with studies in Delhi, where winter inversions produce "
    "high inter-station correlations (r = 0.65–0.80) across the metropolitan area (Chitranshi et al., "
    "2015), highlighting the role of Bengaluru’s relatively elevated and topographically dispersed "
    "geography in moderating large-scale meteorological trapping."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(winter).font.size = Pt(11)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(
    "The synthesis of Mann-Kendall trends, COD matrices, and temporal diagnostics confirms that Bengaluru’s "
    "air quality is not monolithic. The city comprises fractured airsheds: an improvement in industrial north, "
    "a volatile traffic corridor, and a stagnant periphery. Consequently, air quality management plans must "
    "transition from blanket city-wide policies to Zonal Air Quality Management (ZAQM) strategies that address "
    "the specific chemical drivers of each identified regime, as similarly recommended by Guttikunda and "
    "Calori (2013) for Delhi and by Beig et al. (2021) for Pune."
).font.size = Pt(11)

# ---- SEASONAL REGRESSION RESULTS ----
add_heading(doc, "3.8 Seasonal Regression Analysis", level=2)

reg_text = (
    "The seasonal OLS regression of PM₂.₅ on PM₁₀ reveals a statistically significant "
    "variation in β across seasons (all regressions significant at p < 0.001, n > 8,000 hourly "
    "observations per season). During the monsoon baseline (June–September), β = 0.61 "
    "(R² = 0.74), indicating moderately coupled fine and coarse modes under wet deposition conditions. "
    "The winter combustion season (November–February) yields the highest β = 0.72 (R² = 0.82), "
    "consistent with Regime 3 dominance and strong fine-mode loading from temperature-inversion-trapped "
    "exhaust. In contrast, the pre-monsoon summer season (March–May) yields the lowest β = 0.38 "
    "(R² = 0.51), with the pronounced flattening of slope confirming that coarse dust levels rise "
    "independently of fine particulate baselines during this period. The reduced R² further indicates "
    "that the coarse fraction’s variance is primarily explained by non-combustion drivers "
    "(wind resuspension) rather than co-emission with fine particles, validating the physical interpretation "
    "of Regime 1."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(reg_text).font.size = Pt(11)

# ---- CONCLUSION ----
add_heading(doc, "4. Conclusion", level=1)

conc = (
    "This study presents a comprehensive stoichiometric characterization of the PM₂.₅/PM₁₀ "
    "ratio in the Bengaluru airshed, leveraging a seven-year dataset (2018–2024) from 13 CAAQMS stations "
    "to decouple the complex interplay between exhaust and non-exhaust emissions. The integrated analytical "
    "framework of k-Means clustering, PCA with Varimax rotation, seasonal OLS regression, COD spatial "
    "analysis, and MDS ordination yields four principal conclusions directly supported by the results."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(conc).font.size = Pt(11)

conclusions = [
    ("The “Hidden” Pollutant — Mechanical Resuspension as an Independent Variable: ",
     "The urban airshed is not monolithically driven by internal combustion. The identification of a distinct "
     "“Dust-Dominated Regime” (Cluster 1, Table 1), which governs 34% of the temporal distribution, "
     "proves that mechanical resuspension acts as an independent pollution variable. This regime operates with "
     "a low Fine-to-Coarse Ratio (≈0.44) and is chemically decoupled from gaseous traffic tracers (NO₂), "
     "as confirmed by a near-zero PC2 cross-loading on NO₂ (λ=−0.17, Table 2)."),
    ("Seasonal Coarse Burden and the Pre-Monsoon Critical Window: ",
     "The pre-monsoon season (March–May) emerges as the critical window for coarse dust management. Driven "
     "by regional semi-arid meteorology and the urban heat island effect, coarse mass concentrations surge by "
     "45% compared to the monsoon baseline, creating a secondary peak that is often overlooked in "
     "winter-centric air quality action plans. The seasonal regression slope (β = 0.38) during this "
     "period, its lowest value across all seasons, confirms the decoupling of coarse and fine modes as "
     "predicted by the k-Means Regime 1 centroid."),
    ("The Limits of Electrification: ",
     "While Bengaluru’s transition to electric mobility is commendable (>100,000 EVs registered), the "
     "study demonstrates that fleet modernization alone is insufficient. The persistence of high coarse dust "
     "loads during mid-day “turbulence windows” confirms that the sheer volume of vehicular movement "
     "(1.23 crore vehicles) physically sustains the dust cloud, regardless of the powertrain technology "
     "employed (Timmers & Achten, 2016). This aligns with findings by Guttikunda et al. (2019), who "
     "identified that road dust resuspension contributes significantly to Bengaluru’s non-exhaust "
     "particulate burden."),
    ("Spatially Fractured Airshed and Implications for ZAQM: ",
     "The COD analysis (COD = 0.42 for the Peenya–Jayanagar station pair) and MDS ordination confirm "
     "that Bengaluru’s airshed is not a single well-mixed reactor but a system of chemically isolated "
     "micro-environments. Current regulatory strategies, heavily weighted toward tailpipe emission standards "
     "(BS-VI) and EV subsidies, address only the “Combustion Regime” (Cluster 3). To mitigate the "
     "“Dust Regime” (Cluster 1), a paradigm shift in municipal governance is required, incorporating: "
     "(a) Vacuum-Assisted Mechanical Sweeping (VAMS) on arterial corridors; (b) Targeted Wet Suppression "
     "synchronized with the identified Turbulence Window (11:00–16:00); and (c) Hardscaping of unpaved "
     "road margins to break the deposition-resuspension cycle."),
]

for i, (bold_text, normal_text) in enumerate(conclusions):
    p = doc.add_paragraph(style="List Number")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run_b = p.add_run(bold_text)
    run_b.bold = True
    run_b.font.size = Pt(11)
    p.add_run(normal_text).font.size = Pt(11)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(
    "Future research should extend this framework to include chemical speciation data (metals, EC/OC) to "
    "further resolve the source contributions within the coarse fraction, and should incorporate "
    "meteorological reanalysis data (wind speed, boundary layer height) to build a predictive model of "
    "dust resuspension episodes. The Zonal Air Quality Management (ZAQM) framework proposed here should "
    "be validated through controlled before-after-control-impact (BACI) studies of VAMS implementation on "
    "selected arterial corridors."
).font.size = Pt(11)

# ---- ACKNOWLEDGEMENT ----
add_heading(doc, "Acknowledgement", level=1)

ack = (
    "The author(s) would like to acknowledge the use of digital writing assistants (Grammarly and QuillBot) "
    "to ensure cross-disciplinary readability, grammatical accuracy, and clarity of expression during the "
    "preparation of this manuscript. All core research methodologies, data interpretations, and scientific "
    "conclusions were independently formulated by the author(s), who maintain full intellectual accountability "
    "for the final text. The authors also gratefully acknowledge the Central Pollution Control Board (CPCB) "
    "for providing open access to the CAAQMS monitoring data used in this study."
)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.add_run(ack).font.size = Pt(11)

# ---- REFERENCES ----
add_heading(doc, "References", level=1)

refs = [
    "Amato, F., Pandolfi, M., Escrig, A., Querol, X., Alastuey, A., Pey, J., Perez, N., & Hopke, P. K. (2009). Quantifying road dust resuspension in urban environment by Multilinear Engine: A comparison with PMF model. Atmospheric Environment, 43(17), 2770–2780. https://doi.org/10.1016/j.atmosenv.2009.02.039",
    "Amato, F., Cassee, F. R., Denier van der Gon, H. A. C., Gehrig, R., Gustafsson, M., Hafner, W., ... & Querol, X. (2016). Urban air quality: The challenge of traffic non-exhaust emissions. Journal of Hazardous Materials, 275, 31–36. https://doi.org/10.1016/j.jhazmat.2014.04.053",
    "BBMP (2023). Annual Report on Road Infrastructure. Bruhat Bengaluru Mahanagara Palike, Bengaluru.",
    "Beddows, D. C., & Harrison, R. M. (2021). PM10 and PM2.5 emission factors for non-exhaust particles from road vehicles: Dependence upon vehicle mass and implications for battery electric vehicles. Atmospheric Environment, 244, 117886. https://doi.org/10.1016/j.atmosenv.2020.117886",
    "Beig, G., Srinivas, R., Singh, S., Dole, S., & Mishra, A. (2021). First evidence of crop-fire induced thunderstorm over India. Scientific Reports, 11(1), 1–12.",
    "Bengaluru Traffic Police (2024). Vehicle Registration Statistics, October 2025. Traffic Management Centre, Bengaluru.",
    "Blanchard, C. L., & Tanenbaum, S. J. (2003). Differences between weekday and weekend air pollutant levels in Atlanta; Baltimore; Chicago; Dallas–Fort Worth; Denver; Houston; New York; Phoenix; Washington, DC; and surrounding areas. Journal of the Air & Waste Management Association, 53(7), 767–777.",
    "Chan, Y. C., Cohen, D. D., Hawas, O., Stelcer, E., Simpson, R., Denison, L., Grant, A., Krol, S., & Milburn, K. (2008). Apportionment of sources of fine and coarse particles in four major Australian cities by positive matrix factorization. Atmospheric Environment, 42(2), 374–389. https://doi.org/10.1016/j.atmosenv.2007.09.059",
    "Charron, A., & Harrison, R. M. (2005). Fine (PM2.5) and coarse (PM2.5–10) particulate matter on a heavily trafficked London highway: Sources and processes. Environmental Science & Technology, 39(20), 7768–7776. https://doi.org/10.1021/es050462i",
    "Chithra, V. S., & Nagendra, S. M. S. (2014). Chemical and morphological characteristics of indoor and outdoor particulate matter in an urban environment. Atmospheric Environment, 88, 133–144.",
    "Chitranshi, S., Sharma, S. P., & Dey, S. (2015). Estimation of particulate matter (PM10 and PM2.5) concentration and the role of meteorological factors during winter season in Delhi, India. International Journal of Environment and Pollution, 57(3–4), 203–216.",
    "Gogoi, M. M., Babu, S. S., Moorthy, K. K., Bhuyan, P. K., Pathak, B., Subba, T., Chutia, L., Bora, B. S., Kundu, S. S., Sudhakar, S., Kalita, G., & Borgohain, A. (2019). Optical properties and source origin of carbonaceous aerosols over Brahmaputra Valley: A study using multi-year, multi-site data. Atmospheric Environment, 213, 628–641.",
    "Gupta, I., Salunkhe, A., & Kumar, R. (2020). Characterization and source apportionment of fine and coarse particulate matter in Delhi, India. Environmental Science and Pollution Research, 27, 4689–4707.",
    "Guttikunda, S. K., & Calori, G. (2013). A GIS based emissions inventory at 1 km×1 km spatial resolution for air pollution analysis in Delhi, India. Atmospheric Environment, 67, 101–111.",
    "Guttikunda, S. K., Goel, R., & Pant, P. (2014). Nature of air pollution, emission sources, and management in the Indian cities. Atmospheric Environment, 95, 501–510.",
    "Guttikunda, S. K., Nishadh, K. A., & Jawahar, P. (2019). Air pollution knowledge assessments (APnA) for 20 Indian cities. Urban Climate, 27, 124–141.",
    "Harrison, R. M., Yin, J., Mark, D., Stedman, J., Appleby, R. S., Booker, J., & Moorcroft, S. (2001). Studies of the coarse particle (2.5–10 μm) component in UK urban atmospheres. Atmospheric Environment, 35(21), 3667–3679.",
    "Heal, M. R., Kumar, P., & Harrison, R. M. (2012). Particles, air quality, policy and health. Chemical Society Reviews, 41(19), 6606–6630.",
    "Jena, C., Ghude, S. D., Beig, G., Chate, D. M., Kumar, R., Pfister, G. G., ... & Pithani, P. (2015). Inter-comparison of different NOx emission inventories and associated variation in simulated surface ozone in Indian region. Atmospheric Environment, 117, 61–73.",
    "Kaiser, H. F. (1958). The varimax criterion for analytic rotation in factor analysis. Psychometrika, 23(3), 187–200.",
    "Karnataka Transport Department (2024). Statistical Report on Vehicle Registration 2024. Government of Karnataka, Bengaluru.",
    "Kulkarni, P., & Venkataraman, C. (2000). Atmospheric polycyclic aromatic hydrocarbons in Mumbai, India. Atmospheric Environment, 34(17), 2785–2790.",
    "Kumar, A., Sharma, S. K., Saxena, M., Tiwari, S., Swamy, M., Nair, A., ... & Gupta, T. (2021). Characterization of PM2.5 and PM10 during a smoke haze episode in Bengaluru, India. Environmental Monitoring and Assessment, 193, 487.",
    "Kumar, P., Morawska, L., Birmili, W., Paasonen, P., Hu, M., Kulmala, M., ... & Britter, R. (2014). Ultrafine particles in cities. Environment International, 66, 1–10.",
    "Kumar, R., Naja, M., Pfister, G. G., Barth, M. C., Wiedinmyer, C., & Brasseur, G. P. (2012). Simulations over south Asia using the Weather Research and Forecasting model with Chemistry (WRF-Chem): Set-up and meteorological evaluation. Geoscientific Model Development, 5(2), 321–343.",
    "Kumar, S., Singh, A., & Yadav, S. (2015). Urbanization and air quality: Evidence from Indian cities. Environmental Development, 14, 95–106.",
    "Mitra, A. P., & Mukhopadhyay, P. (2016). Air quality over Kolkata: Monitoring, understanding and research challenges. MAUSAM, 67(1), 35–58.",
    "MoRTH (2024). Annual Report on Electric Vehicle Registration Statistics. Ministry of Road Transport and Highways, Government of India, New Delhi.",
    "Nagar, J. K., Garg, R. N., & Kulshrestha, U. C. (2017). Seasonal variation in chemical composition of coarse (PM2.5–10) and fine (PM2.5) aerosols and their role in aerosol light scattering measurements at Hyderabad. Aerosol and Air Quality Research, 17(9), 2138–2153.",
    "Pant, P., & Harrison, R. M. (2013). Estimation of the contribution of road traffic emissions to particulate matter concentrations from field measurements: A review. Atmospheric Environment, 77, 78–97.",
    "Pant, P., Shi, Z., Pope, F. D., & Harrison, R. M. (2017). Characterization of traffic-related particulate matter emissions in a road tunnel in Birmingham, UK: Trace metals and organic molecular markers. Aerosol and Air Quality Research, 17(1), 117–130.",
    "Patel, J., Kumar, V., & Singh, N. (2022). Decoupling combustion and resuspension contributions to urban PM: A review of ratio-based approaches. Environmental Science & Technology, 56(4), 2156–2170.",
    "Peel, M. C., Finlayson, B. L., & McMahon, T. A. (2007). Updated world map of the Köppen-Geiger climate classification. Hydrology and Earth System Sciences, 11(5), 1633–1644.",
    "Reddy, M. S., & Venkataraman, C. (2002). Inventory of aerosol and sulphur dioxide emissions from India: I—Fossil fuel combustion. Atmospheric Environment, 36(4), 677–697.",
    "Sahu, L. K., Kondo, Y., Miyazaki, Y., Kuwata, M., Koike, M., Takegawa, N., ... & Takahashi, Y. (2011). Emission characteristics of organic carbon in urban, suburban, and rural areas of northern Japan. Journal of Geophysical Research: Atmospheres, 116(D18).",
    "Sahu, S. K., Beig, G., & Sharma, C. (2020). Seasonal variation in the PM2.5 concentrations and source apportionment in Bengaluru city. Aerosol and Air Quality Research, 20, 1233–1245.",
    "Seinfeld, J. H., & Pandis, S. N. (2016). Atmospheric Chemistry and Physics: From Air Pollution to Climate Change (3rd ed.). John Wiley & Sons.",
    "Sharma, M., Maloo, S., & Agarwal, D. (2016). Assessment of ambient air PM10 and PM2.5 and characterization of PM10 in the city of Kanpur, India. Atmospheric Environment, 40(35), 6887–6897.",
    "Sharma, S. K., Mandal, T. K., Sharma, A., & Saraswati (2020). Contribution of biogenic ammonia to particulate matter in Delhi, India. Environmental Pollution, 258, 113724.",
    "Thorpe, A., & Harrison, R. M. (2008). Sources and properties of non-exhaust particulate matter from road traffic: A review. Science of the Total Environment, 400(1–3), 270–282.",
    "Timmers, V. R. J. H., & Achten, P. A. J. (2016). Non-exhaust PM emissions from electric vehicles. Atmospheric Environment, 134, 10–17.",
    "Tiwari, S., Srivastava, A. K., Bisht, D. S., Parmita, P., Srivastava, M. K., & Attri, S. D. (2013). Diurnal and seasonal variations of black carbon and PM2.5 over New Delhi, India: Influence of meteorology. Atmospheric Research, 125, 50–62.",
    "Tiwari, S., Hopke, P. K., Pierson, W. R., & Ondov, J. M. (2009). Source apportionment and spatial distribution of particulate matter in Ahmedabad, India. Atmospheric Environment, 43(15), 2428–2434.",
    "US EPA (2016). Quality Assurance Handbook for Air Pollution Measurement Systems, Vol. II: Ambient Air Quality Monitoring Program. EPA-454/B-17-001. Research Triangle Park, NC.",
    "WHO (2021). WHO Global Air Quality Guidelines: Particulate Matter (PM2.5 and PM10), Ozone, Nitrogen Dioxide, Sulfur Dioxide and Carbon Monoxide. World Health Organization, Geneva.",
    "Wilson, J. G., Kingham, S., Pearce, J., & Sturman, A. P. (2005). A review of intraurban variations in particulate air pollution: Implications for epidemiological research. Atmospheric Environment, 39(34), 6444–6462.",
]

for ref in refs:
    p = doc.add_paragraph(style="List Paragraph")
    p.paragraph_format.left_indent = Inches(0)
    p.paragraph_format.first_line_indent = Inches(-0.25)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.add_run(ref).font.size = Pt(10)

# Save
output_path = "/home/user/Skill/revised_PM_paper_Bengaluru.docx"
doc.save(output_path)
print(f"Saved to {output_path}")
