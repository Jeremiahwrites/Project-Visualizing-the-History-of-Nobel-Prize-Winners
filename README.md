# 🏆 Visualizing the History of Nobel Prize Winners (1901–2023)

## 📌 Project Overview

The **Nobel Prize** is one of the world’s most prestigious honors, awarded annually to individuals and organizations that have made outstanding contributions to humanity.

Since **1901**, prizes have been awarded in:

* Physics
* Chemistry
* Physiology or Medicine
* Literature
* Peace
* Economics *(added later in 1968)*

This project explores over a century of Nobel Prize data using **Python, Pandas, and Seaborn** to uncover historical trends, representation shifts, repeat winners, and demographic patterns.

---

# 🎯 Business Questions Answered

This analysis focused on answering the following key questions:

1. What is the most commonly awarded gender?
2. Which birth country has produced the most Nobel laureates?
3. Which decade had the highest proportion of U.S.-born winners?
4. Which decade and category had the highest proportion of female laureates?
5. Who was the first woman to win a Nobel Prize?
6. Which individuals or organizations have won multiple Nobel Prizes?

---

# 🛠️ Tools & Technologies Used

* **Python**
* **Pandas**
* **Seaborn**
* **Matplotlib**
* **Jupyter Notebook**

---

# 📂 Dataset

Source: Nobel Prize API
File Used: `nobel.csv`

Contains:

* Laureate Name
* Gender
* Birth Country
* Prize Category
* Award Year
* Organization / Individual Info

---

# 🔍 Key Analysis & Insights

---

# 1️⃣ Most Commonly Awarded Gender

### 🏆 Result:

**Male**

### 📌 Insight:

Historically, Nobel Prizes have been overwhelmingly awarded to men, reflecting long-standing global gender inequality in education, research access, and leadership opportunities.

---

# 2️⃣ Country with Most Nobel Laureates

### 🏆 Result:

**United States of America**

### 📌 Insight:

The U.S. has dominated Nobel Prize wins, particularly after World War II, due to:

* Strong university systems
* Research funding
* Immigration of global talent
* Innovation-driven economy

---

# 3️⃣ Decade with Highest Ratio of U.S.-Born Winners

### 🏆 Result:

Stored in:

```python id="gtt1jd"
max_decade_usa
```

### 📌 Insight:

This indicates when American academic and scientific dominance peaked globally.

Likely driven by:

* Cold War research funding
* Growth of Ivy League and STEM institutions
* Post-war innovation boom

---

# 4️⃣ Decade & Category with Highest Female Representation

### 🏆 Result:

Stored in:

```python id="ab7g3v"
max_female_dict
```

Example format:

```python id="n8sm7x"
{2020: 'Literature'}
```

### 📌 Insight:

Female representation has historically been low but has increased significantly in recent decades, especially in:

* Literature
* Peace
* Medicine

This signals progress toward inclusion.

---

# 5️⃣ First Woman Nobel Prize Winner

### 🏆 Result:

| Name        | Category |
| ----------- | -------- |
| Marie Curie | Physics  |

### 📌 Insight:

Marie Curie broke historical barriers and remains one of the most iconic figures in science history.

She later won a second Nobel Prize in Chemistry, making her one of the few repeat winners.

---

# 6️⃣ Repeat Nobel Prize Winners

### 🏆 Examples:

* Marie Curie
* Linus Pauling
* John Bardeen
* International Committee of the Red Cross
* UNHCR

### 📌 Insight:

Winning twice demonstrates exceptional and lasting global impact.

Organizations often reappear in Peace categories due to sustained humanitarian service.

---

# 📈 Visualizations Included

## USA-born Winners Over Time

A line chart showing the proportion of Nobel winners born in the USA by decade.

## Female Laureates by Category

A multi-line chart showing female winner ratios across categories over time.

---

# 💡 Strategic Insights

## 🌍 Global Shift in Innovation

Early Nobel winners were dominated by Europe. Later decades show strong U.S. dominance.

## 👩 Women Representation is Improving

Though still underrepresented, female laureates have risen sharply in modern decades.

## 🧪 Science Drives Prestige

Physics, Chemistry, and Medicine remain the most globally competitive categories.

## 🤝 Organizations Matter Too

Peace Prizes show that institutions can shape the world as much as individuals.

---

# 🧹 Data Skills Demonstrated

✅ Data Cleaning
✅ Boolean Filtering
✅ GroupBy Aggregation
✅ Trend Analysis
✅ Data Visualization
✅ Historical Pattern Discovery

---

# 💻 Sample Code

```python id="z3w4s7"
nobel['decade'] = (nobel['year'] // 10) * 10
```

```python id="b6m2q9"
usa_ratio = nobel.groupby('decade')['usa_born_winners'].mean()
```

---

# 🚀 Final Conclusion

The Nobel Prize dataset tells a larger story beyond awards.

It reveals:

* The rise and fall of global scientific power
* Historical gender inequality
* National investment in innovation
* Individuals whose work changed humanity

Data transforms history into measurable insight.

---

# 📁 Repository Structure

```bash id="5a2rjk"
📦 Nobel-Prize-Analysis
 ┣ 📄 nobel.csv
 ┣ 📄 Nobel_Analysis.ipynb
 ┣ 📄 README.md
```

---

# 🔗 Connect With Me

If you found this project insightful, feel free to ⭐ the repository and connect with me.

---

# #Python #DataAnalytics #DataScience #Pandas #Seaborn #NobelPrize #MachineLearning #EDA #PortfolioProject
