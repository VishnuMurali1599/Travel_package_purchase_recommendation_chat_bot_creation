# app.py
from flask import Flask, render_template, request, redirect, jsonify
import pandas as pd

app = Flask(__name__)

# Route for the welcome page
@app.route('/')
def welcome():
    # Render the template and pass the dictionary to it
    return render_template('welcome_page.html')

@app.route('/destination', methods=['GET', 'POST'])
def destination():
    if request.method == 'POST':
        # Get city and country values from the form
        city = request.form['city']
        country = request.form['country']
        
        # Read the DataFrame from CSV file
        df = pd.read_csv("FinalData.csv")
        
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

# Route to handle form submission
@app.route('/purchase', methods=['POST'])
def purchase():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
