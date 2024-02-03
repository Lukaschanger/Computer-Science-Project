
#import visualisation library matplotlib and PAndas
import matplotlib.pyplot as plt

import pandas as pd

# Import CSV and read
file_path = "/Users/lukas/IU University/Mood_Total.csv"
moods_data = pd.read_csv(file_path)


# Counting moods by category
mood_distribution = moods_data['mood'].value_counts()

# Column chart of the moods activated over time 
plt.figure(figsize=(12, 6))
mood_distribution.plot(kind='bar')
plt.title('Distribution of Moods')
plt.xlabel('Mood')
plt.ylabel('Frequency')
plt.xticks(rotation=90, fontsize=12)
plt.grid(axis='y')
plt.tight_layout()
plt.show()