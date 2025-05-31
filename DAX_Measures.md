# 🧮 DAX Measures – Superstore Sales Dashboard

This document contains all custom DAX measures used in the Power BI Superstore Sales Analytics Dashboard. 

---

## 📦 1. Total Sales
```DAX
Total Sales = SUM(Cleaned_Superstore[Sales])
```

## 🧾 2. Total Orders
```DAX
Order Count = DISTINCTCOUNT(Cleaned_Superstore[Order ID])
```

## 👥 3. Unique Customers
```DAX
Customer Count = DISTINCTCOUNT(Cleaned_Superstore[Customer ID])
```

## 📅 4. Average Sales Per Day
```DAX
Average Sales per Day = 
AVERAGEX(
    VALUES('DateTable'[Date]),
    CALCULATE([Total Sales])
)
```

## 📈 5. Monthly Sales
```DAX
Monthly Sales = 
CALCULATE(
    [Total Sales], 
    DATESMTD('DateTable'[Date])
)
```

## 📉 6. 6-Month Moving Average
```DAX
Sales 6M MA = 
AVERAGEX(
    DATESINPERIOD(
        'DateTable'[Date],
        MAX('DateTable'[Date]),
        -6,
        MONTH
    ),
    [Total Sales]
)
```

```

---

