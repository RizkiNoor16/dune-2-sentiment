import streamlit as st
import time
from transformers import pipeline

st.title("Dune: Part Two Movie Reviews")

st.subheader("Welcome to the sentiment analysis tool for Dune: Part Two reviews")  

st.image("images/1686160178334.png", caption="Dune: Part Two Poster")

# Use st.form to handle user input
with st.form("my-form"):
    st.markdown("**Enter Your Review about Dune: Part Two**")
    # Create a column layout
    cols = st.columns([6, 1])

    # Text input for user review
    human_message = cols[0].text_input(
        "review",
        label_visibility="collapsed",
        placeholder="Dune will go down as the greatest movie series ever made.",
        key="human_message"
    )
    
    # Form submit button
    submitted = cols[1].form_submit_button("Submit", type="primary")

# Process text 
if submitted:
    start_time = time.time()
    with st.spinner("Processing..."):
        classifier = pipeline('text-classification', model='model/dune_rate_models')
        result = classifier(human_message)
    
    st.success("Analysis Complete!")
    end_time = time.time() - start_time
    
    if result[0]['label'] == 'LABEL_0':
        st.markdown("Predicted Rating Sentiment: :star:") 
    elif result[0]['label'] == 'LABEL_1':
        st.markdown("Predicted Rating Sentiment: :star: :star:") 
    elif result[0]['label'] == 'LABEL_2':
        st.markdown("Predicted Rating Sentiment: :star: :star: :star:") 
    elif result[0]['label'] == 'LABEL_3':
        st.markdown("Predicted Rating Sentiment: :star: :star: :star: :star:") 
    elif result[0]['label'] == 'LABEL_4':
        st.markdown("Predicted Rating Sentiment: :star: :star: :star: :star: :star:") 
    st.write("Confidence Score:", result[0]['score'])
    st.caption(f"Inference Time: {end_time:.4f} seconds")

