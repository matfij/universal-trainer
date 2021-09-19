## ML approaches

### 1. Supervised learning
Model is learning from labelled training data to predict a category (class) or value (regression) based on input data.

### 2. Unsupervised learning
Model is building it's own representation of a problem (e.g. Clustering) based on an unlabelled training set.

### 3. Reinforced learning
These algorithms are build from three main components: Agent (decision maker), Environment and Actions. In the learning process the Agent is trying to choose Actions that maximizes the Reward (scores).

---

## General ML pipeline
1. Data acquisition (sensors, web)
2. Data cleaning (outliers, missing values, non-numeric values)
3. Split data into Training and Testing sets (unsupervised learning does not require data split)
4. Train and evaluate model (many models to choose the best architecture)
5. Adjust model parameters until satisfactory results are reached
6. Export and deploy model

---

## Evaluation metrics
 - Accuracy, Recall, Precision - for classification supervised learning, based on correctly predicted outputs, true positives/negatives, identifying relevant data points
 - MAE, MSE, RMSE - for regression supervised learning, based on difference between obtained and target output values
 - Cluster homogenity, rand index - unsupervised learning, measures similarity of cluster datapoints
