![correlation_plot_Rana_Atalla_Python](https://github.com/user-attachments/assets/6bd643c2-5ae7-4078-a253-e42544ebc1bb)

#step1
# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='wine', version=1, as_frame=True)

#step2
print(data.DESCR)
df = data.frame
df.sample(30)
df.describe()
df.dtypes

#step3
features = list(df.columns)
print("Available features:", features)
selected_features = [features[1], features[2], features[6], features[7], features[10]]
print("Selected features: ", selected_features)

#step4
fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, selected_features):
    ax.hist(df[f], bins=5, color='purple', edgecolor='black')
    ax.set_xlabel(f)


#step5
reference_feature = selected_features[0]
y = df[reference_feature]

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, features):
  ax.scatter(df[f], y)
  ax.set_xlabel(f)

plt.show()


#step6
reference_feature = selected_features[3]  # The reference feature
comparison_feature = selected_features[2]  # A feature to compare to

# Create a scatter plot for the selected pair
plt.figure(figsize=(8, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.6, c='Indigo', edgecolors='Indigo')
plt.xlabel(reference_feature, fontsize=20)
plt.ylabel(comparison_feature, fontsize=20)

# Save the plot as an image file
plt.savefig('correlation_plot.png')

plt.show()



