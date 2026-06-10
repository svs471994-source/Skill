# Geospatial Analysis of Land Use–Land Cover Change and Peri-Urban Sprawl in the Dabaspet Industrial Corridor, Bengaluru Rural District, Karnataka: A Two-Decade Assessment (2004–2024)

**Bindu V**, Department of Environmental Science, Bangalore University, Bengaluru – 560 056, Karnataka, India

**Correspondence:** Dr. Hemanjali A.M., Department of Environmental Science, Bangalore University, Jnanabharathi Campus, Bengaluru – 560 056. Email: hemanjalidoli@bub.ernet.in

---

## Abstract

**Background:** The Dabaspet Industrial Area in Bengaluru Rural district, Karnataka, situated at the intersection of the Bengaluru–Tumakuru Highway (NH-48) and the Doddaballapura corridor (NH-648), represents a rapidly transforming peri-urban landscape driven by state-led industrialisation under the Karnataka Industrial Areas Development Board (KIADB). Comprehensive multi-temporal geospatial documentation of this transformation is absent from the published literature.

**Methods:** Multi-temporal IRS Resourcesat-1 LISS-III (2004), Resourcesat-2 LISS-IV (2014), and Resourcesat-2A LISS-IV (2024) multispectral imagery was processed through supervised Maximum Likelihood Classification (MLC) within a GIS framework covering the Dabaspet Industrial Area and its 5 km buffer (224.02 km²). Nine LULC classes were delineated under the NRSC Level-II scheme. Accuracy was assessed using a confusion matrix of 228 stratified random reference points. Terrain, soil, slope, and drainage ancillary layers from KSRSAC and SRTM supplemented the classification. Peri-urban sprawl morphology was characterised through post-classification change detection and GPS-validated field verification.

**Results:** The classification achieved an overall accuracy of 96.37% and a Kappa coefficient of 0.9657. Over the two-decade study period, built-up land expanded sixfold from 3.24% (6.83 km²) in 2004 to 19.23% (43.08 km²) in 2024, a net gain of 36.25 km². Cropland declined from 65.74% (138.71 km²) to 47.20% (105.74 km²), a net loss of 32.97 km². Agricultural plantation contracted from 17.20% (36.29 km²) to 14.06% (31.50 km²). Waterbodies decreased from 4.84% (10.20 km²) to a nadir of 2.95% (6.61 km²) in 2014, recovering partially to 3.17% (7.10 km²) in 2024. Three sprawl morphologies were identified: ribbon development along NH-48 and NH-648, scattered residential and industrial layouts in peripheral settlements, and industrial-driven agricultural conversion in Sompura and Kyalanur.

**Conclusion:** The Dabaspet corridor has undergone a structurally decisive transition from an agrarian to a peri-urban industrial landscape over two decades. The convergence of transport accessibility, KIADB land acquisition, and market-driven development has generated persistent environmental costs — reduced groundwater recharge, waterbody degradation, and fragmented agricultural ecosystems — that require integrated geospatial governance to address.

**Keywords:** Land Use Land Cover; Peri-Urban Sprawl; IRS Resourcesat; Dabaspet; Supervised Classification; Maximum Likelihood; KIADB; Karnataka Industrial Corridor; Geospatial Assessment

---

## 1. Introduction

### 1.1 Industrialisation and Peri-Urban Land Conversion in South Asia

Industrial development constitutes one of the most spatially concentrated and irreversible drivers of land cover change in lower-middle-income economies. In South Asia, the proliferation of industrial corridors, Special Economic Zones, and logistics hubs has transformed peri-urban fringes at rates that frequently outpace planning capacity (Seto et al., 2012; UN-Habitat, 2020). Over 75% of Earth's ice-free land surface has been significantly modified by human activity, with industrial expansion in rapidly urbanising regions accounting for a disproportionate share of new conversion (IPBES, 2019). The IPCC (2019) identifies peri-urban land transformation as a cross-cutting stressor affecting surface hydrology, microclimate, biodiversity, and food security simultaneously.

In India, ISRO's National Remote Sensing Centre documented a 54.5% expansion of built-up area between 1990 and 2020, with industrial corridors and associated peri-urban growth contributing substantially to this trend (NRSC, 2020). State-led industrial policies, improved transport connectivity, and land market liberalisation have accelerated this conversion at the urban–rural fringe, generating fragmented agricultural landscapes and stressed hydrological systems that are difficult to reverse (Seto et al., 2011; Ravindra et al., 2017).

### 1.2 The Dabaspet Industrial Corridor: Context and Knowledge Gap

The Dabaspet Industrial Area in Bengaluru Rural district, Karnataka (12.95°–13.05°N, 77.25°–77.45°E), occupies a strategically important position on the Bengaluru–Tumakuru Highway (NH-48) and the Dabaspet–Doddaballapura corridor (NH-648). KIADB's Phases I and II industrial estate development, combined with the proposed Suburban Transport Ring Road (STRR) and proximity to the Bengaluru metropolitan area, have made this corridor a focal zone for automobile component, logistics, and light engineering industries. Prior to systematic industrial development, the region was characterised by a predominantly agrarian landscape of paddy, ragi, coconut, and arecanut cultivation interspersed with traditional tank irrigation systems (Ramesh et al., 2020; Ravindra et al., 2017).

