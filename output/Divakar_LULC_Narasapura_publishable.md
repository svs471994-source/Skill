# Land Use–Land Cover Change and Peri-Urban Sprawl in the Narasapura Industrial Corridor, Kolar District, Karnataka: A Two-Decade Geospatial Assessment (2004–2024)

**Divakar G**, Department of Environmental Science, Bangalore University, Bengaluru – 560 056, Karnataka, India

**Correspondence:** Dr. Hemanjali A.M., Department of Environmental Science, Bangalore University, Jnanabharathi Campus, Bengaluru – 560 056. Email: hemanjalidoli@gmail.com

---

## Abstract

**Background:** Industrial corridor development in peri-urban South Asia produces rapid and often irreversible land cover transitions, yet multi-temporal assessments covering full two-decade trajectories remain scarce for Karnataka's emerging industrial nodes.

**Methods:** Multi-temporal IRS Resourcesat-1 (2004), Resourcesat-2 (2014), and Resourcesat-2A (2024) multispectral imagery was subjected to supervised Maximum Likelihood Classification (MLC) within a GIS framework for a 213.75 km² study domain encompassing the Narasapura Industrial Area and its 5 km buffer, Kolar district. Eight land cover classes were delineated under the NRSC Level-II scheme. Accuracy was validated against 212 stratified random ground-truth points through confusion matrix analysis; Kappa coefficient and User/Producer accuracies were computed for each class. Peri-urban sprawl morphology was characterised qualitatively and corroborated through GPS-georeferenced field validation.

**Results:** The classification achieved an overall accuracy of 96.81% and a Kappa coefficient of 0.968. Built-up land expanded from 1.3% (2.87 km²) in 2004 to 8.9% (18.99 km²) in 2014, and to 17.3% (36.97 km²) in 2024 — a net gain of 34.10 km² (+1,188%) over the study period. Agricultural plantation contracted from 38.6% (82.49 km²) to 14.2% (30.47 km²), representing a net loss of 52.02 km². Waterbody coverage collapsed from 6.0% (12.74 km²) to 0.4% (0.86 km²) by 2014 before partially recovering to 4.5% (9.49 km²) by 2024 through state-led lake rejuvenation. Three distinct sprawl morphologies — ribbon sprawl along NH-75, cluster sprawl around KIADB estate nodes, and leapfrog sprawl in peripheral villages — were identified.

**Conclusion:** The Narasapura corridor has undergone a structurally irreversible transition from an agrarian to a peri-urban industrial landscape within two decades, driven by Karnataka Industrial Policy and the Bengaluru–Chennai Industrial Corridor (BCIC). The fragmentation of agricultural land, suppression of groundwater recharge, and hydrological disruption to traditional tank systems constitute quantifiable environmental costs requiring integrated spatial governance and ecological buffer enforcement.

**Keywords:** Land Use Land Cover; Peri-Urban Sprawl; IRS Resourcesat; KIADB; Supervised Classification; Kappa Accuracy; Karnataka Industrial Corridor; Geospatial Assessment

---

## 1. Introduction

### 1.1 The Global and National Context of Industrial Land Conversion

Land use and land cover (LULC) change is among the most consequential anthropogenic interventions in terrestrial systems, mediating surface hydrology, microclimate, biodiversity, and ecosystem services (Turner et al., 2007; Lambin & Geist, 2006). Over 75% of Earth's ice-free land surface has been significantly modified by human activity, with industrial development and associated peri-urban expansion constituting an accelerating driver in lower-middle-income economies (IPBES, 2019; World Bank, 2021). The IPCC (2021) identifies peri-urban land conversion as a cross-cutting stressor that simultaneously exacerbates urban heat islands, habitat fragmentation, greenhouse gas emissions, and flood risk.

In India, the built-up area expanded by 54.5% between 1990 and 2020, with a disproportionate share attributable to industrial and logistics land uses rather than residential growth alone (NRSC, 2021). Industrial belts associated with Special Economic Zones and National Industrial Corridors have accelerated this conversion at the urban–rural fringe, often bypassing formal planning safeguards (MoEFCC, 2023). The Ministry of Environment, Forest and Climate Change estimates that more than 10,000 hectares of forest and agricultural land have been diverted to industrial uses in the past two decades, with cascading consequences for surface runoff, groundwater recharge, and livelihoods (MoEFCC, 2023).

### 1.2 The Narasapura Industrial Corridor: A Transformation Node

Karnataka has experienced marked LULC change over the past four decades, with built-up areas in the Bengaluru Metropolitan Region expanding by over 584% between 1973 and 2013 while forest cover declined from 20.2% to 14.6% (Ramachandra et al., 2014). Within Kolar district, the Narasapura Industrial Area has become a focal node of this transformation following its designation as a priority growth hub under the Karnataka Industrial Areas Development Board (KIADB) and subsequent development under the Bengaluru–Chennai Industrial Corridor (BCIC) framework. Between 2000 and 2020, built-up land in Kolar district increased by over 200%, while agricultural land declined by more than 15% in the vicinity of industrial clusters (Ravindra et al., 2021; Prakash & Sudhira, 2016).

The entry of anchor industries — Honda Motorcycle and Scooter India (HMSI), Mahindra Aerospace, Volvo Bus, Scania, and Wistron/Tata Electronics — transformed the region's economic geography and land market dynamics. Despite this magnitude of change, a comprehensive multi-temporal geospatial assessment covering the full 2004–2024 arc has not previously been published for the Narasapura corridor.

