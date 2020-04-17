#Name : Sankalp Tomar
#ID : 2018ht12033

# Requirements
- python3
- pip3 install -r requirements.txt
- Download trained model from - https://www.dropbox.com/s/j6jnf060aovimdy/model.zip?dl=0
and keep it in model folder

# Deploy Flask-API
BERT QA model deployed as rest api

```bash
python flask_api.py
```
API will be live at `127.0.0.1:8000` endpoint `predict`

### API Input 
```
Passage : Amitabh Bachchan was born on 11 October 1942. He is an Indian film actor, film producer, television host, occasional playback singer and former politician. He first gained popularity in the early 1970s for films such as Zanjeer, Deewaar and Sholay, and was dubbed Indias "angry young man" for his on-screen roles in Bollywood. Referred to as the Shahenshah of Bollywood, Sadi ka Mahanayak, Star of the Millennium, or Big B, he has since appeared in over 190 Indian films in a career spanning almost five decades. Bachchan is widely regarded as one of the greatest and most influential actors in the history of Indian cinema as well as world cinema. So total was his dominance on the Indian movie scene in the 1970s and 1980s that the French director François Truffaut called him a "one-man industry". Beyond the Indian subcontinent, he also has a large overseas following in markets including Africa, the Middle East, United Kingdom, Russia and parts of the United States.

Question : Who is Amitabh Bachchan?
```
#### Output
```
Answer : film actor, film producer, television host, occasional playback singer and former politician
```
