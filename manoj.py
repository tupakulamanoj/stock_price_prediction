from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from sqlalchemy.sql import text
import time
import pandas as pd
import threading
import manoj2
from IPython.display import HTML
import hello



db=SQLAlchemy()
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manoj.db'
db.__init__(app)
 
 
class database(db.Model):
    username=db.Column(db.String)
    password=db.Column(db.String)
    column_not_exist_in_db = db.Column(db.Integer, primary_key=True)
    
with app.app_context():
    db.create_all()
    query2='select username from database'
    c=db.session.execute(text(query2))
    query3='select password from database'
    d=db.session.execute(text(query3))

user_names=[]
for i in c:
    user_names.append(i[0])
passwords=[]
for i in d:
    passwords.append(i[0])





c=["Microsoft Corp - MSFT","APPLE - AAPL","GOOGLE - GOOGL","AMAZON - AMZN","TESLA - TSLA"]
d=['STOCK','DATE','OPEN','HIGH','LOW','CLOSE','VOLUME','FUTURE-PREDICTION']

          

    






@app.route('/',methods=['GET','POST'])
def manoj():
    if request.method=='POST':
        username=request.form['user']
        password=request.form['password']
        if str(username) not in user_names:
            query=database(username=username,password=password)
            db.session.add(query)
            db.session.commit()
            user_names.append(str(username))
            passwords.append(str(password))
        else:
            f=user_names.index(username)
            l=passwords[f]
            print(f)
            print(str(password) == l)
            if str(password) == l:
                print(c)
                data5=pd.read_csv('data.csv')
                data6=pd.read_csv('data1.csv')
                data7=pd.read_csv('data2.csv')
                data8=pd.read_csv('data3.csv')
                data9=pd.read_csv('data4.csv')
                lis=[]
                for j in range(6):
                    b=[]
                    b.append(data5.iloc[0][j])
                    b.append(data6.iloc[0][j])
                    b.append(data7.iloc[0][j])
                    b.append(data8.iloc[0][j])
                    b.append(data9.iloc[0][j])
                    lis.append(b)
               
               
               
                return render_template('base2.html',lis=lis,c=c,d=d)
            else:
                return render_template('base.html')

        return render_template('index2.html',username=username,password=password)
        
        
            
    return render_template('index.html')



@app.route('/microsoft',methods=['GET','POST'])
def micro():
        microsoft_price=manoj2.price('data.csv')
        dataframe1=microsoft_price.to_html()
        text_file = open("./templates/base4.html", "w")
        text_file.write(dataframe1)
        text_file.close()

        return render_template('base4.html',microsoft_price=microsoft_price)

    
@app.route('/apple',methods=['GET','POST'])
def apple():
        apple_price=manoj2.price('data1.csv')
        dataframe2=apple_price.to_html()
        text_file = open("./templates/base5.html", "w")
        text_file.write(dataframe2)
        text_file.close()

        return render_template('base5.html',apple_price=apple_price)
    
@app.route('/google',methods=['GET','POST'])
def google():
        google_price=manoj2.price('data2.csv')
        dataframe3=google_price.to_html()
        text_file = open("./templates/base6.html", "w")
        text_file.write(dataframe3)
        text_file.close()

        return render_template('base6.html',google_price=google_price)
    
@app.route('/amazon',methods=['GET','POST'])
def amazon():
        amazon_price=manoj2.price('data3.csv')
        dataframe4=amazon_price.to_html()
        text_file = open("./templates/base7.html", "w")
        text_file.write(dataframe4)
        text_file.close()

        return render_template('base7.html',amazon_price=amazon_price)
    
@app.route('/tesla',methods=['GET','POST'])
def tesla():
        tesla_price=manoj2.price('data4.csv')
        dataframe5=tesla_price.to_html()
        text_file = open("./templates/base8.html", "w")
        text_file.write(dataframe5)
        text_file.close()

        return render_template('base8.html',tesla_price=tesla_price)
    
    
    
    
    
if __name__=='__main__':
    t=threading.Thread(target=hello.pasg)
    t1=threading.Thread(target=app.run) 
    t.start()
    
    t1.start()   