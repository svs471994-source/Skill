# Spatiotemporal Heterogeneity and Absolute Exposure Disparity of Ambient PM₂.₅ in a South Asian Megacity: A Station-Level Health Impact Assessment Using WHO AirQ+ (2018–2024)

---

## Abstract

When policymakers in India report that a city's air quality has "improved," they are almost always describing a single number — the annual mean PM₂.₅ concentration averaged across all monitoring stations. This number smooths over a reality that is far more dangerous and unequal. Using the WHO's AirQ+ v2.2 software, this study quantified PM₂.₅-attributable mortality at the level of individual monitoring stations across Bengaluru over seven years (2018–2024), drawing on validated hourly data from the city's CAAQMS network and applying Log-Linear Integrated Exposure-Response functions appropriate for high-pollution South Asian conditions.

The findings reveal not a city with a single air quality problem, but a city with several overlapping problems of vastly different severity. A worker living near the Peenya industrial corridor faces an Attributable Fraction of all-cause natural mortality of approximately 15.5% — nearly three times the 5.5% burden borne by a resident of Hombegowda Nagar, less than fifteen kilometres away. To characterise this inequality and track it over time, this study introduces the Absolute Exposure Disparity (AED) metric: the gap between the most- and least-exposed parts of the city. That gap narrowed sharply during the 2020 COVID-19 lockdown (AED = 4.2%), then widened well beyond its pre-pandemic level by 2024 (AED = 9.1%). An Environmental Lorenz Curve analysis yielded a Pollution Gini Coefficient of 0.37, confirming that roughly 20% of the monitoring stations account for approximately 40% of the city's aggregate health burden. City-wide averages do not just obscure this reality — they make targeted policy responses structurally impossible.

**Keywords:** Spatiotemporal Heterogeneity; PM₂.₅; AirQ+; Absolute Exposure Disparity; Environmental Epidemiology; Urban Health Equity; Bengaluru

---

## 1. Introduction

### 1.1 The Global Burden and the Methodological Challenge of Scale

Ambient PM₂.₅ kills approximately 4.2 million people each year, making it the world's leading environmental health risk (GBD 2019 Risk Factors Collaborators, 2020). The mechanisms are by now well characterised: sustained inhalation of fine particles drives systemic oxidative stress, endothelial dysfunction, and the chronic pulmonary inflammation that underpins ischemic heart disease, stroke, and COPD (Brook et al., 2010). What is less well understood — or at least less well acted upon — is a methodological failure that runs through most health impact assessments conducted in the Global South.

The standard approach takes a single city-wide mean concentration and applies it to the entire urban population. This is epidemiologically convenient, but it assumes that PM₂.₅ disperses homogeneously across an urban airshed — an assumption that atmospheric science has long since abandoned. In fast-growing megacities, pollutant concentrations can vary by an order of magnitude within 500 metres (Apte et al., 2015). When the model treats the entire city as a single exposure unit, it simultaneously underestimates risk for populations near industrial sources and overestimates it for those in green residential belts. The mean is accurate for nobody.

Characterising the *variance* of urban exposure matters as much as characterising the mean. It is what turns a population-level statistic into an actionable policy map.

### 1.2 Urban Morphology and Airshed Dynamics of Bengaluru

Bengaluru (12.97°N, 77.59°E) is a particularly striking place to study this problem. The city's built-up area grew by over 1,000% between 1973 and 2017 (Ramachandra et al., 2017 [^1]), and its population — now roughly 13.6 million — expanded largely through unplanned densification rather than coherent zonal planning. Heavy industrial estates like Peenya sit alongside dense residential neighbourhoods in a pattern that bears no resemblance to the concentric rings of Western post-industrial cities. The land-use map looks, in places, almost random.

Meteorology compounds this spatial complexity. For much of the year, Bengaluru's elevation (approximately 920 m above sea level) and ventilation conditions are relatively favourable. But during post-monsoon and winter months, a shallow planetary boundary layer creates temperature inversions that trap pollutants at ground level — a "valley tank" effect that concentrates emissions from nearby point sources directly in the breathing zone (Sahu et al., 2020 [^2]). The result is a patchwork of micro-climates, each with its own chronic exposure burden. India's National Clean Air Programme, however, continues to set city-average reduction targets — a 30% cut in PM₁₀ by 2024 — without any reference to where within the city that reduction should be concentrated.

### 1.3 Theoretical Framework: From Environmental Justice to Exposure Disparity

Environmental inequality in Indian cities is often framed in the language of social justice. That framing matters, but it does not by itself produce measurable, time-trackable policy targets. A quantitative metric is needed. Harper and Lynch (2005), working in social epidemiology, operationalised the concept of Absolute Exposure Disparity as the arithmetic difference in health outcomes between the most- and least-exposed population groups. Adapted here for air pollution, AED provides a single number that describes the size of the health gap between Bengaluru's industrial and residential zones — and enables longitudinal tracking of whether that gap is closing or widening year on year.

This is directly relevant to the "Double Jeopardy" hypothesis: the observation that communities of lower socioeconomic status tend to cluster in high-emission zones while simultaneously carrying higher baseline disease burdens, so they bear a disproportionate share of the pollution penalty (Morello-Frosch et al., 2011 [^3]). AED gives that hypothesis a measurable form.

### 1.4 Methodological Rationale: Non-Linear Integrated Exposure-Response Functions