### 1.3 Research Objectives

Two specific objectives structure this investigation:

1. To analyse and classify LULC changes in the Narasapura Industrial Area and its 5 km buffer for 2004, 2014, and 2024 using supervised geospatial classification, and to quantify the magnitude and direction of two-decade transitions.
2. To assess peri-urban sprawl morphology and document the environmental consequences of industrial expansion within the study domain.

---

## 2. Materials and Methods

### 2.1 Study Area

The study domain encompasses the Narasapura Industrial Area, Kolar district, Karnataka (approximately 13.1°N, 77.7°E), and a 5 km buffer, yielding a total analytical area of 213.75 km². The region falls within the Bengaluru Metropolitan Region Development Authority (BMRDA) planning periphery and is traversed by National Highway 75 (Bengaluru–Kolar corridor). Elevation ranges from 844 m to 1,154 m above mean sea level, with the central industrial zone occupying relatively flat terrain (870–920 m). Soils are predominantly Kandic Paleustalfs and Rhodic Kandustalfs, historically supporting millet, groundnut, and horticultural plantation cultivation.

**Figure 1** | *Location map of the Narasapura Industrial Area and its 5 km buffer zone, Kolar district, Karnataka. The study domain encompasses 213.75 km² across an elevation range of 844–1,154 m a.m.s.l. NH-75 traverses the central corridor from west to east.*

**Figure 2** | *Topographic map of the study area derived from SRTM DEM data. The central industrial zone (Narasapura–Vadagur–Appasandra) occupies flat terrain at 870–920 m; elevated hillocks (>1,000 m) in the northeast and east restrict industrial development and function as ecological buffer zones.*

### 2.2 Satellite Data and Image Processing

Multi-temporal multispectral imagery from three IRS Resourcesat sensors was acquired for this study: Resourcesat-1 LISS-III (2004), Resourcesat-2 LISS-IV (2014), and Resourcesat-2A LISS-IV (2024). Data products were sourced from KSRSAC. Preprocessing included radiometric correction to Top-of-Atmosphere (TOA) reflectance, geometric registration to WGS84/UTM projection (Zone 43N), and atmospheric correction.

| Sensor | Year | Spatial Resolution | Bands Used |
|---|---|---|---|
| IRS Resourcesat-1 LISS-III | 2004 | 23.5 m | Green, Red, NIR, SWIR |
| IRS Resourcesat-2 LISS-IV | 2014 | 5.8 m | Green, Red, NIR |
| IRS Resourcesat-2A LISS-IV | 2024 | 5.8 m | Green, Red, NIR |

*Table 1: Satellite data specifications.*

### 2.3 Classification Methodology

Supervised Maximum Likelihood Classification (MLC) was applied to all three image epochs within ERDAS Imagine and ArcGIS platforms, following the NRSC Level-II classification scheme. Eight land cover classes were delineated: Agricultural Plantation, Barren Rocky/Stony Waste, Built-up Land, Crop Land, Forest Plantation, Land with Scrub, Scrub Forest, and Water Bodies. Training samples were collected from field reconnaissance, Google Earth high-resolution imagery, and existing KSRSAC thematic maps.

The classification workflow proceeded from band composite generation → training sample collection → MLC execution → post-classification filtering (3×3 majority filter) → accuracy assessment → change detection. Supplementary ancillary data (SRTM DEM for slope and drainage extraction, KSRSAC soil survey data) informed class delineation in terrain-ambiguous zones.

**Figure 3** | *Supervised classification workflow applied to IRS Resourcesat imagery for all three study epochs. Training samples were drawn from ground-truth points, Google Earth imagery, and KSRSAC thematic maps, with post-classification 3×3 majority filtering applied before accuracy assessment.*

**Figure 4** | *Flowchart of the LULC mapping methodology, illustrating the sequence from satellite data ingestion through preprocessing, supervised classification, accuracy assessment, and change detection analysis.*

### 2.4 Accuracy Assessment

Accuracy was assessed for the 2024 LULC map — the terminal epoch — against 212 stratified random test points cross-validated against contemporaneous Google Earth imagery and KSRSAC reference data. The same classification procedure was applied consistently across all three epochs; accuracy for 2004 and 2014 is therefore assumed to be of comparable order (Roy et al., 2015). The confusion matrix yielded User Accuracy (commission error), Producer Accuracy (omission error), and the Kappa coefficient following standard formulae (Olofsson et al., 2014; Pontius & Millones, 2011).

### 2.5 Peri-Urban Sprawl Analysis

Sprawl morphology was characterised from the 2004–2024 LULC change layers and corroborated through GPS-georeferenced field validation across 56 waypoints. Three canonical sprawl typologies — ribbon, cluster, and leapfrog — were evaluated against the spatial distribution of built-up land gains in relation to the NH-75 corridor, KIADB estate boundaries, and peripheral village boundaries.

---

## 3. Results and Discussion

### 3.1 Biophysical Baseline: Terrain, Soil, and Drainage Characteristics

The spatial distribution of biophysical constraints exerts a strong conditioning influence on land conversion trajectories in the study area. Soil mapping reveals a dominance of Kandic Paleustalfs in the central zone (Vemgal, Vadagur, Appasandra), soils that historically supported high-value millet and groundnut cultivation and are now preferentially targeted for industrial and residential conversion given their constructibility. Rocky and shallow Typic Ustorthents near Budigere cross and Gollahalli, by contrast, constrain development and have consequently remained largely in non-agricultural use.

