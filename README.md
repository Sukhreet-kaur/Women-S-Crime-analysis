# 🌸 HerSafetyMetrics — Women's Crime Analysis Dashboard

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C72B0?style=for-the-badge)
![Netlify](https://img.shields.io/badge/Netlify-Deployed-00C7B7?style=for-the-badge&logo=netlify&logoColor=white)

**An interactive data analysis dashboard uncovering two decades of women's crime trends across India (2001–2020)**

🔗 **Live Demo:** [hersafetymetrics.netlify.app](https://hersafetymetrics.netlify.app)  
📊 **Data Source:** National Crime Records Bureau (NCRB), Government of India

</div>

---

## 📌 Project Overview

**HerSafetyMetrics** is a data-driven web application that analyzes women-related crimes in India from **2001 to 2020** using official NCRB data. It enables users to explore crime patterns, regional disparities, and temporal trends through interactive visualizations — helping raise awareness and support informed policy decisions.

> *"Data is the most powerful tool for advocacy. This project turns raw numbers into insights that matter."*

---

## 🎯 Problem Statement

Gender-based violence in India remains a deeply systemic issue. With rising incidents of rape, domestic violence, child exploitation (POCSO), and outdoor crimes, understanding the **where**, **when**, and **how much** becomes critical for:

- 📣 Raising public awareness
- 🏛️ Informing policymakers and NGOs
- 📈 Tracking the effectiveness of legal interventions over time
- 🔍 Identifying high-risk states and crime clusters

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🏠 **Home Dashboard** | Dataset preview with dynamic row selection and shape info |
| 🔍 **Smart Data Explorer** | Filter data by state, year, and custom column combinations |
| 📊 **Total Cases Visualizer** | Bar and line charts grouped by state or year |
| 🔗 **Correlation Heatmaps** | Understand how different crime types co-occur |
| 📈 **Scatter Regression Plots** | Visualize directional relationships between crime types |
| 🗂️ **4 Crime Category Pages** | Deep-dive into Rape, Domestic Violence, POCSO, and Outdoor Crimes |
| 📉 **Frequency Histograms** | Year-wise distribution with KDE for skewness analysis |
| 📅 **Trend Line Analysis** | Crime rate evolution across 20 years |
| 🗺️ **State-wise Bar Charts** | Compare crime volumes across all Indian states |
| 📐 **Multi-parameter Analysis** | Dual-crime regression for any state/year combination |

---

## 🗂️ Crime Categories Covered

```
📁 Rape Cases
   ├── Rape
   ├── Attempt to Rape
   ├── Gang Rape
   └── Murder with Rape

📁 Domestic Violence
   ├── Dowry Deaths
   ├── Dowry Prohibition Act
   ├── Cruelty by Husband/Relatives (IPC 498A)
   └── Dowry Harassment

📁 POCSO Cases (Child Protection)
   ├── POCSO Rape
   ├── POCSO Assault
   ├── POCSO Harassment
   ├── Child Marriage Prohibition Act
   ├── Procuration of Minor Girls
   └── Importation of Girls

📁 Outdoor Crimes
   ├── Sexual Harassment at Workplace
   ├── Attempt to Kidnap
   ├── Cyber Stalking / Bullying
   ├── Cyber Crime (Obscenity)
   ├── Trafficking
   ├── Stalking (IPC 354D)
   ├── Acid Attack
   └── Attempt to Acid Attack
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.11 |
| **Web Framework** | Streamlit |
| **Data Manipulation** | Pandas |
| **Visualizations** | Seaborn, Matplotlib |
| **Data** | CSV (NCRB Cleaned Dataset, ~1.5 MB) |
| **Deployment** | Netlify (Landing Page) + GitHub Codespaces (Streamlit App) |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure

```
Women-S-Crime-analysis/
│
├── 📄 home.py                                  # Main Streamlit application
├── 📊 women_crime_india_2001_2021_cleaned.csv  # Cleaned NCRB dataset
├── 📋 requirements.txt                         # Python dependencies
├── 📖 README.md                                # Project documentation (this file)
├── 📝 CONTRIBUTING.md                          # Contribution guidelines
├── 🗒️  CHANGELOG.md                            # Version history
│
├── 📁 .devcontainer/
│   └── devcontainer.json                       # GitHub Codespaces configuration
│
└── 📁 .git/                                    # Git version control
```

---

## 📊 Dataset Overview

- **Source:** National Crime Records Bureau (NCRB), Ministry of Home Affairs, India
- **Time Period:** 2001 – 2020 (20 years)
- **Granularity:** State-wise and District-wise
- **Total Columns:** 41 crime-related features + `state`, `year`, `district`, `total_cases`
- **File Size:** ~1.5 MB (cleaned CSV)

### Sample Columns

```
rape, attempt_to_rape, gang_rape, murder_with_rape,
kidnapping_and_abduction, dowry_deaths, acid_attack,
stalking_354D, pocso_rape, pocso_assault,
cyber_stalking_bullying_against_women, trafficking,
cruelty_by_husband_or_relatives_498A, total_cases ...
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Srikanthbanoth7533/Women-S-Crime-analysis.git
cd Women-S-Crime-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run home.py
```

### Open in Browser
The app will open automatically at: `http://localhost:8501`

---

## ☁️ GitHub Codespaces (Zero Setup)

This project is fully configured for **GitHub Codespaces** — no local setup needed!

1. Click **Code → Open with Codespaces** on GitHub
2. The environment auto-installs all dependencies
3. The Streamlit app launches automatically on port `8501`

---

## 📱 Application Pages & Navigation

```
🏠 Home
 ├── Dataset Preview (configurable row count)
 ├── DataFrame Explorer (filter by state/year/columns)
 ├── Total Cases Visualizer (state or year-wise)
 ├── Crime Correlation Analysis (scatter / heatmap)
 └── Navigate to Crime Category ──────────────┐
                                               │
 ┌─────────────────────────────────────────────┘
 │
 ├── 🔴 Rape Cases Page
 ├── 🏠 Domestic Violence Page
 ├── 👶 POCSO Cases Page
 └── 🌆 Outdoor Crime Page
       ├── Data Preview (state + year filter)
       ├── Frequency Histogram (KDE)
       ├── Year-wise Trend Line
       ├── Grouped Bar Chart (state or year)
       ├── Multi-parameter Comparison
       └── Statistical Analysis (Scatter / Heatmap)
```

---

## 📸 Screenshots

> 🔗 Visit the live site: [hersafetymetrics.netlify.app](https://hersafetymetrics.netlify.app)

| Section | Description |
|---|---|
| 🏠 Landing Page | Hero section with navigation to all modules |
| 📊 Dashboard | Interactive crime category exploration |
| 📈 EDA Insights | Correlation heatmaps and trend analysis |
| 🔮 Prediction | Future crime trend forecasting (2021–2030) |

---

## 🔮 Future Scope

- [ ] 🗺️ **Choropleth Maps** — State-level crime intensity using Plotly/Folium
- [ ] 🤖 **ML Prediction Model** — Forecast crime rates for 2021–2030
- [ ] 📥 **Export Reports** — Download filtered data and charts as PDF/PNG
- [ ] 🔔 **Alert System** — Flag states with sudden crime spikes
- [ ] 📱 **Mobile Responsive UI** — Better layout for smaller screens
- [ ] 🌐 **Multi-language Support** — Hindi and regional language options

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how to get started.

---

## 📃 License

This project is open-source and available under the [MIT License](./LICENSE).

---

## 👨‍💻 Authors

**Srikanth Banoth**  
Data Analyst | Python Developer  
📧 banothsrikanth75338@gmail.com  
📞 9392327533

[![GitHub](https://img.shields.io/badge/GitHub-Srikanthbanoth7533-181717?style=flat&logo=github)](https://github.com/Srikanthbanoth7533)

**Sukhreet Kaur**  
Data Analyst | Python Developer

---

## 🙏 Acknowledgements

- **NCRB (National Crime Records Bureau)** — For making the data publicly accessible
- **Streamlit Community** — For the amazing open-source framework
- **Every advocate and researcher** working to make India safer for women

---

<div align="center">

*"Until every woman is safe, the work is not done."* 💜

**⭐ Star this repo if you find it impactful!**

</div>
