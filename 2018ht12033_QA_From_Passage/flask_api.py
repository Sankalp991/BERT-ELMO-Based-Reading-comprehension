from flask import Flask, render_template, request, send_file
import warnings
warnings.filterwarnings("ignore")
from bert import QA

DEBUG = False
app = Flask(__name__)
app.config.from_object(__name__)


model = QA("model")

@app.route('/')
def single_people_code():
    print('here')
    # return render_template('index.html')
    return render_template('index.html')

@app.route("/",methods=['POST','GET'])
def predict():
    if request.method == 'POST':

        form = request.form
        results = request.form
        print(results)
        doc = results['passage']
        print(doc)
        q = results['question']
        print(q)
        try:


            out = model.predict(doc,q)
            res = str(out['answer'])

            # flash(res)
            print(out)
            # return ('Answer : ' + str(out))
        except Exception as e:
            res = e
            print(e)
            # return ("Answer"+" : "+"Model Failed")
    # return redirect(url_for('single_people_code'))
    return render_template('index.html',messages=res,passage=doc,question=q)

if __name__ == "__main__":
    app.run('127.0.0.1',port=8000)


from bert import QA

model = QA('model')
#
# doc = "Our narrator, Nick Carraway, moves to the East Coast to work as a bond trader in Manhattan. He rents a small house in West Egg, a nouveau riche town in Long Island." \
#       "In East Egg, the next town over, where old money people live, Nick reconnects with his cousin Daisy Buchanan, her husband Tom, and meets their friend Jordan Baker." \
#       "Tom takes Nick to meet his mistress, Myrtle Wilson. Myrtle is married to George Wilson, who runs a gas station in a gross and dirty neighborhood in Queens. Tom, Nick, and Myrtle go to Manhattan, where she hosts a small party that ends with Tom punching her in the face." \
#       "Nick meets his next-door neighbor, Jay Gatsby, a very rich man who lives in a giant mansion and throws wildly extravagant parties every weekend, and who is a mysterious person no one knows much about." \
#       "Gatsby takes Nick to lunch and introduces him to his business partner - a gangster named Meyer Wolfshiem." \
#       "Nick starts a relationship with Jordan. Through her, Nick finds out that Gatsby and Daisy were in love five years ago, and that Gatsby would like to see her again." \
#       "Nick arranges for Daisy to come over to his house so that Gatsby can “accidentally” drop by. Daisy and Gatsby start having an affair." \
#       "Tom and Daisy come to one of Gatsby’s parties. Daisy is disgusted by the ostentatiously vulgar display of wealth, and Tom immediately sees that Gatsby’s money most likely comes from crime." \
#       "We learn that Gatsby was born into a poor farming family as James Gatz. He has always been extremely ambitious, creating the Jay Gatsby persona as a way of transforming himself into a successful self-made man - the ideal of the American Dream."
#
# q = 'Who is the narrator??'
#
doc = "Victoria has a written constitution enacted in 1975, but based on the 1855 colonial constitution, passed by the United Kingdom Parliament as the Victoria Constitution Act 1855, which establishes the Parliament as the state's law-making body for matters coming under state responsibility. The Victorian Constitution can be amended by the Parliament of Victoria, except for certain 'entrenched' provisions that require either an absolute majority in both houses, a three-fifths majority in both houses, or the approval of the Victorian people in a referendum, depending on the provision."

doc = """Amitabh Bachchan was born on 11 October 1942. He is an Indian film actor, film producer, television host, occasional playback singer and former politician. He first gained popularity in the early 1970s for films such as Zanjeer, Deewaar and Sholay, and was dubbed Indias "angry young man" for his on-screen roles in Bollywood. Referred to as the Shahenshah of Bollywood, Sadi ka Mahanayak, Star of the Millennium, or Big B, he has since appeared in over 190 Indian films in a career spanning almost five decades. Bachchan is widely regarded as one of the greatest and most influential actors in the history of Indian cinema as well as world cinema. So total was his dominance on the Indian movie scene in the 1970s and 1980s that the French director François Truffaut called him a "one-man industry". Beyond the Indian subcontinent, he also has a large overseas following in markets including Africa, the Middle East, United Kingdom, Russia and parts of the United States."""
q = 'Who is Amitabh Bachchan?'

answer = model.predict(doc,q)

print(answer['answer'])
# # # 1975
# # # print(answer.keys())
# # # dict_keys(['answer', 'start', 'end', 'confidence', 'document']))