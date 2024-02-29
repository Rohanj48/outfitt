from flask import Flask,render_template,request,jsonify,redirect
from flask_sqlalchemy import SQLAlchemy
import os
import random
#from rembg import remove 
#from PIL import Image
# setup
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

picfolder = os.path.join('static','tops')
app.config['UPLOAD_FOLDER'] = picfolder

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(200), nullable=False)
    data = db.Column(db.LargeBinary)






#pages
@app.route('/',methods=['POST', 'GET'])
def index():
    return redirect("/showpage")
    return render_template("index.html") 



@app.route('/addpage',methods=['POST', 'GET'])
def addpage():
    if request.method == 'POST':
        
        if request.form.get("action") =="bottomb":
            lst = os.listdir("static/bottoms") # your directory path
            n_files= len(lst)
            files = request.files["bottomImageFile"]
            file_extension =  os.path.splitext(files.filename)[1]
            #upload = Upload(fname = files.filename,data = files.read())
            
            
            files.save(os.path.join("static/bottoms",f"bottom{n_files}{file_extension}")) ##NORMALSAVE

            
            #print(os.path.join("/static/tops", files.filename))
            #return files.filename

            """FANCYSAVE"""
            #imgbg = Image.open(files)
            #img_no_bg = remove(imgbg)
            #img_no_bg.save(os.path.join("static/bottoms",f"bottom{n_files}.png"))
            ##

        if request.form.get("action") =="topb":
            lst = os.listdir("static/tops") # your directory path
            n_files= len(lst)
            files = request.files["topImageFile"]
            file_extension =  os.path.splitext(files.filename)[1]
            #upload = Upload(fname = files.filename,data = files.read())
            files.save(os.path.join("static/tops",f"top{n_files}{file_extension}")) ##NORMALSAVE
            #print(os.path.join("/static/tops", files.filename))
            #return files.filename

            """FANCYSAVE"""
            #imgbg = Image.open(files)
            #img_no_bg = remove(imgbg)
            #img_no_bg.save(os.path.join("static/tops",f"bottom{n_files}.png"))
            #

    return render_template("addpage2.html")


@app.route('/showpage',methods=['POST', 'GET'])
def showpage():
    lst = os.listdir("static/bottoms") 
    botn= len(lst)
    botlist = []
    for i in lst:
        botlist.append(botlist.append(os.path.join("/static/bottoms",i)))

    botlist = [i for i in botlist if i != None]

    #print(botlist)

    lst = os.listdir("static/tops") 
    topn= len(lst)
    toplist = []
    for i in lst:
        toplist.append(os.path.join("/static/tops",i))
    
    toplist = [i for i in toplist if i != None]
    #print(toplist)


    context ={
        "botlist":botlist,
        "toplist":toplist
    }
    return render_template("showpage2.html",**context)




@app.route('/randpage',methods=['POST', 'GET'])
def randpage():
    # geting bottoms into bottoms
    lst = os.listdir("static/bottoms") 
    botn= len(lst)
    botlist = []
    for i in lst:
        botlist.append(botlist.append(os.path.join("/static/bottoms",i)))

    bottoms = [i for i in botlist if i != None]

    #GETTING TOPS IINTO TOPS

    lst = os.listdir("static/tops") 
    topn= len(lst)
    toplist = []
    for i in lst:
        toplist.append(os.path.join("/static/tops",i))
    
    tops = [i for i in toplist if i != None]


    # randomizing

    top_image = random.choice(tops)
    bottom_image = random.choice(bottoms)
    
    context = {
        "top_image":top_image,
        "bottom_image":bottom_image
    }



    return render_template("randpage.html",**context)




@app.route('/randomize',methods=['POST'])
def rangett():

    # geting bottoms into bottoms
    lst = os.listdir("static/bottoms") 
    botn= len(lst)
    botlist = []
    for i in lst:
        botlist.append(botlist.append(os.path.join("/static/bottoms",i)))

    bottoms = [i for i in botlist if i != None]

    #GETTING TOPS IINTO TOPS

    lst = os.listdir("static/tops") 
    topn= len(lst)
    toplist = []
    for i in lst:
        toplist.append(os.path.join("/static/tops",i))
    
    tops = [i for i in toplist if i != None]


    # randomizing

    top_image = random.choice(tops)
    bottom_image = random.choice(bottoms)
    return jsonify({"top_image": top_image, "bottom_image": bottom_image})



if __name__ == "__main__":
    app.run(debug=True)
