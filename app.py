import streamlit as st
import pickle
import numpy as np

# Load the pickled model
with open("stock_price_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)


# Function to make predictions
def predict(stock_data):
    # Make predictions
    prediction = model.predict(stock_data)
    return prediction


# Streamlit UI
def main():
    st.title("Stock Price Prediction")
    st.write("Enter stock data to predict its price:")

    # Input fields for user to enter stock data
    stock_data = {}
    stock_data["high"] = st.number_input("High")
    stock_data["low"] = st.number_input("Low")
    stock_data["open"] = st.number_input("Open")
    stock_data["volume"] = st.number_input("Volume")

    if st.button("Predict"):
        # Convert user input to a format acceptable by the model
        input_data = np.array(
            [
                [
                    stock_data["high"],
                    stock_data["low"],
                    stock_data["open"],
                    stock_data["volume"],
                ]
            ]
        )

        # Make prediction
        result = predict(input_data)

        st.write("Predicted Closed Price:", result)


if __name__ == "__main__":
    main()
