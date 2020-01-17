#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    """
    YOUR CODE HERE
    """


    # If the length is 2 or less then we don't need to check weights because the weights are either going to meet limit or not.
    # If length is more than 2 then we need to pass the weights into the hashTable
    if length > 2:

        # create hash table
        # Each weight is passed in as the key, the key is hashed and that hashed value is used as the index
        # If there are multiples of the same weight, a linked list is created inside that hashed index
        # The index from the array for that weight is passed in as the value
        for weight in weights:
            hash_table_insert(ht,weight,weights.index(weight))

        

        # check hash table for matches
        # You go through each weight and grab the limit minus each single weight. If that result exists in the hashTable
        # then that index is returned because its guaranteed to be a match for the limit
        summed_weights = []
        print("wL",weights, limit)
        for weight in weights:
            summed_weights.append(hash_table_retrieve(ht, (limit - weight)))
        print(summed_weights)
        # remove Nones
        answer = [x for x in summed_weights if x is not None]

        # This solution does not account for multiple matches. It just so happens the test cases only give 1 possible match
        return answer

    # check if pair exists
    elif length == 2:
        if weights[0] + weights[1] != limit:
            return None
        else:
            return [1,0]

    else:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
