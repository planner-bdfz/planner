import webbrowser;
import os;
def gets(ev=None):
    path=os.path.dirname(__file__);
    webbrowser.open("file://"+path+"/agegets/gets.html");