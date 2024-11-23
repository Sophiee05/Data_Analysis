import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("nobel_prize_data.csv")

print(data.head())

data = data.dropna()

print(data.describe())

grouped = data.groupby("birth_country")["year"].mean()
print(grouped)

per_country = data["birth_country"].value_counts()
print(f"{per_country}\nThis shows that the United States of America "
      f"has had the most number of Laureates over the years.")

print(data.columns)

per_year = data.groupby(["year", "sex"]).size().unstack()
per_year.plot(kind="line")
plt.xlabel('Year')
plt.ylabel('Number of Laureates')
plt.title('Number of Males vs. Female Nobel Laureates per Year')
plt.tight_layout()
plt.show()
print("\nTHE LINE CHART SHOWS THAT MORE MALES WERE AWARDED OVER THE YEARS\n")

per_country.head(20).plot(kind="bar", color="purple")
plt.xlabel('Birth Country')
plt.ylabel('Number of Laureates')
plt.title('Top 20 Countries by Number of Laureates')
plt.tight_layout()
plt.show()
print("\nTHE BAR PLOT SHOWS THAT THE UNITED STATES OF AMERICA HAS HAD THE MOST LAUREATES\n")

data["year"].plot(kind="hist", bins=15, color="lightgreen")
plt.xlabel('Year')
plt.ylabel('Frequency')
plt.title('Distribution of Nobel Prize Awards by Year')
plt.show()

per_year = data.groupby("year").size()
plt.scatter(per_year.index, per_year.values, color="red")
plt.xlabel('Year')
plt.ylabel('Number of Laureates')
plt.title('Year vs. Number of Laureates')
plt.show()

print("\nTHE HISTOGRAM AND SCATTER PLOT SHOW THAT THE NUMBER OF LAUREATES AND AWARDS GREW OVER THE YEARS\n")

