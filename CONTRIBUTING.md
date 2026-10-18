# 🤝 Contributing to HerSafetyMetrics

Thank you for your interest in contributing to **HerSafetyMetrics**! This project aims to make women's crime data in India more accessible and understandable through data visualization. Every contribution, big or small, is valued.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Guidelines](#development-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)

---

## 🌟 Code of Conduct

This project is dedicated to providing a respectful and inclusive environment. By participating, you agree to:

- Use inclusive and respectful language
- Be considerate of different viewpoints
- Accept constructive criticism gracefully
- Focus on what is best for the community and the cause

---

## 💡 How Can I Contribute?

### 🐛 Bug Reports
Found something broken? Open an issue with:
- A clear, descriptive title
- Steps to reproduce the bug
- Expected vs actual behavior
- Your OS and Python version

### ✨ Feature Suggestions
Have an idea? Open a feature request issue with:
- A clear description of the feature
- Why it would benefit users or the project's mission
- Any relevant examples or mockups

### 📊 Data Improvements
- Additional NCRB datasets (post-2020)
- Data cleaning or normalization improvements
- New crime categories or sub-categories

### 💻 Code Contributions
- Fix bugs from the issues list
- Implement features from the roadmap
- Improve visualizations or UI/UX
- Add new analysis pages or chart types
- Write or improve documentation

---

## 🚀 Getting Started

### 1. Fork the Repository

Click the **Fork** button on GitHub to create your own copy.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/Women-S-Crime-analysis.git
cd Women-S-Crime-analysis
```

### 3. Set Up the Development Environment

```bash
# Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### 4. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 5. Run the App Locally

```bash
streamlit run home.py
```

---

## 🛠️ Development Guidelines

### Code Style

- Follow **PEP 8** Python style conventions
- Use meaningful variable names (avoid single-letter names like `r`, `op` for new code)
- Add docstrings to all functions
- Keep functions short and focused on a single responsibility

### Visualization Standards

- Use consistent color palettes (prefer `darksalmon`, `skyblue`, `Blues` already in use)
- Always add titles to charts via `plt.title()`
- Include axis labels for all plots
- Use `st.pyplot(fig)` and always pass the `fig` object explicitly

### Session State & Navigation

- Use `st.session_state.page` for all page navigation
- Always define `go_to(page_name)` helper before using it
- New pages should be added as `elif st.session_state.page == "your_page":` blocks

### File Structure for New Pages

If adding a new crime category or analysis page:
```python
elif st.session_state.page == "new_page":
    crime_analysis_page("Category Name", columns['CategoryKey'])
```

---

## 📥 Pull Request Process

1. **Ensure** your code runs without errors locally
2. **Update** `README.md` if you added or changed features
3. **Update** `CHANGELOG.md` with a brief description of your changes
4. **Commit** with a clear, descriptive message:
   ```bash
   git commit -m "feat: add choropleth map for state-wise crime visualization"
   git commit -m "fix: correct outdoor crime page routing bug"
   git commit -m "docs: update README with new feature screenshots"
   ```
5. **Push** to your fork and open a Pull Request against `main`
6. Fill in the PR template with context about what you changed and why

### Commit Message Format
```
type: short description

Types: feat | fix | docs | style | refactor | test | chore
```

---

## 🐛 Reporting Issues

Use GitHub Issues with the appropriate label:
- `bug` — Something isn't working
- `enhancement` — New feature request
- `documentation` — Docs improvements
- `data` — Dataset-related issues
- `good first issue` — Great for newcomers

---

## 🙏 Recognition

All contributors will be acknowledged in the project README. Thank you for helping make this project better and supporting the mission of women's safety awareness through data! 💜
