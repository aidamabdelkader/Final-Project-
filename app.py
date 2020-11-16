from flask import Flask, render_template, request
import joblib


app = Flask(__name__)

model = joblib.load('model.pkl')
 
@app.route("/")
def home():
	return render_template('index.html')

 
@app.route("/predict", methods=["POST"])
def predict():

	contract = request.form['Contract']
	gender = request.form["Gender"]
	car = request.form["Car"]
	child = request.form['Child']
	credit = request.form['Credit']
	annuity = request.form['Annuity']
	familystatus = request.form['Familystatus']
	income = request.form["Income"]
	education = request.form["Education"]
	housing = request.form["Housing"]
	employed = request.form["Employed"]
	registration = request.form["Registration"]
	carage = request.form["CarAge"]
	age = request.form["Age"]
	return (model.predict([[contract , gender, car, child,credit, annuity, familystatus, income,education,housing,employed,registration,carage,age]])[0])
	return render_template("index.html", result=result)
if __name__ == "__main__":
	app.run()  