from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import SVD
from surprise import accuracy
import pandas as pd


file_path = "ratings.csv"  
reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1, rating_scale=(1, 5))
data = Dataset.load_from_file(file_path, reader=reader)


trainset, testset = train_test_split(data, test_size=0.2, random_state=42)


model = SVD()
model.fit(trainset)


predictions = model.test(testset)


def get_top_n_recommendations(predictions, user_id, n=10):
    top_n = {}
    for uid, iid, true_r, est, _ in predictions:
        if uid == user_id:
            if user_id not in top_n:
                top_n[user_id] = []
            top_n[user_id].append((iid, est))

    
    top_n[user_id].sort(key=lambda x: x[1], reverse=True)
    top_n[user_id] = top_n[user_id][:n]

    return top_n


example_user_id = '1'
example_user_predictions = get_top_n_recommendations(predictions, example_user_id, n=5)[example_user_id]


movie_data = pd.read_csv(file_path.replace("ratings.csv", "movies.csv"))  
movie_titles = dict(zip(movie_data['movieId'], movie_data['title']))

print(f"Top 5 Recommendations for User {example_user_id}:")
for movie_id, estimated_rating in example_user_predictions:
    movie_title = movie_titles[int(movie_id)]
    print(f"{movie_title}: Estimated Rating = {estimated_rating:.2f}")


user_id_input = input("The above is an example of how for a particular user id top 5 recommendation is retrieved.\nEnter a user ID to get recommendations: ")
user_id_input = str(user_id_input)


user_predictions = get_top_n_recommendations(predictions, user_id_input, n=5).get(user_id_input, [])


print(f"\nTop 5 Recommendations for User {user_id_input}:")
for movie_id, estimated_rating in user_predictions:
    movie_title = movie_titles[int(movie_id)]
    print(f"{movie_title}: Estimated Rating = {estimated_rating:.2f}")
