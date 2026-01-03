import pandas as pd
import folium
import sqlite3

from flask import Flask, request, render_template

itemLookingFor = ['bread', 'steak','califlower'] #this will be modified by webpage
itemLookingFor = 'bread'

app = Flask(__name__)
#base index.html
@app.route('/')
def home():
    return render_template('index.html')



@app.route("/submit-selection", methods=["POST"])
def submit_selection():
    # Connect to the database
    conn = sqlite3.connect("database.db")
    itemLookingFor = request.form.get("product")
    zipcode = request.form.get("zipcode")
    zipcode = str(zipcode)
    print(f"product ID {itemLookingFor} | zipcode {zipcode}")
    #product_name = PRODUCTS.get(product_id, "Unknown Product")


    # Write your SQL query (change 'users' to your table name)
    storeQuery = "SELECT storeID, storeName, long, lat, zipcode FROM stores"
    itemQuery = "SELECT storeID, item, price FROM items"

    # Load data into a Pandas DataFrame
    storeDF = pd.read_sql_query(storeQuery, conn)
    # Convert column 'zipcode' to strings
    storeDF['zipcode'] = storeDF['zipcode'].astype(str)
    itemDF = pd.read_sql_query(itemQuery, conn)
    print(storeDF)
    print(itemQuery)
    # Close the connection
    conn.close()


    m = folium.Map(location=[40.497346, -74.440088], zoom_start=12)
    
    """
    Filter DATABASES HERE 
    """
    
    filteredItems = itemDF[itemDF['item'] == itemLookingFor]
    #filteredItems = filteredItems.sort_values(by='price', ascending=True) #make it so smallest price 
    #cheepestPrice = filteredItems['price'].iat[0]
    #cheepestID = filteredItems['storeID'].iat[0]
    filteredStore = storeDF[storeDF['storeID'].isin(filteredItems['storeID'])]
    filteredStore = filteredStore[filteredStore['zipcode'] == zipcode]
    print(f"filteredStore {filteredStore}")
    print(f"store DF {filteredStore}")
    print(f"item DF {filteredItems}")
    for _, row in filteredStore.iterrows():

        lat = row['lat']
        print(f"lat {lat}")
        lon = row['long']
        lon *= -1
        print(f"lon {lon}")
        store_name = row['storeName']
        store_id = row['storeID']
        price = filteredItems.loc[filteredItems['storeID'] == store_id, 'price']
        price = float(price)
        print(float(price))
        #price = result.values(0)
        item = itemLookingFor



        folium.CircleMarker(
            location=(lat, lon),
            radius=5,
            color="blue",
            fill=True,
            fill_color="cyan",
            fill_opacity=0.6,
            popup=f"Store Name: {store_name} |\n {itemLookingFor} ${price}",
        ).add_to(m)

    map_path = "templates/map.html"
    m.save(map_path)
    print("Interactive map saved as 'map.html'")
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True)