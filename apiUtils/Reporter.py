from flask import request
from apiUtils.DatabaseRepository import DatabaseRepository

class Reporter:
    
    def createComplaint():
        complaint = request.json
        response = DatabaseRepository().create(complaint)
        return {"isSuccessful":response}
    
    def readComplaint():
        data = request.json
        return DatabaseRepository().read(
            DatabaseRepository().query.reporterId == data["reporterId"]
            )
    
    def updateComplaint():
        data = request.json
        updateField = {str(data["update"]["attribute"]):data["update"]["value"]}
        updatedEntity = DatabaseRepository().query.reporterId == data["reporterId"]
        response = DatabaseRepository().update(
            updateField,
            updatedEntity
            )
        return {"isSuccessful":response}
    
    def deleteComplaint():
        data = request.json
        response = DatabaseRepository().delete(
            DatabaseRepository().query.reporterId == data["reporterId"]
            )
        return {"isSuccessful":response}
    
    def viewCount():
        data = request.json
        return {"viewsCount":DatabaseRepository().viewCount(data["complaintId"])}
        