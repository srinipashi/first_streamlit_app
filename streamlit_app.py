import streamlit 
import pandas 

streamlit.title('My parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach, & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
# Below is to show all the fruits and show default 2 ['Avocado','Strawberries']
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),default=['Avocado','Strawberries'])
# Display the table on the page.
#streamlit.dataframe(my_fruit_list)

#Below is to show default and selected fruits into a variable fruits_selected and show only those which are in the selected list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),default=['Avocado','Strawberries'])
fruits_toshow = my_fruit_list.loc[fruits_selected]
#Display the table on the app with select fruits only
streamlit.dataframe(fruits_toshow)

## New Section to display Fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
## Added to get User inputs on fruits choice
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered: ',fruit_choice)

import requests
##fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon") ## This is default watermelon

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) ## This is to list the user choice Fruit Details

## streamlit.text(fruityvice_response.json())   # just writes the data to the screen        ## removed to not to display raw Json                

# use the pandas package to load the jason into Dataframes 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Display the Dataframes
streamlit.dataframe(fruityvice_normalized)

#import snowflake.connector