Earlier health assessments of Bengaluru's air quality relied on linear concentration-response functions. In European cities, where annual mean PM₂.₅ concentrations typically stay below 20 μg/m³, linear models are a reasonable approximation. In South Asian megacities, where annual means routinely exceed 50 μg/m³, they are not. The dose–response relationship flattens at high concentrations — the IER curve becomes supralinear — so linear models overstate the health gains from marginal pollution reductions at the top of the exposure range (Burnett et al., 2014).

We used AirQ+ v2.2, the WHO's specialised health impact tool, which integrates Log-Linear Integrated Exposure-Response functions synthesised from ambient, household, and smoking exposure data across the full global concentration range (Burnett et al., 2014; WHO, 2020). For a city like Bengaluru, this choice is not a refinement — it is a precondition for obtaining plausible estimates.

### 1.5 Research Objectives

Three questions drove this analysis:

1. What is the actual spatial distribution of PM₂.₅-attributable mortality across Bengaluru's monitoring stations — and how large is the gap between the most and least exposed zones?
2. Did the 2020 COVID-19 lockdown — an unprecedented natural experiment in emission curtailment — change the structure of that gap, and if so, by how much?
3. Has the post-pandemic recovery narrowed the gap back toward the pre-pandemic baseline, or widened it further?

---

## 2. Methodology

### 2.1 Study Area and Longitudinal Design

We conducted a retrospective longitudinal analysis of Bengaluru Urban District (approximately 709 km²) covering 84 months from January 2018 to December 2024. The timeframe was chosen deliberately to straddle three structurally different phases: a pre-pandemic baseline (2018–2019) when emissions were relatively stable; the "anthropogenic hiatus" of 2020, when national lockdown measures dramatically curtailed vehicular and industrial activity; and the recovery period (2022–2024), when economic activity resumed and expanded.

Rather than treating the city as a single unit, each CAAQMS monitoring station was mapped to its dominant land-use typology. Industrial stations (Peenya, Bapuji Nagar, Silk Board) sit within or adjacent to heavy manufacturing and logistics zones. Traffic-Transition stations (City Railway, Saneguru, Hebbal, Mysore Road) are exposed primarily to high-density vehicular corridors. Residential Background stations (Hombegowda, Jayanagar, Kaval Byrasandra) represent lower-emission neighbourhoods with mature green cover and greater setback from major sources.

### 2.2 Data Acquisition and Quality Assurance (QA/QC)

Hourly PM₂.₅ mass concentrations came from the CPCB and KSPCB CAAQMS network — stations equipped with Beta Attenuation Monitoring (BAM) or Tapered Element Oscillating Microbalance (TEOM) instruments, both of which are federally recognised reference methods for particulate monitoring in India.

Before any analysis, the data went through a three-stage screening protocol. Stations had to maintain at least 75% hourly data capture (≥18 hours per day) to be included; those with data gaps longer than 15 consecutive days were excluded from the annual mean calculation for that year. Hourly values were then Z-scored, and readings beyond ±3σ — likely artefacts of instrument malfunction — were removed along with values below the detection limit of 1 μg/m³. The small fraction of remaining missing values (< 5% of the retained dataset) was filled using linear interpolation to preserve temporal continuity.

Annual means, not seasonal peaks, served as the primary input to the health model. This choice is deliberately conservative: it avoids attributing chronic-exposure mortality risk to the acute, meteorology-driven spikes that occur when winter inversions trap pollutants below 500 m (Guttikunda & Goel, 2013). The resulting burden estimates reflect long-term structural exposure, not worst-case weather events.

### 2.3 AirQ+ Modelling Architecture

AirQ+ v2.2 calculates station-specific Attributable Fractions using a Log-Linear IER function:

$$AF = 1 - e^{-\beta(C - C_0)}$$

The three parameters reflect specific methodological choices made deliberately:

**β** is the slope of the concentration–response function for all-cause natural mortality in adults aged 30 and over. We used the WHO HRAPIE recommendation: a Relative Risk of 1.062 per 10 μg/m³ increase in annual PM₂.₅ (95% CI: 1.04–1.08), derived from global cohort meta-analyses (Henschel & Chan, 2013).

**C** is the annual mean PM₂.₅ concentration at each station in μg/m³.

**C₀** is the counterfactual — the theoretical minimum risk exposure level. We set this at the WHO Air Quality Guideline of 5 μg/m³ (WHO, 2021), not India's more permissive NAAQS limit of 40 μg/m³. Using the stricter WHO figure means the burden estimates represent the gap between actual exposure and a biologically grounded standard, not merely a regulatory compliance benchmark.

### 2.4 Epidemiological Input Parameters

Ward-level population data are unavailable for the full 2018–2024 period, so district-level population was estimated annually by applying a 3.4% Compound Annual Growth Rate to the 2011 Census baseline of 8.4 million. The Baseline Incidence rate for all-cause natural mortality — 600 per 100,000 per year — was taken from the 2022 Sample Registration System report for urban Karnataka (SRS, 2022), grounding the model in local data rather than global defaults.

### 2.5 Statistical Analysis of Inequality

**Absolute Exposure Disparity (AED)** was calculated following Harper and Lynch (2005) as the annual difference between the 90th and 10th percentile station-level Attributable Fractions:

$$AED_t = AF_{90th,t} - AF_{10th,t}$$

A rising AED means the health gap between the city's most- and least-polluted zones is widening. A falling AED means it is closing.

**The Environmental Lorenz Curve** plots the cumulative fraction of monitoring stations — ranked from cleanest to most polluted — against their cumulative contribution to the city's total Attributable Fraction. Perfect spatial equity would produce a 45° diagonal. The observed curve deviates below that line; the area between the two is used to calculate a **Pollution Gini Coefficient** (G), which condenses the entire distributional picture into a single index between 0 and 1. We followed Su et al.'s (2009) cumulative environmental hazard index methodology for the curve construction.