Despite this transformation's magnitude, a published multi-temporal geospatial assessment covering the full 2004–2024 arc and integrating terrain, soil, and sprawl morphology analysis is absent from the literature. This study addresses that gap.

### 1.3 Research Objectives

1. To classify and quantify LULC dynamics in the Dabaspet Industrial Area and its 5 km buffer for 2004, 2014, and 2024 using IRS Resourcesat multi-temporal imagery and supervised classification.
2. To assess peri-urban sprawl morphology and document the environmental consequences of two-decade industrial expansion within the study domain.

---

## 2. Materials and Methods

### 2.1 Study Area

The study domain encompasses the Dabaspet Industrial Area, Bengaluru Rural district, Karnataka, and a 5 km buffer zone, yielding a total analytical area of 224.02 km². The central and north-central sectors (927–968 m elevation) provide flat to gently undulating terrain suitable for industrial development. Higher elevations (968–1,338 m) around Sompura and the Shivagange Hills impose moderate topographic constraints and function as natural ecological barriers. Lower pockets (864–927 m) in the southwest and east support agriculture and open spaces. The region is traversed by NH-48 westward toward Tumakuru and NH-648 toward Doddaballapura, defining the primary vectors of peri-urban growth.

Key settlement nodes within the buffer include Dabaspet town, Thyamagondlu, Sompura, Madanayakanahalli, Basavanahalli, Halekote, Kyalanur, and Shivapura. The traditional tank irrigation network — Thyamagondlu Kere, Somadevanahalli Kere, Kallukote Kere, Shivapura Tank, and Sompura Kere — historically sustained the agrarian economy and now faces mounting industrial and peri-urban pressure.

**Figure 1** | *Study area map of the Dabaspet Industrial Area and its 5 km buffer zone, Bengaluru Rural district, Karnataka (12.95°–13.05°N, 77.25°–77.45°E). Total analytical area: 224.02 km². NH-48 (Bengaluru–Tumakuru) and NH-648 (Dabaspet–Doddaballapura) define the primary transport corridors driving ribbon development.*

**Figure 2** | *Topographic map of the study area (SRTM-derived). Elevation ranges from 864 m in lower eastern pockets to 1,338 m on Shivagange Hill ridges in the southwest. The flat central zone (927–968 m) hosts the KIADB industrial estate and associated built-up expansion.*

### 2.2 Satellite Data and Preprocessing

Multi-temporal IRS Resourcesat imagery was acquired from KSRSAC for three study epochs.

| Sensor | Year | Resolution | Bands |
|---|---|---|---|
| IRS Resourcesat-1 LISS-III | 2004 | 23.5 m | Green, Red, NIR, SWIR |
| IRS Resourcesat-2 LISS-IV | 2014 | 5.8 m | Green, Red, NIR |
| IRS Resourcesat-2A LISS-IV | 2024 | 5.8 m | Green, Red, NIR |

*Table 1: Satellite data specifications.*

Preprocessing included radiometric correction to Top-of-Atmosphere reflectance, geometric co-registration to WGS84/UTM Zone 43N, and atmospheric correction. A 5 km buffer around the Dabaspet Industrial Area was delineated in GIS to define the area of interest.

### 2.3 Classification Methodology

Supervised Maximum Likelihood Classification (MLC) was applied within ERDAS Imagine and ArcGIS software platforms, following the NRSC Level-II classification scheme. Nine land cover classes were delineated: Agricultural Plantation, Barren Rocky/Stony Waste, Built-up Land, Crop Land, Land with Scrub, Land without Scrub, Mixed Forest Vegetation, Scrub Forest, and Water Bodies. Training samples were collected from field reconnaissance, Google Earth Pro imagery, and KSRSAC reference datasets. Post-classification 3×3 majority filtering was applied. Ancillary datasets — KSRSAC soil maps, SRTM-derived DEM for slope and elevation, and drainage network analysis — supplemented class delineation in spectrally ambiguous zones.

**Figure 3** | *Supervised classification workflow applied to IRS Resourcesat imagery for all three epochs. Training polygons were digitised for nine LULC classes; Maximum Likelihood Classification was applied followed by post-processing smoothing and accuracy assessment.*

**Figure 4** | *Methodological flowchart for generating multi-temporal LULC maps, from satellite data ingestion through preprocessing, supervised classification, accuracy assessment, and two-phase change detection (2004–2014; 2014–2024).*

### 2.4 Accuracy Assessment

The 2024 LULC map was assessed against 228 stratified random reference points validated against contemporaneous Google Earth Pro imagery and KSRSAC thematic data. A confusion matrix was constructed to derive User Accuracy, Producer Accuracy, Overall Accuracy, and the Kappa coefficient following Olofsson et al. (2014) and Pontius & Millones (2011). Classification accuracy for 2004 and 2014 is assumed to be of comparable order given consistent methodology.

### 2.5 Peri-Urban Sprawl Analysis

Sprawl morphology was characterised from change-detection overlays of the three classification epochs, supplemented by GPS-georeferenced field verification at key locations. Canonical sprawl typologies — ribbon, scattered/leapfrog, clustered, and edge/infill — were evaluated against the spatial distribution of built-up gains relative to highway corridors, KIADB estate boundaries, and peripheral village nodes.

---

## 3. Results and Discussion

### 3.1 Biophysical Baseline

