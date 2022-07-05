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
#streamlit.dataframe(fruits_toshow)





