# Azure credentials
SPEECH_KEY = '7ULJLA5QawY3EPqG9FjdXO8B87lWRLYPSjVMPnLrnZ70V8f2aHucJQQJ99BCACqBBLyXJ3w3AAAYACOGD8jG'
SPEECH_REGION = 'Southeast Asia'
TEXT_ANALYTICS_KEY = '4AcIdqhyMOg7ylwxJ2tu4uyRmysJWTkGtiH5s2bohKdEuJIuXRmuJQQJ99BCACqBBLyXJ3w3AAAaACOGhHiu'
TEXT_ANALYTICS_ENDPOINT = 'https://nursetextanalytics.cognitiveservices.azure.com/'

class Config_db:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///hospital.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