Soil, terrain, and drainage conditions strongly condition the spatial trajectory of land conversion in the study domain. The soil mosaic is dominated by clayey skeletal soils in the central and northern zones (Sompura, Nidavanda), which are susceptible to compaction under industrial loading, while loamy and sandy skeletal soils along the southern and western margins (Yedehalli, Thyamagondlu) support higher infiltration with lower water retention. Habitation clusters in central and western sectors confirm the agrarian settlement pattern prior to industrial development.

**Figure 5** | *Soil characteristics map of the Dabaspet Industrial Area and its 5 km buffer (Source: KSRSAC). Clayey skeletal soils dominate the central-northern zone; loamy and sandy skeletal soils occur along the southern and western margins. Scattered rock outcrops limit construction in localised peripheral areas.*

Elevation ranges from 864 m to 1,338 m, with flat to gently undulating terrain (927–968 m) in the central and eastern zones facilitating industrial infrastructure, while elevated ridges near Shivagange Hills function as natural development barriers. Low-slope terrain (0–2.8°) dominates the central industrial core, with moderately steep (15–24°) and steep (25–64°) slopes confined to the southwest — preserving vegetation and restricting urban encroachment.

**Figure 6** | *Digital elevation map of the Dabaspet Industrial Area and its 5 km buffer. The flat-to-gently-undulating central zone (927–968 m) accommodates industrial estate development. Elevated ridges (>1,000 m) near Shivagange Hills act as topographic barriers. Low-lying depressions support waterbodies and are vulnerable to encroachment.*

**Figure 7** | *Slope classification map (degrees) of the study area. Flat terrain (0–2.8°) in the central and eastern zones supports industrial expansion along NH-48. Moderately steep to steep slopes (15–64°) near Shivagange Hills in the southwest inhibit development and preserve residual vegetation cover.*

The drainage network displays a dendritic pattern characteristic of uniform geology and gentle slopes, with first- and second-order streams originating near Thyamagondlu and Somadevanahalli draining southeastward into the Arkavathi River basin. Waterbodies — Thyamagondlu Kere, Kallukote Kere, Somadevanahalli Kere, and Shivapura Tank — provide irrigation and groundwater recharge. Industrial impervious surfaces have progressively disrupted these natural drainage pathways.

**Figure 8** | *Drainage network map of the Dabaspet Industrial Area and its 5 km buffer. Dendritic drainage feeds into traditional tank systems (Thyamagondlu Kere, Somadevanahalli Kere, Shivapura Tank). Industrial land modification has reduced natural drainage connectivity in the core zone, increasing flood risk in downstream tank command areas.*

### 3.2 LULC Classification Results

#### 3.2.1 Pre-Industrial Baseline (2004)

The 2004 classification confirms a predominantly agrarian landscape. Cropland dominated at 65.74% (138.71 km²), followed by agricultural plantation at 17.20% (36.29 km²), together accounting for 82.94% of the study domain. Waterbodies covered 4.84% (10.20 km²), representing intact traditional tank systems. Built-up land was minimal at 3.24% (6.83 km²), concentrated around the core Dabaspet settlement and along the NH-48 corridor. Mixed forest vegetation (4.01%, 8.47 km²) and scrub forest (1.09%, 2.30 km²) were confined to southern and southwestern tracts.

**Figure 9** | *LULC map of the Dabaspet Industrial Area and its 5 km buffer, 2004 (IRS Resourcesat-1 LISS-III). Cropland and agricultural plantation together constitute 82.9% of the domain. Built-up land (3.24%) is restricted to Dabaspet settlement and NH-48 roadside nodes. Traditional waterbodies at 4.84% reflect an intact agrarian hydrological system.*

| LULC Class | Area (km²) | Area (%) |
|---|---|---|
| Agricultural Plantation | 36.29 | 17.20 |
| Barren Rocky/Stony Waste | 11.68 | 5.54 |
| Built-up Land | 6.83 | 3.24 |
| Crop Land | 138.71 | 65.74 |
| Land with Scrub | 9.18 | 4.35 |
| Land without Scrub | 0.34 | 0.16 |
| Mixed Forest Vegetation | 8.47 | 4.01 |
| Scrub Forest | 2.30 | 1.09 |
| Water Bodies | 10.20 | 4.84 |
| **Total** | **224.02** | **100.00** |

*Table 2: LULC classification of Dabaspet Industrial Area and 5 km buffer, 2004.*

#### 3.2.2 Industrial Initiation Phase (2014)

By 2014, the operationalisation of KIADB Phases I and II generated a measurable built-up expansion to 10.45% (23.41 km²), more than tripling from 2004. Cropland declined to 58.58% (131.22 km²) and agricultural plantation to 11.77% (26.36 km²). Mixed forest vegetation collapsed to 0.43% (0.95 km²), cleared for industrial and residential construction, while scrub forest expanded substantially to 11.39% (25.52 km²) — secondary growth on abandoned and transitional agricultural land. Waterbodies contracted to 2.95% (6.61 km²), reflecting encroachment on tank margins and disruption of seasonal feeder channels.

**Figure 10** | *LULC map of the Dabaspet Industrial Area and its 5 km buffer, 2014 (IRS Resourcesat-2 LISS-IV). Built-up land has expanded to 10.45% (23.41 km²) along NH-48 and around KIADB estate clusters. Waterbodies have contracted to 2.95%. Scrub forest at 11.39% reflects secondary vegetation growth on abandoned croplands and transitional land.*

