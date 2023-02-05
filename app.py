from flask import Flask

application = Flask(__name__)

@application.route('/',methods=['GET','POST'])
def welcome():
    return ' ',200

@application.route('/poc',methods=['GET','POST'])
def poc():
    return 'takeover poc by bibekshah',200

if __name__ == "__main__":
    application.run()
