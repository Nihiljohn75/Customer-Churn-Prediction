#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    roc_curve,
    classification_report,
    cohen_kappa_score,
    ConfusionMatrixDisplay
)

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import pickle


# In[2]:


df=pd.read_csv('customer_churn_cleaned.csv')
df.head()


# In[3]:


df.info()


# In[4]:


df.shape


# In[5]:


X=df.drop('Churn',axis=1)
Y=df['Churn']


# In[6]:


le=LabelEncoder()

Y= le.fit_transform(Y)

Y[:5]


# In[7]:


X=pd.get_dummies(X, columns=['Gender','Contract', 'PaymentMethod'], drop_first=True, dtype=int
)
X.head()


# In[8]:


x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=42, stratify=Y)


# In[9]:


print(x_train.shape)
print(x_test.shape)

print(y_train.shape)
print(y_test.shape)


# In[10]:


Numerical_cols=['Age','Tenure','MonthlyCharges','TotalCharges']


# In[11]:


scale=StandardScaler()


# In[15]:


x_train[Numerical_cols]=scale.fit_transform(x_train[Numerical_cols])
x_test[Numerical_cols]=scale.fit_transform(x_test[Numerical_cols])
x_train.head()


# In[17]:


models = []
accuracy = []
precision = []
recall = []
f1 = []
roc_auc = []
kappa = []
cv_accuracy = []

def model_validation(model, X_train, y_train, X_test, y_test):

    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    y_prob = model.predict_proba(X_test)[:, 1]

    print("=" * 60)
    print(f"Model : {model.__class__.__name__}")
    print("=" * 60)

    print(f"Training Accuracy : {accuracy_score(y_train, train_pred):.4f}")
    print(f"Testing Accuracy  : {accuracy_score(y_test, test_pred):.4f}")
    print(f"ROC-AUC Score     : {roc_auc_score(y_test, y_prob):.4f}")

    print("\nClassification Report\n")
    print(classification_report(y_test, test_pred))

    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
    plt.title("Confusion Matrix")
    plt.show()

    fpr, tpr, threshold = roc_curve(y_test, y_prob)

    plt.figure(figsize=(6, 5))
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc_score(y_test, y_prob):.3f}")
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.show()

    cv = cross_val_score(
        model,
        X_train,
        y_train,
        cv=5,
        scoring='accuracy'
    ).mean()

    print(f"Cross Validation Accuracy : {cv:.4f}")

    if hasattr(model, "coef_"):

        coef = pd.DataFrame({
            "Feature": X_train.columns,
            "Coefficient": model.coef_[0]
        })

        coef = coef.sort_values(
            by="Coefficient",
            ascending=False
        )

        print("\nTop Features\n")
        print(coef.head(10))

    elif hasattr(model, "feature_importances_"):

        imp = pd.DataFrame({
            "Feature": X_train.columns,
            "Importance": model.feature_importances_
        })

        imp = imp.sort_values(
            by="Importance",
            ascending=False
        )

        print("\nTop Features\n")
        print(imp.head(10))

    models.append(model.__class__.__name__)
    accuracy.append(accuracy_score(y_test, test_pred))
    precision.append(precision_score(y_test, test_pred))
    recall.append(recall_score(y_test, test_pred))
    f1.append(f1_score(y_test, test_pred))
    roc_auc.append(roc_auc_score(y_test, y_prob))
    kappa.append(cohen_kappa_score(y_test, test_pred))
    cv_accuracy.append(cv)

    scorecard = pd.DataFrame({
        "Model": models,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "ROC-AUC": roc_auc,
        "Cohen Kappa": kappa,
        "CV Accuracy": cv_accuracy
    })

    return scorecard


# In[19]:


lr = LogisticRegression(random_state=42)

scorecard = model_validation(
    lr,
    x_train,
    y_train,
    x_test,
    y_test
)

scorecard


# In[20]:


dt=DecisionTreeClassifier(random_state=42)

scorecard = model_validation(
    dt,
    x_train,
    y_train,
    x_test,
    y_test
)

scorecard



# In[21]:


rf = RandomForestClassifier(random_state=42)

scorecard = model_validation(
    rf,
    x_train,
    y_train,
    x_test,
    y_test
)

scorecard


# In[22]:


xgb = XGBClassifier(random_state=42)

scorecard = model_validation(
    xgb,
    x_train,
    y_train,
    x_test,
    y_test
)

scorecard


# In[23]:


scorecard.sort_values(by=["ROC-AUC", "F1 Score", "Accuracy"],ascending=False)


# In[25]:


params = {
    'n_estimators': [100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1],
    'subsample': [0.8, 1.0]
}


# In[27]:


xgb = XGBClassifier(
    random_state=42,
    eval_metric='logloss'
)

grid = GridSearchCV(
    estimator=xgb,
    param_grid=params,
    cv=5,
    scoring='roc_auc',
    n_jobs=-1
)

grid.fit(x_train, y_train)


# In[28]:


grid.best_score_


# In[29]:


best_xgb = grid.best_estimator_


# In[30]:


scorecard = model_validation(
    best_xgb,
    x_train,
    y_train,
    x_test,
    y_test
)

scorecard


# In[31]:


importance = pd.DataFrame({
    'Feature': x_train.columns,
    'Importance': best_xgb.feature_importances_
})

importance = importance.sort_values(
    by='Importance',
    ascending=False
)

importance.head(15)


# In[32]:


plt.figure(figsize=(10,6))

plt.barh(
    importance['Feature'][:15],
    importance['Importance'][:15]
)

plt.title("Top 15 Important Features")
plt.xlabel("Importance")
plt.gca().invert_yaxis()

plt.show()


# In[34]:


with open("customer_churn_model.pkl", "wb") as file:
    pickle.dump(best_xgb, file)


# In[35]:


with open("scaler.pkl", "wb") as file:
    pickle.dump(scale, file)


# In[36]:


with open("label_encoder.pkl", "wb") as file:
    pickle.dump(le, file)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