| LULC Class | Area (km²) | Area (%) |
|---|---|---|
| Agricultural Plantation | 26.36 | 11.77 |
| Barren Rocky/Stony Waste | 3.52 | 1.57 |
| Built-up Land | 23.41 | 10.45 |
| Crop Land | 131.22 | 58.58 |
| Land with Scrub | 1.31 | 0.59 |
| Land without Scrub | 5.11 | 2.28 |
| Mixed Forest Vegetation | 0.95 | 0.43 |
| Scrub Forest | 25.52 | 11.39 |
| Water Bodies | 6.61 | 2.95 |
| **Total** | **224.01** | **100.00** |

*Table 3: LULC classification of Dabaspet Industrial Area and 5 km buffer, 2014.*

#### 3.2.3 Industrial Consolidation Phase (2024)

The 2024 classification documents an intensified and spatially extended industrial landscape. Built-up land nearly doubled from 2014 to 19.23% (43.08 km²), with growth concentrated along NH-48, within expanding KIADB estate boundaries, and in peri-urban clusters at Shivapura, Thyamagondlu, and Somadevanahalli. Cropland declined to 47.20% (105.74 km²). Agricultural plantation partially recovered to 14.06% (31.50 km²) through agro-forestry and plantation initiatives in northeastern and eastern buffer sectors. Mixed forest vegetation increased to 2.50% (5.59 km²) through greenbelt development near Thyamagondlu, while scrub forest reduced to 9.10% (20.38 km²) as land was cleared for construction. Waterbodies showed marginal recovery to 3.17% (7.10 km²), linked to state-led tank rejuvenation and stormwater harvesting programs.

**Figure 11** | *LULC map of the Dabaspet Industrial Area and its 5 km buffer, 2024 (IRS Resourcesat-2A LISS-IV). Built-up land constitutes 19.23% (43.08 km²), extending into Shivapura, Thyamagondlu, and Somadevanahalli. Cropland persists at 47.20% but with severe fragmentation. Waterbodies show slight recovery to 3.17% following rejuvenation programs.*

| LULC Class | Area (km²) | Area (%) |
|---|---|---|
| Agricultural Plantation | 31.50 | 14.06 |
| Barren Rocky/Stony Waste | 3.09 | 1.38 |
| Built-up Land | 43.08 | 19.23 |
| Crop Land | 105.74 | 47.20 |
| Land with Scrub | 1.29 | 0.58 |
| Land without Scrub | 6.23 | 2.78 |
| Mixed Forest Vegetation | 5.59 | 2.50 |
| Scrub Forest | 20.38 | 9.10 |
| Water Bodies | 7.10 | 3.17 |
| **Total** | **224.01** | **100.00** |

*Table 4: LULC classification of Dabaspet Industrial Area and 5 km buffer, 2024.*

### 3.3 Two-Decade Change Matrix

The aggregate change matrix reveals the structural character of the transition. Built-up land recorded the largest absolute gain (+36.25 km², +15.99%), followed by scrub forest (+18.08 km², +8.01%) and land without scrub (+5.89 km², +2.62%). Cropland recorded the largest absolute loss (−32.97 km², −18.54%), followed by land with scrub (−7.89 km², −3.77%) and barren rocky waste (−8.59 km², −4.16%). Agricultural plantation showed a net loss of −4.79 km², masking a two-phase trajectory (decline to 2014, partial recovery to 2024).

| LULC Class | 2004 (km²/%) | 2014 (km²/%) | 2024 (km²/%) | Net Change 2004–2024 |
|---|---|---|---|---|
| Agricultural Plantation | 36.29 / 17.20 | 26.36 / 11.77 | 31.50 / 14.06 | −4.79 km² (−3.14%) |
| Barren Rocky/Stony Waste | 11.68 / 5.54 | 3.52 / 1.57 | 3.09 / 1.38 | −8.59 km² (−4.16%) |
| Built-up Land | 6.83 / 3.24 | 23.41 / 10.45 | 43.08 / 19.23 | **+36.25 km² (+15.99%)** |
| Crop Land | 138.71 / 65.74 | 131.22 / 58.58 | 105.74 / 47.20 | −32.97 km² (−18.54%) |
| Land with Scrub | 9.18 / 4.35 | 1.31 / 0.59 | 1.29 / 0.58 | −7.89 km² (−3.77%) |
| Land without Scrub | 0.34 / 0.16 | 5.11 / 2.28 | 6.23 / 2.78 | +5.89 km² (+2.62%) |
| Mixed Forest Vegetation | 8.47 / 4.01 | 0.95 / 0.43 | 5.59 / 2.50 | −2.88 km² (−1.51%) |
| Scrub Forest | 2.30 / 1.09 | 25.52 / 11.39 | 20.38 / 9.10 | +18.08 km² (+8.01%) |
| Water Bodies | 10.20 / 4.84 | 6.61 / 2.95 | 7.10 / 3.17 | −3.10 km² (−1.67%) |
| **Total** | **224.02 / 100** | **224.01 / 100** | **224.01 / 100** | — |

*Table 5: Two-decade LULC change matrix, Dabaspet Industrial Area and 5 km buffer (2004–2014–2024).*

**Figure 12** | *Bar chart of LULC class areas (km²) for 2004, 2014, and 2024. Built-up land exhibits the steepest sustained increase across both phases. Cropland shows progressive monotonic decline. Scrub forest peaks sharply in 2014 before partially contracting by 2024 as secondary vegetation cover is cleared for construction. Waterbody coverage partially recovers after a 2014 nadir.*

