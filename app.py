import streamlit as st
import requests
import json

st.title("Movie Cluster Prediction App :clapper:")

# Taking user inputs
year = st.sidebar.slider("Year", 1900, 2100, 2021)
metascore = st.sidebar.slider("Metascore", 0, 100, 50)
duration_in_minutes = st.sidebar.slider("Duration in Minutes", 0, 500, 90)
score = st.sidebar.slider('Score', 0.0, 10.0, 7.6)

# Converting the inputs into a JSON format
inputs = {
    "Year": year,
    "Metascore": metascore,
    "Duration_in_minutes": duration_in_minutes,
    "Score": score
}

# When the user clicks on the button, it will fetch the API
if st.button('Get Prediction'):
    try:
        res = requests.post(
            url="https://film-api-2zs2.onrender.com/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(inputs)
        )
        res.raise_for_status()
        response_json = res.json()

        # Debug: Print the full response
        

        # Extract and display the predicted cluster
        predicted_cluster = response_json.get("Cluster")
        if predicted_cluster is not None:
            st.write(f"The movie is in cluster: {predicted_cluster}")
        else:
            st.write("The API did not return a valid cluster prediction.")
    
    except requests.exceptions.RequestException as e:
        st.error(f"HTTP Request failed: {e}")
     
    except ValueError as e:
        st.error(f"Failed to parse JSON response: {e}")