**Figure 5** | *Soil characteristics map of the Narasapura Industrial Area and its 5 km buffer. Kandic Paleustalfs dominate the central zone, historically supporting millet and groundnut cultivation. Rocky land (Typic Ustorthents) near Budigere cross limits agricultural and industrial development. Soil diversity explains the region's differential vulnerability to land conversion.*

Elevation ranges from 844 m to 1,154 m, with flat terrain (0–2°) in the industrial core facilitating large-scale development, while moderately sloping zones (4–9°) support agriculture and peri-urban expansion, and steep slopes (>18°) in the northeast function as erosion-prone zones best conserved under green cover. The dendritic drainage network, fed by seasonal first- to third-order streams, terminates in traditional tank irrigation systems — Vokkaleri Lake, Tekal Lake, Vemgal Kere, and Bendiganahalli — that historically sustained the agrarian economy and that now face disruption from industrial impervious surfaces.

**Figure 6** | *Digital Elevation Model (DEM) of the Narasapura Industrial Area and its 5 km buffer (844–1,154 m a.m.s.l.). The central industrial zone lies at 870–920 m, facilitating infrastructure development. Eastern and northeastern hillocks (>1,000 m) restrict dense development and maintain natural drainage functions.*

**Figure 7** | *Slope classification map (degrees) of the study area. Flat to gently sloping terrain (0–4°) in the central and western sectors favours industrial and urban expansion. Steeper slopes (8–36°) near Budigere Cross and Bendiganahalli form ecological buffer zones prone to erosion if disturbed.*

**Figure 8** | *Drainage network map of the Narasapura Industrial Area and its 5 km buffer. The dendritic drainage pattern feeds traditional tank systems (Vokkaleri Lake, Tekal Lake, Vemgal Kere) critical for groundwater recharge and irrigation. Industrial expansion disrupts natural runoff pathways and threatens tank inflows.*

### 3.2 LULC Classification Results: 2004, 2014, and 2024

#### 3.2.1 Pre-Industrial Baseline (2004)

In 2004, the study domain was overwhelmingly agrarian. Crop land and agricultural plantation together constituted 85.3% of the total area (97.73 km² and 82.49 km² respectively), reflecting an economy organised around millet, groundnut, paddy, coconut, arecanut, and mango cultivation. Waterbodies accounted for 6.0% (12.74 km²), representing major traditional irrigation tanks. Built-up land was restricted to 1.3% (2.87 km²), confined to existing village settlements and pre-industrial roadside nodes. This baseline validates the pre-industrial rural character of the region before KIADB's systematic land acquisition programme.

**Figure 9** | *LULC map of the Narasapura Industrial Area and its 5 km buffer, 2004 (IRS Resourcesat-1 LISS-III). Cropland and agricultural plantation together constitute 85.3% of the study domain. Built-up land is restricted to 1.3%, concentrated at village settlements and nascent NH-75 roadside nodes. Waterbodies at 6.0% reflect intact traditional tank irrigation systems.*

| LULC Class | Area (km²) | Area (%) |
|---|---|---|
| Agricultural Plantation | 82.49 | 38.6 |
| Barren Rocky/Stony Waste | 7.30 | 3.4 |
| Built-up Land | 2.87 | 1.3 |
| Crop Land | 97.73 | 46.7 |
| Forest Plantation | 4.56 | 2.1 |
| Land with Scrub | 2.07 | 1.0 |
| Scrub Forest | 3.99 | 1.9 |
| Water Bodies | 12.74 | 6.0 |
| **Total** | **213.75** | **100.0** |

*Table 2: LULC classification of Narasapura Industrial Area and its 5 km buffer, 2004.*

#### 3.2.2 Industrial Initiation Phase (2014)

By 2014, the establishment and early expansion of the KIADB Narasapura Industrial Estate had produced measurable built-up land growth to 8.9% (18.99 km²), a +16.1 km² increase on 2004. Crop land declined to 39.6% (84.83 km²) and agricultural plantation to 22.9% (48.85 km²). The most severe change was the collapse of waterbody coverage to 0.4% (0.86 km²), a loss of 11.88 km² attributable to tank encroachment, feeder channel blockage, and siltation from construction activity. Forest plantation (8.7%) and scrub forest (17.7%) increased, reflecting compensatory afforestation requirements within and around KIADB estate boundaries — gains that are policy-mandated rather than ecologically spontaneous.

**Figure 10** | *LULC map of the Narasapura Industrial Area and its 5 km buffer, 2014 (IRS Resourcesat-2 LISS-IV). Built-up land has expanded to 8.9% (18.99 km²) along the NH-75 corridor and around the KIADB estate core. Waterbody coverage has collapsed to 0.4% (0.86 km²). Ribbon development is visible along the highway, with cluster development emerging near the industrial estate.*

| LULC Class | Area (km²) | Area (%) |
|---|---|---|
| Agricultural Plantation | 48.85 | 22.9 |
| Barren Rocky/Stony Waste | 1.06 | 0.5 |
| Built-up Land | 18.99 | 8.9 |
| Crop Land | 84.83 | 39.6 |
| Forest Plantation | 18.54 | 8.7 |
| Land with Scrub | 2.75 | 1.3 |
| Scrub Forest | 37.87 | 17.7 |
| Water Bodies | 0.86 | 0.4 |
| **Total** | **213.75** | **100.0** |

*Table 3: LULC classification of Narasapura Industrial Area and its 5 km buffer, 2014.*

