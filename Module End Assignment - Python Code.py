# Survey Feedback Analyzer

# Step 1: Preloaded Feedback Data
feedback_data = {
    "S_No": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    
    "Name": [
        "Ravi", "Neera", "Sam", "Anju", "Raj",
        "Divya", "Arjun", "Kiran", "Latha", "Nisha"
    ],
    
    "Feedback": [
        "Very GOOD Service!!!!",
        "Poor support,  not happy   ",
        "GREAT experience! will come again.",
        "Very okay...",
        "BAD",
        "Excellent care, excellent staff!",
        "Good food and good ambience!!",
        "Poor response and poor handling of issue.",
        "Satisfied, but could be better.",
        "Good support... quick service."
    ],
    
    "Rating": [5, 2, 3, 4, 2, 5, 4, 1, 3, 4]
}


# Step 2: Add More Feedbacks

n = int(input("How many more feedbacks do you want to add? "))

for i in range(n):
    print("\nEnter details for feedback", i + 1)
    
    name = input("Enter Name: ")
    feedback = input("Enter Written Feedback: ")
    
    rating = int(input("Enter Rating (1-5): "))
    
    # Automatically assign S_No starting from 11
    s_no = len(feedback_data["S_No"]) + 1
    
    feedback_data["S_No"].append(s_no)
    feedback_data["Name"].append(name)
    feedback_data["Feedback"].append(feedback)
    feedback_data["Rating"].append(rating)


# Step 3: Text Cleaning

for i in range(len(feedback_data["Feedback"])):
    
    text = feedback_data["Feedback"][i]
    
    # Remove punctuation
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    
    # Remove extra spaces
    text = " ".join(text.split())
    
    # Convert to lowercase
    text = text.lower()
    
    # Update cleaned feedback
    feedback_data["Feedback"][i] = text


# Step 4: Word Count Insights

def count_word_in_feedbacks(word):
    count = 0
    
    for feedback in feedback_data["Feedback"]:
        words = feedback.split()
        
        if word.lower() in words:
            count += 1
    
    return count


print("\n----- WORD COUNT INSIGHTS -----")

print("Number of feedbacks containing 'good':",
      count_word_in_feedbacks("good"))

print("Number of feedbacks containing 'poor':",
      count_word_in_feedbacks("poor"))

print("Number of feedbacks containing 'excellent':",
      count_word_in_feedbacks("excellent"))


# Step 5: Final Summary & Insights

print("\n----- FINAL CLEANED FEEDBACK DATA -----")
print(feedback_data)


# Average Rating

total_rating = sum(feedback_data["Rating"])
number_of_feedbacks = len(feedback_data["Rating"])

average_rating = total_rating / number_of_feedbacks

print("\nAverage Rating:", round(average_rating, 2))


# Find feedback with longest comment

longest_index = 0
longest_words = 0

for i in range(len(feedback_data["Feedback"])):
    
    word_count = len(feedback_data["Feedback"][i].split())
    
    if word_count > longest_words:
        longest_words = word_count
        longest_index = i


print("\n----- LONGEST FEEDBACK -----")
print("Name:", feedback_data["Name"][longest_index])
print("Feedback:", feedback_data["Feedback"][longest_index])
print("Word Count:", longest_words)


# Unique Words

unique_words = set()

for feedback in feedback_data["Feedback"]:
    words = feedback.split()
    
    for word in words:
        unique_words.add(word)


print("\n----- UNIQUE WORDS -----")
print(sorted(unique_words))


# Optional: Sort feedbacks by rating

sorted_feedbacks = sorted(
    zip(
        feedback_data["Name"],
        feedback_data["Feedback"],
        feedback_data["Rating"]
    ),
    key=lambda x: x[2],
    reverse=True
)

print("\n----- FEEDBACKS SORTED BY RATING -----")

for name, feedback, rating in sorted_feedbacks:
    print("Name:", name)
    print("Feedback:", feedback)
    print("Rating:", rating)
    print()
