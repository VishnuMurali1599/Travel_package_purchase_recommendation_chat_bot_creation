from flask import Flask, render_template, request, redirect, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Route for the welcome page
@app.route('/',methods=['POST'])
def welcome():
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
    
    with open('artifacts\trained_pipeline_trans.pkl', 'rb') as file:
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


if __name__=="__main__":
    app.run(debug=True)