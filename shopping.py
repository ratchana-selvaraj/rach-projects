from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import MySQLdb
app=Flask(__name__)
dl=[]
@app.route("/")
def form():
    db=MySQLdb.connect("localhost","root","Goodluck","productdetails")
    cur1=db.cursor()
    cur2=db.cursor()
    query1="select product_name from inventory"
    query2="select market_price from inventory"
    cur1.execute(query1)
    cur2.execute(query2)
    m=cur1.fetchall()
    n=cur2.fetchall()
        #dl=m
        #print(dl)
    cur1.close()
    cur2.close()
    return render_template("shopB.html",m=m,n=n)
@app.route("/result",methods=["POST","GET"])
def result():
    if request.method == 'POST':
        search=request.form["product_name"]
        db=MySQLdb.connect("localhost","root","Goodluck","productdetails")
        cur=db.cursor()
        query="select * from inventory where product_name="+search
        cur.execute(query)
        m=cur.fetchall()
        cur.close()
        return render_template("index.html" ,m=m)

        #return render_template("result.html" ,name=search)
#@app.route("/addtocart",methods=["POST","GET"]
#def addtocart():
    
    
    
    
    
if __name__=="__main__":
    app.run(debug=True)
