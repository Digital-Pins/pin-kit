import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# إنشاء بيانات افتراضية
np.random.seed(42)
data = pd.DataFrame({
    'ad_spending': np.random.randint(1000, 5000, size=100),
    'season': np.random.randint(1, 4, size=100),
    'holiday': np.random.randint(0, 2, size=100),
    'sales': np.random.randint(5000, 10000, size=100)
})

# عرض أول 5 صفوف من البيانات
print(data.head())

# فصل الميزات والهدف
X = data[['ad_spending', 'season', 'holiday']]
y = data['sales']

# تقسيم البيانات إلى مجموعة تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# بناء النموذج
model = LinearRegression()
model.fit(X_train, y_train)

# التنبؤ
y_pred = model.predict(X_test)

# تقييم النموذج
rmse = mean_squared_error(y_test, y_pred, squared=False)  # استخدام squared=False لحساب RMSE
print(f"RMSE: {rmse}")
print(f"R²: {r2_score(y_test, y_pred)}")

# عرض معاملات النموذج
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