#### 3.2.3 Consolidation Phase (2024)

The 2024 classification captures a mature peri-urban industrial landscape. Built-up land expanded further to 17.3% (36.97 km²), with industrial sheds, logistics parks, worker colonies, and road infrastructure now pervasive across the formerly agricultural core. Agricultural plantation contracted to 14.2% (30.47 km²) and forest plantation to 4.2% (9.05 km²), indicating that the compensatory buffers established around 2014 have themselves been encroached. Scrub categories persisted in marginal non-arable lands. Waterbodies partially recovered to 4.5% (9.49 km²) under state-led rejuvenation schemes — Jal Shakti Abhiyan, KSPCB tank rehabilitation — though encroachment pressures on Vemgal Kere and Bendiganahalli Kere continue.

**Figure 11** | *LULC map of the Narasapura Industrial Area and its 5 km buffer, 2024 (IRS Resourcesat-2A LISS-IV). Built-up land constitutes 17.3% (36.97 km²), extending into villages of Vemgal, Vadagur, and Appasandra. Agricultural plantation has declined to 14.2%. Waterbodies show partial recovery to 4.5% following state-led rejuvenation. Forest plantation buffers established by 2014 have been partially cleared.*

| LULC Class | Area (km²) | Area (%) |
|---|---|---|
| Agricultural Plantation | 30.47 | 14.2 |
| Barren Rocky/Stony Waste | 3.81 | 1.8 |
| Built-up Land | 36.97 | 17.3 |
| Crop Land | 101.97 | 47.7 |
| Forest Plantation | 9.05 | 4.2 |
| Land with Scrub | 7.39 | 3.5 |
| Scrub Forest | 14.60 | 6.8 |
| Water Bodies | 9.49 | 4.5 |
| **Total** | **213.75** | **100.0** |

*Table 4: LULC classification of Narasapura Industrial Area and its 5 km buffer, 2024.*

### 3.3 Two-Decade Change Matrix and Net Transitions

The aggregate change matrix across the full study period reveals the structural character of the transformation. Built-up land recorded the largest absolute gain (+34.10 km², +1,188%), followed by scrub forest (+10.61 km², +4.9%) and land with scrub (+5.32 km², +2.5%). Agricultural plantation recorded the largest absolute loss (−52.02 km², −24.4%), followed by barren rocky waste (−3.49 km², −1.6%). Crop land showed a marginal net increase (+4.24 km², +1.0%) over the full period, masking a substantial decline between 2004 and 2014 and a compensatory recovery by 2024 as peripheral fields were reclassified. Water bodies showed a net loss of −3.25 km² (−1.5%) with a pronounced mid-period collapse.

| LULC Class | 2004 (km²/%) | 2014 (km²/%) | 2024 (km²/%) | Net Change 2004–2024 |
|---|---|---|---|---|
| Agricultural Plantation | 82.49 / 38.6 | 48.85 / 22.9 | 30.47 / 14.2 | −52.02 km² (−24.4%) |
| Barren Rocky/Stony Waste | 7.30 / 3.4 | 1.06 / 0.5 | 3.81 / 1.8 | −3.49 km² (−1.6%) |
| Built-up Land | 2.87 / 1.3 | 18.99 / 8.9 | 36.97 / 17.3 | **+34.10 km² (+16.0%)** |
| Crop Land | 97.73 / 46.7 | 84.83 / 39.6 | 101.97 / 47.7 | +4.24 km² (+1.0%) |
| Forest Plantation | 4.56 / 2.1 | 18.54 / 8.7 | 9.05 / 4.2 | +4.49 km² (+2.1%) |
| Land with Scrub | 2.07 / 1.0 | 2.75 / 1.3 | 7.39 / 3.5 | +5.32 km² (+2.5%) |
| Scrub Forest | 3.99 / 1.9 | 37.87 / 17.7 | 14.60 / 6.8 | +10.61 km² (+4.9%) |
| Water Bodies | 12.74 / 6.0 | 0.86 / 0.4 | 9.49 / 4.5 | −3.25 km² (−1.5%) |

*Table 5: Two-decade LULC change matrix for the Narasapura Industrial Area and 5 km buffer (2004–2014–2024). Total study area = 213.75 km².*

**Figure 12** | *LULC change matrix diagram (2004–2014–2024) illustrating net transitions among eight land cover classes. The dominant signal is a sustained conversion from agricultural plantation and crop land into built-up land across both phases, with a temporary expansion of scrub-forest buffers around 2014 and their subsequent partial contraction by 2024.*

**Figure 13** | *Bar chart of LULC class areas (km²) for 2004, 2014, and 2024. Built-up land exhibits the steepest monotonic rise across both phases. Agricultural plantation shows a sustained decline. Waterbody coverage collapses to near-zero in 2014 before partially recovering by 2024.*

### 3.4 Accuracy Assessment

The confusion matrix for the 2024 classification confirms high classification fidelity. Overall accuracy reached 96.81%, with a Kappa coefficient of 0.968 — indicative of near-perfect agreement between classified and reference data (Teferi et al., 2013; Wasige et al., 2013). User Accuracy ranged from 85.71% (Scrub Forest) to 100% across all other classes; Producer Accuracy ranged from 90.9% (Water Bodies, Forest Plantation, Land with Scrub) to 100% (Barren Rocky/Stony Waste, Built-up Land).

