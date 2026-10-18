# HerSafetyMetrics — Project Documentation

## Overview
This document provides technical documentation for the HerSafetyMetrics Streamlit application.

---

## Architecture

```
User Request
     │
     ▼
Streamlit (home.py)
     │
     ├── st.session_state.page  ← Navigation State Machine
     │        │
     │        ├── "home"     → Home Page
     │        ├── "rape"     → Rape Cases Analysis
     │        ├── "domestic" → Domestic Violence Analysis
     │        ├── "POCSO"    → POCSO Cases Analysis
     │        └── "outdoor"  → Outdoor Crime Analysis
     │
     ├── load_data() [cached]  ← Pandas CSV loader
     │        │
     │        └── women_crime_india_2001_2021_cleaned.csv
     │
     └── crime_analysis_page()  ← Reusable page component
```

---

## Core Components

### `load_data()`
```python
@st.cache_data
def load_data():
    return pd.read_csv("women_crime_india_2001_2021_cleaned.csv")
```
- Uses Streamlit's `@st.cache_data` decorator for performance
- Loads the dataset once and caches it across all reruns
- Returns a Pandas DataFrame

---

### Navigation State Machine

```python
# Initialize
if "page" not in st.session_state:
    st.session_state.page = "home"

# Navigate
def go_to(page_name: str):
    st.session_state.page = page_name

# Route
if st.session_state.page == "home":
    ...
elif st.session_state.page == "rape":
    crime_analysis_page("Rape", columns['Rape'])
...
```

- All navigation is managed via `st.session_state.page`
- `go_to()` is passed as `on_click` callback to buttons
- No URL routing — purely session-based

---

### Crime Column Mapping

```python
columns = {
    'Rape': [
        'rape', 'murder_with_rape',
        'attempt_to_rape', 'gang_rape'
    ],
    'Domestic Violence': [
        'dowry_deaths', 'dowry_prohibition_act',
        'cruelty_by_husband_or_relatives_498A', 'dowry_harassment'
    ],
    'POCSO Cases': [
        'pocso_rape', 'pocso_assault', 'pocso_harassment',
        'child_marriage_prohibition_act',
        'procuration_of_minor_girls', 'importation_of_girls'
    ],
    'Outdoor Crime': [
        'sexual_harassment_workplace', 'attempt_to_kidnap',
        'cyber_stalking_bullying_against_women',
        'cyber_crime_obscenity_against_women', 'trafficking',
        'stalking_354D', 'acid_attack', 'attempt_to_acid_attack'
    ]
}
```

---

### `crime_analysis_page(case_name, columns)`

The reusable page template used for all 4 crime categories.

**Parameters:**
- `case_name` (str): Display name of the crime category (e.g., "Rape")
- `columns` (list): List of column names from the dataset for this category

**Sections rendered:**
1. Title + Back button
2. Data preview (optional, filtered by state/year)
3. Frequency histogram with KDE
4. Year-wise trend line chart
5. Grouped bar chart (by state or year)
6. Multi-parameter regression (2 crimes × state × year)
7. Statistical analysis (scatter / heatmap)

---

## Dataset Schema

| Column | Type | Description |
|---|---|---|
| `state` | string | Indian state or union territory |
| `year` | int | Year of record (2001–2020) |
| `district` | string | District within the state |
| `total_cases` | int | Total women-related crimes reported |
| `rape` | int | Rape cases reported |
| `attempt_to_rape` | int | Attempt to rape cases |
| `gang_rape` | int | Gang rape cases |
| `murder_with_rape` | int | Murder combined with rape |
| `kidnapping_and_abduction` | int | Kidnapping and abduction |
| `dowry_deaths` | int | Deaths related to dowry |
| `dowry_prohibition_act` | int | Cases under Dowry Prohibition Act |
| `cruelty_by_husband_or_relatives_498A` | int | IPC 498A cases |
| `acid_attack` | int | Acid attack cases |
| `attempt_to_acid_attack` | int | Attempt to acid attack |
| `stalking_354D` | int | Stalking cases (IPC 354D) |
| `trafficking` | int | Human trafficking cases |
| `pocso_rape` | int | POCSO rape cases |
| `pocso_assault` | int | POCSO assault cases |
| `pocso_harassment` | int | POCSO harassment cases |
| `cyber_stalking_bullying_against_women` | int | Cyber stalking/bullying |
| `cyber_crime_obscenity_against_women` | int | Cyber obscenity crimes |
| `sexual_harassment_workplace` | int | Workplace sexual harassment |
| `dowry_harassment` | int | Dowry harassment |
| `child_marriage_prohibition_act` | int | Child marriage cases |
| *(+ 17 more columns)* | int | Additional crime sub-types |

---

## Visualization Reference

| Chart Type | Library | Usage |
|---|---|---|
| Line Plot | Seaborn | Year-wise crime trends |
| Bar Plot | Seaborn | State-wise comparisons |
| Histogram + KDE | Seaborn | Frequency distribution |
| Regression Plot | Seaborn | Correlation between two crimes |
| Heatmap | Seaborn | Multi-variable correlation matrix |

---

## Dependencies

```
streamlit       # Web app framework
pandas          # Data manipulation
numpy           # Numerical computing
matplotlib      # Plot rendering backend
seaborn         # Statistical visualization
```

---

## Environment Configuration

### `.devcontainer/devcontainer.json`
- Base image: `mcr.microsoft.com/devcontainers/python:1-3.11-bookworm`
- Post-attach: auto-starts Streamlit on port `8501`
- Extensions: `ms-python.python`, `ms-python.vscode-pylance`
- Forwards port `8501` for browser preview

---

## Known Limitations

| Issue | Impact | Notes |
|---|---|---|
| `go_to()` defined twice | Minor | Second definition overrides the first — no runtime impact |
| `outdoor` page uses POCSO columns | Bug | Should use `columns["Outdoor Crime"]` |
| `st.set_page_config` called after initial markdown | Warning | Should be the first Streamlit call |
| No input validation on state names | UX | Case-sensitive state matching |

---

## Performance Notes

- Dataset is ~1.5 MB and loads in < 1s with caching
- All Matplotlib figures are generated on-demand per user interaction
- No database — all operations are in-memory Pandas operations
- `@st.cache_data` prevents reloading CSV on every Streamlit rerun

---

*Generated for HerSafetyMetrics v1.0.0*
