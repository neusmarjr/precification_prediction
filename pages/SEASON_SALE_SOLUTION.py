import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import time

st.set_page_config(
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

def get_data(path):
    df_raw = pd.read_csv(path)

    return df_raw

def get_pickle(path):
    transformer = pickle.load(open(path, 'rb'))

    return transformer

def how_to_work():
    with st.sidebar:
        st.subheader("How does the solution work?")
        st.write("Inform the requested characteristics of the property that will be evaluated and press the 'Season-sale evaluation' button, the AI will calculate the probability of selling the property in each if the seasons.")
        st.write("Did you know that through the characteristics of your property it is possible to calculate the sale price, according to a successful history of property sales? For more information, access the 'PRICE PREDICTION SOLUTION' tab.")

    return None

def price_filters(df_raw):
    st.title("Season-Sale Solution")
    st.subheader("Provide the requested informations regarding the house that will be evaluated")

    c1, c2, c3 = st.columns((1, 1, 1,))

    sqft_living = c1.number_input(
        label = "Size of total living area (sqft)",
        min_value = float(df_raw['sqft_living'].min()),
        max_value = float(df_raw['sqft_living'].max()),
        value = float(df_raw['sqft_living'].min()),
        step = 1.0,
        help = "Inform the size of total living area"
    )

    sqft_lot = c2.number_input(
        label = "Size of total lot area (sqft)",
        min_value = float(df_raw['sqft_lot'].min()),
        max_value = float(df_raw['sqft_lot'].max()),
        value = float(df_raw['sqft_lot'].min()),
        step = 1.0,
        help = "Inform the size of total lot area"
    )

    sqft_above = c3.number_input(
        label = "Size of above area (sqft)",
        min_value = float(df_raw['sqft_above'].min()),
        max_value = float(df_raw['sqft_above'].max()),
        value = float(df_raw['sqft_above'].min()),
        step = 1.0,
        help = "Inform the size of above area"
    )
    
    zipcode = c1.selectbox(
        label = 'Zipcode',
        options = df_raw['zipcode'].unique(),
        help = 'Inform the zipcode of the house'
    )

    price = c2.number_input(
        label = "Total price",
        min_value = float(df_raw['price'].min()),
        max_value = float(df_raw['price'].max()),
        value = float(df_raw['price'].min()),
        step = 1.0,
        help = "Inform the total price of the house"
    )

    waterfront_view = c1.selectbox(
        label = 'Waterfront view',
        options = df_raw['waterfront_view'].unique(),
        help = 'Inform if the house has waterfront view'
    )

    landscape_view = c2.selectbox(
        label = 'Landscape view',
        options = df_raw['landscape_view'].unique(),
        help = 'Inform if the house has landscape view'
    )

    x_raw = [sqft_living, sqft_lot, sqft_above, zipcode, waterfront_view, landscape_view, price]
    
    return x_raw

def param_adequations(x_raw, encoder, scaler):
    x = encoder.transform([x_raw])
    x = scaler.transform(x)

    return x

def price_prediction(model, x):
    if st.button("Season-sale evaluation"):
        with st.spinner("Loading..."):
            time.sleep(1.5)

            prediction_proba = model.predict_proba(x)

            df_proba = pd.DataFrame(columns = ['Seasons', 'Sale Probability (%)'])
            df_proba['Seasons'] = ['Autumn', 'Spring', 'Summer', 'Winter']
            df_proba['Sale Probability (%)'] = prediction_proba[0] * 100

            fig = plt.figure()
            sns.barplot(x = 'Seasons', y = 'Sale Probability (%)', data = df_proba)
            st.pyplot(fig)
    else:
        st.write("Provide the requested informations and press the button!")

    return None

if __name__ == "__main__":

    data_path = 'datasets/df_sale.csv'
    encoder_path = 'pickle/encoder_rf_sale.pickle'
    scaler_path = 'pickle/scaler_rf_sale.pickle'
    model_path = 'pickle/rfc_model.pickle'

    how_to_work()
    df_raw = get_data(data_path)
    encoder = get_pickle(encoder_path)
    scaler = get_pickle(scaler_path)
    model = get_pickle(model_path)

    x_raw = price_filters(df_raw)
    x = param_adequations(x_raw, encoder, scaler)
    price_prediction(model, x)