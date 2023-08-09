from tinydb import TinyDB, Query
import rx
from rx import operators as ops


class DatabaseRepository:
    
    def __init__(self):
        self.db = TinyDB("complaintsDB.json")
        self.query = Query()

        rx.of(self.db).pipe(
            ops.map(lambda i:i)
        ).subscribe(
            lambda x: self.notify(x.all()))
        
        
    def notify(self,x):
        print(x)
            
    def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(DatabaseRepository, cls).__new__(cls)
            return cls.instance
    
    def create(self,complaint):
        try:
            self.db.insert(complaint)
            return True
        except:
            return False
    
    def read(self,searchCriterion):
        try:
            if(len(self.db.all()) > 0):
                response = self.db.search(searchCriterion)
                return {"response":response}
            else:
                return {"response":[]}
        except:
            return {"response":[]}
            
        
    def update(self,fieldToBeUpdated,entitiesToBeUpdated):
        try:
            self.db.update(fieldToBeUpdated, entitiesToBeUpdated)
            return True
        except:
            return False
        
    def delete(self,entityToBeDeleted):
        try:
            self.db.remove(entityToBeDeleted)
            return True
        except:
            return False
        
    def readAll(self):
        try:
            response = self.db.all()
            return {"response":response}
        except:
            return {"response":[]}
        
    def complaintViewedBy(self,complaintId,recipientId):
        try:
            result = self.read(
                self.query.complaintId == complaintId
                )
            viewsList = result["response"][0]["viewedBy"]
            if recipientId in viewsList:
                return True
            viewsList.append(recipientId)
            updatedField = {"viewedBy":viewsList}
            updatedEntry = self.query.complaintId == complaintId        
            self.update(updatedField,updatedEntry)
            return True
        except:
            return False
        
    def complaintAddressedBy(self,complaintId,recipientId):
        try:
            result = self.read(
                self.query.complaintId == complaintId
                )
            addressList = result["response"][0]["addressedBy"]
            if recipientId == addressList:
                return True
            addressList = recipientId
            updatedField = {"addressedBy":addressList}
            updatedEntry = self.query.complaintId == complaintId        
            self.update(updatedField,updatedEntry)
            return True
        except:
            return False
        
    def viewCount(self,complaintId):
        return len(self.read(self.query.complaintId == complaintId)["response"][0]["viewedBy"])
        