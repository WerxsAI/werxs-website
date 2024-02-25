import datetime

class UploadModel:
    def __init__(self, db):
        self.collection = db.uploads

    def create_upload_record(self, userid, s3_key):
        record = {
            "userid": userid,
            "s3_key": s3_key,
            "upload_date": datetime.utcnow(),
        }
        return self.collection.insert_one(record).inserted_id
