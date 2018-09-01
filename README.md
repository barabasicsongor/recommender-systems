# Recommender Systems


### How to use?

1. Install Docker from: https://www.docker.com/

2. Start the Docker daemon and navigate to the root folder

3. From terminal run `make server`

4. Now you will have two endpoints open at the url *http://0.0.0.0:5000/*

    - */top-items* - returns the most voted items
    
    - */collab-filt* - returns the most suggested products for the user

### How to use the end points?

You have to make a POST request to the end points, the body containing JSON data.

### */top-items* end point

For the */top-items* end point, you have to send a JSON which has a key *items* and the value for the key is an array which contains also JSON objects. Each object is an item from the dataset, and has the following values in it.

        - id - item id integer
        - name - item name string
        - vote_average - vote average for the item, float
        - vote_count - number of times the item was voted, integer
        - description - description of the item, string

It returns the same objects in a JSON array, but ordered according to the criteria. Then you only have to display them.

### */collab-filt* end point

For the */collab-filt* end point, you have to send a JSON which has two keys.

        1. *ratings*, which has as value an array which in fact contains objects of the JSON form

                - userId - integer
                - itemId - integer
                - rating - float between 1 and 5
        
        2. *recomm_user_id*, is the ID of the current user to which we want to make a recommendation

It returns a JSON object which has a key *result* and value an array of item IDs. Those item ID's are the recommendations which you have to show.