import re
import hashlib
from datetime import datetime
def valid_email(email):
    return re.match(r"[\w\.-]+@[\w\.-]+\.\w+$",email)
def valid_mobile(phone):
    return re.match(r"^(010|011|012|015)\d{8}$",phone)
def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest() # encode --> bytes  (hashlib donnot accept strings )--> hexdecimal 
def validate_date(date):
        try:
            datetime.strptime(date,"%Y-%m-%d")
            return True
        except  ValueError :
            return False 