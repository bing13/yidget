#!/home/bhadmin13/f.bernardhecker.com/bin/python

#### TO DO:
## 1 errors when phrase has a quotation mark in it.
## 2 "hello.py"??
## 3 need a non-brain viewer

#from flask import Flask
import random, simplejson, flask;

yidget_file = 'yidget/y_input.txt'

flaskRoute = flask.Flask(__name__);
###############################################
@flaskRoute.route("/hi")
def hello():
    return "Hello World!"

@flaskRoute.route("/bye")
def bye():
    return "See ya later, alligator!"

###################################################

@flaskRoute.route("/yidget")
def yiddish_phrase_server():
    yiddish, english = fetch_random_phrase();
    resultx = '{ "yid":"'+yiddish+'", "eng":"'+english+'" }' ;
    #resultx = flask.jsonify(yid="Peter", eng="Paul");
    #resultx = flask.jsonify(yid=yiddish, eng=english.strip()); # , spath = sys.path)
    result_jsonp =  "yidParse("+resultx+");";
    responsex = flask.Response(response=result_jsonp, status=200, mimetype="application/json"); 
    return responsex;
 
#@flaskRoute.route("/yiddish")
#def build_html_page():
#    yiddish, english = fetch_random_phrase();
#    return render_template('yidget.html'); #, yid=yiddish, eng=english);

def fetch_random_phrase():
    YINF = open(yidget_file, 'r')
    yl = YINF.readlines()
    n = int(round(random.random()*len(yl)))
    yiddish, english = yl[n].split('\t')
    return(yiddish, english[:-1])

app.debug=True;
if __name__ == "__main__":
    app.run(host='0.0.0.0')
