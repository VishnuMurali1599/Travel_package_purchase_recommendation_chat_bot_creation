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