| Class | User Accuracy (%) | Producer Accuracy (%) |
|---|---|---|
| Water Bodies | 100.0 | 90.9 |
| Barren Rocky/Stony Waste | 100.0 | 100.0 |
| Scrub Forest | 85.71 | 100.0 |
| Forest Plantation | 100.0 | 90.9 |
| Agricultural Plantation | 96.0 | 96.4 |
| Crop Land | 97.91 | 98.9 |
| Built-up Land | 100.0 | 100.0 |
| Land with Scrub | 100.0 | 90.9 |
| **Overall Accuracy** | **96.81%** | — |
| **Kappa Coefficient** | **0.968** | — |

*Table 6: Accuracy assessment results for the 2024 LULC classification (212 stratified random test points).*

### 3.5 Peri-Urban Sprawl Morphology

Field validation combined with the 2004–2024 change layers reveals three spatially distinct sprawl typologies operating simultaneously within the study domain.

**Ribbon Sprawl** is the dominant form, expressed as a continuous linear belt of industrial sheds, godowns, service garages, and commercial units along NH-75 and the Narasapura–Vemgal–Kolar arterial corridor. Settlements including Vemgal, Koratagerepalya, and Seegihalli display this morphology. Ribbon development concentrates exposure to traffic-derived pollution and exerts linear encroachment pressure on roadside waterbodies, particularly Vemgal Kere.

**Cluster Sprawl** manifests as dense nuclei of housing layouts, industrial parks, and service facilities coalescing around the KIADB estate core and spreading into adjacent villages — Narasapura, Doddabasavanahalli, and Belur. Worker colonies and ancillary industries serving HMSI, Mahindra Aerospace, and Wistron have created self-contained peri-urban clusters that fragment surrounding plantation and scrub lands.

**Leapfrog Sprawl** is identified in peripheral locations including Malamachanahalli and Hejjala, where isolated villa projects and gated residential plots have been converted from farmland in non-contiguous patches, bypassing intervening agricultural fields. This morphology maximises infrastructure costs and disrupts contiguous agricultural landscapes most severely (Bhatta et al., 2010; Herold et al., 2005).

**Figures 14–15** | *Google Earth Pro imagery (2012 and 2024) of agricultural land near Vemagal, illustrating the conversion of cropland and plantation to non-agricultural and built-up uses over a 12-year interval. Fragmentation of field boundaries and encroachment of industrial layouts onto formerly productive farmland are evident.*

**Figures 16–17** | *Google Earth Pro imagery (2012 and 2024) of built-up area expansion in the Narasapura industrial core. The 2024 image shows densification of industrial sheds, logistics units, and worker colonies, with concomitant loss of intervening green cover and impervious surface expansion into former cropland.*

**Figures 18–19** | *Google Earth Pro imagery (2012 and 2024) of waterbodies in the study domain, illustrating the encroachment of built-up land into tank margins and buffer zones. The partial recovery of open water visible in 2024 reflects state-funded rejuvenation, while the loss of vegetated tank bunds indicates continued ecological stress.*

---

## 4. Discussion

### 4.1 Drivers of the Built-Up Land Surge and Their Policy Architecture

The near-twelvefold increase in built-up land coverage between 2004 and 2024 reflects a deliberate and sustained policy architecture rather than spontaneous urbanisation. The KIADB Narasapura Industrial Estate's Phase I and Phase II development, the entry of anchor industries beginning around 2006–2010, and the subsequent designation of the Bengaluru–Chennai Industrial Corridor (BCIC) created a self-reinforcing cycle of land acquisition, infrastructure investment, and secondary peri-urban growth. The rate of built-up expansion was faster in the consolidation phase (2014–2024: +17.98 km²) than in the initiation phase (2004–2014: +16.12 km²), suggesting that momentum — rather than direct policy investment alone — is now the primary engine of sprawl. This pattern is consistent with findings from comparable industrial corridors in South India (Chowdary et al., 2020; Rao et al., 2022).

### 4.2 The Agricultural Plantation Trajectory as a Structural Loss Indicator

The progressive decline of agricultural plantation from 38.6% (2004) to 14.2% (2024) represents the most consequential single-class change in the study. Plantation crops — coconut, arecanut, mango — generate substantially higher per-hectare returns and more stable household income than annual cropland, and their conversion therefore carries both ecological and socio-economic costs that land cover area statistics alone understate. Unlike cropland, which can theoretically be restored, mature plantations require years to re-establish and are rarely recovered once converted. The 52.02 km² net loss of plantation cover constitutes a largely irreversible ecological and agricultural capital destruction.

### 4.3 The Waterbody Collapse and Partial Revival: Interpretation and Limits

The collapse of waterbody coverage from 6.0% to 0.4% between 2004 and 2014 represents one of the most severe single-class losses documented in this study. Traditional tank systems in southern Karnataka function not merely as surface water storage but as integrated socio-ecological infrastructure — recharging shallow aquifers, sustaining irrigated agriculture, and maintaining riparian biodiversity (Sudhira et al., 2004; Shaw & Satish, 2018). The 2014 near-elimination of this infrastructure through encroachment and feeder channel blockage is therefore likely to have cascading hydrological effects that persist beyond the partial 2024 recovery.

The recovery to 4.5% by 2024, while superficially encouraging, warrants cautious interpretation. State-funded rejuvenation under Jal Shakti Abhiyan and Karnataka tank rehabilitation schemes has restored open water extent, but remote sensing alone cannot distinguish healthy, ecologically functional waterbodies from impounded surface water in structurally compromised tanks (Narasimhan & Venkatesh, 2021). Field observations confirm persistent encroachment pressure on tank margins and the replacement of natural vegetated bunds with hardened edges in several locations.

