"""
Configuration file for the profile-search application.
"""

#db parameters
db = {
    "host" : "localhost",
    "port" : 27017,
    "dbname" : "FraudBuddyDB"
}

#thresholds
thresholds = {
    "processor_interest_threshold": 0.4,
    "notif_interest_threshold": 0
}

DEFAULT_LIMIT = 10
MAX_LIMIT = 100