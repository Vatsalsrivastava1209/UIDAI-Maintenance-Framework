# Aadhaar Identity Maintenance Risk Framework — UIDAI Hackathon Project

**Built for UIDAI Data Hackathon 2026**  
District-level prioritization engine using Aadhaar enrolment/update data to identify high-risk areas for stale records and authentication failures.

**Live Demo / Interactive Dashboard**: [Link to nbviewer or GitHub Pages if you host it — or "Run locally with Jupyter"]  
**Full Report (PDF)**: [Upload the PDF to repo and link here: Aadhaar_Risk_Framework_Report.pdf]

### Problem
High-enrolment districts suffer low update rates → stale biometric/demographic data → authentication failures, exclusion, governance risk.

### Solution
- **District-level aggregation** via pincode mapping
- **Composite Risk Index**: Enrolment volume + update rate + age-group balance
- **K-means clustering** → 4 archetypes (High-Growth Low-Maintenance, etc.)
- **NITI Aayog validation** — correlation with Financial Inclusion progress
- **Prophet forecasting** for future backlog trends
- **Interactive dashboard** (ipywidgets + Plotly choropleth)

### Key Insights
- ~61% of analysed enrolments in priority archetypes needing urgent action
- Higher risk in Aspirational Districts (0.7904 vs 0.7819 avg risk score)
- Negative correlation: Faster financial inclusion progress → lower maintenance risk
- Forecast: Update demand growing → backlog risk rising without intervention

### Tech Stack
- Python: pandas, numpy, scikit-learn, Prophet, Plotly, ipywidgets
- Jupyter Notebook: `UIDAI Project.ipynb`
- Data: UIDAI anonymized enrolment/update CSVs + NITI Champions of Change (Financial Inclusion)

### Repository Structure