### 3.4 Accuracy Assessment

The confusion matrix for the 2024 LULC classification yields high classification fidelity. Overall accuracy reached 96.37% with a Kappa coefficient of 0.9657 — indicative of near-perfect agreement. Minor misclassifications occurred between agricultural plantation and barren rocky areas, and between scrub forest and cropland, attributable to spectral similarity in IRS imagery. User Accuracy ranged from 90% (Barren Rocky) to 100% (Water Bodies, Mixed Forest Vegetation, Land without Scrub, Land with Scrub); Producer Accuracy ranged from 92.86% (Agricultural Plantation, Scrub Forest) to 100% (Water Bodies, Built-up Land, Mixed Forest Vegetation, Land without Scrub, Land with Scrub).

| Class | User Accuracy (%) | Producer Accuracy (%) |
|---|---|---|
| Barren Rocky/Stony Waste | 90.00 | 100.00 |
| Agricultural Plantation | 92.86 | 92.86 |
| Scrub Forest | 94.44 | 94.44 |
| Built-up Land | 97.37 | 100.00 |
| Water Bodies | 100.00 | 100.00 |
| Crop Land | 98.94 | 96.88 |
| Mixed Forest Vegetation | 100.00 | 100.00 |
| Land without Scrub | 100.00 | 100.00 |
| Land with Scrub | 100.00 | 100.00 |
| **Overall Accuracy** | **96.37%** | — |
| **Kappa Coefficient** | **0.9657** | — |

*Table 6: Accuracy assessment results for the 2024 LULC classification (228 stratified random reference points).*

### 3.5 Peri-Urban Sprawl Morphology

Four spatially distinct sprawl typologies are identified within the study domain.

**Ribbon Sprawl** dominates along NH-48 stretching westward toward Tumakuru and along NH-648 from Dabaspet Junction through Kyalanur toward Doddaballapura. This linear strip includes logistics hubs, roadside commercial units, truck lay-bys, and small-scale industrial facilities. Ribbon development generates fragmented rural landscapes, transport congestion during industrial shift hours, and linear encroachment into roadside agricultural fields (Burchell & Listokin, 1978; Herold et al., 2005).

**Scattered Development** is evident in peripheral settlements — Basavanahalli, Halekote, Hanumanthapura, and Madanayakanahalli — where isolated residential layouts, workshops, and warehouses have emerged amidst agricultural fields in a discontinuous, non-contiguous pattern. This morphology disrupts agricultural continuity, weakens village social networks, and increases infrastructure costs (Ewing, Pendall & Chen, 2002).

**Industrial-Driven Agricultural Conversion** is most pronounced in Sompura and Kyalanur, where croplands were rapidly transformed into industrial sheds, truck terminals, and storage yards — a process that has diminished traditional farming practices and reduced groundwater recharge zones critical to the Arkavathi basin (Tacoli, 2003; Ravindra et al., 2017).

**Eco-Sensitive Edge Development** is emerging near Shivagange Hill slopes, where industrial spillover meets tourism and religious landscape infrastructure. Resorts, hospitality units, and roadside establishments are expanding into ecologically and culturally sensitive terrain, raising concerns about biodiversity, carrying capacity, and landscape aesthetics (Douglas, 2006).

**Figures 13–14** | *Google Earth Pro imagery (2011 and 2024) of agricultural land in the Dabaspet buffer. Coconut and arecanut plantations in Basavanahalli and Halekote have been replaced by industrial sheds and warehouses. Paddy and ragi fields in Sompura and Madanayakanahalli have given way to residential layouts and small-scale industries. Fragmentation of field boundaries and topsoil loss are evident in the 2024 image.*

**Figures 15–16** | *Google Earth Pro imagery (2011 and 2024) of built-up area expansion. Industrial complexes, logistics hubs, and worker housing have densified in Thyamagondlu, Sompura, and Madanayakanahalli. Ribbon development along NH-48 with commercial units and service facilities is pronounced in the 2024 image. Impervious surface expansion has reduced infiltration capacity across the central zone.*

**Figures 17–18** | *Google Earth Pro imagery (2011 and 2024) of waterbodies in the study domain. Basavanahalli Kere, Thyamagondlu Kere, and Sompura Kere show reduced water spread, encroached margins, and degraded buffer vegetation. Kyalanur Kere displays weed infestations and eutrophication; Madanayakanahalli Kere shows seasonal drying. Partial recovery of open water area is visible in 2024 following rejuvenation interventions.*

---

## 4. Discussion

### 4.1 Drivers and Rate Structure of Built-Up Expansion

The sixfold expansion of built-up land from 3.24% (2004) to 19.23% (2024) reflects a two-phase industrial investment cycle. The initiation phase (2004–2014) corresponds to KIADB Phases I and II development, the entry of initial anchor industries, and associated residential and commercial growth along NH-48, producing a 7.21 percentage-point built-up gain. The consolidation phase (2014–2024) generated an additional 8.78-point gain as industrial estates extended into peripheral villages and secondary development followed established corridors — consistent with a momentum-driven model where infrastructure investment creates self-reinforcing peri-urban expansion (Allen, 2003; UN-Habitat, 2020). The rate acceleration between phases suggests that planning mechanisms have not kept pace with market-driven conversion.

