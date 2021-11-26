import streamlit as st #for web dev
from aitextgen import aitextgen #for ai text gen
from keytotext import pipeline
from streamlit_tags import st_tags, st_tags_sidebar

st.title("Text Generation")

# instantiate the model / download


# create a prompt text for the text generation
#prompt_text = "Python is awesome"
form = st.form(key='my_form')
prompt_text = form.text_input( "Enter your text...")
            #value = "Computer is beautiful"
submit_button = form.form_submit_button('Generate')


#st.write("# Code for streamlit tags")
# st.code(body='''keywords = st_tags(
#     label='# Enter Keywords:',
#     text='Press enter to add more',
#     value=['Zero', 'One', 'Two'],
#     suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
#     maxtags = 4,
#     key='1')''',
#         language="python")
maxtags = st.slider('Number of tags allowed?', 1, 10, 3, key='jfnkerrnfvikwqejn')

keywords = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    #value=['Zero', 'One', 'Two'],
    suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
    maxtags=maxtags,
    key="aljnf")

#st.write("### Results:")
#st.write(type(keywords))


with st.spinner("text is generating........"):
    # text generation
    ai = aitextgen(model="EleutherAI/gpt-neo-125M"
         )

    gpt_text = ai.generate_one(prompt=prompt_text,
            max_length = 1000, temperature=1.2,no_repeat_ngram_size=3)
    nlp = pipeline("mrm8488/t5-base-finetuned-common_gen")

# form.text_input(label='Enter some text')
#st.success("Successfully generated the below text ")
#st.balloons()
# print ai generated text
print(gpt_text)
st.text(gpt_text)