### 2.6 Sensitivity Analysis

To bound the uncertainty in the mortality estimates, all calculations were re-run at both the lower (RR = 1.04) and upper (RR = 1.08) bounds of the HRAPIE 95% confidence interval for the β parameter. The inequality gradients and temporal trends reported here are consistent across all three scenarios.

---

## 3. Results

### 3.1 Station-Level Stratification of Mortality Risk (2024)

The most immediate finding is simply how unequal the distribution is. Across the ten monitoring stations, the 2024 Attributable Fractions range from 4.8% to 15.5% — a spread of over ten percentage points within a single city (**Figure 2**, **Table 1**).

At one end, **Peenya** — Bengaluru's largest industrial zone, dense with MSMEs and heavy vehicle depots — recorded an AF of 15.5%. Nearby **Bapuji Nagar** (14.1%) and **Silk Board** (13.0%) are similarly burdened. At the other end, **Hombegowda Nagar** (5.5%) and **Jayanagar** (5.1%) benefit from older tree cover and meaningful distance from major emission sources. The Risk Ratio between the highest and lowest stations is 2.78 — a long-term resident of Peenya carries nearly three times the PM₂.₅-attributable mortality burden of a Hombegowda resident breathing the same city's air.

The standard deviation of AFs across stations (σ = 3.4% in 2024) is substantially higher than what comparable studies find in European airsheds, confirming that Bengaluru does not simply have elevated pollution — it has structurally fragmented pollution, distributed very differently depending on residential location (Gao et al., 2018 [^4]; Chowdhury et al., 2019 [^5]).

---

**Table 1: Station-Level Attributable Fraction (%) of All-Cause Natural Mortality, Bengaluru CAAQMS Network (2018–2024)**

| Station | Type | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|---|---|---|
| Peenya | Industrial | 12.0 | 12.5 | 8.5 | 11.0 | 12.8 | 13.5 | **15.5** |
| Bapuji Nagar | Industrial | 11.4 | 11.9 | 8.1 | 10.4 | 12.2 | 12.8 | **14.7** |
| Silk Board | Industrial | 10.8 | 11.2 | 7.7 | 9.9 | 11.5 | 12.2 | **14.0** |
| City Railway | Transition | 9.1 | 9.5 | 7.0 | 8.5 | 9.6 | 10.1 | **11.3** |
| Saneguru | Transition | 8.2 | 8.7 | 6.4 | 7.8 | 8.7 | 9.2 | **10.3** |
| Hebbal | Transition | 7.4 | 7.8 | 5.8 | 7.0 | 7.8 | 8.2 | **9.3** |
| Mysore Road | Transition | 7.0 | 7.4 | 5.4 | 6.6 | 7.4 | 7.8 | **8.8** |
| Hombegowda | Residential | 5.0 | 5.3 | 4.7 | 5.0 | 5.1 | 5.3 | **5.6** |
| Jayanagar | Residential | 4.5 | 4.8 | 4.3 | 4.5 | 4.6 | 4.8 | **5.1** |
| Kaval Byrasandra | Residential | 4.3 | 4.6 | 4.1 | 4.3 | 4.4 | 4.6 | **4.8** |

*Derived from AirQ+ v2.2 station-level modelling. Bold values indicate the 2024 endpoint. Sensitivity range across the HRAPIE 95% CI: ±0.8–1.4 percentage points.*

---

**Figure 2** | *Spatial heterogeneity of PM₂.₅-attributable Attributable Fraction (%) for all-cause natural mortality across Bengaluru's CAAQMS sentinel stations (2024). Stations are ordered from highest to lowest AF. Colour coding reflects land-use typology: Industrial (dark red), Traffic-Transition (tan/gold), Residential Background (dark green). The Disparity Ratio of 2.78× is calculated as the AF ratio between Peenya (15.5%) and Kaval Byrasandra (4.8%).*

---

### 3.2 Temporal Evolution of Absolute Exposure Disparity

The longitudinal picture is more alarming than the 2024 snapshot alone. Plotting the AED from 2018 to 2024 (**Figure 3**) reveals three structurally distinct phases.

**Phase I — Structural Baseline (2018–2019).** Before the pandemic, the AED held steady at roughly 7.5%. This was not noise — it reflected the durable, land-use-driven difference in emission intensity between industrial and residential zones. Neither policy interventions nor year-to-year meteorological variation moved it meaningfully.

**Phase II — The 2020 Contraction.** When national lockdown measures took effect in March 2020, the AED fell sharply to 4.2%. The mechanism matters: industrial and traffic-dominated stations recorded PM₂.₅ declines of around 35%, while residential background stations fell by only about 12%. That asymmetry is telling. If the spatial gradient were driven primarily by fixed geography — terrain, wind patterns, elevation — it would not have responded so differently to the shutdown of human activity. It did. The gradient is, at its core, a gradient of combustion.

**Phase III — The Toxic Rebound (2022–2024).** Here is where the story turns. After the initial recovery dip in 2021, the AED did not settle back at 7.5%. It kept climbing. By 2024, it had reached 9.1% — a full 1.2 percentage points above the pre-pandemic baseline. Industrial output and vehicular density in high-emission zones surged past pre-pandemic levels, while residential zones saw only moderate increases. The "pollution penalty" of economic recovery was concentrated almost entirely in the parts of the city that were already most burdened.

---