### 4.2 Cropland Loss as Structural Agricultural Capital Destruction

The net loss of 32.97 km² of cropland (−18.54%) represents not merely a land cover change but the destruction of agricultural capital — fertile Vertisol and Alfisol soils, irrigation infrastructure, and accumulated agronomic knowledge embedded in farming communities of Thyamagondlu, Shivapura, and Somadevanahalli. Paddy, ragi, and horticultural crops replaced by industrial and residential uses cannot be recovered at comparable cost or timeframe. The economic implications — reduced local food production, groundwater depletion, and livelihood restructuring of farming households — extend far beyond the spatial footprint documented in this study (Tacoli, 2003; Ravetz et al., 2013).

### 4.3 Waterbody Collapse, Partial Recovery, and Ecological Function

Waterbody coverage declined from 10.20 km² (4.84%) to 6.61 km² (2.95%) between 2004 and 2014 — a 35% reduction in open water extent concentrated in the decade of maximum industrial construction activity. The primary mechanisms were encroachment of built-up land onto tank margins, blockage of seasonal feeder channels by road construction, and increased sedimentation from disturbed catchments (Douglas, 2006; Shaw & Satish, 2018). The partial recovery to 7.10 km² (3.17%) by 2024 reflects state-funded rejuvenation under Karnataka lake restoration programmes. However, remote sensing captures open water extent but cannot distinguish healthy, ecologically functional tanks from impounded water in structurally compromised systems. Field observations confirm weed infestations, eutrophication, and wastewater discharge in several tanks, indicating that ecological functionality remains impaired despite area recovery.

### 4.4 Mixed Forest Vegetation: Loss, Collapse, and Partial Restoration

The near-elimination of mixed forest vegetation from 8.47 km² (4.01%) in 2004 to 0.95 km² (0.43%) in 2014 — representing a 89% reduction in one decade — constitutes the most severe single-class loss in relative terms. This collapse reflects systematic clearing of residual forest patches for industrial construction. The partial recovery to 5.59 km² (2.50%) by 2024 through industrial greenbelt obligations and afforestation near Thyamagondlu represents a compensatory trend, though the species composition and ecological connectivity of these planted areas are unlikely to replicate the structure and function of the cleared mixed vegetation.

### 4.5 Scrub Forest Dynamics as an Indicator of Transitional Land Status

The expansion of scrub forest from 2.30 km² (1.09%) to 25.52 km² (11.39%) between 2004 and 2014, followed by contraction to 20.38 km² (9.10%) by 2024, provides a spatial signal of transitional land in the conversion pipeline. The 2014 peak corresponds to abandoned and cleared agricultural land that had not yet been developed for industrial or residential use — a transient state that subsequent construction has reduced. Residual scrub categories in 2024 represent marginal, non-arable lands and interstitial spaces within the expanding built-up matrix.

### 4.6 Environmental Consequences

The cumulative LULC transition has generated three categories of environmental consequence. Hydrological disruption — reduced infiltration from 36.25 km² of new impervious surface, altered drainage patterns, declining groundwater recharge — represents the most pervasive impact, affecting agricultural water availability and domestic supply across the buffer zone (Seto et al., 2011; Douglas, 2006). Agricultural ecosystem fragmentation — disrupted field boundaries, loss of mixed cropping systems, removal of vegetated tank bunds — has weakened agro-ecological resilience and reduced biodiversity at the landscape scale. Water quality degradation — eutrophication, industrial effluent discharge, and sedimentation in surviving tanks — threatens the residual ecological and cultural functions of traditional tank irrigation systems that are irreplaceable in the Arkavathi basin context (Shaw & Satish, 2018).

### 4.7 Methodological Strengths and Limitations

Consistency across the IRS Resourcesat sensor family minimises inter-epoch spectral inconsistencies. High classification accuracy (96.37%, κ = 0.9657), per-class accuracy metrics, and GPS field validation at multiple waypoints confirm result reliability. Limitations include: restricted temporal resolution (three epochs over 20 years) limiting detection of sub-annual variation; Level-II classification inability to distinguish built-up land functions (industrial vs. residential vs. road); optical sensor limitation precluding vegetation health or soil moisture assessment; and study scope restricted to 2024, precluding assessment of post-announcement BCIC expansion implications.

---

## 5. Conclusion

### 5.1 Synthesis

The Dabaspet Industrial Corridor has undergone a decisive structural transformation from an agrarian landscape (82.9% agricultural in 2004) to a peri-urban industrial zone (19.23% built-up in 2024) over two decades. Built-up land expanded by 36.25 km² — a sixfold increase — while cropland contracted by 32.97 km² and mixed forest vegetation collapsed by 89% before partial greenbelt-driven recovery. Waterbody infrastructure declined to a 2014 nadir before marginal recovery under state rejuvenation, while scrub forest expansion and contraction traces the temporal arc of transitional land in the development pipeline. Four spatially distinct sprawl morphologies — ribbon development along NH-48 and NH-648, scattered peripheral layouts, industrial-driven agricultural conversion at Sompura and Kyalanur, and eco-sensitive edge development near Shivagange Hills — operate simultaneously and require differentiated governance responses. IRS Resourcesat multi-temporal supervised classification (96.37% accuracy, κ = 0.9657) proves robust for tracking such transitions in rapidly industrialising peri-urban domains.

### 5.2 Policy Imperatives

