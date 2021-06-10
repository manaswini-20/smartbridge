from flask import Flask , render_template , request
import pickle
import numpy as np
app = Flask(__name__)
d = pickle.load(open('regression1.pkl','rb'))

@app.route('/')
def home():
    return render_template('cars.html')
@app.route('/predict', methods = ['POST'])
def demo():
    
    cyl = int(request.form["cylinders"])
    dis = int(request.form["displacement"])
    hp = int(request.form["horsepower"])
    w = int(request.form["weight"])
    a = int(request.form["acceleration"])
    my = int(request.form["model year"])
    ori = int(request.form["origin "])
    total = np.array([[cyl,dis,hp,w,a,my,ori]])
    
    result = d.predict(total)
    #result =p[0]
    x=result
    return render_template('cars.html',x='Mileage Of Car is {} Mpg'.format(*x))

if __name__=='__main__':
    app.run()