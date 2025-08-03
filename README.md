# 🏡 House Price Prediction Using Linear Regression

This project is part of the **SkillCraft Internship** and focuses on building a simple machine learning model to predict house prices based on key features like square footage, number of bedrooms, and number of bathrooms.

## 📌 Objective

To implement a **Linear Regression** model that can accurately predict house prices using structured housing data.

## 📊 Features Used
- `square_footage`
- `bedrooms`
- `bathrooms`

## 🛠️ Tech Stack
- Python
- Pandas
- scikit-learn
- NumPy
- VS Code

## 📁 Project Structure
```
house-price-prediction/
│
├── data/
│   └── house_price_dataset.csv
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── src/
│   └── model.py
│
├── README.md
└── requirements.txt
```

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/house-price-prediction.git
   cd house-price-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the model:
   ```bash
   python src/model.py
   ```

## 📈 Model Evaluation

- **Metric Used:** Mean Squared Error (MSE)
- The model was trained using an 80/20 train-test split.
- Coefficients were interpreted to understand the influence of each feature on the predicted price.

## ✨ Learnings

- Building and evaluating a regression pipeline
- Understanding feature importance
- Applying scikit-learn for real-world ML tasks
- Structuring code and folders for clarity and scalability

