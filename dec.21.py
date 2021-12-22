# Given: an array containing hashes of names
# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

# Example:
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

def namelist(names):
    #  if the list is empty, my function should return an empty string, like so:
    if len(names)==0:
        return '' 
    # if there is only one name in the list then that name should be returned on its own as a string:
    # The key to note with step two is that by looping through the list of names, we can isolate each dictionary element (example: {name: ‘Bart’}) and then split that dictionary by adding .items() at the end. The “name” is the key and “Bart” is the value, so this is how we extract only the value to return, i.e. ‘Bart’.
    if len(names)==1:
        for i in names:
            for key, value in i.items():
                return value
    else:
    # we will go about getting multiple names. 
    # loop through each element in the “names” list, then index into each dictionary pair and pull out the value. The difference is that because there are multiple pairs, we are going to store each value in a list (created as an empty list prior to the “for” loop) called “just_names”. Now that the names have all been extracted, we just need to join them back together in the correct string pattern.
        just_names = []
        for i in names:
            for key, value in i.items():
                just_names.append(value)   #step 4 (below)
                # Once we have that list of names, we just call in the .join() function to string together all BUT the very last name, then add the ampersand and the last name to finish off the string:
    return ', '.join(just_names[:-1]) + ' & ' + just_names[-1]