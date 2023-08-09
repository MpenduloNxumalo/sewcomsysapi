from flask import request
from apiUtils.DatabaseRepository import DatabaseRepository

class Recipient:
    
    def getAllComplaints():
        return DatabaseRepository().readAll()
    
    def viewComplaint():
        data = request.json
        return {"isSuccessful":DatabaseRepository().complaintViewedBy(data["complaintId"],data["recipientId"])}
    
    
    def addressComplaint():
        data = request.json
        return {"isSuccessful":DatabaseRepository().complaintAddressedBy(data["complaintId"],data["recipientId"])}
    