# Obesity Prediction using Machine Learning

This project predicts obesity levels based on health and lifestyle factors using a K-Nearest Neighbors (KNN) classifier. Below are key insights from the analysis.

## Key Visualizations

### 1. Feature Importance
![Feature Importance](https://raw.githubusercontent.com/manisharyal2001/Obesity-Prediction/main/feature_importance.png)
*Top features influencing obesity prediction. Weight and Age show the highest impact.*

---

### 2. Obesity Level Distribution
![Obesity Distribution](https://raw.githubusercontent.com/manisharyal2001/Obesity-Prediction/main/obesity_distribution.png)
*Class distribution in the dataset. Obesity_Type_I and Normal_Weight are most prevalent.*

---

### 3. Correlation Heatmap
![Correlation Heatmap](https://raw.githubusercontent.com/manisharyal2001/Obesity-Prediction/main/correlation_heatmap.png)
*Relationships between numerical features. Weight and Height show moderate correlation (0.46).*

---

### 4. Pair Plot of Numerical Features
![Pair Plot](https://raw.githubusercontent.com/manisharyal2001/Obesity-Prediction/main/pairplot.png)
*Pairwise relationships between Age, Weight, Height, and obesity levels.*

---

### 5. Confusion Matrix
![Confusion Matrix](https://raw.githubusercontent.com/manisharyal2001/Obesity-Prediction/main/confusion_matrix.png)
*Performance of the KNN model across obesity categories.*

## Project Structure
- `knn.ipynb`: Jupyter notebook with data preprocessing, model training, and evaluation.
- `submission.csv`: Predicted obesity levels for test data.
- `obesity.csv`: Training dataset.

## Results
- Model Accuracy: **83.97%**
- Key Findings:
  - Weight and Age are top predictors.
  - Classes are moderately balanced (12-17% distribution).

## How to Run
1. Install requirements:
   ```bash
   pip install pandas scikit-learn matplotlib seaborn
