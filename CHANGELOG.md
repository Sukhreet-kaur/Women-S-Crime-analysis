# 📜 Changelog — HerSafetyMetrics

All notable changes to this project will be documented in this file.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.0.0] — 2024 (Initial Release)

### ✅ Added
- Home page with NCRB dataset preview and configurable row count
- Interactive DataFrame explorer with state/year/column filters
- Total cases visualizer — state-wise bar chart and year-wise line chart
- Crime correlation heatmap across 41 crime types (normalized)
- Scatter regression plots between any two crime types
- 4 dedicated crime category analysis pages:
  - **Rape Cases** (rape, attempt_to_rape, gang_rape, murder_with_rape)
  - **Domestic Violence** (dowry_deaths, 498A, dowry_prohibition_act, dowry_harassment)
  - **POCSO Cases** (pocso_rape, pocso_assault, pocso_harassment, child_marriage, etc.)
  - **Outdoor Crimes** (acid_attack, trafficking, cyber_stalking, stalking, etc.)
- Per crime category:
  - Frequency histogram with KDE
  - Year-wise trend line chart
  - Grouped bar chart by state or year
  - Multi-parameter regression analysis (two crimes, filtered by state/year)
  - Statistical heatmap and scatter plot
- Session-state-based multi-page navigation
- GitHub Codespaces support via `.devcontainer/devcontainer.json`
- Landing page deployed on Netlify at [hersafetymetrics.netlify.app](https://hersafetymetrics.netlify.app)
- Custom domain: `hersafety.com` (via CNAME)

### 🗃️ Data
- Cleaned NCRB dataset: `women_crime_india_2001_2021_cleaned.csv`
- Coverage: 2001–2020, state and district level
- 41 crime-type columns + total_cases, state, year, district

---

## [Upcoming] — Planned

### 🔮 Planned Features
- [ ] Choropleth maps for state-level crime heatmaps (Folium/Plotly)
- [ ] ML prediction model for 2021–2030 crime forecasting
- [ ] Export charts and filtered data as PDF/CSV
- [ ] Alert system for states with sudden crime spikes
- [ ] Mobile-responsive layout improvements
- [ ] Multi-language support (Hindi)
