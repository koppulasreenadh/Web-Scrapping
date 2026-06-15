import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup

# =========================================================================
# STEP 1: LIVE DATA SOURCE EMULATION (Job Board Target DOM)
# =========================================================================
job_portal_html = """
<!DOCTYPE html>
<html>
<body>
    <div class="search-results">
        <div class="job-card" data-skills="Python, SQL"><h2 class="job-title">Senior Data Analyst</h2><div class="company">Fintech Global</div><div class="job-metadata"><span class="salary">$115,000</span><span class="location">Remote</span></div></div>
        <div class="job-card" data-skills="Python, AWS"><h2 class="job-title">Data Engineer</h2><div class="company">CloudScale Systems</div><div class="job-metadata"><span class="salary">$142,000</span><span class="location">Hybrid</span></div></div>
        <div class="job-card" data-skills="Python, PyTorch"><h2 class="job-title">AI/ML Engineer</h2><div class="company">Neural Labs</div><div class="job-metadata"><span class="salary">$168,000</span><span class="location">Remote</span></div></div>
        <div class="job-card" data-skills="SQL, PowerBI"><h2 class="job-title">BI Analyst</h2><div class="company">Retail Giant Corp</div><div class="job-metadata"><span class="salary">$95,000</span><span class="location">On-Site</span></div></div>
        <div class="job-card" data-skills="Python, R"><h2 class="job-title">Data Scientist</h2><div class="company">BioHealth AI</div><div class="job-metadata"><span class="salary">$135,000</span><span class="location">Remote</span></div></div>
    </div>
</body>
</html>
"""

# =========================================================================
# STEP 2: HTML PROCESSING & STRUCTURAL PARSING
# =========================================================================
soup = BeautifulSoup(job_portal_html, "html.parser")
scraped_jobs = []

for card in soup.find_all("div", class_="job-card"):
    title = card.find("h2", class_="job-title").text.strip()
    company = card.find("div", class_="company").text.strip()
    metadata = card.find("div", class_="job-metadata")
    location = metadata.find("span", class_="location").text.strip()
    
    raw_salary = metadata.find("span", class_="salary").text
    clean_salary = int(raw_salary.replace("$", "").replace(",", ""))
    
    scraped_jobs.append({
        "Job_Title": title,
        "Company": company,
        "Base_Salary_USD": clean_salary,
        "Work_Model": location
    })

df = pd.DataFrame(scraped_jobs)

# Ensure folders exist in your VS Code workspace background
os.makedirs("data", exist_ok=True)
os.makedirs("dashboards", exist_ok=True)
df.to_csv("data/scraped_job_market_analytics.csv", index=False)

# =========================================================================
# STEP 3: HIGH-END CLIENT EXECUTIVE DASHBOARD DESIGN
# =========================================================================
# Establish a modern presentation foundation
sns.set_theme(style="white", rc={"grid.linestyle": "-", "grid.color": "#F0F0F0"})
plt.rcParams["font.sans-serif"] = "Arial"
plt.rcParams["font.family"] = "sans-serif"

# Initialize 1-row, 2-column Canvas
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Define an ultra-clean corporate color palette
primary_blue = "#1A365D"
accent_teal = "#2C7A7B"
palette_gradient = ["#1A365D", "#2A4365", "#2B6CB0", "#3182CE", "#4299E1"]

# --- PANEL A: EXECUTIVE VALUATION INDEX ---
sorted_df = df.sort_values(by="Base_Salary_USD", ascending=False)
barplot = sns.barplot(
    x="Base_Salary_USD", 
    y="Job_Title", 
    data=sorted_df, 
    ax=axes[0], 
    palette=palette_gradient,
    edgecolor="none",
    width=0.6
)

# Inject direct corporate numerical metrics inside the layout
for p in barplot.patches:
    width = p.get_width()
    axes[0].text(
        width - 15000, 
        p.get_y() + p.get_height() / 2, 
        f"${width:,.0f}", 
        va="center", 
        ha="right", 
        color="white", 
        fontweight="bold", 
        fontsize=10
    )

axes[0].set_title("Annual Compensation Index Across Domains", fontsize=14, fontweight="bold", pad=15, color=primary_blue)
axes[0].set_xlabel("Market Base Salary (USD)", fontsize=11, color="#4A5568", labelpad=10)
axes[0].set_ylabel("")
axes[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))
sns.despine(ax=axes[0], left=True, bottom=True)
axes[0].grid(axis="x", color="#E2E8F0", linestyle="--")

# --- PANEL B: STRUCTURAL DISTRIBUTION BREAKDOWN ---
# Premium violin plot showing continuous density
sns.violinplot(
    x="Work_Model", 
    y="Base_Salary_USD", 
    data=df, 
    ax=axes[1], 
    color="#E2E8F0", 
    inner=None, 
    width=0.6,
    edgecolor="#CBD5E0"
)
# Overlay absolute metrics tracking markers
sns.stripplot(
    x="Work_Model", 
    y="Base_Salary_USD", 
    data=df, 
    ax=axes[1], 
    color=accent_teal, 
    size=9, 
    jitter=0.05, 
    linewidth=1.5, 
    edgecolor="white"
)

axes[1].set_title("Compensation Density by Workplace Model", fontsize=14, fontweight="bold", pad=15, color=primary_blue)
axes[1].set_xlabel("Work Model Classification", fontsize=11, color="#4A5568", labelpad=10)
axes[1].set_ylabel("")
axes[1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))
sns.despine(ax=axes[1], left=True, bottom=True)
axes[1].grid(axis="y", color="#E2E8F0", linestyle="--")

# --- GLOBAL DASHBOARD DECORATIONS ---
plt.suptitle("  TECH MARKET ANALYTICS REPORT | EXECUTIVE BRIEF", 
             fontsize=18, fontweight="bold", x=0.08, y=0.98, ha="left", color=primary_blue)

# Clean, automated padding calculation engine
plt.tight_layout(rect=[0, 0, 1, 0.93])

# Save high-resolution client presentation artifact
client_dashboard_file = "dashboards/executive_client_dashboard.png"
plt.savefig(client_dashboard_file, dpi=300, bbox_inches="tight")

print("\n" + "🚀" * 35)
print(f" CLIENT ASSETS RE-ENGINEERED: Saved to '{client_dashboard_file}'")
print("🚀" * 35 + "\n")
plt.show()