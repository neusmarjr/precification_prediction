# Price & Season-Sale Prediction Solution

## 1.0 Description
In order to improve and develop myself within the field of data science, the creation of this solution works both as a topic of study and as a portfolio project.

### 1.1 Scenario
To create the solution, I created a scenario where it would be necessary to deliver the MVP of a data science project, with the objective of predicting the liquidity of the property price as well as the best period of the year for this property to be sold. In this scenario, the solution would be used by people from the business area (data citizens), so one of the goals would be to build a self-service solution, with a simple and intuitive interface.

## 2.0 Data Attributes
The data for this project were obtained from a public file available on the [kaggle website](https://www.kaggle.com/datasets/shivachandel/kc-house-data).

### 2.1 Variables Glossary
- `id` - property identification number
- `date` - date of sale of the property
- `price` - sale price of the property
- `bedrooms` - number of bedrooms
- `bathrooms` - number of bathrooms, with 0.5 referring to bathrooms without shower (washroom)
- `sqft_living` - footage (in square feet) of the interior area of ​​the property
- `sqft_lot` - yardage (in square feet) of the land
- `floors` - number of floors
- `waterfront` - whether the property has a sea view (0: no, 1: yes)
- `view` - whether the property has a landscape view (0: no, 1: yes)
- `condition` - concerns the condition of the property (1 to 5)
- `grade` - deals with the construction and design of the property (1-3: low quality, 7: medium quality, 11-13: high quality)
- `sqft_above` - footage (in square feet) of the interior space that is above ground level
- `sqft_basement` - footage (in square feet) of the interior space that is below ground level
- `yr_built` - year of construction of the property
- `yr_renovated` - year of renovation of the property
- `zipcode` - Zip code of the property
- `lat` - latitude
- `long` - longitude
- `sqft_living15` - average footage (in square feet) of the interior area of ​​the property of the 15 closest neighbors
- `sqft_lot15` - average footage (in square feet) of the land of the 15 closest neighbors

## 3.0 Solution Strategy
### 3.1 Research Strategy
1. Removal of duplicate data
2. Adequacy of data types
    2.1. `date` --> datetime64[ns]
    2.2. `bathrooms` --> int64
    2.3. `floors` --> int64
3. Outlier analysis
    3.1. Z-score method
    3.2. IQR method
    3.3. boxplot visualization
4. Feature engineering
    4.1. `waterfront view` - whether the property has a sea view (Yes, No)
    4.2. `landscape-view` - whether the property has a landscape view (Yes, No)
    4.3. `condition_evaluation` - concerns the condition of the property (Really Good, Good, Regular, Bad, Really Bad)
    4.4. `grade_evaluation` - deals with the construction and design of the property (Good, Regular, Bad)
    4.5. `price/sqft` - sale price for square feet of the property
    4.6. `renovated` - whether the property has been renovated (Yes, No)
    4.7. `season` - season of sale of the property (Spring, Summer,  Autumn, Winter)
5. Descriptive analysis
    5.1. Univariate analysis
    5.2. Bivariate analysis
    5.3. Multivariate analysis
    5.4. Analysis by maps
6. Price & Sale Prediction Model
    6.1. Features selection
    6.2. Preparation of parameters
    6.3. Models training and test

### 3.2 Production Strategy
1. Loading the data
2. Loading the adequation models
    2.1. Scaler
    2.2. Encoder
3. Loading prediction models
4. Creation of the input structure
5. Application of the prediction model
6. Output of the result

### 3.3 Deploy Strategy
1. Use of the `poetry` library to create the environment and the package structure
2. Use of the `docker` to create the container with the solution environment, maintaining the integrity of the built structure
3. Deployment of the solution, with an interface built from the `streamlit` framework, on the `Heroku` cloud platform, ensuring the high availability of the solution
[<img alt="Heroku App" src="[https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Heroku_logo.svg/2560px-Heroku_logo.svg.png](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSn9bQiBVei5RUWI-ZHMwe7lZhTg_Pl0cHZRjIaVSlpw7lTlORgTbMs7ZXinBpV9_sSa_k&usqp=CAU)"/>](https://price-sale-prediction.herokuapp.com/)

## 4.0 Solution Architecture
![image](https://github.com/neusmarjr/precification_prediction/blob/master/images/architecture.png)

## 5.0 Important Informations
It is important to mention that we are dealing with a statistical model, where there are always associated errors. The objective proposed here would be the delivery of an MVP that can be used by the business area, which can be improved in subsequent development cycles;

## 6.0 Next Steps
It can be listed the next steps to be taken, in the next solution maintenance cycles, seeking to improve the prediction results.
1. Explore methods of cleaning, adequacy and normalization of data distribution
2. Work with APIs, searching for latitude and longitude information of properties from the address input
3. Explore different machine learning models and hyperparameter optimization methods
