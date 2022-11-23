from src.http import getActivitiesResponse, postUserSessions
from src.app import sortActivitiesByDateAndUserId, createListOfUserSessions

def main():
    '''Complete algorithm for the slang challenge.
        Complexity time for this algorithm is O(n*log n) with n total activities,
        because we sorted the list, and that was the "slowest" procedure in all the code.'''

    activity_list = getActivitiesResponse()
    user_dict = sortActivitiesByDateAndUserId(activity_list)
    user_sessions = createListOfUserSessions(user_dict)

    postUserSessions({"user_sessions": user_sessions})

if __name__ == "__main__":
    main()