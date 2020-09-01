# Predicting what costumer likes

Using Amazon's review database, for each reviewer, i will randomly erase 5 products that costumer gave 5 stars, and the model will try to predict what products were those. This could be an idea to a recommendation system, where an IA is recommending products to a customer based on predictions of what this customer would like.


# Results

I divided the database into a test and a training set, the model first uses the training database for learning and then tries to recommend to the test data. Incredibles **87.82%** of the products that the IA recommended for the test database costumers was those that received 5 stars and I erased, we could say then that 87.82% of the recommendations from the model would receive 5 stars, and, for 49.62% of the costumers, it simply predicted all of the 5 products I hid, what would mean that 49.62% of the user would give 5 stars to all of the recommendations the model gave.
