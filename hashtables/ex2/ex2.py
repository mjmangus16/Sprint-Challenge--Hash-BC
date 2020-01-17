#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    # pass all tickets into the hash table. The starting location is the key, they destination is the value
    for ticket in tickets:
        hash_table_insert(hashtable,ticket.source, ticket.destination)

    route = []
    # The hash table item with the key of "NONE" marks the start of the trip
    route.append(hash_table_retrieve(hashtable, "NONE"))

    # Once the length of our route list meets the total length oif the trip then we have completed the trip.
    # We grab the last value added to route list and use that value to grab the key of the next ticket.
    while len(route) < length:
        route.append(hash_table_retrieve(hashtable, route[len(route)-1]))

    return route
