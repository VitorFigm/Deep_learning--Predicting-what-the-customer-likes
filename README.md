# Predicting what costumer likes

Based on an Amazon food review database, for each reviewer, i will randomly erase 5 products that he gave 5 stars, and the model will try to predict what products were those.

## Recommendation System

We could say that those products that it predicts are a recommendation that an e-commerce website is showing for its clients, then this AI would transform into a great recommendation system. This would be an awesome alternative for using algorithms that constantly needs to make costly calculation in an entire database for recommending the product (like Nearest Neighbors algorithm) or update the model and detect a trend. MLP neural network only needs the database once in its training, don’t need many computations for recommending a product to the user and can easily detect trend since it uses each one of the recommendations to learn and become better.

# Results

I divided the database into a test and a training set, the model first uses the training database for learning and then tries to recommend to the test data. Incredibles **99.91%** of the products that the IA recommended for the test database costumers was those that received 5 stars and I erased, we could say then that 99.91% of the recommendations from the model would receive 5 stars, and, for 47.10% of the costumers, it simply predicted all of the 5 products I hid, what would mean that 47.10% of the user would give 5 stars to all of the recommendations the model gave.
