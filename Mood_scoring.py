import pandas as pd

# Step 1: Insert the previously created CSV with test data
df = pd.read_csv('/Users/lukas/IU University/dummy_data')

# Step 2: Prepare Data - Create lists out of the semicolon data
for column in ['Mood', 'Languages', 'Interests']:
    df[column] = df[column].apply(lambda x: x.split(';'))

# 3 Define weights for scoring as before or adjust based on new insights
weights = {
    'age': 1,
    'course': 2,
    'mood': 3,  
    'interests': 3,
    'languages': 2
}

# Step 4: Create Funtions for the different Scores
    
# Age needs a different scoring due to its data nature - Calculates the age difference and scores based on that
def calculate_age_score(age1, age2, weight=1):
    """Calculate age compatibility score."""
    age_difference = abs(age1 - age2)
    # Scoring negatively affected if the difference is greater than 5 years
    score = max(0, (5 - age_difference) / 5.0)
    return score * weight

#Score for all the other user parameters (except semester) - Checks how many parameters are the same
def calculate_common_elements_score(list1, list2, weight=1):
    """Calculate score based on common elements in lists."""
    common_elements = len(set(list1) & set(list2))
    max_possible = max(len(list1), len(list2))
    score = common_elements / max_possible if max_possible > 0 else 0
    return score * weight

#based on previous scoring of all considered parameters it sums up all the subscores to the total score
def calculate_total_match_score(user1, user2, weights):
    """Calculate total match score between two users."""
    age_score = calculate_age_score(user1['Age'], user2['Age'], weights['age'])
    course_score = calculate_common_elements_score(user1['Course'], user2['Course'], weights['course'])
    mood_score = calculate_common_elements_score(user1['Mood'], user2['Mood'], weights['mood'])
    interests_score = calculate_common_elements_score(user1['Interests'], user2['Interests'], weights['interests'])
    language_score = calculate_common_elements_score(user1['Languages'], user2['Languages'], weights['languages'])
    
    total_score = age_score + course_score + mood_score + interests_score + language_score
    return total_score


# Step 5: Calculate Match Scores for all user pairs
def calculate_scores_for_all_pairs(df, weights):
    scores = []
    for i in range(len(df)):
        user1 = df.iloc[i].to_dict()
        for j in range(i+1, len(df)):
            user2 = df.iloc[j].to_dict()
            total_score = calculate_total_match_score(user1, user2, weights)
            scores.append(((user1['User ID'], user2['User ID']), total_score))
    return scores


 # Assign all_scores dataframe
all_scores = calculate_scores_for_all_pairs(df, weights)

# Sort the scores in descending order based on the score
sorted_scores = sorted(all_scores, key=lambda x: x[1], reverse=True)

# Print the 10 highest scores for testing the scoring script
print("Top 10 Highest Match Scores:")
for pair, score in sorted_scores[:10]:
    print(f"Match Score between User {pair[0]} and User {pair[1]}: {score}")

# Further work needed to maximise matches among others.