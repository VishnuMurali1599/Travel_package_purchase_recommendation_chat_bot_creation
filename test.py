<!--<form action="/purchase" method="post">
            <label for="destination">Destination:</label>
            <input type="text" id="destination" name="destination" required>
            <button type="submit">Explore Packages</button>
        </form> -->
        
        
@app.route("/",methods=['GET','POST']) ## Code for chatbot
def chatbot():
    if request.method == "POST":
        dict1 = {"Message":"Hi"}
        return render_template('welcome_page.html',data=dict1)
    
    
    
<p>Welcome to our platform where you can explore and purchase various travel packages.</p>
        <p>Choose your desired destination and start planning your dream vacation!</p>
        <!-- <p>{{ dict1['Message'] }}</p> -->
        
        
<ul>
        <li>City: {{ city }}</li>
        <li>Country: {{ country }}</li>
        <li>State: {{ state }}</li>
        <li>Number of days: {{ number_of_days }}</li>
    </ul>
    
https://www.bandt.com.au/information/uploads/2021/04/Expedia-logo-1260x840.jpg



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
        #return render_template("new_package.html",results=results[0])