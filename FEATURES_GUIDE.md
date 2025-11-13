# 📊 Feature Descriptions for SafeBalance

## Financial Metrics Guide

### Current Assets & Liquidity

**X1 - Current Assets**
- Description: Total value of assets that can be converted to cash within one year
- Examples: Cash, accounts receivable, inventory, marketable securities
- Importance: Indicates short-term financial health and liquidity

**X2 - Inventory**
- Description: Total value of goods available for sale
- Examples: Raw materials, work-in-progress, finished goods
- Importance: Affects working capital and operational efficiency

**X3 - Quick Assets**
- Description: Most liquid assets excluding inventory
- Formula: Current Assets - Inventory
- Importance: Better measure of immediate liquidity

### Current Liabilities

**X4 - Current Liabilities**
- Description: Obligations due within one year
- Examples: Accounts payable, short-term debt, accrued expenses
- Importance: Measures short-term financial obligations

**X5 - Accounts Payable**
- Description: Money owed to suppliers and vendors
- Importance: Indicates payment management and supplier relationships

**X14 - Short Term Debt**
- Description: Debt obligations due within one year
- Examples: Credit lines, current portion of long-term debt
- Importance: Critical for liquidity analysis

### Profitability & Income

**X6 - Net Income**
- Description: Bottom-line profit after all expenses and taxes
- Formula: Total Revenue - Total Expenses - Taxes
- Importance: Ultimate measure of profitability

**X11 - EBIT (Earnings Before Interest and Taxes)**
- Description: Operating profit before financing costs
- Formula: Revenue - Operating Expenses
- Importance: Shows core business profitability

**X13 - Gross Profit**
- Description: Revenue minus cost of goods sold
- Formula: Revenue - COGS
- Importance: Measures production efficiency

### Assets & Equity

**X7 - Accounts Receivable**
- Description: Money owed by customers for goods/services delivered
- Importance: Indicates sales on credit and collection efficiency

**X8 - Cash & Cash Equivalents**
- Description: Most liquid assets immediately available
- Examples: Bank deposits, money market funds, Treasury bills
- Importance: Critical for operational stability

**X9 - Stockholders' Equity**
- Description: Owners' residual interest in the company
- Formula: Total Assets - Total Liabilities
- Importance: Represents net worth of the company

**X10 - Total Assets**
- Description: Sum of all company assets
- Examples: Current assets + Fixed assets + Intangibles
- Importance: Measures company size and resource base

**X12 - Retained Earnings**
- Description: Cumulative profits retained in the business
- Formula: Previous Retained Earnings + Net Income - Dividends
- Importance: Shows reinvestment and dividend policy

### Revenue & Debt

**X15 - Working Capital**
- Description: Difference between current assets and liabilities
- Formula: Current Assets - Current Liabilities
- Importance: Measures operational liquidity

**X16 - Other Expenses**
- Description: Miscellaneous operational expenses
- Examples: Administrative costs, marketing, R&D
- Importance: Affects overall profitability

**X17 - Total Revenue**
- Description: Total sales from all business operations
- Examples: Product sales + Service revenue
- Importance: Top-line growth indicator

**X18 - Total Liabilities**
- Description: Sum of all company debts and obligations
- Formula: Current Liabilities + Long-term Liabilities
- Importance: Measures leverage and financial risk

### Company Classification

**Division**
- Description: Industry division code (SIC-based)
- Values: A, B, C, D, E, F, G, H, I
- Examples:
  - A: Agriculture, Forestry, Fishing
  - B: Mining
  - C: Construction
  - D: Manufacturing
  - E: Transportation, Communications, Utilities
  - F: Wholesale Trade
  - G: Retail Trade
  - H: Finance, Insurance, Real Estate
  - I: Services
- Importance: Industry-specific risk factors

**MajorGroup**
- Description: Detailed industry classification code
- Examples:
  - 35: Industrial Machinery
  - 36: Electronic Equipment
  - 37: Transportation Equipment
  - 38: Instruments & Related Products
  - 50: Wholesale Trade - Durable Goods
  - 51: Wholesale Trade - Non-Durable Goods
  - 73: Business Services
- Importance: Fine-grained industry analysis

---

## 🔍 Engineered Financial Ratios

The model automatically calculates these ratios from your input:

### 1. Current Ratio
- **Formula**: X1 / X14
- **Meaning**: Ability to pay short-term obligations
- **Healthy Range**: > 1.5

### 2. Leverage Ratio
- **Formula**: X18 / X10
- **Meaning**: Proportion of debt financing
- **Healthy Range**: < 0.6

### 3. Profit Margin
- **Formula**: X6 / X17
- **Meaning**: Profitability per dollar of revenue
- **Healthy Range**: > 0.05 (5%)

### 4. Asset Turnover
- **Formula**: X17 / X10
- **Meaning**: Revenue generation efficiency
- **Healthy Range**: > 1.0

### 5. Debt-to-Equity
- **Formula**: X18 / (X10 - X18)
- **Meaning**: Financial leverage
- **Healthy Range**: < 2.0

### 6. EBIT Margin
- **Formula**: X11 / X17
- **Meaning**: Operating profitability
- **Healthy Range**: > 0.10 (10%)

### 7. Gross Margin
- **Formula**: X13 / X17
- **Meaning**: Production efficiency
- **Healthy Range**: > 0.20 (20%)

### 8. Receivables Ratio
- **Formula**: X7 / X10
- **Meaning**: Asset composition
- **Healthy Range**: 0.10 - 0.30

### 9. Inventory Turnover
- **Formula**: X2 / X5
- **Meaning**: Inventory management efficiency
- **Healthy Range**: Industry-specific

---

## 📝 Data Entry Tips

1. **Use actual values** from financial statements (balance sheet, income statement)
2. **Maintain consistent units** (all in same currency)
3. **Use positive values** for assets, revenue, equity
4. **Use positive values** for liabilities, expenses, debt
5. **Check for reasonableness** (e.g., X10 should be > X1)
6. **Verify Division and MajorGroup** codes match your industry

---

## ⚠️ Common Mistakes

- ❌ Mixing different fiscal periods
- ❌ Using ratios instead of absolute values
- ❌ Negative values for positive accounts
- ❌ Missing or zero values for required fields
- ❌ Inconsistent currency units

---

## 💡 Example: Healthy Company Profile

```
X1 (Current Assets): 2,500,000
X2 (Inventory): 800,000
X3 (Quick Assets): 1,700,000
X4 (Current Liabilities): 1,200,000
X5 (Accounts Payable): 400,000
X6 (Net Income): 450,000
X7 (Receivables): 600,000
X8 (Cash): 900,000
X9 (Equity): 3,000,000
X10 (Total Assets): 8,000,000
X11 (EBIT): 650,000
X12 (Retained Earnings): 2,200,000
X13 (Gross Profit): 1,800,000
X14 (Short-term Debt): 800,000
X15 (Working Capital): 1,300,000
X16 (Other Expenses): 1,150,000
X17 (Total Revenue): 6,000,000
X18 (Total Liabilities): 5,000,000
Division: D (Manufacturing)
MajorGroup: 36 (Electronic Equipment)
```

**Key Indicators:**
- Current Ratio: 3.13 (Excellent)
- Profit Margin: 7.5% (Good)
- Debt-to-Equity: 1.67 (Acceptable)
- Expected Prediction: **Alive** with Low Risk

---

For more information, see README.md
