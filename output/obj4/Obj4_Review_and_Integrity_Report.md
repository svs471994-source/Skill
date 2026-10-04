# Objective 4 manuscript: simulated peer review and integrity check

Manuscript: *Valued but hard to reach and poorly managed: community perceptions of seven types of urban green space in Bengaluru, India* (draft v1)
Target: Urban Forestry & Urban Greening (Q1) or a comparable Q1/Q2 journal
Review mode: five-perspective panel (editor, methodology, domain, planning, devil's advocate) plus an integrity audit of numbers, references and claims.

---

## 1. Editorial decision on draft v1: **Major revision**

The topic fits the journal and the analysis is careful about multiple testing. Three issues block acceptance in v1. The construct validity of the five dimensions is not fully defended. The "appreciation vs awareness" framing claims more than the items measure. The literature base is thin (22 references, several not verified). All three are fixable without new data, and draft v2 addresses them (Section 4).

## 2. Reviewer comments on v1 (condensed)

### Reviewer 1: Methodology

| # | Concern | Severity | Response in v2 |
|---|---|---|---|
| M1 | Parallel analysis retains 4 factors, but the paper uses 5. | Major | Added nested CFA tests. Merging VEG+SOIL worsens fit (Δχ²(4) = 130.2, *p* < .001; CFI .988 → .949), and so does merging ENV+VEG (Δχ²(4) = 155.6). The 5-factor model also has the lowest AIC. Parallel analysis is reported as a conservative bound, not a decision rule. |
| M2 | Fornell–Larcker fails for VEG–SOIL (latent *r* = .72). | Major | Added HTMT (Henseler et al., 2015). All HTMT values are ≤ .737, and the bootstrap 95% upper bound for VEG–SOIL is .812, below the .85 threshold. Discriminant validity is supported by the criterion the methods literature now recommends. Fornell–Larcker is still reported, and its known conservatism is acknowledged. |
| M3 | Should GSPI exist if the dimensions are correlated? | Minor | Added a second-order CFA (χ²(372) = 417.8, CFI .986, RMSEA .020, lowest BIC). This supports a single higher-order perception factor with first-order loadings of .59–.90, which justifies GSPI as a composite. |
| M4 | ML estimation on 5-point ordinal items. | Minor | Stated as a limitation. Items are near-symmetric (skew −0.67 to 0.02) with five categories. |
| M5 | No measurement-invariance test before group comparisons. | Minor | Stated as a limitation. Group cells are too small for multi-group CFA (smallest class n = 18). |
| M6 | Quota sample; class choice not designed. | Major (inherent) | Kept prominent in Methods and Limitations. Prevalence is not interpreted. |
| M7 | Fieldwork period not reported. | Minor | **Author decision required.** Reviewers at Q1 journals routinely ask for it. See Section 5. |

### Reviewer 2: Domain (urban ecology / green space)

- D1. The Indian and Bengaluru literature was thin. *v2 adds* Nagendra and Gopal (2011), Vailshery et al. (2013), Shah et al. (2021), Plieninger et al. (2022) and Thapa et al. (2024).
- D2. The equity framing needs the access literature. *v2 adds* Rigolon (2016), Kabisch and Haase (2014) and Schipperijn et al. (2010).
- D3. Governance findings need a safety and maintenance link. *v2 adds* Sreetheran and van den Bosch (2014) and Kothencz and Blaschke (2017).

### Reviewer 3: Planning perspective

- P1. Recommendations should map onto specific findings. *v2* ties each of three actions to one result.
- P2. The contribution of the typology should be explicit. *v2* states it in the Introduction and Discussion.

### Reviewer 4: Devil's advocate

- DA1. "Ecological awareness" is not measured. Items Q24–Q29 are self-rated endorsements, and Q27–Q29 are value statements. **Accepted.** The construct is renamed "ecological-function endorsement" throughout, and the gap is called a *salience gap*, not a knowledge gap.
- DA2. The class pattern in the gap was presented as a story in early discussions. **Accepted.** The heterogeneity test is non-significant (*p* = .40), and v2 reports the pattern as descriptive only.
- DA3. The near-perfect fit (RMSEA .019) needs replication. Kept in the Discussion.

### Reviewer 5: Editor-in-chief synthesis
After revision, the paper makes a modest but clear contribution: a typology-anchored, validated perception profile for an under-studied Global South city, with honest handling of multiple testing. **Recommendation for v2: minor revision**, conditional on the author confirmations in Section 5.

---

## 3. Integrity audit

### 3.1 Numbers
Every statistic in v2 was cross-checked against `results.json` and `validity_extra.json`, which are produced by `analysis.py` and `validity_extra.py` from the response file. No mismatches remain.

One correction was made relative to the user's earlier chart: Usage & access is **67.4**, not 67.5. The chart value was rounded from a slightly different computation.

### 3.2 References: problems found in v1 and fixed in v2
| Problem | v1 | v2 |
|---|---|---|
| **Wrong title** | Taylor & Hochuli (2017) "…Multiple uses across multiple *meanings*" | Corrected to "…multiple *disciplines*" (publisher record). |
| **Claim not supported by source** | Ramachandra et al. (2015, J Environ Manage 148) cited for Bengaluru vegetation loss | Source concerns Delhi, so it was **removed**. The Bengaluru claim now rests on Nagendra et al. (2012). |
| **Claim not supported by source** | Reyes-Riveros et al. (2021) cited as saying "perceived quality matters as much as proximity" | Rewritten to what the review actually reports (structure, biodiversity and naturalness, plus a reliance on perception methods). |
| Incomplete entry | Plieninger et al. (2022) without authors or volume | Completed: Plieninger, Thapa, Bhaskar, Nagendra, Torralba, Zoderer; LUP 222, 104399. |
| Unverified entries | 18 of 22 not checked | All 41 v2 references checked (Section 3.3). |

### 3.3 Verification status of all 41 references
Each reference was confirmed in this session against a publisher or indexing record (title, authors, year, journal; volume, pages and DOI where shown) through web search of publisher, Semantic Scholar and Scopus-indexed records, or the Consensus academic database. Crossref and DOI resolvers are blocked in this computing environment. Before submission, run the list through the journal's reference checker or Zotero/EndNote DOI lookup as a final pass.

Two entries carry details from the authors' synopsis that the search confirmed only at title, journal and year level. Their volume and article numbers should be checked on the publisher page:
- Reyes-Riveros et al. (2021), UFUG 61, 127105
- Thapa et al. (2024), Landscape Ecology 39, 68

### 3.4 Orphan check
A script cross-matched every in-text citation against the reference list (Section 6 of the README). Result for v2: **0 citations without a reference, 0 references without a citation.**

### 3.5 Plagiarism
v2 was written fresh in this session from the analysis outputs. It contains no copied passages from sources; quoted phrases are limited to article titles. I cannot run iThenticate or Turnitin here. **Run the journal's similarity check (or Turnitin) before submission.** Expect hits only on reference strings, standard method phrases and the questionnaire wording.

---

## 4. How the dimension-validity problem was overcome

| Evidence | Result | Reading |
|---|---|---|
| HTMT, all pairs | 0.31–0.74 (max VEG–SOIL 0.737, 95% CI 0.656–0.812) | All below 0.85, so discriminant validity holds. |
| Nested CFA, VEG+SOIL merged | Δχ²(4) = 130.2, *p* < .001; CFI .949 | Separating VEG and SOIL is warranted. |
| Nested CFA, ENV+VEG merged | Δχ²(4) = 155.6, *p* < .001; CFI .941 | Separating ENV and VEG is warranted. |
| 5-factor vs 1-factor | Δχ²(10) = 906.7 | The construct is multidimensional. |
| Second-order model | CFI .986, RMSEA .020, BIC 777.1 (lowest) | One higher-order perception factor underlies the five dimensions, so GSPI is justified. |
| Parallel analysis | 4 factors; 5th eigenvalue 1.21 vs 1.40 random | Reported openly as conservative. Content validity and the nested tests support five. |

The paper can therefore present the instrument as a five-dimension, second-order measure with demonstrated discriminant validity in this sample. External validity still needs replication in a second sample, and the paper says so.

---

## 5. Items only the authors can settle (marked [CONFIRM] in v2)
1. **Fieldwork period.** You asked to omit it. Most Q1 reviewers will request it, so a single sentence is safest.
2. **Ethics.** Elsevier journals ask for approval or an institutional exemption. A short exemption letter from the department or university would remove the risk of desk rejection.
3. How quotas were filled, and the online/interview split.
4. Author list, data availability, funding and the AI-use declaration (Elsevier requires the declaration).

## 6. Style pass
The text was rewritten following the humanizer-academic-v9 guidance:
- plain words
- varied sentence length
- active voice
- no stock AI phrases (the blocklist was scanned)
- hedging where the data are limited

Two of that skill's rules were **deliberately not applied**, because they conflict with Q1 journal register:
- forced contractions in every paragraph
- informal author asides such as "Frankly…"

The AI-use declaration is retained. Journals require it whatever the text sounds like.
