from flask import Flask, render_template, request  
  
app = Flask(__name__)  
 
@app.route("/")  
def index():  
     return render_template('index.html')

@app.route('/hello', methods=['POST'])  
def hello():  
    Weight = float(request.form.get('weight'))  
    Height = float(request.form.get('height'))  
    data=round(Weight/((Height/100)**2),2)
    return render_template('hello.html',value=data)

    
if __name__ == '__main__':  
    #app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)  
    app.run('localhost', 4459)  