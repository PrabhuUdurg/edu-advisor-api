import firebase_admin
from firebase_admin import credentials

try:
    firebase_admin.get_app()  # Attempt to get the default app
except ValueError:
    cred = credentials.Certificate('/home/prabhu/Downloads/edu-advisor-5c99b-firebase-adminsdk-o94pn-bd861b8db5.json')
    firebase_admin.initialize_app(cred)