### 4.4 Forest Plantation Dynamics: Buffer Creation and Loss

The expansion of forest plantation from 2.1% (2004) to 8.7% (2014) reflects mandatory greenbelt requirements within KIADB estates under Karnataka environmental policy. The subsequent contraction to 4.2% by 2024 indicates that these compensatory buffers have themselves been encroached as industrial expansion accelerated into peripheral areas — precisely the failure mode anticipated by critics of compensatory afforestation as a primary environmental safeguard (MoEFCC, 2023). Net forest plantation gain over the full period (+4.49 km²) masks this internal dynamic and provides a misleadingly positive signal.

### 4.5 Environmental Consequences

The cumulative LULC transition has generated environmental consequences across three domains. First, the expansion of impervious built-up surfaces from 2.87 km² to 36.97 km² has dramatically reduced infiltration capacity within the study domain, increasing surface runoff volumes, attenuating groundwater recharge to shallow aquifers, and elevating flood risk for low-lying tank command areas during monsoon events (Ewing et al., 2002; Douglas, 2006). Second, the fragmentation of plantation and agricultural landscapes has reduced ecological connectivity and biodiversity, with remnant vegetation patches near Agalakote Reserve Forest now isolated within a matrix of impervious and disturbed land. Third, effluent discharge and domestic wastewater from industrial and residential complexes have contributed to eutrophication and algal infestations in surviving waterbodies, compounding the structural damage from encroachment (Sudhira et al., 2007; Allen, 2003).

### 4.6 Methodological Strengths and Limitations

The multi-temporal IRS Resourcesat series provides a consistent sensor family across the study period, minimising inter-epoch spectral inconsistencies. The high overall accuracy (96.81%, κ = 0.968) and per-class accuracy metrics confirm classification reliability. GPS field validation at 56 waypoints provides direct ground-truth confirmation of key transitions. Limitations include: the absence of sub-annual imagery to capture seasonal LULC fluctuations; classification at Level-II NRSC scheme, which does not distinguish functional land use within the built-up class (industrial shed vs. residential vs. road); and the restriction of spectral analysis to optical sensors, precluding assessment of vegetation health or surface moisture stress. Post-2024 trajectories, particularly given announced expansions under BCIC Phase II, remain outside study scope.

---

## 5. Conclusion

### 5.1 Synthesis

The Narasapura Industrial Corridor has undergone a structurally irreversible transition from a predominantly agrarian landscape (85.3% agricultural in 2004) to a peri-urban industrial hub (17.3% built-up in 2024) within two decades. Built-up land expanded by 34.10 km² — a 1,188% increase — while agricultural plantation contracted by 52.02 km². Three morphologically distinct sprawl types operate simultaneously: ribbon sprawl along NH-75, cluster sprawl around KIADB estate nodes, and leapfrog sprawl in peripheral villages. Waterbody infrastructure collapsed to near-zero by 2014 before partially recovering under state-led rejuvenation, though functional hydrological integrity remains uncertain. The IRS Resourcesat multi-temporal supervised classification framework, achieving 96.81% accuracy and κ = 0.968, proves robust for tracking such transitions in rapidly industrialising peri-urban domains.

### 5.2 Policy Imperatives

Four policy imperatives emerge from this evidence base. First, ecological buffer zones around surviving waterbodies and remnant vegetation patches require legal designation and enforcement independent of compensatory afforestation obligations, which have demonstrably failed to provide permanent buffers in this context. Second, terrain-sensitive zoning — directing development toward flat constructible land and protecting steep slopes, tank command areas, and drainage corridors from encroachment — should be embedded in KIADB estate expansion approvals and Kolar Local Planning Area regulations. Third, hydrological impact assessment should be mandatory for new industrial development proposals, incorporating modelled runoff and groundwater recharge effects rather than relying solely on greenbelt area targets. Fourth, geospatial monitoring at five-year intervals, integrating LULC change with land surface temperature and NDVI trends, should be institutionalised within KSRSAC and KSPCB reporting frameworks to enable early detection of encroachment and provide an evidence base for adaptive governance.

---

## Funding Statement

This research received no external funding. The work constitutes partial fulfilment of the Master of Science in Environmental Science, Bangalore University.

## Declaration of Competing Interests

The authors declare no competing interests.

## Author Contributions

Divakar G: conceptualisation, data acquisition, image classification, field validation, analysis, and writing. Dr. Hemanjali A.M.: supervision, methodology guidance, and manuscript review.

## Data Availability

IRS Resourcesat imagery is available from Karnataka State Remote Sensing Applications Centre (KSRSAC), Bengaluru. Ground-truth GPS waypoints and confusion matrix data are available from the corresponding author on reasonable request.

---

## References

Abebe, G., Getachew, D., & Ewunetu, A. (2022). Analysing land use/land cover changes and its dynamics using remote sensing and GIS in Gubalafito district, Northeastern Ethiopia. *SN Applied Sciences*, 4(1), 30.

Allen, A. (2003). Environmental planning and management of the peri-urban interface. *Environment and Urbanization*, 15(1), 135–148.

Angel, S., Parent, J., Civco, D. L., Blei, A., & Potere, D. (2011). The dimensions of global urban expansion. *Progress in Planning*, 75(2), 53–107.