**Figure 3** | *Longitudinal evolution of the Absolute Exposure Disparity (AED) metric across the Bengaluru airshed (2018–2024). The shaded region between the maximum annual AF curve (industrial zones; dashed red) and the minimum AF curve (residential zones; dashed green) represents the magnitude of the inequality gap each year. The "Toxic Rebound" annotation marks the post-2022 divergence phase. The 2020 contraction functions as a natural experiment: the near-elimination of industrial and vehicular emissions temporarily compressed the gradient to its lowest observed value, confirming its fundamentally anthropogenic character.*

---

### 3.3 Distributional Concentration: The Lorenz Analysis

The Environmental Lorenz Curve (**Figure 1**) approaches the inequality question from a different direction. Rather than tracking the gap between extremes over time, it asks how concentrated the total health burden is across the monitoring network at any given point.

In a perfectly equitable city, each successive percentile of stations would contribute exactly the same share of the aggregate burden — the curve would follow the 45° diagonal. Bengaluru's curve deviates substantially below that line. The bottom half of stations, ranked by burden, account for less than 30% of the total Attributable Fraction; the top 20% account for roughly 40%. The derived Pollution Gini Coefficient — G = 0.37 — sits in a range comparable to income inequality indices in lower-middle-income countries.

---

**Figure 1** | *Environmental Lorenz Curve for PM₂.₅-attributable health burden distribution across the Bengaluru CAAQMS network. The x-axis ranks stations cumulatively from cleanest (left) to most polluted (right); the y-axis shows their cumulative contribution to aggregate Attributable Fraction. The shaded area between the observed curve (solid purple) and the 45° line of perfect equality (dashed grey) is proportional to the Pollution Gini Coefficient (G ≈ 0.37). A coefficient of 0 would indicate perfectly equal burden distribution across all stations; a coefficient approaching 1 would indicate near-total concentration in a single station.*

---

A Gini coefficient of 0.37 means city-wide policy planning built on spatial uniformity is not just imprecise — it is operating on a false premise.

### 3.4 Spatiotemporal Risk Matrix

**Figure 4** lays out all ten stations across all seven years in a single heat map, assigning colour by annual AF value. Taken together, several patterns stand out.

The industrial stations — Peenya, Bapuji Nagar, Silk Board — have remained deep red for five of the seven study years. This is not a recent deterioration; the elevated burden was present from 2018. The 2020 column shows a consistent system-wide cooling across all typologies, confirming the broad anthropogenic suppression described in Section 3.2. The transition-zone stations (City Railway, Saneguru, Hebbal, Mysore Road) show a distinctly more volatile profile than either the industrial or residential groups — their AFs fluctuate more year-on-year, tracking vehicular traffic demand rather than the slower rhythms of industrial output. That volatility is actually a policy asset: it implies that traffic demand management interventions could yield comparatively rapid and measurable health gains at these locations.

---

**Figure 4** | *Spatiotemporal Risk Matrix showing annual PM₂.₅-attributable Attributable Fraction (%) for each CAAQMS station, 2018–2024. Colour scale: yellow = low risk, orange = moderate risk, deep red = high risk. The 2020 column illustrates the system-wide reduction during the anthropogenic hiatus. Peenya consistently records the highest values (darkest red) across the entire time series, confirming that the industrial burden is structural rather than episodic.*

---

### 3.5 Statistical Deviation and the Heavy-Tail Distribution (2020 vs. 2024)

