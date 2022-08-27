import streamlit as st
import pandas as pd
import pickle
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
        st.write("Inform the requested characteristics of the property that will be evaluated and press the 'Price evaluation' button, the AI will calculate the price/sqft forecast and display the value on the screen.")
        st.write("Did you know that through the characteristics of your property it is possible to calculate in which period of the year it is most likely to be sold? For more information, access the 'SEASON-SALE SOLUTION' tab.")

    return None

def price_filters(df_raw):
    st.title("Price Prediction Solution")
    st.subheader("Provide the requested informations regarding the house that will be evaluated")

    c1, c2, c3 = st.columns((1, 1, 1,))

    bedrooms = c1.number_input(
        label = "Number of bedrooms",
        min_value = df_raw['bedrooms'].min(),
        max_value = df_raw['bedrooms'].max(),
        value = 1,
        step = 1,
        help = "Inform the number for bedrooms"
    )

    bathrooms = c2.number_input(
        label = "Number of bathrooms",
        min_value = df_raw['bathrooms'].min(),
        max_value = df_raw['bathrooms'].max(),
        value = 1,
        step = 1,
        help = "Inform the number for bathrooms"
    )

    floors = c3.number_input(
        label = "Number of floors",
        min_value = df_raw['floors'].min(),
        max_value = df_raw['floors'].max(),
        value = 1,
        step = 1,
        help = "Inform the number for floors"
    )
    
    sqft_living = c1.number_input(
        label = "Size of total living area (sqft)",
        min_value = float(df_raw['sqft_living'].min()),
        max_value = float(df_raw['sqft_living'].max()),
        value = float(df_raw['sqft_living'].min()),
        step = 1.0,
        help = "Inform the size of total living area"
    )

    zipcode = c2.selectbox(
        label = 'Zipcode',
        options = df_raw['zipcode'].unique(),
        help = 'Inform the zipcode'
    )

    yr_built = c3.number_input(
        label = "Year built",
        min_value = df_raw['yr_built'].min(),
        max_value = df_raw['yr_built'].max(),
        value = df_raw['yr_built'].min(),
        step = 1,
        help = "Inform the construction year"
    )

    renovated = c1.selectbox(
        label = 'Renovated house',
        options = df_raw['renovated'].unique(),
        help = 'Inform if the house is renovated'
    )

    condition_evaluation = c2.selectbox(
        label = 'Condition evaluation',
        options = df_raw['condition_evaluation'].unique(),
        help = 'Inform the condition of the house'
    )

    grade_evaluation = c3.selectbox(
        label = 'Grade evaluation',
        options = df_raw['grade_evaluation'].unique(),
        help = 'Inform the grade of the house'
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

    x_raw = [bedrooms, bathrooms, sqft_living, floors, yr_built, zipcode, waterfront_view, landscape_view, condition_evaluation, grade_evaluation, renovated]
    
    return x_raw

def param_adequations(x_raw, encoder, scaler):
    x = encoder.transform([x_raw])
    x = scaler.transform(x)

    return x

def price_prediction(model, x):
    if st.button("Price evaluation"):
        with st.spinner("Loading..."):
            time.sleep(1.5)
            prediction = model.predict(x)
            st.markdown(
                "<h4>The price/sqft of the house is $ {:.2f}</h4>".format(prediction[0]),
                unsafe_allow_html=True
            )
    else:
        st.write("Provide the requested informations and press the button!")

    return None

if __name__ == "__main__":

    data_path = 'datasets/df_price.csv'
    encoder_path = 'pickle/encoder_price.pickle'
    scaler_path = 'pickle/scaler_price.pickle'
    model_path = 'pickle/rxg_model.pickle'

    how_to_work()
    df_raw = get_data(data_path)
    encoder = get_pickle(encoder_path)
    scaler = get_pickle(scaler_path)
    model = get_pickle(model_path)

    x_raw = price_filters(df_raw)
    x = param_adequations(x_raw, encoder, scaler)
    price_prediction(model, x)