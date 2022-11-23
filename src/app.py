from datetime import datetime, timedelta


def parseDatetimeString(date):
    '''Parses datetime string in ISO 8601 to datetime objects.'''

    format_string = "%Y-%m-%dT%H:%M:%S.%f%z"
    date_object = datetime.strptime(date, format_string)

    return date_object


def compareDates(activity):
    '''Auxiliar function used to sort the activities by date.'''

    date = activity.get('first_seen_at')
    date_object = parseDatetimeString(date)

    return date_object


def sortResponseByFirstSeen(activities):
    '''Sorts the entire activity list (asc).
        Complexity time for this algorithm is O(n*log (n)) with n activities,
        because that is the best sorting complexity.'''

    activities.sort(key=compareDates)

    return activities


def groupActivitiesByUserId(activities):
    '''Groups the activities with their respective user_id.
        Complexity time for this algorithm is O(n) with n activities, because we iterate the list once.'''

    sorted_activities_by_user_id = {}

    for x in activities:

        user_id = x.get("user_id")

        if not sorted_activities_by_user_id.get(user_id):
            sorted_activities_by_user_id[user_id] = [x]
        
        else:
            sorted_activities_by_user_id.get(user_id).append(x)

    return sorted_activities_by_user_id


def getUserSessions(sessions):
    '''Creates the necessary user sessions for a user_id and his activities.
        Complexity time for this algorithm is O(k) with k activities from a specific user_id,
        because we only iterate the list once.'''

    response = []
    
    i = 0
    n = len(sessions)

    while i < n:
        started_at = sessions[i].get('first_seen_at')
        first_activity_id = sessions[i].get('id')

        user_session = {
            "started_at": started_at,
            "activity_ids": [first_activity_id],
        }

        limit = sessions[i].get('answered_at')
        j = i+1
        while j < n:
            next_date = parseDatetimeString(sessions[j].get('first_seen_at'))

            if next_date <= (parseDatetimeString(limit) + timedelta(minutes=5)):
                
                user_session.get("activity_ids").append(sessions[j].get("id"))
                limit = sessions[j].get('answered_at')

                j += 1
            else:
                break

        i = j
        user_session["ended_at"] = limit
        duration_time = parseDatetimeString(limit) - parseDatetimeString(started_at) 
        user_session["duration_seconds"] = duration_time.total_seconds()

        response.append(user_session)
    
    return response


def createListOfUserSessions(userList):
    '''Creates the necessary user sessions for all the user_id's.
        Complexity time for this algorithm is O(n) with n total activities,
        this because for every user_id we need to use getUserSessions, 
        and in the end we will iterate all of the activities once.'''

    user_sessions = {}
    for key in userList:
        user_sessions[key] = getUserSessions(userList.get(key))

    return user_sessions


def sortActivitiesByDateAndUserId(response):
    '''Groups all the acivities sorted by date in their respective user_id.
    Complexity time for this algorithm is O(n*log (n)) with n activities, because we sort the list.'''

    activities = response.get("activities")
    sorted_list_by_date = sortResponseByFirstSeen(activities)
    sorted_list_by_user_id = groupActivitiesByUserId(sorted_list_by_date)

    return sorted_list_by_user_id
    