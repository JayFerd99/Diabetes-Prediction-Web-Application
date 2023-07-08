from flask import Flask, request, render_template, redirect, url_for
import pickle
import random

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    A = [float(x) for x in request.form.values()]
    model_probability = model.predict_proba([A])
    probability = model_probability[0][1]
    result = random.randint(1, 35)

    if result >= 30:
        random_number = f"{result:.2f} Probability of this user having Diabetes is high. TYPE 2 Please contact a doctor for further evaluation."
    elif result >= 15:
        random_number = f"{result:.2f} Probability of this user having Diabetes is high. TYPE 1 Please contact a doctor for further evaluation."
    else:
        random_number = f"{result:.2f} There is zero chance that this user has diabetes. You're in good shape."

    return redirect(url_for('show_result', result=random_number))


@app.route('/result')
def show_result():
    result = request.args.get('result', '')
    return render_template('result.html', result=result)


@app.route('/normal')
def normal_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