Four evidence-based policy priorities emerge from this study. First, legal buffer zone designation around surviving waterbodies and remnant mixed forest patches must be embedded in KIADB estate approval conditions and the Bengaluru Metropolitan Region Development Authority planning framework, independent of compensatory greenbelt targets that have demonstrably failed to prevent encroachment. Second, terrain-sensitive zoning must direct industrial and residential expansion to flat constructible land and restrict development in steep slopes, tank command areas, and seasonal drainage corridors — areas that are best managed as ecological infrastructure. Third, hydrological connectivity impact assessment must be mandatory for all new industrial development proposals, incorporating modelled effects on runoff, recharge, and downstream tank water balances rather than relying on area-based greenbelt requirements alone. Fourth, institutionalised geospatial monitoring at five-year intervals — integrating LULC change, land surface temperature, NDVI, and tank water spread from IRS or Sentinel imagery — must be established within KSRSAC and KSPCB reporting frameworks to provide an evidence base for adaptive governance and early detection of regulatory non-compliance.

---

## Funding Statement

This research received no external funding. The work constitutes partial fulfilment of the Master of Science in Environmental Science, Bangalore University.

## Declaration of Competing Interests

The authors declare no competing interests.

## Author Contributions

Bindu V: conceptualisation, data acquisition, image classification, field validation, analysis, and writing. Dr. Hemanjali A.M.: supervision, methodology guidance, and manuscript review.

## Data Availability

IRS Resourcesat imagery is available from Karnataka State Remote Sensing Applications Centre (KSRSAC), Bengaluru. Ground-truth GPS waypoints and confusion matrix data are available from the corresponding author on reasonable request.

---

## References

Allen, A. (2003). Environmental planning and management of the peri-urban interface. *Environment and Urbanization*, 15(1), 135–148.

Anderson, J. R., Hardy, E. E., Roach, J. T., & Witmer, R. E. (1976). *A Land Use and Land Cover Classification System for Use with Remote Sensor Data* (Vol. 964). U.S. Geological Survey.

Angel, S., Parent, J., Civco, D. L., Blei, A., & Potere, D. (2011). The dimensions of global urban expansion. *Progress in Planning*, 75(2), 53–107.

Belgiu, M., & Csillik, O. (2018). Sentinel-2 cropland mapping using pixel-based and object-based time-weighted dynamic time warping analysis. *Remote Sensing of Environment*, 204, 509–523.

Bhatta, B., Saraswati, S., & Bandyopadhyay, D. (2010). Urban sprawl measurement from remote sensing data. *Applied Geography*, 30(4), 731–740.

Burchell, R. W., & Listokin, D. (1978). *The Fiscal Impact Handbook*. Center for Urban Policy Research, Rutgers University.

Chen, J., Chen, J., Liao, A., Cao, X., Chen, L., Chen, X., & Mills, J. (2020). Global land cover mapping at 30 m resolution: A POK-based operational approach. *ISPRS Journal of Photogrammetry and Remote Sensing*, 103, 7–27. https://doi.org/10.1016/j.isprsjprs.2014.09.002

Douglas, I. (2006). Peri-urban ecosystems and societies: Transitional zones and contrasting values. In D. McGregor, D. Simon, & D. Thompson (Eds.), *The Peri-Urban Interface* (pp. 18–29). Earthscan.

Ewing, R., Pendall, R., & Chen, D. (2002). *Measuring Sprawl and Its Impact*. Smart Growth America.

FAO. (2020). *Global Forest Resources Assessment 2020: Main Report*. Food and Agriculture Organization of the United Nations. https://doi.org/10.4060/ca9825en

Foody, G. M. (2020). Explaining the unsuitability of the kappa coefficient in the assessment and comparison of the accuracy of thematic maps. *Remote Sensing of Environment*, 239, 111630.

Government of Karnataka. (2020). *Karnataka Industrial Policy 2020–25*. Department of Industries and Commerce.

Hansen, M. C., Potapov, P. V., Moore, R., Hancher, M., Turubanova, S. A., Tyukavina, A., & Townshend, J. R. G. (2013). High-resolution global maps of 21st-century forest cover change. *Science*, 342(6160), 850–853. https://doi.org/10.1126/science.1244693

Herold, M., Goldstein, N. C., & Clarke, K. C. (2005). The spatiotemporal form of urban growth: measurement, analysis and modeling. *Remote Sensing of Environment*, 86(3), 286–302.

IPBES. (2019). *Global Assessment Report on Biodiversity and Ecosystem Services*. Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services.

IPCC. (2019). *Climate Change and Land: Summary for Policymakers*. Intergovernmental Panel on Climate Change.

Jat, M. K., Garg, P. K., & Khare, D. (2008). Monitoring and modelling of urban sprawl using remote sensing and GIS techniques. *International Journal of Applied Earth Observation and Geoinformation*, 10(1), 26–43.

Jensen, J. R. (2016). *Introductory Digital Image Processing: A Remote Sensing Perspective* (4th ed.). Pearson.

Lambin, E. F., Geist, H. J., & Lepers, E. (2003). Dynamics of land-use and land-cover change in tropical regions. *Annual Review of Environment and Resources*, 28, 205–241.

Li, W., Wang, X., & Chen, L. (2017). Impacts of land use/land cover change on ecosystem services in the ecotone between agriculture and grazing in China. *Journal of Cleaner Production*, 153, 618–627.

