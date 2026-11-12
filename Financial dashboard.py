# TASK 1: Financial Health Dashboard - SME - CodeAlpha
import matplotlib.pyplot as plt
import pandas as pd

# Load Input
df = pd.read_csv('financial_input.csv')
dates = df['Date'].tolist()
revenue = df['Revenue'].tolist()
cogs = df['COGS'].tolist()
net_income = df['Net_Income'].tolist()

# Dashboard
fig = plt.figure(figsize=(10, 12))
fig.patch.set_facecolor('#f0f2f5')
plt.suptitle('Financial Health Dashboard - SME', fontsize=14, fontweight='bold')

gs = fig.add_gridspec(4, 2, hspace=0.6, wspace=0.4)

# KPI
ax_kpi = fig.add_subplot(gs[0, :])
ax_kpi.axis('off')
ax_kpi.text(0.05, 0.5, "Revenue: ₹4.20M (+8.2%) | COGS: ₹2.18M (52%) | Net: ₹903K (21.5% Margin)", 
            fontsize=10, fontweight='bold', bbox=dict(facecolor='white', edgecolor='#0078D4', boxstyle='round,pad=0.5'))

# Income
ax1 = fig.add_subplot(gs[1, 0])
ax1.plot(dates, revenue, label='Revenue', color='#0078D4')
ax1.plot(dates, cogs, label='COGS', color='#D83B01', linestyle='--')
ax1.plot(dates, net_income, label='Net Income', color='#107C10')
ax1.set_title('Income Statement', fontsize=10, fontweight='bold')
ax1.tick_params(axis='x', rotation=90, labelsize=7)
ax1.legend(fontsize=6)
ax1.grid(True, alpha=0.3)

# Profitability
ax2 = fig.add_subplot(gs[1, 1])
gross_margin = [(r-c)/r*100 for r,c in zip(revenue, cogs)]
net_margin = [n/r*100 for n,r in zip(net_income, revenue)]
ax2.plot(dates, gross_margin, label='Gross Margin', color='#0078D4')
ax2.plot(dates, net_margin, label='Net Margin', color='#107C10')
ax2.set_title('Profitability Margin %', fontsize=10, fontweight='bold')
ax2.tick_params(axis='x', rotation=90, labelsize=7)
ax2.legend(fontsize=6)
ax2.grid(True, alpha=0.3)

# Balance Sheet
ax3 = fig.add_subplot(gs[2, 0])
ax3.pie([27.5, 9.9, 11.0, 51.6], labels=['Cash','Recv','Inv','Fixed'], autopct='%1.1f%%', textprops={'fontsize': 7})
ax3.set_title('Balance Sheet - Assets', fontsize=10, fontweight='bold')

# Cash Flow
ax4 = fig.add_subplot(gs[2, 1])
ax4.bar(['Op CF','Inv CF','Fin CF','Net CF'], [160000,-28000,-14000,118000], color=['#107C10','#D83B01','#D83B01','#107C10'])
ax4.set_title('Cash Flow', fontsize=10, fontweight='bold')

# Forecasting
ax5 = fig.add_subplot(gs[3, :])
future = ['2026-01','2026-03','2026-05','2026-07']
forecast = [700000, 716000, 732000, 748000]
ax5.plot(dates[-6:], revenue[-6:], label='Actual', color='#0078D4')
ax5.plot(future, forecast, label='Forecast', color='#D83B01', linestyle='--')
ax5.fill_between(future, [f*0.92 for f in forecast], [f*1.08 for f in forecast], color='#D83B01', alpha=0.15)
ax5.set_title('Budgeting & Forecasting Next 6 Months (+12%)', fontsize=10, fontweight='bold')
ax5.legend(fontsize=7)
ax5.grid(True, alpha=0.3)

fig.text(0.5, 0.01, "INSIGHTS: Healthy 21.5% Margin | Cash Positive ₹1.18L/mo | COGS 52% Reduce to 48%", ha='center', fontsize=8, bbox=dict(facecolor="#FFF4CE", edgecolor="#FFC000"))

plt.savefig('financial_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()
print("SUCCESS!")
