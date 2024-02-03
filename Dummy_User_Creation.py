import pandas as pd
import numpy as np
import random

# Parameters used for our test users, further data can be added easily
n_users = 100
age_range = (16, 35)
courses = ['Computer Science', 'Data Science', 'Economics', 'Psychology', 'Engineering', 'Biology']
moods = ['running', 'coffee', 'lunch', 'study buddy', 'language_exchange', 'gym', 'gaming']
languages = ['English', 'Spanish', 'French', 'German', 'Chinese', 'Japanese']
interests_list = ['programming', 'gaming', 'reading', 'hiking', 'cooking', 'traveling', 'photography', 'music', 'sports', 'gym','chess']
semester_range = (1, 8) # decided for typical range of 8 semesters -> more should be included and a sepparation for Bachelors, Masters and other degrees make sense

# The app allows a maximum of 10 interests and minimum 3
def generate_interests():
    return random.sample(interests_list, random.randint(3, 10))  # Generate 1 to 10 interests

# The app allows a maximum of 3 moods and minimum of 1 is needed for match
def generate_moods():
    return random.sample(moods, random.randint(1, 3))  # Generate 1 to 3 moods

# The app allows to choose as many lnaguages as the user wants and minimum of 1 is needed to proceed
def generate_languages():
    return random.sample(languages, random.randint(1, 5))  # Generate 1 to 5 languages - decided to cap at 5 to not overcomplicate the matching

# Create 100 users between 16 and 35 assign one of the six given courses, one to three moods, 1-5 languages, 3-10 interests and choose a semester from 1-8

users_data = {
    'User ID': np.arange(1, n_users + 1),
    'Age': np.random.randint(age_range[0], age_range[1] + 1, size=n_users),
    'Course': [random.choice(courses) for _ in range(n_users)],
    'Mood': [generate_moods() for _ in range(n_users)],
    'Languages': [generate_languages() for _ in range(n_users)],
    'Interests': [generate_interests() for _ in range(n_users)],
    'Semester': np.random.randint(semester_range[0], semester_range[1] + 1, size=n_users)
}


users_df = pd.DataFrame(users_data) #create users dataframe

csv_path = "/Users/lukas/IU University/dummy_data.csv" # show path where to save
users_df.to_csv(csv_path, index=False) # no indices rows

