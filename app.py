from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gallary')
def gallary():
    return render_template('gallary.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

model = pickle.load(open('loan_pred.pkl','rb'))
@app.route('/predict', methods=['post'])
def predict():
    gender = request.form.get('gender')
    married = request.form.get('married')
    dependents = request.form.get('dependents')
    education = request.form.get('education')
    selfemployed = request.form.get('selfemployed')
    applicantincome= request.form.get('applicantincome')
    coapplicantincome = request.form.get('coapplicantincome')
    loanamount = request.form.get('loanamount')
    loanamountterm = request.form.get('loanamountterm')
    credithistory = request.form.get('credithistory')
    propertyarea = request.form.get('propertyarea')

    a = int(dependents)
    b = int(applicantincome)
    c = float(coapplicantincome)
    d = float(loanamount)
    e = float(loanamountterm)
    f = float(credithistory)
    if gender == 'Male':
        g = 1
    else:
        g = 0
    if married == 'Yes':
        h = 1
    else:
        h = 0
    if education == 'Graduate':
        i = 1
    else:
        i = 0
    if selfemployed == 'Yes':
        j = 1
    else:
        j = 0
    if propertyarea == 'Semiurban':
        k = 1
        l = 0
    elif propertyarea == 'Urban':
        k = 0
        l = 1
    else:
        k = 0
        l = 0

    data = model.predict([[a, b, c, d, e, f, g, h, i, j, k, l]])

    print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i), type(j), type(k), type(l))
    # return f'{a}, {b}, {c}, {d}, {e}, {f}, {g}, {h}, {i}, {j}, {k}, {l}'
    if data[0] == 'N':
        return 'Sorry. You are not eligible for the loan.'
    else:
        return 'Congratulations! You are eligible for the loan.'

if __name__ == "__main__":
    app.run(debug=True)