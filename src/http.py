import requests
from tests.test_case import EXAMPLE
from src.token import TOKEN

def getResponseFake():
   '''Function that help us test code functionality without doing any http requests,
      it uses the test case above.'''
   
   return EXAMPLE

def getActivitiesResponse():
   '''Retrieve all activities from the slang page.'''

   activities_response = requests.get(
      "https://api.slangapp.com/challenges/v1/activities",
      headers={"Authorization": TOKEN}
      )
   
   return activities_response.json()

def postUserSessions(user_sessions):
   '''Post the resulting user_sessions to slang web page.'''

   print(user_sessions)

   user_session_response = requests.post(
      "https://api.slangapp.com/challenges/v1/activities/sessions",
      headers={"Authorization": TOKEN},
      json=user_sessions
      )

   print(f"The status code posting the user_sessions was: {user_session_response.status_code}")
   print("Done! :)")

def postUserSessionsFake(user_sessions):
   '''Function that prints the result of all the code.'''

   print(user_sessions)
   print("Done! :)")

