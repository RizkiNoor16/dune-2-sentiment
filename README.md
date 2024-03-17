# dune-2-sentiment

This is sentiment analytic model from Dune Part Two movies based on [Letterbox Website](https://letterboxd.com/film/dune-part-two/)

**Download Model** : [Google Drive](https://drive.google.com/drive/folders/1OzKE_Cuu0rgwGrMuQMh-d1GeMHT21lA7?usp=sharing)

## Running [Streamlit](https://streamlit.io/) demo locally

```bash
git clone https://github.com/RizkiNoor16/dune-2-sentimen.git
pip install -r requirements.txt
streamlit run app.py
```
![Screenshot from 2024-03-17 13-02-09](https://github.com/RizkiNoor16/dune-2-sentiment/assets/99520100/3aab0ae3-76f1-4fc2-97ea-b37aea2396a7)


## Results
```
'epoch ' : 50.0
#Training data
'training_loss' : 0.29483315798315674

#Validaion data
'eval_loss': 3.877136468887329,
'eval_accuracy': 0.4370737755734656,
'eval_f1': 0.43468557129075325
```

## Follow up Question
1. How did you vectorize the reviews? /justify your choice of algorithm?
   
   Answer :
   
   The reviews are vectorized using a pre-trained transformer-based model for text classification. This is because the community providing movie reviews on Letterboxd website is highly 
   creative, and it requires a model that can understand the context of these text reviews effectively.
   The BERT model is a powerful transformer-based architecture known for its effectiveness in capturing contextual information in text data. This choice is justified as BERT models have     shown state-of-the-art performance in various NLP tasks, including sentiment analysis.
3. How would you calculate the accuracy of your sentiment predictor?
   
   Answer :
   
   To determine the accuracy of the sentiment predictor, we compare the predicted labels generated by the model with the actual labels from the validation dataset. The accuracy   
   evaluation result is: 0.437073775573465
4. How would you calculate the speed of inference ?
   
   Answer :
   
   The inference speed can be calculated by measuring the time taken by the model to process each input sample. In the demonstration, the observed inference speed is approximately ~0.06     seconds.
5. What would be your next steps to improve the solution ?
   
   Answer :
   - Fine-tuning the pre-trained BERT model on a larger dataset to further improve its performance on sentiment analysis for movie reviews.
   - Performing hyperparameter tuning to optimize the performance of the model.
   - Implementing techniques for handling class imbalance in the dataset.
     
## Contact
Noor Muhamad Rizki 

Email : deede.rizki@gmail.com

Linkedin : [Noor Muhamad Rizki](https://www.linkedin.com/in/noor-muhamad-rizki-114600231/)


##
