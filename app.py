
import streamlit as st
from PIL import Image

# Set page to wide and lable tab
st.set_page_config(layout="wide",page_title="My Tab Title")

# Page title and subheader
st.title('Streamlit Test Page')
st.subheader('Here, a subheader')

# Example text
st.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum.')
st.write('This is can be used for text and other features.')

# Insert a picture
image = Image.open(r"C:\Users\stuar\PycharmProjects\Streamlit Test\assets\images\streamlit-logo-primary-colormark-darktext.png")
st.image(image)

# Radio Buttons
st.radio('Choose your option', options=('Option 1', 'Option 2', 'Option 3'))
# Slider
st.slider('<-- Slide to the sides -->', min_value=0, max_value=10, value=5, step=1)
# Multiselect
st.text('Checkbox')
st.multiselect('What are your favorite colors',
            ['Green', 'Yellow', 'Red', 'Blue'],
            ['Blue', 'Green'])
# Selectbox
st.selectbox('Select Box',options=('Option 1', 'Option 2', 'Option 3'))
# text input
title = st.text_input('My App Text Input', 'Write Something...')
st.write('You wrote:  ', title)

# Adding a text in the sidebar
#st.sidebar.text('Your Text Here')# Add a radio button
#st.sidebar.radio('label', options=[])The other gadgets follow the same syntax.