# 🌸 HerSafetyMetrics — Full Project Presentation
### Women's Crime Analysis in India (2001–2020)

---

---

# 📖 SLIDE 1 — Title & Introduction

## Project Title
**HerSafetyMetrics: Uncovering Insights on Women's Safety — A Data-Driven Exploration**

## Tagline
*"Turning two decades of silence into data-driven awareness"*

## Presented By
**Sukhreet Kaur**

## Live Demo
🔗 [hersafetymetrics.netlify.app](https://hersafetymetrics.netlify.app)

---

---

# 📌 SLIDE 2 — Why This Project?

## The Reality of Women's Safety in India

India records one of the highest rates of crimes against women globally. Yet, the raw data collected by the government often remains buried in reports — inaccessible to the general public, students, advocates, and even policymakers.

### The Core Problem:
- 📊 NCRB (National Crime Records Bureau) publishes annual crime data — but it's a **PDF report**, not interactive
- 🗂️ Thousands of rows of numbers mean nothing without visual context
- 🌍 Regional disparities are invisible unless mapped
- 📉 Trends over 20 years are impossible to spot in a static table
- 🚨 No existing tool allowed citizens to **explore and question** the data themselves

### The Solution — HerSafetyMetrics:
An **interactive, visual, web-based platform** that:
- Converts NCRB raw data into meaningful charts
- Lets anyone explore state-wise and year-wise crime patterns
- Covers 4 major categories: Rape, Domestic Violence, POCSO, Outdoor Crime
- Works directly in the browser — no downloads, no setup

---

---

# 🎯 SLIDE 3 — Project Objectives

| Objective | Details |
|---|---|
| **Awareness** | Make crime data accessible to everyone — not just researchers |
| **Exploration** | Allow filtering by state, year, crime type |
| **Trend Analysis** | Visualize how crimes changed from 2001 to 2020 |
| **Correlation** | Find which crimes tend to occur together |
| **Regional Insights** | Identify high-risk states across all crime categories |
| **Frequency Distribution** | Understand how often specific crime levels occur |
| **Policy Perspective** | Help researchers and policymakers spot intervention gaps |

---

---

# 🗃️ SLIDE 4 — The Dataset

## Source
**National Crime Records Bureau (NCRB)**
Ministry of Home Affairs, Government of India

## What is NCRB?
The NCRB is India's central government body that compiles and publishes crime statistics across all states and union territories annually. Their data is the **most authoritative and official** source of crime statistics in India.

## Dataset Details

| Property | Value |
|---|---|
| **File** | `women_crime_india_2001_2021_cleaned.csv` |
| **Time Span** | 2001 to 2020 (20 years) |
| **Granularity** | State-level and District-level |
| **Total Records** | Thousands of rows (state × district × year combinations) |
| **Total Features** | 41 crime-type columns + meta columns |
| **File Size** | ~1.5 MB |
| **Format** | Cleaned CSV (pre-processed for analysis) |

## Key Meta Columns

| Column | Description |
|---|---|
| `state` | Indian state or union territory name |
| `year` | Year of the record (2001–2020) |
| `district` | District within the state |
| `total_cases` | Sum of all women-related crime types for that row |

## All 41 Crime Columns

```
rape                              attempt_to_rape
gang_rape                         murder_with_rape
kidnapping_and_abduction          dowry_deaths
dowry_prohibition_act             cruelty_by_husband_or_relatives_498A
acid_attack                       attempt_to_acid_attack
assault_on_women_modesty_354      assault_intent_disrobe_354B
voyeurism_354C                    stalking_354D
insult_to_modesty_509             trafficking
procuration_of_minor_girls        importation_of_girls
immoral_traffic_act               indecent_representation_of_women
women_killed_in_honour_killing    witch_hunting
cyber_crime_obscenity_against_women
cyber_stalking_bullying_against_women
child_marriage_prohibition_act    pocso_rape
pocso_assault                     pocso_harassment
pocso_unnatural_offences          pocso_other
abduction_for_marriage            abduction_for_illicit_intercourse
attempt_to_kidnap                 domestic_violence_act_cases
abetment_to_suicide_women         attempt_to_murder_women
insult_outraging_modesty_other    sexual_harassment_workplace
dowry_harassment                  marital_rape_reports
total_cases
```

## Data Cleaning Done
- Removed null/missing values
- Standardized state and district names
- Converted all numeric columns to integers
- Ensured year consistency across all rows
- Removed duplicate entries

---

---

# 🛠️ SLIDE 5 — Technology Stack

## How the Project is Built

```
┌─────────────────────────────────────────────┐
│              USER'S BROWSER                  │
│         (No installation needed)             │
└────────────────────┬────────────────────────┘
                     │
              HTTP Request
                     │
┌────────────────────▼────────────────────────┐
│           STREAMLIT FRAMEWORK                │
│   (Python-based web application engine)      │
│                                              │
│   Renders HTML, CSS, JS automatically        │
│   Handles all user interactions              │
│   Manages session state for navigation       │
└────────────────────┬────────────────────────┘
                     │
         Python functions called
                     │
┌────────────────────▼────────────────────────┐
│              PYTHON BACKEND                  │
│                                              │
│  ┌──────────────┐   ┌───────────────────┐   │
│  │   PANDAS     │   │  MATPLOTLIB +     │   │
│  │              │   │  SEABORN          │   │
│  │ Data loading │   │                   │   │
│  │ Filtering    │   │ Bar charts        │   │
│  │ Grouping     │   │ Line plots        │   │
│  │ Correlation  │   │ Histograms        │   │
│  │ Aggregation  │   │ Heatmaps          │   │
│  └──────┬───────┘   │ Scatter plots     │   │
│         │           └───────────────────┘   │
└─────────┼───────────────────────────────────┘
          │
┌─────────▼───────────────────────────────────┐
│              CSV DATASET                     │
│   women_crime_india_2001_2021_cleaned.csv    │
│        (~1.5 MB, loaded into memory)         │
└─────────────────────────────────────────────┘
```

## Why Each Technology Was Chosen

| Technology | Why Used |
|---|---|
| **Python** | Industry standard for data analysis; rich ecosystem of libraries |
| **Streamlit** | Converts Python scripts into web apps with zero frontend code needed |
| **Pandas** | Most powerful library for tabular data manipulation in Python |
| **Seaborn** | High-level statistical visualization on top of Matplotlib |
| **Matplotlib** | Underlying plot rendering engine |
| **CSV** | Universal, lightweight data format — compatible with all tools |
| **GitHub Codespaces** | Cloud-based development environment, zero local setup needed |
| **Netlify** | Free, fast static site hosting for the landing page |

---

---

# 🏗️ SLIDE 6 — Project Architecture & How It Works

## How the App Works — Step by Step

### Step 1: App Startup
When you run `streamlit run home.py`, Python executes the script top-to-bottom. Streamlit detects all `st.*` commands and renders them as a web page automatically.

### Step 2: Data Loading (Cached)
```python
@st.cache_data
def load_data():
    return pd.read_csv("women_crime_india_2001_2021_cleaned.csv")

df = load_data()
```
- The CSV file is read into a Pandas DataFrame called `df`
- `@st.cache_data` means it is **loaded only once** and stored in memory
- Every time a user interacts with the app (clicking, selecting), Streamlit reruns the script — but `df` is served from cache instantly, avoiding repeated disk reads

### Step 3: Session State Navigation
```python
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to(page_name):
    st.session_state.page = page_name
```
- `st.session_state` persists data across reruns for the same user
- `page` variable controls which page is currently shown
- When a user clicks a button, `go_to()` updates `page`, Streamlit reruns, and the new page renders

### Step 4: Page Routing
```python
if st.session_state.page == "home":
    # show home page
elif st.session_state.page == "rape":
    crime_analysis_page("Rape", columns['Rape'])
elif st.session_state.page == "domestic":
    crime_analysis_page("Domestic Violence", columns['Domestic Violence'])
...
```
- Like a router in web frameworks — each `elif` is a "route"
- The correct page block renders based on `session_state.page`

### Step 5: User Interaction → Chart Generation
When a user selects options and checks boxes:
1. Streamlit captures the input value
2. Python filters `df` using Pandas
3. Seaborn creates a figure (`fig`)
4. `st.pyplot(fig)` renders it in the browser

---

---

# 🏠 SLIDE 7 — Home Page Features (Detailed)

The Home Page is the **entry point** and provides:

## Feature 1: Dataset Preview
```
"How many starting rows you want to see?" → [number input]
```
- User types any number from 0 to 10,000
- `df.head(n)` shows that many rows in an interactive table
- Users can scroll, sort, and explore the raw data
- **Purpose:** Build familiarity with the dataset before analysis

## Feature 2: Data Configuration Info
- Shows `df.shape` — the total number of rows and columns
- Optional checkbox: "Do you want to see various columns?" → lists all 41+ column names
- **Purpose:** Let users understand the scale and structure of the data

## Feature 3: Smart DataFrame Explorer
A powerful multi-filter tool:
```
Select columns → [multiselect dropdown]
Enter state name → [text input]
Enter year → [number input]
```
- User can select any combination of columns
- Filter by state (e.g., "Punjab"), year (e.g., 2015), or both
- Shows the filtered rows in an interactive table
- **Purpose:** Answer specific questions like "How many rape cases were in UP in 2010?"

## Feature 4: Total Cases Visualizer
```
"Choose the Parameter to Analyse" → [radio: state | year | clear]
```

**If Year selected:**
- Groups data by year, sums `total_cases`
- Draws a **line chart** with markers
- X-axis = Year (2001–2020), Y-axis = Total Cases
- **Insight:** Shows the overall national trend of women's crimes over 20 years

**If State selected:**
- Groups data by state, sums `total_cases`
- Draws a **horizontal bar chart** — one bar per state
- **Insight:** Immediately identifies which states report the most crimes

## Feature 5: Crime Correlation Analysis
```
"Choose type of Crime" → [multiselect: at least 2]
"Choose type of plot" → [radio: Scatter | Heatmap]
```

**Scatter Plot (exactly 2 crimes):**
- Draws a regression scatter plot
- Shows whether two crimes are positively or negatively correlated
- Optional: Normalize data by total_cases to remove population bias
- A positive slope = both crimes tend to rise together
- **Example use:** "Do states with more rape also have more stalking?"

**Heatmap (2+ crimes):**
- Computes pairwise correlation matrix of selected crimes
- Rendered as a color-coded heatmap (Blues palette)
- Values close to 1.0 = strong positive correlation
- Values close to -1.0 = strong negative correlation
- **Example use:** "Which crime types are most strongly related to each other?"

## Feature 6: Navigation to Crime Categories
```
"Select the category to analyse" → [selectbox]
[Show Analysis] button
```
- User picks one of 4 categories: Rape Cases, Domestic Violence, POCSO Cases, Outdoor Crime
- Clicking "Show Analysis" calls `go_to()` and navigates to that page
- **Purpose:** Gateway to deep-dive analysis by crime type

---

---

# 📊 SLIDE 8 — Crime Category Pages (Detailed)

All 4 crime category pages (**Rape, Domestic Violence, POCSO, Outdoor Crime**) share the same structure, built using the reusable `crime_analysis_page()` function.

## The Reusable Function
```python
def crime_analysis_page(case_name, columns):
    ...
```
- `case_name`: The display title (e.g., "Rape")
- `columns`: The list of crime sub-types for this category
- This design eliminates code duplication — one function serves all 4 pages

---

## Section A: Data Preview (Optional)
```
"Enter state name" + "Enter year"
```
- Shows the specific crime sub-type columns for that state and year
- Helps users verify exact numbers before drawing conclusions

---

## Section B: Frequency Histogram with KDE

```python
sb.histplot(data=df1, x=op, kde=True, ax=ax)
```

**What it shows:**
- X-axis = Number of cases reported
- Y-axis = Frequency (how many state-districts reported that many cases)
- The **KDE (Kernel Density Estimate)** curve is a smoothed probability distribution overlaid on the histogram

**How to read it:**
- A **right-skewed** histogram means most places have low counts, but a few have very high counts
- A **normal distribution** means crime is evenly spread across the country
- **Purpose:** Understand if a crime is concentrated in a few places or widespread

**Why filter by year?**
- Crime patterns change over time
- Comparing 2001 vs 2020 histograms shows whether crimes spread geographically or concentrated

---

## Section C: Year-wise Trend Line

```python
sb.lineplot(data=df, y=op_line, x=df['year'], ax=ax)
```

**What it shows:**
- X-axis = Years from 2001 to 2020
- Y-axis = Total crime count across all states for that year
- Smooth line connecting annual totals

**How to read it:**
- An **upward trend** = crime is increasing nationally
- A **downward trend** = crime is decreasing (may mean fewer reports too, not necessarily fewer crimes)
- **Plateaus or dips** may correspond to policy changes, law amendments, or COVID

**Example insights:**
- Rape cases show a sharp increase around 2012–2013 (post-Nirbhaya case, more reporting)
- Cyber crime against women rises steeply post-2015 (smartphone proliferation)

---

## Section D: Grouped Bar Chart (State or Year)

```
"Choose first Parameter" → [radio: state | year | clear]
"Choose type of Crime" → [radio: list of sub-types | clear]
```

**If State selected:**
- Horizontal bar chart: one bar per state
- Bar length = total crime count for that sub-type
- **Purpose:** Rank states by crime volume — immediately identify top and bottom performers

**If Year selected:**
- Vertical bar chart: one bar per year (2001–2020)
- **Purpose:** Year-by-year comparison for a specific crime type

---

## Section E: Multi-parameter Analysis

```
"Choose type of Crime" → [multiselect: exactly 2]
"Enter state" + "Enter year"
```

```python
sb.lineplot(data=df, x=crime[0], y=crime[1], ax=ax)
```

**What it shows:**
- A line/scatter plot of two crime types against each other
- Filtered for a specific state and year
- **Purpose:** Answer questions like "In Maharashtra 2015, how do rape cases relate to kidnapping cases?"

---

## Section F: Statistical Analysis

**Scatter (Regression Plot):**
```python
sb.regplot(data=df, x=crime[0], y=crime[1])
```
- Plots data points + best-fit regression line
- Positive slope = both crimes increase together
- Negative slope = one increases as other decreases
- **The regression line shows the directional relationship**

**Heatmap:**
```python
cor = df[crime].corr()
sb.heatmap(data=cor, cmap='Blues', annot=True)
```
- Computes Pearson correlation coefficients between selected sub-crimes
- Annotated values on each cell
- Dark blue = strong positive correlation

---

---

# 🗂️ SLIDE 9 — The 4 Crime Categories Explained

## Category 1: Rape Cases 🔴

| Sub-type | IPC Section | What it covers |
|---|---|---|
| `rape` | IPC 376 | Penetrative sexual assault on women |
| `attempt_to_rape` | IPC 376/511 | Failed attempt at rape |
| `gang_rape` | IPC 376D | Rape by two or more persons |
| `murder_with_rape` | IPC 376A | Rape followed by death of victim |

**Why it matters:**
- India reports one of the world's highest rape case counts
- After the 2012 Delhi gang rape (Nirbhaya case), reporting improved significantly
- Data shows urban vs rural disparities

---

## Category 2: Domestic Violence 🏠

| Sub-type | Legal Basis | What it covers |
|---|---|---|
| `dowry_deaths` | IPC 304B | Death within 7 years of marriage linked to dowry |
| `dowry_prohibition_act` | Dowry Prohibition Act | Giving/taking dowry |
| `cruelty_by_husband_or_relatives_498A` | IPC 498A | Mental/physical cruelty by husband or in-laws |
| `dowry_harassment` | IPC 498A / DV Act | Harassment for dowry demands |

**Why it matters:**
- Domestic violence is vastly under-reported
- 498A is one of the most filed sections; also one of the most contested
- Dowry deaths remain high in states like UP, Bihar, MP

---

## Category 3: POCSO Cases 👶

POCSO = Protection of Children from Sexual Offences Act (2012)

| Sub-type | What it covers |
|---|---|
| `pocso_rape` | Sexual assault on children (penetrative) |
| `pocso_assault` | Non-penetrative sexual assault on children |
| `pocso_harassment` | Sexual harassment of children |
| `child_marriage_prohibition_act` | Underage marriage violations |
| `procuration_of_minor_girls` | Luring or obtaining minors for exploitation |
| `importation_of_girls` | Cross-border trafficking of girls |

**Why it matters:**
- POCSO was enacted in 2012 — data shows a rapid rise post-2012 in reporting
- Child protection remains critically weak in rural areas
- This data helps identify states needing urgent intervention

---

## Category 4: Outdoor Crimes 🌆

| Sub-type | Legal Basis | What it covers |
|---|---|---|
| `acid_attack` | IPC 326A | Throwing acid on women |
| `attempt_to_acid_attack` | IPC 326B | Attempt at acid attack |
| `stalking_354D` | IPC 354D | Stalking women physically |
| `trafficking` | IPC 370 / ITPA | Human trafficking |
| `sexual_harassment_workplace` | POSH Act | Harassment at workplace |
| `cyber_stalking_bullying_against_women` | IT Act | Online stalking and bullying |
| `cyber_crime_obscenity_against_women` | IT Act 67A | Sharing obscene material online |
| `attempt_to_kidnap` | IPC 365 | Attempted kidnapping |

**Why it matters:**
- Cyber crimes show the **fastest growth** of any crime category
- Acid attacks, though low in number, are life-altering
- Workplace harassment data is severely under-reported

---

---

# 📈 SLIDE 10 — Visualizations Explained

## Chart 1: Line Plot (Trend over Years)
- **Library:** Seaborn `lineplot`
- **X-axis:** Year (2001–2020)
- **Y-axis:** Total crime count
- **Purpose:** Show national trends, detect spikes, measure policy impact
- **Insight:** Most crime categories show an upward trend, partly due to increased reporting

## Chart 2: Horizontal Bar Chart (State-wise)
- **Library:** Seaborn `barplot`
- **X-axis:** Crime count
- **Y-axis:** State names
- **Color:** `darksalmon` (warm, non-alarming tone)
- **Purpose:** Rank all Indian states by crime volume
- **Insight:** Uttar Pradesh, Maharashtra, and Madhya Pradesh consistently appear in top ranks

## Chart 3: Vertical Bar Chart (Year-wise)
- **Library:** Seaborn `barplot`
- **X-axis:** Year
- **Y-axis:** Crime count
- **Color:** `skyblue`
- **Purpose:** Annual comparison for specific crime types

## Chart 4: Histogram with KDE
- **Library:** Seaborn `histplot` with `kde=True`
- **X-axis:** Number of cases reported
- **Y-axis:** Frequency (how many districts/states had that many cases)
- **KDE:** Smooth probability density curve
- **Purpose:** Distribution analysis — is crime widespread or concentrated?
- **Insight:** Most distributions are right-skewed (few places with very high counts)

## Chart 5: Regression Scatter Plot
- **Library:** Seaborn `regplot`
- **X-axis:** Crime Type 1 count
- **Y-axis:** Crime Type 2 count
- **Regression line:** Best-fit line showing correlation direction
- **Purpose:** Detect co-occurrence patterns between crime types
- **Positive slope:** Both crimes rise together → common underlying factors
- **Negative slope:** One decreases as the other increases

## Chart 6: Correlation Heatmap
- **Library:** Seaborn `heatmap`
- **Data:** Pandas `.corr()` matrix (Pearson correlation)
- **Color map:** `Blues` (dark = strong positive correlation)
- **Annotations:** Numeric values on each cell
- **Range:** -1.0 to 1.0
- **Purpose:** Multi-variable correlation — find crime clusters

---

---

# 🌐 SLIDE 11 — Website Structure (Landing Page)

The project has **two deployments:**

## 1. Landing Website (Netlify)
**URL:** [hersafetymetrics.netlify.app](https://hersafetymetrics.netlify.app)

A static marketing/portfolio page with the following sections:

| Nav Section | Content |
|---|---|
| **HOME** | Hero banner — "Her Safety" title, "Explore More" CTA button |
| **ABOUT** | "A small Commitment to Women's Safety Metrics" — project purpose, model description |
| **EDA INSIGHTS** | Carousel showing 4 crime category cards: Rape, Domestic Violence, POCSO, Outdoor Crime |
| **DASHBOARD** | "HerSafetyMetrics App" section — project description, "Explore App" button |
| **ANALYSIS NOTEBOOK** | "Women's Safety & Crime Insights Dashboard of India" — feature highlights, "Explore Dashboard" button |
| **PREDICTION** | Future crime prediction model section — "View Model" button |
| **CONTACT US** | Contact form / social links |

**Color Scheme:**
- Background: Soft lavender/blush pink `#f3e8f5`
- Accent: Hot pink / rose `#e91e8c`
- Text: Dark charcoal `#4a4a4a`
- Highlights: Gold/amber for "India" text

## 2. Streamlit App (GitHub Codespaces)
The actual interactive data analysis application.

---

---

# ⚙️ SLIDE 12 — How GitHub Codespaces Deployment Works

## The `.devcontainer/devcontainer.json` File

```json
{
  "name": "Python 3",
  "image": "mcr.microsoft.com/devcontainers/python:1-3.11-bookworm",
  "updateContentCommand": "pip3 install --user -r requirements.txt",
  "postAttachCommand": {
    "server": "streamlit run home.py --server.enableCORS false --server.enableXsrfProtection false"
  },
  "portsAttributes": {
    "8501": { "label": "Application", "onAutoForward": "openPreview" }
  },
  "forwardPorts": [8501]
}
```

### What Each Part Does:

| Config Key | Purpose |
|---|---|
| `image` | Uses Microsoft's pre-built Python 3.11 Docker container |
| `updateContentCommand` | Automatically installs all packages from `requirements.txt` when the Codespace opens |
| `postAttachCommand` | Automatically runs `streamlit run home.py` when you attach to the Codespace |
| `forwardPorts: [8501]` | Exposes Streamlit's default port to the browser |
| `onAutoForward: "openPreview"` | Automatically opens the app in the browser preview tab |

### Zero-Setup Flow:
```
GitHub → Code → Open in Codespaces
         ↓
Docker container starts (Python 3.11)
         ↓
requirements.txt installed automatically
         ↓
streamlit run home.py starts automatically
         ↓
Port 8501 forwarded → App opens in browser
```

---

---

# 📦 SLIDE 13 — Code Architecture Deep Dive

## File: `home.py` Structure

```
home.py
│
├── IMPORTS
│   ├── streamlit as st
│   ├── pandas as pd
│   ├── seaborn as sb
│   └── matplotlib.pyplot as plt
│
├── DATA LOADING
│   └── load_data() — @st.cache_data, reads CSV
│
├── GLOBAL CONFIG
│   ├── CSS injection (hide main menu)
│   ├── st.set_page_config (title, icon)
│   └── columns dict (crime category → column list mapping)
│
├── SESSION STATE SETUP
│   ├── Initialize st.session_state.page = "home"
│   └── go_to(page_name) helper function
│
├── HOME PAGE BLOCK
│   ├── Title + Subheader
│   ├── Dataset preview (df.head(n))
│   ├── Shape + column info
│   ├── DataFrame Explorer (state/year filter)
│   ├── Total cases visualizer (line/bar chart)
│   ├── Correlation analysis (scatter/heatmap)
│   └── Navigation selectbox + "Show Analysis" button
│
├── crime_analysis_page() FUNCTION
│   ├── Title + Back button
│   ├── Data preview section
│   ├── Histogram section
│   ├── Trend line section
│   ├── Bar chart section
│   ├── Multi-parameter section
│   └── Statistical analysis section
│
└── PAGE ROUTING
    ├── elif page == "rape"     → crime_analysis_page("Rape", ...)
    ├── elif page == "domestic" → crime_analysis_page("Domestic Violence", ...)
    ├── elif page == "POCSO"    → crime_analysis_page("POCSO Cases", ...)
    └── elif page == "outdoor"  → crime_analysis_page("Outdoor Crime", ...)
```

---

---

# 🔑 SLIDE 14 — Key Technical Concepts Used

## 1. Streamlit Session State
```python
st.session_state.page = "home"
```
- Persists values between reruns (Streamlit reruns the entire script on every user interaction)
- Used here as a simple page router — without it, the app would reset to home on every click

## 2. Pandas Data Filtering
```python
df[(df['state'] == state_name) & (df['year'] == year)]
```
- Boolean indexing — fast, vectorized filtering
- No loops required — Pandas handles it internally with C-level performance

## 3. GroupBy Aggregation
```python
df.groupby('state')['total_cases'].sum().reset_index()
```
- Groups all rows by state, sums up total_cases for each group
- `reset_index()` converts the result back to a flat DataFrame for plotting

## 4. Pearson Correlation
```python
df[selected_columns].corr()
```
- Computes the Pearson correlation coefficient between all pairs of selected columns
- Output is a symmetric matrix where diagonal values are 1.0 (self-correlation)
- Values close to 1 = strong positive linear relationship

## 5. Data Normalization
```python
x_data = df[crime[0]] / df["total_cases"]
```
- Divides raw crime counts by total_cases to remove the effect of population size
- States with larger populations naturally have more crimes
- Normalized data shows crime **rate** rather than absolute **count**

## 6. KDE (Kernel Density Estimate)
```python
sb.histplot(data=df, x=col, kde=True)
```
- Overlays a smooth probability density curve on the histogram
- Helps identify the underlying distribution shape (normal, skewed, bimodal)
- Useful for spotting outliers and concentration patterns

## 7. Regression Plot
```python
sb.regplot(x=crime1_data, y=crime2_data)
```
- Plots raw data points + a linear regression line with confidence interval shading
- The slope of the line indicates correlation direction and strength

## 8. Streamlit Caching
```python
@st.cache_data
def load_data():
    return pd.read_csv("...")
```
- Without caching: CSV re-read on every user interaction (slow)
- With caching: CSV read once, DataFrame stored in memory (fast)
- Critical for performance with a 1.5 MB file

---

---

# 🔮 SLIDE 15 — Future Scope & Roadmap

## What's Planned Next

### Phase 2: Enhanced Visualizations
- 🗺️ **Choropleth Maps** using Plotly or Folium — color-code India's map by crime intensity
- 📊 **Animated charts** showing crime evolution year by year (Plotly Express `animation_frame`)
- 📉 **Box plots** for outlier detection in crime data

### Phase 3: Machine Learning
- 🤖 **Time Series Forecasting** — predict crime rates for 2021–2030 using ARIMA or Prophet
- 🔍 **Clustering Analysis** — group states with similar crime profiles using K-Means
- 📈 **Regression Models** — predict total cases based on socio-economic indicators

### Phase 4: User Experience
- 📥 **Export Feature** — download filtered data as CSV, charts as PNG/PDF
- 🔔 **Alert System** — notify when a state shows sudden spike in any crime category
- 🌐 **Multi-language** — Hindi and regional language interface
- 📱 **Mobile Responsive** — optimize layout for phone screens

### Phase 5: Data Enrichment
- 📅 **2021–2023 Data** — update dataset with latest NCRB reports
- 🏙️ **Urban vs Rural** breakdown for each crime type
- 💰 **Socio-economic overlay** — correlate crime with literacy rate, poverty index

---

---

# 💡 SLIDE 16 — Key Insights This Project Reveals

> *(Sample insights that users can discover using the app)*

1. **Uttar Pradesh** consistently ranks as the state with the highest total women's crime cases across most years

2. **Post-2012 spike in rape reporting** — after the Nirbhaya case, IPC amendments and public awareness caused a significant increase in reported cases nationwide

3. **Cyber crimes grew 10x** between 2012 and 2020 as smartphone penetration increased across India

4. **498A (Cruelty by Husband)** is the single most filed crime against women — dwarfing all other domestic violence categories

5. **POCSO cases rose sharply after 2012** when the law was enacted — indicating improved legal awareness, not necessarily more crimes

6. **Acid attacks** are concentrated in specific states (UP, MP, West Bengal) suggesting localized socio-cultural factors

7. **Southern states** like Tamil Nadu and Kerala show relatively lower crime rates when normalized by population

8. **Correlation between rape and kidnapping** is strongly positive — suggesting similar geographic and socio-economic root causes

---

---

# 🏆 SLIDE 17 — Project Impact & Value

## For Students & Researchers
- Ready-to-use interactive tool for data exploration without coding
- Can generate publication-quality charts in seconds
- Useful for sociology, criminology, public policy research

## For Journalists & Activists
- Quickly find state-specific data to support articles or campaigns
- Visualize trends that make complex data understandable to the public

## For Policymakers
- Identify states that need urgent intervention
- Track the effectiveness of new laws (e.g., POCSO 2012, IPC 2013 amendments)
- Compare crime trajectories across neighboring states

## For Technologists
- Demonstrates full-stack data science: data cleaning → analysis → visualization → web deployment
- Shows proficiency in Python, Pandas, Seaborn, Streamlit, GitHub, Netlify
- Open-source and extendable

---

---

# 📋 SLIDE 18 — Project Summary Card

| Attribute | Details |
|---|---|
| **Project Name** | HerSafetyMetrics |
| **Domain** | Data Science / Social Analytics |
| **Language** | Python 3.11 |
| **Framework** | Streamlit |
| **Libraries** | Pandas, Seaborn, Matplotlib |
| **Dataset** | NCRB Women's Crime Data (2001–2020) |
| **Dataset Size** | ~1.5 MB, 41 crime columns |
| **Pages** | 5 (Home + 4 crime category pages) |
| **Chart Types** | 6 (Line, Bar, Histogram, Heatmap, Scatter, Regression) |
| **Deployment** | Netlify (landing) + GitHub Codespaces (app) |
| **Live URL** | hersafetymetrics.netlify.app |
| **GitHub** | github.com/Sukhreet-kaur/Women-S-Crime-analysis |
| **License** | MIT |

---

---

# 🙏 SLIDE 19 — Closing

## Thank You

This project is more than a data science exercise.

It is a step towards making critical government data accessible, understandable, and actionable for everyone — from a student writing a report to an NGO building awareness campaigns.

Every chart generated, every trend discovered, every correlation found — is a small contribution to the larger movement of making India safer for women.

---

> *"In God we trust. All others must bring data."*
> — W. Edwards Deming

---

**Sukhreet Kaur**
🔗 [hersafetymetrics.netlify.app](https://hersafetymetrics.netlify.app)
💻 [github.com/Sukhreet-kaur/Women-S-Crime-analysis](https://github.com/Sukhreet-kaur/Women-S-Crime-analysis)

---
*Questions Welcome* 💜
