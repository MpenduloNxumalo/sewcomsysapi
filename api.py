from flask import Flask
from apiUtils.Reporter import Reporter
from apiUtils.Recipient import Recipient

app = Flask(__name__)

@app.route('/create_complaint', methods=['POST'])
def createComplaint():
    return Reporter.createComplaint()


@app.route('/read_complaint', methods=['GET'])
def readComplaint():
    return Reporter.readComplaint()
    

@app.route('/update_complaint', methods=['POST'])
def updateComplaint():
    return Reporter.updateComplaint()

@app.route('/delete_complaint', methods=['POST'])
def deleteComplaint():
    return Reporter.deleteComplaint()

@app.route('/get_all_complaints', methods=['GET'])
def getAllComplaints():
    return Recipient.getAllComplaints()

@app.route('/view_complaint', methods=['POST'])
def viewComplaint():
    return Recipient.viewComplaint()

@app.route('/views_count', methods=['POST'])
def viewsCount():
    return Reporter.viewCount()

@app.route('/address_complaint', methods=['POST'])
def addressComplaint():
    return Recipient.addressComplaint()

if __name__ == '__main__':
    app.run(debug=True)
    