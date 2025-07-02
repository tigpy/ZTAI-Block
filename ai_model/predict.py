# AI Risk Engine: Prediction Script
import sys
import joblib
import pandas as pd

# Usage: python predict.py <feature1> <feature2>
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python predict.py <feature1> <feature2>')
        sys.exit(1)
    feature1 = float(sys.argv[1])
    feature2 = float(sys.argv[2])
    model = joblib.load('model.pkl')
    X = pd.DataFrame([[feature1, feature2]], columns=['feature1', 'feature2'])
    risk_score = model.predict_proba(X)[0][1]
    print(f'Predicted risk score: {risk_score:.4f}')
