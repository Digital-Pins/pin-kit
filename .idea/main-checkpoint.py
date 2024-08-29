import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# تحميل البيانات
# يمكنك استبدال 'your_dataset.csv' بملف البيانات الخاص بك
data = pd.read_csv('CVS.csv')

# افترض أن البيانات تحتوي على ميزات في الأعمدة من 0 إلى -2 والهدف في العمود الأخير
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# تقسيم البيانات إلى مجموعة تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# إنشاء مصفوفة DMatrix الخاصة بـ XGBoost
train_data = xgb.DMatrix(X_train, label=y_train)
test_data = xgb.DMatrix(X_test, label=y_test)

# ضبط معلمات XGBoost
params = {
    'objective': 'binary:logistic',  # استخدم 'reg:squarederror' للتوقعات العددية
    'max_depth': 6,
    'eta': 0.3,
    'eval_metric': 'logloss'
}

# تدريب النموذج
bst = xgb.train(params, train_data, num_boost_round=10)

# التنبؤ باستخدام النموذج المدرب
y_pred = bst.predict(test_data)
predictions = [1 if pred > 0.5 else 0 for pred in y_pred]

# حساب الدقة
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")
