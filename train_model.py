import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, precision_score, recall_score
import joblib   # ✅ use joblib instead of pickle

# Load dataset
df = pd.read_csv("heart.csv")

# Continuous columns
num_cols = ['age','trestbps','chol','thalach','oldpeak']

# Categorical columns
cat_cols = ['sex','cp','fbs','restecg','exang','slope','ca','thal']

# --- Encoding ---
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded_cat = encoder.fit_transform(df[cat_cols])
encoded_cat_df = pd.DataFrame(
    encoded_cat,
    columns=encoder.get_feature_names_out(cat_cols)
)

# Combine numeric + categorical
data = pd.concat([df[num_cols], encoded_cat_df], axis=1)

# Target
y = df['target']

# --- Scaling ---
scaler = StandardScaler()
data[num_cols] = scaler.fit_transform(data[num_cols])

# --- Train-test split ---
X_train, X_test, y_train, y_test = train_test_split(
    data, y, test_size=0.2, random_state=0
)

# --- Model ---
model = KNeighborsClassifier()
model.fit(X_train, y_train)

# ✅ SAVE using joblib (IMPORTANT)
joblib.dump(model, "model.pkl")
joblib.dump(encoder, "encoder.pkl")
joblib.dump(scaler, "scaler.pkl")

# --- Evaluation ---
y_pred = model.predict(X_test)

print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))