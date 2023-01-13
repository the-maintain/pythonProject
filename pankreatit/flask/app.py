""""
Application that predicts heart disease percentage in the population of a town
based on the number of bikers and smokers.
Trained on the data set of percentage of people biking
to work each day, the percentage of people smoking, and the percentage of
people with heart disease in an imaginary sample of 500 towns.
"""

from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
#Create an app object using the Flask class.
app = Flask(__name__,template_folder='/home/rahman/PycharmProjects/pythonProject/pankreatit/flask/templates')

#Load the trained model. (Pickle file)
model = pickle.load(open('/home/rahman/PycharmProjects/pythonProject/pankreatit/model.pk1', 'rb'))

a= pd.DataFrame(columns=['SEX', 'AGE', 'WBC', 'NEU', 'LYM', 'HGB', 'PLT', 'NEU*PLT', 'SII', 'GLU',
                         'UREA', 'CREA', 'AST', 'ALT', 'LDH', 'AMYLASE', 'LIPASE', 'CRP', 'PLR', 'NLR',
                         'RADIO_SCORE', 'NEW_AMY_LIP', 'NEW_WBC_EQL', 'NEW_AMY_UREA', 'NEW_AMY_CREA'],
                data=[[1.0,81.0,12.9,11.44,0.96,10.9,132.0,1510.08,1573.0,111.0,
                       36.4,0.61,43.0,25.0,229.0,2615.0,3225.0,2.53,137.0,11.0,
                       81.0,5840.0,0.5,0.01392,4286.885246]])
model.predict(a)

#Define the route to be home.
#The decorator below links the relative route of the URL to the function it is decorating.
#Here, home function is with '/', our root directory.
#Running the app sends us to index.html.
#Note that render_template means it looks for the file in the templates folder.

#use the route() decorator to tell Flask what URL should trigger our function.

@app.route('/')
def home():
    return render_template('index.html')

#You can use the methods argument of the route() decorator to handle different HTTP methods.
#GET: A GET message is send, and the server returns data
#POST: Used to send HTML form data to the server.
#Add Post method to the decorator to allow for form submission.
#Redirect to /predict page with the output

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()] #Convert string inputs to float.
    features = [np.array(int_features)]  #Convert to the form [[a, b]] for input to the model
    a = pd.DataFrame(data=features,
        columns=['SEX', 'AGE', 'WBC', 'NEU', 'LYM', 'HGB',
                 'PLT', 'NEU*PLT', 'SII', 'GLU', 'UREA', 'CREA',
                 'AST', 'ALT','LDH', 'AMYLASE', 'LIPASE', 'CRP',
                 'PLR', 'NLR', 'RADIO_SCORE', 'NEW_AMY_LIP',
                 'NEW_WBC_EQL','NEW_AMY_UREA', 'NEW_AMY_CREA'])
    prediction = model.predict(a)  # features Must be in the form [[a, b]]
    output = prediction[0]
    return render_template('index.html',
                           prediction_text="The patient's progression will be  {}".format("worse" if output==1 else "better"))




#When the Python interpreter reads a source file, it first defines a few special variables.
#For now, we care about the __name__ variable.
#If we execute our code in the main program, like in our case here, it assigns
# __main__ as the name (__name__).
#So if we want to run our code right here, we can check if __name__ == __main__
#if so, execute it here.
#If we import this file (module) to another file then __name__ == app (which is the name of this python file).

if __name__ == "__main__":
    app.run(debug=False)