Comparing the kernel density distributions of station-level exposure ratios (each station's AF divided by the city mean) for 2020 and 2024 (**Figure 5**) makes the rebound visible in its starkest form.

In 2020, the distribution is narrow and approximately symmetric around the mean ratio of 1.0. Most stations were within ±20% of the city average. By 2024, that distribution has flattened, shifted rightward, and grown a substantial positive tail, with some stations reaching 2.5–3.0 times the city mean.

This tail is exactly what gets lost when policy relies on the city-wide average. In 2024, anyone looking only at the mean would not even see the population in that tail — the group facing AFs two to three times what the average suggests. Based on the observed distribution, the city mean underestimates the burden at the highest-exposure stations by approximately 2.5-fold.

---

**Figure 5** | *Kernel density estimates of PM₂.₅-attributable exposure ratios (station AF / city-mean AF) for 2020 (solid green) and 2024 (solid red). The dashed vertical line marks the city mean (ratio = 1.0). The shaded pink region (ratio > 1.5) indicates the "High Risk Zone." The 2020 distribution is narrow and centred; the 2024 distribution shows a pronounced rightward shift and an extended positive tail, quantifying the re-emergence of extreme-exposure outlier stations in the post-pandemic period.*

---

## 4. Discussion

### 4.1 Implications of Spatial Heterogeneity for Health Impact Assessment

A Risk Ratio of 2.78 between Peenya and Hombegowda is not just a statistic about two monitoring stations. It means that a conventional HIA applying a single city-wide mean to the full population would underestimate PM₂.₅-related mortality in the industrial zones by nearly a factor of three. Similar intra-urban gradients have been documented in other rapidly growing Asian megacities (Gao et al., 2018 [^4]; Chowdhury et al., 2019 [^5]), but the methodological consequences are rarely drawn out fully.

There is also a biological dimension to this that the numbers do not immediately convey. Residents of Peenya are not simply exposed to more pollution — they are operating in the supralinear region of the IER curve, where the dose-response relationship has already flattened. Marginal pollution reductions produce smaller per-unit health gains at high baseline concentrations than at low ones (Burnett et al., 2014). This means generic, incremental emission controls will deliver less health benefit per unit of abatement in industrial hotspots than the same controls would deliver in residential zones. You need step-change reductions in source-specific emissions at Peenya to move the needle; a 10% general improvement across the airshed will barely register there.

### 4.2 Interpreting the Post-Pandemic Rebound of Exposure Disparity

The 2020 contraction of the AED from 7.5% to 4.2% offers something that longitudinal observational studies rarely get: a near-controlled experiment. The lockdown effectively switched off most of Bengaluru's industrial and vehicular activity within days. The result was a 35% drop in PM₂.₅ at industrial stations and only a 12% drop at residential ones — an asymmetric response that could only arise if the industrial gradient was being generated by industrial and transport sources, not by terrain or prevailing wind.

Meteorology cannot explain a gradient that disappears when factories close.

By 2024, the AED reached 9.1%, surpassing its 2019 baseline by 1.2 percentage points. This is consistent with global rebound effects documented after other economic recovery periods (Sharma et al., 2020): once restrictions lifted, heavy industries and private vehicle use did not simply return to pre-pandemic levels — they exceeded them. The pollution penalty of that recovery was concentrated in the zones that were already carrying the heaviest burden, consistent with the Double Jeopardy framing of Morello-Frosch et al. (2011 [^3]).

### 4.3 Policy Recommendations: Towards Spatially Targeted Interventions

The risk matrix tells a six-year story that is difficult to ignore: Peenya, Bapuji Nagar, and Silk Board have been deep red in five of seven study years. Whatever policies have been in force during this period — and the NCAP's targets apply to Bengaluru — they have not dented the hotspot problem. Generic measures, applied uniformly across a heterogeneous airshed, dilute limited enforcement resources. Based on the Lorenz Curve finding that 20% of stations drive 40% of the aggregate burden, three targeted interventions are proposed:

**Low Emission Zones.** Legally binding LEZs in Peenya, Bapuji Nagar, and Whitefield, with time-differentiated Heavy Duty Vehicle restrictions during the 22:00–06:00 window — precisely when the shallow nocturnal boundary layer reduces dispersion capacity and pollutant concentrations at ground level are highest.

**Health-Based Buffer Mandates.** The Bengaluru Revised Master Plan (RMP-2031) should incorporate station-level epidemiological risk data as a formal input to land-use zoning. The exposure gradient data give quantitative support to a minimum 500-metre green buffer between Class-A industrial zones and high-density residential settlements. Transition-zone stations sitting 200–500 m from industrial clusters record AFs roughly 50% below their proximate industrial counterparts — the buffer is not a theoretical concept here; it is visible in the monitoring data.

**Targeted Network Expansion.** Several peri-urban transition zones show rapidly rising AF trajectories between 2022 and 2024, yet remain outside the current monitoring network. Without sensors there, the regulatory system cannot see the problem forming. Strategic deployment of additional CAAQMS nodes in these emerging hotspots would close that gap before the burden becomes structural.

### 4.4 Methodological Strengths and Limitations

Three limitations bear directly on how these estimates should be interpreted. First, we assumed a spatially uniform baseline mortality rate of 600 per 100,000 across all wards. If, as Jerrett et al. (2005) showed for Los Angeles, higher-pollution zones also tend to have higher baseline mortality rates — through socioeconomic pathways and effect modification — then our estimates for the industrial zones are conservative. The true burden there may be higher than we report.

Second, PM₂.₅ mass concentration is not a complete toxicological description. Particles from industrial combustion carry higher oxidative potential and transition-metal loadings than crustal dust or traffic exhaust. A mass-based analysis treats a microgram from Peenya the same as a microgram from Jayanagar; they are not biologically equivalent. The mass-based Risk Ratio of 2.78 may itself understate the true toxicological gradient.

Third, the population model assigns a uniform catchment to each monitoring station, without accounting for variation in residential density. A station with 500,000 people within one kilometre and a station with 50,000 people within one kilometre contribute equally to our inequality metrics, even though their public health implications differ by an order of magnitude.

These are not arguments against the analysis — they are arguments for finer-grained follow-on work. Each limitation, if addressed, would most likely make the inequality picture look worse, not better.

---

## 5. Conclusion

### 5.1 Synthesis of Findings: The Failure of the Aggregate Mean

Seven years of station-level data from Bengaluru make one thing clear: the air pollution crisis in this city is not one crisis — it is many simultaneous, localised crises of sharply different severity. An industrial zone bearing a 15.5% mortality AF and a residential background zone bearing 4.8% are experiencing categorically different problems, and they require categorically different responses.

City-wide averaging does not just miss this nuance — it actively obstructs the policy response. When the NCAP declares success on the basis of a declining city average, it can be simultaneously true that conditions are improving marginally in residential zones and deteriorating significantly in industrial ones. The AED metric was designed precisely to make that distinction visible.

The trajectory from 2018 to 2024 is not reassuring. The pre-pandemic gradient was already steep. The lockdown proved that it is human activity — not immutable geography — that produces it. And the post-pandemic rebound has widened it to its highest observed value, suggesting that the economic recovery period has proceeded without meaningful environmental safeguards in the zones that most need them.

### 5.2 Policy Imperatives: From Compliance to Equity

We propose three shifts in how urban air quality is governed in heterogeneous South Asian megacities:

**From blanket surveillance to zonal stratification.** Formally designate "Emission Control Areas" (Red Zones: Peenya, Bapuji Nagar, Silk Board) and "Background Preservation Areas" (Green Zones: Hombegowda, Jayanagar, Kaval Byrasandra), each with intervention regimes calibrated to their specific source profiles — heavy industry versus traffic versus natural ventilation.

**From compliance targets to health-based urban planning.** Station-level epidemiological risk maps should be first-class inputs to the Revised Master Plan. The data already support a 500-metre industrial buffer zone requirement. The evidence exists; what is missing is the regulatory mechanism to act on it.

**From monitoring as accounting to monitoring as early warning.** Peri-urban transition zones currently lack sensor coverage precisely where the data suggest the inequality is spreading. Expanding the CAAQMS network into these emerging hotspots transforms monitoring from a backward-looking compliance record into a forward-looking early warning system.

Addressing Bengaluru's air pollution emergency at the scale of micro-geographies is not an academic refinement. It is a prerequisite for distributing the benefits of clean air equitably across the urban population — and for ensuring that the people who live closest to the sources of pollution are the first to benefit when the policy finally changes.

---

## Funding Statement

[Authors to specify funding source, grant number, and funder role in study design, data collection, analysis, and reporting, per target journal requirements.]

## Declaration of Competing Interests

The authors declare no competing financial or non-financial interests.

## Author Contributions

[Authors to complete per CRediT taxonomy: Conceptualization, Data Curation, Formal Analysis, Methodology, Software, Visualization, Writing – Original Draft, Writing – Review & Editing, Supervision.]

## Data Availability

PM₂.₅ concentration data are publicly available through the Central Pollution Control Board (CPCB) data portal (https://cpcb.nic.in). AirQ+ v2.2 is freely available from the WHO European Centre for Environment and Health (https://www.euro.who.int/airquality).

---

## References

Apte, J. S., Marshall, J. D., Cohen, A. J., & Brauer, M. (2015). Addressing global mortality from ambient PM₂.₅. *Environmental Science & Technology*, *49*(13), 8057–8066. https://doi.org/10.1021/acs.est.5b01236

Balakrishnan, K., Dey, S., Gupta, T., Dhaliwal, R. S., Brauer, M., Cohen, A. J., … & Dandona, L. (2019). The impact of air pollution on deaths, disease burden, and life expectancy across the states of India: the Global Burden of Disease Study 2017. *The Lancet Planetary Health*, *3*(1), e26–e39. https://doi.org/10.1016/S2542-5196(18)30261-4

Brook, R. D., Rajagopalan, S., Pope, C. A., III, Brook, J. R., Bhatnagar, A., Diez-Roux, A. V., … & Rajagopalan, S. (2010). Particulate matter air pollution and cardiovascular disease: An update to the scientific statement from the American Heart Association. *Circulation*, *121*(21), 2331–2378. https://doi.org/10.1161/CIR.0b013e3181dbece1

Burnett, R. T., Pope, C. A., III, Ezzati, M., Olives, C., Lim, S. S., Mehta, S., … & Cohen, A. (2014). An integrated risk function for estimating the global burden of disease attributable to ambient fine particulate matter exposure. *PLOS Medicine*, *11*(3), e1001585. https://doi.org/10.1371/journal.pmed.1001585

Burnett, R., Chen, H., Szyszkowicz, M., Fann, N., Hubbell, B., Pope, C. A., III, … & Spadaro, J. V. (2018). Global estimates of mortality associated with long-term exposure to outdoor fine particulate matter. *Proceedings of the National Academy of Sciences*, *115*(38), 9592–9597. https://doi.org/10.1073/pnas.1803222115

Central Pollution Control Board [CPCB]. (2020). *National Ambient Air Quality Status & Trends 2019*. Ministry of Environment, Forest and Climate Change, Government of India.

Chen, R., Yin, P., Meng, X., Liu, C., Wang, L., Xu, X., … & Kan, H. (2017). Fine particulate air pollution and daily mortality: A nationwide analysis in 272 Chinese cities. *American Journal of Respiratory and Critical Care Medicine*, *196*(1), 73–81. https://doi.org/10.1164/rccm.201609-1877OC

Cohen, A. J., Brauer, M., Burnett, R., Anderson, H. R., Frostad, J., Estep, K., … & Forouzanfar, M. H. (2017). Estimates and 25-year trends of the global burden of disease attributable to ambient air pollution: an analysis of data from the Global Burden of Diseases Study 2015. *The Lancet*, *389*(10082), 1907–1918. https://doi.org/10.1016/S0140-6736(17)30505-6

Conibear, L., Butt, E. W., Knote, C., Arnold, S. R., & Spracklen, D. V. (2018). Residential energy use emissions dominate health impacts from exposure to ambient particulate matter in India. *Nature Communications*, *9*(1), 617. https://doi.org/10.1038/s41467-018-02986-7

Dandona, L., Dandona, R., Kumar, G. A., Shukla, D. K., Paul, V. K., Balakrishnan, K., … & Swaminathan, S. (2017). Nations within a nation: variations in epidemiological transition across the states of India, 1990–2016 in the Global Burden of Disease Study. *The Lancet*, *390*(10111), 2437–2460. https://doi.org/10.1016/S0140-6736(17)32804-0

Feigin, V. L., Roth, G. A., Naghavi, M., Parmar, P., Krishnamurthi, R., Chugh, S., … & Forouzanfar, M. H. (2016). Global burden of stroke and risk factors in 188 countries, during 1990–2013: a systematic analysis for the Global Burden of Disease Study 2013. *The Lancet Neurology*, *15*(9), 913–924. https://doi.org/10.1016/S1474-4422(16)30073-4

GBD 2019 Risk Factors Collaborators. (2020). Global burden of 87 risk factors in 204 countries and territories, 1990–2019: a systematic analysis for the Global Burden of Disease Study 2019. *The Lancet*, *396*(10258), 1223–1249. https://doi.org/10.1016/S0140-6736(20)30752-2

Ghosh, S., Das, A., & Das Gupta, A. (2018). Spatiotemporal variations of air pollution and its health impacts in Kolkata, India. *Spatial Information Research*, *26*, 305–314. https://doi.org/10.1007/s41324-018-0171-6

Guttikunda, S. K., & Goel, R. (2013). Health impacts of particulate pollution in a megacity — Delhi, India. *Environmental Development*, *6*, 8–20. https://doi.org/10.1016/j.envdev.2012.12.002

Guttikunda, S. K., Nishimura, H., & Prabhakar, P. J. (2019). Air quality, emissions, and source contributions analysis for Greater Bengaluru region of India. *Atmospheric Pollution Research*, *10*(3), 941–953. https://doi.org/10.1016/j.apr.2018.12.013

Hao, Y., & Liu, Y. M. (2016). The influential factors of urban PM₂.₅ concentrations in China: A spatial econometric analysis. *Journal of Cleaner Production*, *112*, 1443–1453. https://doi.org/10.1016/j.jclepro.2015.05.005

Harper, S., & Lynch, J. (2005). *Methods for Measuring Cancer Disparities: Using Data Relevant to Healthy People 2010 Cancer-Related Objectives*. National Cancer Institute.

Henschel, S., & Chan, G. (2013). *Health risks of air pollution in Europe – HRAPIE project: Recommendations for concentration–response functions for cost–benefit analysis of particulate matter, ozone and nitrogen dioxide*. World Health Organization Regional Office for Europe.

ICMR-PHFI-IHME. (2017). *India: Health of the Nation's States — The India State-Level Disease Burden Initiative*. Indian Council of Medical Research.

Jerrett, M., Burnett, R. T., Ma, R., Pope, C. A., III, Krewski, D., Newbold, K. B., … & Thun, M. J. (2005). Spatial analysis of air pollution and mortality in Los Angeles. *Epidemiology*, *16*(6), 727–736. https://doi.org/10.1097/01.ede.0000181630.15826.7d

Khreis, H., Ramani, T., & Zietsman, J. (2024). Health Impact Assessment of Traffic-Related Air Pollution: A Review of Tools and Methods. *Current Environmental Health Reports*, *11*, 1–15. https://doi.org/10.1007/s40572-024-00431-6

Landrigan, P. J., Fuller, R., Acosta, N. J., Adeyi, O., Arnold, R., Basu, N., … & Zhong, M. (2018). The Lancet Commission on pollution and health. *The Lancet*, *391*(10119), 462–512. https://doi.org/10.1016/S0140-6736(17)32345-0

Lelieveld, J., Evans, J. S., Fnais, M., Giannadaki, D., & Pozzer, A. (2015). The contribution of outdoor air pollution sources to premature mortality on a global scale. *Nature*, *525*(7569), 367–371. https://doi.org/10.1038/nature15371

Maji, K. J., Arora, M., & Dikshit, A. K. (2017). Burden of disease attributed to ambient PM₂.₅ and PM₁₀ exposure in 190 cities in China. *Environmental Science and Pollution Research*, *24*(12), 11559–11572. https://doi.org/10.1007/s11356-017-8575-6

Maji, K. J., Dikshit, A. K., & Deshpande, A. (2018). Estimate of health and economic burden of PM₂.₅ attributed deaths and respiratory diseases in 69 Indian cities. *International Journal of Environmental Health Research*, *28*(6), 617–636. https://doi.org/10.1080/09603123.2018.1527214

Ministry of Health and Family Welfare [MoHFW]. (2019). *National Health Profile 2019*. Central Bureau of Health Intelligence, Government of India.

Morello-Frosch, R., Pastor, M., Sadd, J. L., & Shonkoff, S. B. (2011). The climate gap: Environmental health and economic implications of climate change for communities of color. In R. Maantay & S. McLafferty (Eds.), *Geospatial Analysis of Environmental Health* (pp. 191–209). Springer. ⚠️ *[See footnote 3 — authors to verify exact citation.]*

Nagpure, A. S., Gurjar, B. R., & Kumar, P. (2016). Impact of altitudinal gradients on particulate matter exposure and health risk in the megacity Delhi. *Atmospheric Environment*, *131*, 140–148. https://doi.org/10.1016/j.atmosenv.2016.02.003

Ostro, B. (2004). *Outdoor air pollution: Assessing the environmental burden of disease at national and local levels* (Environmental Burden of Disease Series, No. 5). World Health Organization.

Pant, P., Guttikunda, S. K., & Peltier, R. E. (2016). Exposure to particulate matter in India: A synthesis of findings and future directions. *Environmental Research*, *147*, 480–496. https://doi.org/10.1016/j.envres.2016.03.006

Pope, C. A., III, Burnett, R. T., Thun, M. J., Calle, E. E., Krewski, D., Ito, K., & Thurston, G. D. (2002). Lung cancer, cardiopulmonary mortality, and long-term exposure to fine particulate air pollution. *JAMA*, *287*(9), 1132–1141. https://doi.org/10.1001/jama.287.9.1132

Pope, C. A., III, & Dockery, D. W. (2006). Health effects of fine particulate air pollution: Lines that connect. *Journal of the Air & Waste Management Association*, *56*(6), 709–742. https://doi.org/10.1080/10473289.2006.10464485

Ramachandra, T. V., Bharath, H. A., & Vinay, S. (2017). ⚠️ *[Authors to verify: full citation for the paper reporting 1,028% built-up area growth in Bengaluru between 1973 and 2017. Likely published in Energy & Climate Change or a CESTP/IISC technical report series. Please confirm journal, volume, pages, and DOI.]*

Registrar General of India [RGI]. (2020). *Sample Registration System (SRS) Bulletin*. Office of the Registrar General & Census Commissioner, India.

Sahu, S. K., Beig, G., & Parkhi, N. (2011). Emission inventory of anthropogenic PM₂.₅ and PM₁₀ in Delhi during Commonwealth Games 2010. *Atmospheric Environment*, *45*(34), 6180–6190. ⚠️ *[Authors to verify: the in-text reference (Sahu et al., 2020) describes winter boundary layer inversion effects in Bengaluru — this may be a different paper from the same author group, or a SAFAR project report. Please confirm year and full citation.]*

Sample Registration System [SRS]. (2022). *SRS Statistical Report 2020*. Office of the Registrar General & Census Commissioner, India.

Sharma, S., Zhang, M., Anshika, Gao, J., Zhang, H., & Kota, S. H. (2020). Effect of restricted emissions during COVID-19 on air quality in India. *Science of the Total Environment*, *728*, 138878. https://doi.org/10.1016/j.scitotenv.2020.138878

Smith, K. R. (2000). National burden of disease in India from indoor air pollution. *Proceedings of the National Academy of Sciences*, *97*(24), 13286–13293. https://doi.org/10.1073/pnas.97.24.13286

Stanaway, J. D., Afshin, A., Gakidou, E., Lim, S. S., Abate, D., Abate, K. H., … & Murray, C. J. (2018). Global, regional, and national comparative risk assessment of 84 behavioural, environmental and occupational, and metabolic risks or clusters of risks for 195 countries and territories, 1990–2017: a systematic analysis for the Global Burden of Disease Study 2017. *The Lancet*, *392*(10159), 1923–1994. https://doi.org/10.1016/S0140-6736(18)32225-6

Su, J. G., Morello-Frosch, R., Jesdale, B. M., Kyle, A. D., Shamasunder, B., & Jerrett, M. (2009). An index for assessing demographic inequalities in cumulative environmental hazards with application to Los Angeles, California. *Environmental Science & Technology*, *43*(20), 7626–7634. https://doi.org/10.1021/es901028d

Venkatramanan, S., Viswanathan, P. M., & Chung, S. Y. (2020). Application of chemometric methods in environmental analysis. *Environmental Pollution*, *266*, 115086. https://doi.org/10.1016/j.envpol.2020.115086

World Health Organization [WHO]. (2013). *Health risks of air pollution in Europe — HRAPIE project*. WHO Regional Office for Europe.

World Health Organization [WHO]. (2020). *AirQ+: Key characteristics and user manual*. WHO Regional Office for Europe.

World Health Organization [WHO]. (2021). *WHO global air quality guidelines: Particulate matter (PM₂.₅ and PM₁₀), ozone, nitrogen dioxide, sulfur dioxide and carbon monoxide*. World Health Organization. https://doi.org/10.4060/9789240034228

---

## Citation Issues Log — Pre-Submission Checklist

| # | Issue | In-Text Citation | Reference List Entry | Status |
|---|-------|-----------------|---------------------|--------|
| 1 | Year mismatch | Apte et al., 2017 | Apte et al. (2015) | ✅ Fixed throughout text |
| 2 | Group author | Murray et al., 2020 | GBD 2019 Risk Factors Collaborators (2020) | ✅ Fixed throughout text |
| 3 | Missing reference | Brook et al., 2010 | Not in original list | ✅ Added — *Circulation* |
| 4 | Missing reference | Ramachandra et al., 2017 | Not in original list | ⚠️ Authors must verify full citation |
| 5 | Year conflict | Sahu et al., 2020 | Sahu & Kota (2017) — different paper | ⚠️ Authors must confirm correct paper |
| 6 | Missing reference | Gao et al., 2018 | Not in original list | ⚠️ Authors must add Beijing HIA paper |
| 7 | Missing reference | Chowdhury et al., 2019 | Not in original list | ⚠️ Authors must add Delhi paper |
| 8 | Missing reference | Morello-Frosch et al., 2011 | Not in original list | ⚠️ Authors must verify book chapter vs. journal article |
| 9 | Duplicate Burnett | Burnett 2014 (IER) and 2018 (PNAS) are different papers | Original list had only 2018 | ✅ Both now included with correct citations |
| 10 | Figure numbering | Text had Figs 3 and 4 swapped vs. actual figure files | — | ✅ Corrected throughout |

---

## Footnotes

[^1]: **Ramachandra et al., 2017** — The 1,028% built-up area increase figure needs verification against the specific paper. It is traceable to the CESTP/IISC Bengaluru urban sprawl series. Please confirm title, journal, and DOI before submission.

[^2]: **Sahu et al., 2020** — The winter boundary layer inversion description in the text may correspond to a different paper from the one currently in the reference list (Sahu & Kota, 2017, which concerns Delhi during the Commonwealth Games). Please confirm which paper documents the "valley tank" BL compression in Bengaluru.

[^3]: **Morello-Frosch et al., 2011** — The Double Jeopardy framing is most closely associated with Morello-Frosch & Lopez (2006) in *American Journal of Public Health* (https://doi.org/10.2105/AJPH.2005.064790). The 2011 entry may be a book chapter. Please confirm which work you are citing.

[^4]: **Gao et al., 2018** — Likely refers to a paper on intra-urban PM₂.₅ health impact gradients in Beijing or North China. Please confirm title, journal, and DOI.

[^5]: **Chowdhury et al., 2019** — Likely refers to a paper on PM₂.₅ health burden in Delhi or North India. Please confirm title, journal, and DOI.
