#!/home/bhadmin13/f.bernardhecker.com/bin/python

#### TO DO:
## 1 errors when phrase has a quotation mark in it.
## 2 "hello.py"??
## 3 need a non-brain viewer

#from flask import Flask
import sys,random, simplejson, flask;

posters = [
    "99.jpg",
    "DudisFiddle.jpg",
    "Klezmerola-Yiddish-theater.jpg",
    "ShulamithSheetMusic248.jpg",
    "StreamGate1.jpg",
    "abe_goldfaden_fr_of_Ytheatre.jpg",
    "aletterforsweetheart.jpg",
    "bhs_1988015111_yiddsheetmus3_t.jpg",
    "daily-heller-121511-YiddishPoster1.jpg",
    "expand_jewish2.jpg",
    "expand_jewish4.jpg",
    "hebrewfrontpg2.jpg",
    "index-10.jpg",
    "index-12.jpg",
    "index-4.jpg",
    "index-5.jpg",
    "index-7.jpg",
    "index-9.jpg",
    "jacobadlerposter.jpg",
    "pretzels-female-impersonator1927.jpg",
    "sm0057r.jpg"]


yidget_file = 'yidget/y_input.txt'

flaskRoute = flask.Flask(__name__);
#, template_folder="/home/bhadmin13/f.bernardhecker.com/yidget/templates/");
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
    #resultx = flask.jsonify(yid=yiddish, eng=english.strip()); # , spath = sys.path)
    result_jsonp =  "yidParse("+resultx+");";
    responsex = flask.Response(response=result_jsonp, status=200, mimetype="application/json"); 
    return responsex;
 
@flaskRoute.route("/yiddish") 
def build_html_page():
    yiddish, english = fetch_random_phrase();
    n = int(round(random.random()*len(posters)))
    return flask.render_template('y_display.html', yid=yiddish, eng=english, poster=posters[n]);

def fetch_random_phrase():
    YINF = open(yidget_file, 'r')
    yl = YINF.readlines()
    n = int(round(random.random()*len(yl)))
    yiddish, english = yl[n].split('\t')
    yiddish.replace('"','&quot;');
    english.replace('"','&quot;');	
    return(yiddish, english[:-1])

# uncommentingn seems to cause error (!)
#app.debug=True;



if __name__ == "__main__":
    app.run(host='0.0.0.0')
