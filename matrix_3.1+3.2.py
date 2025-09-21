import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Average Noise Level / dB': [61.5, 64.9, 65.9, 59.7, 69.8, 69.7, 63.9, 65.9, 64.7, 62.3, 54.8, 54.7],
    'Pedestrian Volume': [82, 82, 199, 70, 39, 57, 48, 117, 67, 21, 13, 28],
}

df = pd.DataFrame(data)
corr_matrix = df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Average Noise Level (dB) vs. Pedestrian Volume")
plt.show()