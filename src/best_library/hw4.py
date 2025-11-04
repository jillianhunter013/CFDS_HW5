import pandas as pd

##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts and returns
# the number of times that Simba appears in a list of
# strings. Example:
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#
def count_simba(strings):
    list_counts = list(map(lambda x: x.lower().count("simba"), strings))
    return sum(list_counts)

#count_simba(["Simba and Nala are lions.", "I laugh in the face of danger.",
#"Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."])

# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

def get_day_month_year(dates):
    data = [(date.day, date.month, date.year) for date in dates]
    df = pd.DataFrame(data, columns=['day', 'month', 'year'])
    return df


# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#
from geopy.distance import distance

def compute_distance(list_of_tuples):
    return list(map(lambda x: distance(x[0], x[1]).km, list_of_tuples))


#################################################
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#

def sum_general_int_list(lista):
    total = 0
    for element in lista:
        if isinstance(element, int):
            total += element
        elif isinstance(element, list):
            total += sum_general_int_list(element)  # recursive call
        else:
            raise ValueError(f"Unsupported type: {type(element)}")
    return total