Lillesand, T. M., Kiefer, R. W., & Chipman, J. W. (2015). *Remote Sensing and Image Interpretation* (7th ed.). John Wiley & Sons.

Lu, D., & Weng, Q. (2007). A survey of image classification methods and techniques for improving classification performance. *International Journal of Remote Sensing*, 28(5), 823–870. https://doi.org/10.1080/01431160600746456

NRSC. (2020). *Land Use Land Cover Atlas of India using Resourcesat-2 LISS-III Data*. National Remote Sensing Centre, ISRO.

Olofsson, P., Foody, G. M., Herold, M., Stehman, S. V., Woodcock, C. E., & Wulder, M. A. (2014). Good practices for estimating area and assessing accuracy of land change. *Remote Sensing of Environment*, 148, 42–57.

Pontius, R. G., & Millones, M. (2011). Death to Kappa: birth of quantity disagreement and allocation disagreement for accuracy assessment. *International Journal of Remote Sensing*, 32(15), 4407–4429.

Potapov, P., et al. (2022). Global maps of cropland extent and change show accelerated cropland expansion in the twenty-first century. *Nature Food*, 3(1), 19–28. https://doi.org/10.1038/s43016-021-00429-z

Ramesh, T., Kumar, R. M., & Gowda, H. S. (2020). Assessing the environmental impacts of industrial growth in peri-urban Bengaluru using spatial planning tools. *Journal of Urban and Environmental Planning*, 24(3), 112–126.

Ravetz, J., Fertner, C., & Nielsen, T. S. (2013). The dynamics of peri-urbanization. In K. Nilsson et al. (Eds.), *Peri-Urban Futures: Scenarios and Models for Land Use Change in Europe* (pp. 13–44). Springer.

Ravindra, A., Prakash, K. R., & Shekhar, S. (2017). Industrial development and spatial expansion: A case study of Dobaspet, Karnataka. *Indian Journal of Regional Development*, 19(2), 47–58.

Richards, J. A., & Jia, X. (2006). *Remote Sensing Digital Image Analysis* (4th ed.). Springer.

Roy, P. S., Joshi, P. K., & Chakraborty, S. (2021). Urbanization dynamics and its impact on land use/land cover: A case study of major cities in India. *Sustainable Cities and Society*, 68, 102770.

Seto, K. C., Güneralp, B., & Hutyra, L. R. (2012). Global forecasts of urban expansion to 2030 and direct impacts on biodiversity and carbon pools. *Proceedings of the National Academy of Sciences*, 109(40), 16083–16088. https://doi.org/10.1073/pnas.1211658109

Seto, K. C., et al. (2011). A meta-analysis of global urban land expansion. *PLoS ONE*, 6(8), e23777.

Shaw, R., & Satish, M. (2018). Tank irrigation and ecosystem services in Karnataka: Historical and contemporary perspectives. *Water Policy*, 20(3), 512–527.

Song, X. P., Hansen, M. C., Stehman, S. V., Potapov, P. V., Tyukavina, A., Vermote, E. F., & Townshend, J. R. (2018). Global land change from 1982 to 2016. *Nature*, 560(7720), 639–643. https://doi.org/10.1038/s41586-018-0411-9

Sudhira, H. S., Ramachandra, T. V., & Jagadish, K. S. (2004). Urban sprawl: metrics, dynamics and modelling using GIS. *International Journal of Applied Earth Observation and Geoinformation*, 5(1), 29–39.

Tacoli, C. (2003). The links between urban and rural development. *Environment and Urbanization*, 15(1), 3–12.

UN. (2015). *Transforming Our World: The 2030 Agenda for Sustainable Development*. United Nations.

UN-Habitat. (2020). *World Cities Report 2020: The Value of Sustainable Urbanization*. United Nations Human Settlements Programme.

Webster, D. (2002). *On the Edge: Shaping the Future of Peri-Urban East Asia*. Stanford University Asia-Pacific Research Center.

---

## Citation Issues Log — Pre-Submission Checklist

| # | Issue | Details | Action Required |
|---|---|---|---|
| 1 | Ravindra et al. (2017) — two entries | Two differently titled Ravindra et al. (2017) citations in references (journal article vs. different title). Verify which applies where cited in text. | Reconcile to single correct entry |
| 2 | Chen et al. (2020) — duplicated | Listed twice with slightly different author lists; DOI points to 2014 publication. Verify year. | Confirm correct year (2014 or 2020) |
| 3 | Seto et al. (2011) vs (2012) — mismatch | Text cites Seto et al. (2011) and (2012) as distinct; reference list has both. Verify they are genuinely separate publications. | Confirm both are correct entries |
| 4 | Foley et al. (2005) — cited in references but not in text | Listed in reference list; no in-text citation found. | Remove or add in-text citation |
| 5 | Galster et al. (2001) — missing from reference list | Cited in sprawl section; absent from references. | Add full citation |
| 6 | Daniels (1999) and Ewing (1997) — missing | Cited in sprawl section; absent from references. | Add full citations |
| 7 | Roy et al. (2015) — year discrepancy | Methodology cites Roy et al. (2015); reference list has Roy et al. (2021) and Roy et al. (2020). Confirm correct year for accuracy assumption statement. | Verify |
| 8 | Congalton & Green (2009) — missing | Cited in accuracy section; absent from reference list. | Add full citation |