Belgiu, M., & Csillik, O. (2018). Sentinel-2 cropland mapping using pixel-based and object-based time-weighted dynamic time warping analysis. *Remote Sensing of Environment*, 204, 509–523.

Bhatta, B., Saraswati, S., & Bandyopadhyay, D. (2010). Urban sprawl measurement from remote sensing data. *Applied Geography*, 30(4), 731–740.

Bharath, A., Manjunatha, M., Reshma, T. V., Tangadagi, R. B., & Bahij, S. (2023). Evaluation of land use/land cover changes due to urban sprawl in Bengaluru Rural, Karnataka, India. *Discrete Dynamics in Nature and Society*, 2023, 8077644.

Burchell, R. W., & Listokin, D. (1978). *The Fiscal Impact Handbook*. Center for Urban Policy Research, Rutgers University.

Chowdary, V. M., Sreenivas, K., & Adhikari, R. N. (2020). Spatio-temporal analysis of land use dynamics using remote sensing and GIS: A case study from an industrializing region in South India. *Journal of the Indian Society of Remote Sensing*, 48, 705–718.

Douglas, I. (2006). Peri-urban ecosystems and societies: Transitional zones and contrasting values. In D. McGregor, D. Simon, & D. Thompson (Eds.), *The Peri-Urban Interface: Approaches to Sustainable Natural and Human Resource Use* (pp. 18–29). Earthscan.

Ewing, R., Pendall, R., & Chen, D. (2002). *Measuring Sprawl and Its Impact*. Smart Growth America.

FAO. (2021). *State of the World's Land and Water Resources for Food and Agriculture*. Food and Agriculture Organization of the United Nations.

Foody, G. M. (2020). Explaining the unsuitability of the kappa coefficient in the assessment and comparison of the accuracy of thematic maps obtained by image classification. *Remote Sensing of Environment*, 239, 111630.

Government of Karnataka. (2020). *Karnataka Industrial Policy 2020–25*. Department of Industries and Commerce.

Government of Karnataka. (2002). *Karnataka State Water Policy*. Government of Karnataka.

Guru Balamurugan, P., Vinothkumar, V., & Subramani, T. (2020). Spatio-temporal analysis of LULC changes and urban growth in peri-urban areas using GIS. *Journal of Critical Reviews*, 7(3), 415–421.

Herold, M., Goldstein, N. C., & Clarke, K. C. (2005). The spatiotemporal form of urban growth: measurement, analysis and modeling. *Remote Sensing of Environment*, 86(3), 286–302.

IPBES. (2019). *Global Assessment Report on Biodiversity and Ecosystem Services*. Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services.

IPCC. (2021). *Climate Change 2021: The Physical Science Basis*. Cambridge University Press.

Jat, M. K., Garg, P. K., & Khare, D. (2008). Monitoring and modelling of urban sprawl using remote sensing and GIS techniques. *International Journal of Applied Earth Observation and Geoinformation*, 10(1), 26–43.

Jensen, J. R. (2007). *Remote Sensing of the Environment: An Earth Resource Perspective* (2nd ed.). Pearson Prentice Hall.

Jensen, J. R. (2016). *Introductory Digital Image Processing: A Remote Sensing Perspective* (4th ed.). Pearson.

KSRSAC. (2020). *Land Use Land Cover Atlas of Karnataka*. Karnataka State Remote Sensing Applications Centre, Bengaluru.

Kumar, N., Singh, S. K., & Rai, A. (2022). Assessment of land use land cover change and its impact on urban growth using geospatial tools: A study of an industrial corridor in India. *Environmental Challenges*, 7, 100449.

Lambin, E. F., & Geist, H. (Eds.). (2006). *Land-Use and Land-Cover Change: Local Processes and Global Impacts*. Springer.

Lillesand, T. M., Kiefer, R. W., & Chipman, J. W. (2015). *Remote Sensing and Image Interpretation* (7th ed.). John Wiley & Sons.

Lu, D., & Weng, Q. (2007). A survey of image classification methods and techniques for improving classification performance. *International Journal of Remote Sensing*, 28(5), 823–870.

MoEFCC. (2006). *EIA Notification*. Ministry of Environment, Forest and Climate Change, Government of India.

MoEFCC. (2023). *Annual Report 2022–23*. Ministry of Environment, Forest and Climate Change, Government of India.

MoWR. (2012). *National Water Policy 2012*. Ministry of Water Resources, Government of India.

Narasimhan, D., & Venkatesh, M. (2021). Impact of industrial expansion on water bodies and land use in Kolar district. *Journal of Environmental Planning and Management*, 64(9), 1564–1581.

NRSC. (2021). *National Land Use Land Cover Mapping*. National Remote Sensing Centre, ISRO.

Olofsson, P., Foody, G. M., Herold, M., Stehman, S. V., Woodcock, C. E., & Wulder, M. A. (2014). Good practices for estimating area and assessing accuracy of land change. *Remote Sensing of Environment*, 148, 42–57.

Pontius, R. G., & Millones, M. (2011). Death to Kappa: birth of quantity disagreement and allocation disagreement for accuracy assessment. *International Journal of Remote Sensing*, 32(15), 4407–4429.

Prakash, T. N., & Sudhira, H. S. (2016). Urban growth and industrial sprawl in Kolar district: A multi-temporal analysis. *Journal of Environmental Management*, 175, 78–89.

Ramachandra, T. V., Bharath, H. A., & Durgappa, D. S. (2014). Insights to urban dynamics through landscape spatial pattern analysis. *International Journal of Applied Earth Observation and Geoinformation*, 18, 329–343.

