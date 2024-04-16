# app.py
from flask import Flask, render_template, request, redirect, jsonify
import pandas as pd
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
import pickle

app = Flask(__name__)

# Route for the welcome page
@app.route('/',methods=['GET','POST'])
def welcome():
    # Render the template and pass the dictionary to it
    if request.method=='GET':
        return render_template('welcome_page.html')
    else:
        data = request.get_json()
        capital = data['queryResult']['parameters']['geo-capital'][0]
        country = data['queryResult']['parameters']['geo-country'][0]
        number = data['queryResult']['parameters']['number'][0]
        transport_mode = data['queryResult']['parameters']['City-countrydetails'][0]
        
        print(capital)
        print(country)
        print(number)
        print(transport_mode)
        
        cost = transportation_cost(capital,country,number,transport_mode)
        
        response = {
            "fulfillmentText":"Can expect Travel cost around {} USD".format(round(cost[0],2))
        }
        print(cost)
        print(response)
        #return "<h1> hello </h1>"
        return jsonify(response)

def transportation_cost(capital: str, country: str, number: int, transport_mode: str):
    capital = capital.capitalize()
    country = country.capitalize()
    transport_mode = transport_mode.capitalize()

    #df = pd.read_csv("travel_accomedation_costs.csv")

    # Filter the DataFrame based on the provided parameters
    #filtered_df = df[(df['City'] == capital) & (df['Country'] == country) & (df['Duration'] == number) & (df['Transportation type'] == transport_mode)]

    # Check if there are any matching records
    
    with open('artifacts/trained_pipeline_trans.pkl', 'rb') as file:
        loaded_pipeline = pickle.load(file)
        
        new_data = pd.DataFrame({"Duration": [number], "Transportation type": [transport_mode],
                                 "City": [capital],
                                 "Country": [country]},index=[0])  # Specify an index for the DataFrame
        
        new_predictions = loaded_pipeline.predict(new_data)
        print(new_predictions[0])
    
        #if not new_predictions.empty:
            #transportation_cost = new_predictions[0]
            #return transportation_cost
        #else:
            #return "Sorry we are unable to fecth cost for provided country"
            
        if new_predictions.size > 0:  # Check if new_predictions contains any elements
            transportation_cost = new_predictions[0]
            return transportation_cost
        else:
            return "Sorry we are unable to fetch the cost for the provided country"


@app.route('/destination', methods=['GET', 'POST'])
def destination():
    if request.method == 'POST':
        # Get city and country values from the form
        city = request.form['city']
        country = request.form['country']
        city = city.capitalize()
        
        # Read the DataFrame from CSV file
        df = pd.read_csv("research/data/FinalData.csv")
        
        # Filter and sort DataFrame based on city and country
        filtered_df = df[(df["Country"] == country) & (df["City"] == city)]
        sorted_df = filtered_df.sort_values(by=["Ratings"], ascending=False).head(20)
        sorted_df.drop(columns=["Unnamed: 0","City","Country","City_desc"],inplace=True)
        sorted_df.loc[:,["Place","Ratings","Distance","Place_desc","Best_time_to_visit"]]
        
        # Pass the DataFrame to the template for rendering
        return render_template('destination_results.html', data=sorted_df.to_html(index=False))
    else:
        return render_template('destination.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/package',methods=['GET','POST'])
def package():
    if request.method=='GET':
        return render_template('new_package.html')
    else:
        data=CustomData(
            Age = float(request.form.get('Age')),
            TypeofContact = request.form.get('TypeofContact'),
            CityTier = int(request.form.get('CityTier')),
            Occupation = request.form.get('Occupation'),
            Gender = request.form.get('Gender'),
            NumberOfPersonVisiting = int(request.form.get('NumberOfPersonVisiting')),
            PreferredPropertyStar = float(request.form.get('PreferredPropertyStar')),
            MaritalStatus = request.form.get('MaritalStatus'),
            NumberOfTrips = float(request.form.get('NumberOfTrips')),
            Passport = int(request.form.get('Passport')),
            OwnCar = int(request.form.get('OwnCar')),
            NumberOfChildrenVisiting = float(request.form.get('NumberOfChildrenVisiting')),
            Designation = request.form.get('Designation'),
            MonthlyIncome = float(request.form.get('MonthlyIncome'))
        )
        
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template("new_package.html",results=results[0])
        #return render_template("new_package.html")
    

if __name__ == '__main__':
    app.run(debug=True)