Rao, S., Prakash, T., & Hegde, K. (2022). Industrial corridor development and urbanization: A case study of Narasapura Industrial Area. *Journal of Urban and Regional Development*, 14(1), 45–59.

Ravindra, K., et al. (2021). Land cover dynamics and peri-urban transitions in Kolar, Karnataka: A 20-year perspective. *Environmental Monitoring and Assessment*, 193, 412.

Rawat, J. S., & Kumar, M. (2015). Monitoring land use/cover change using remote sensing and GIS techniques: A case study of Hawalbagh block, district Almora, Uttarakhand, India. *The Egyptian Journal of Remote Sensing and Space Science*, 18(1), 77–84.

Reis, S. (2008). Analyzing land use/land cover changes using remote sensing and GIS in Rize, North-East Turkey. *Sensors*, 8(10), 6188–6202.

Roy, M., Dutta, D., & Pradhan, B. (2024). Geospatial modeling of urban sprawl and land transformation in industrial clusters: A case study from Karnataka, India. *Land Use Policy*, 134, 106973.

Samal, N. R., & Gedam, S. S. (2021). Peri-urban sprawl and its implications on local land use planning: Insights from growing industrial zones in India. *Cities*, 114, 103216.

Seto, K. C., Güneralp, B., & Hutyra, L. R. (2012). Global forecasts of urban expansion to 2030 and direct impacts on biodiversity and carbon pools. *Proceedings of the National Academy of Sciences*, 109(40), 16083–16088.

Shaw, R., & Satish, M. (2018). Tank irrigation and ecosystem services in Karnataka: Historical and contemporary perspectives. *Water Policy*, 20(3), 512–527.

Singh, A., Rai, A., & Singh, V. (2020). Advances in geospatial techniques for urban land use monitoring: A review. *Remote Sensing Applications: Society and Environment*, 17, 100271.

Srinivasan, V., Seto, K. C., Emerson, R., & Gorelick, S. M. (2013). The impact of urbanization on water vulnerability: A coupled human–environment system approach for Chennai, India. *Global Environmental Change*, 23(1), 229–239.

Sudhira, H. S., Ramachandra, T. V., & Jagadish, K. S. (2004). Urban sprawl: metrics, dynamics and modelling using GIS. *International Journal of Applied Earth Observation and Geoinformation*, 5(1), 29–39.

Sudhira, H. S., Ramachandra, T. V., & Subrahmanya, M. H. B. (2007). Bangalore, in E. Razin et al. (Eds.), *Urban Sprawl in Europe and the USA*. Ashgate.

Tacoli, C. (2003). The links between urban and rural development. *Environment and Urbanization*, 15(1), 3–12.

Teferi, E., Bewket, W., Uhlenbrook, S., & Wenninger, J. (2013). Understanding recent land use and land cover dynamics in the source region of the Upper Blue Nile, Ethiopia. *Applied Geography*, 45, 174–185.

Turner, B. L., Lambin, E. F., & Reenberg, A. (2007). The emergence of land change science for global environmental change and sustainability. *Proceedings of the National Academy of Sciences*, 104(52), 20666–20671.

UN-Habitat. (2020). *World Cities Report 2020: The Value of Sustainable Urbanization*. United Nations Human Settlements Programme.

UNEP. (2022). *Making Peace with Nature: A Scientific Blueprint to Tackle the Climate, Biodiversity and Pollution Emergencies*. United Nations Environment Programme.

United Nations. (2022). *The Sustainable Development Goals Report 2022*. United Nations.

Wasige, J. E., Groen, T. A., Smaling, E., & Jetten, V. (2013). Monitoring basin-scale land cover changes in Kagera Basin of Lake Victoria using ancillary data and remote sensing. *International Journal of Applied Earth Observation and Geoinformation*, 21, 32–42.

World Bank. (2021). *Urban Development Overview*. The World Bank Group.

Zhang, C., Sargent, I., Pan, X., Li, H., Gardiner, A., Hare, J., & Atkinson, P. M. (2019). Joint deep learning for land cover and land use classification. *Remote Sensing of Environment*, 221, 173–187.

---

## Citation Issues Log — Pre-Submission Checklist

| # | Issue | Details | Action Required |
|---|---|---|---|
| 1 | Ravindra et al. (2021) — incomplete | Cited in text; journal/volume/pages not provided in reference list | Verify full citation |
| 2 | Prakash & Sudhira (2016) — incomplete | Cited in text; not in reference list as written | Verify against Prakash, T. N., & Sudhira (2016) entry |
| 3 | Burai et al. (2015) — missing | Cited in Introduction; absent from reference list | Add full citation |
| 4 | Jat et al. (2017) — mismatch | Cited in text as 2017; Jat et al. in reference list dated 2008 | Confirm correct year |
| 5 | KIADB (2012) — grey literature | Cited in change analysis; verify availability and formal citation format | Add institutional citation |
| 6 | Bharath & Ramachandra (2019) — incomplete | Cited as "Ramachandra & Bharath, 2019" in text; listed as Bharath et al. (2020) in references | Reconcile year and author order |
| 7 | Pontius & Millones (2011) — DOI recommended | Standard reference; add DOI for indexing |  |
| 8 | Roy et al. (2015) — mismatch | Cited in methods as Roy et al. (2015); full reference lists Roy et al. (2024) | Confirm correct year |
