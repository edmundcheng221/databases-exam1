# write your Python code here according to the instructions

## import the csv module
import csv

def get_csv_data(filepath):
    dictionaryList = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for ele in reader:
            dictionaryList.append(ele)
    return dictionaryList
    """
    Opens the file at filepath, reads the data using the csv module's DictReader, 
    converts that data to a regular list containing a dictionary for each row of data in the CSV file
    and returns that list.

    :param filepath: The file path of the CSV data file to open
    :returns: A list of dictionaries, where each dictionary represents one row from the file
    """

def remove_rows_with_blank_fields(data):
    """
    Removes any rows with one or more blank fields from the data set.

    :param data: The data, as a list of dictionaries
    :returns: The modified data, as a list of dictionaries
    """
    ## place your code here to complete this method according to the instructions above
    dictionaryList = data
    newList = []
    for ele in dictionaryList:
        if ele.get('id') == '' or ele.get('handle') == '' or ele.get('first_name') == '' or ele.get('last_name') == '' or ele.get('email') == '' or ele.get('street') == '' or ele.get('city') == '' or ele.get('state') == '' or ele.get('state_animal') == '' or ele.get('real_food_affinity_category_id') == '' or ele.get('luxury_brand_affinity_category_id') == '' or ele.get('tech_gadget_affinity_category_id') == '' or ele.get('travel_affinity_category_id') == '':
            pass
        else:
            newList.append(ele)
    return newList
def remove_rows_with_state(data, state):
    """
    Removes any rows with the given value in the 'state' field.

    :param data: The data, as a list of dictionaries
    :param state: The state value of interest, e.g 'United Kingdom' 
    :returns: The modified data, as a list of dictionaries
    """
    ## place your code here to complete this method according to the instructions above
    modifiedData = []
    for ele in data:
        if ele.get('state') == state:
            pass
        else:
            modifiedData.append(ele)
    return modifiedData

def remove_rows_under_affinity_id_level(data, affinity_type, threshold):
    """
    Removes any rows with a value in a given affinity category id field lower than the supplied threshold.

    :param data: The data, as a list of dictionaries
    :param affinity_type: The type of affinity category id of interest...
    :param threshold: The maximum acceptable value for this affinity type... records with lower values will be removed.
    :returns: The modified data, as a list of dictionaries
    """
    ## place your code here to complete this method according to the instructions above
    modifiedData = []
    for ele in data:
        if int(ele.get(affinity_type)) < threshold:
            pass
        else:
            modifiedData.append(ele)
    return modifiedData

def replace_email_domain(data, old_domain, new_domain):
    """
    Updates any rows where the 'email' ends in the old domain.  Updates to the new domain.

    :param data: The data, as a list of dictionaries
    :param old_domain: The old domain to remove, e.g. '@dmoz.org'
    :param new_domain: The new domain to replace the old_domain with, e.g. '@dmoz.com'
    :returns: The modified data, as a list of dictionaries
    """
    ## place your code here to complete this method according to the instructions above
    modifiedData = []
    for ele in data:
        # print(ele.get('email')[-10:-1])
        if (ele.get('email')[-9:-1] == old_domain[-9:-1]) and (ele.get('email')[-1] == old_domain[-1]):
            ele['email'] = new_domain
            modifiedData.append(ele)
        else:
            modifiedData.append(ele)
    return modifiedData

def save_csv_data(data, filepath):
    """
    Saves the data into the specified file.  Include the field headers as the first row.

    :param data: The data, as a list of dictionaries
    :param filepath: The file path of the CSV data file to save to
    """
    ## place your code here to complete this method according to the instructions above
    with open(filepath, 'w') as f:
        f.write('id,handle,first_name,last_name,email,street,city,state,state_animal,real_food_affinity_category_id,luxury_brand_affinity_category_id,tech_gadget_affinity_category_id,travel_affinity_category_id')
    with open(filepath, 'a') as f:
        for ele in data:
            f.write(ele.get('id') + ',')
            f.write(ele.get('handle') + ',')
            f.write(ele.get('first_name') + ',')
            f.write(ele.get('last_name') + ',')
            f.write(ele.get('email') + ',')
            f.write(ele.get('street') + ',')
            f.write(ele.get('city') + ',')
            f.write(ele.get('state') + ',')
            f.write(ele.get('state_animal') + ',')
            f.write(ele.get('real_food_affinity_category_id') + ',')
            f.write(ele.get('luxury_brand_affinity_category_id') + ',')
            f.write(ele.get('tech_gadget_affinity_category_id') + ',')
            f.write(ele.get('travel_affinity_category_id'))
            f.write('\n')


def get_average_affinity_id(data, affinity_type):
    total = 0
    count = 0
    for ele in data:
        total += int(ele.get(affinity_type))
        count += 1
    average = total/count
    return format(average, '.0f')
    
    """
    Calculates the average affinity category id of all records in the data set.

    :param data: The data, as a list of dictionaries
    :param affinity_type: The type of affinity category id of interest...
    :returns: returns: The average affinity id for the given affinity_type
    """
    
    ## place your code here to complete this method according to the instructions above


#################################################
## Do not modify the code below this line      ##
## except to comment out any function calls    ##
## that you do not wish to test at the moment  ##
#################################################

def main():
    ## use the functions defined above to complete munging of the data file

    # get the data from the file
    data = get_csv_data('data/users.csv')

    # munge it
    data = remove_rows_with_blank_fields(data)
    data = remove_rows_with_state(data, 'United Kingdom')
    data = remove_rows_under_affinity_id_level(data, 'real_food_affinity_category_id', 2)
    data = replace_email_domain(data, '@dmoz.org', '@dmoz.com')

    # dave to the new csv file
    save_csv_data(data, 'data/users_clean.csv')

    # print the average cost per impression from the data in the file
    avg = get_average_affinity_id(data, 'real_food_affinity_category_id')
    print( 'The average affinity id for real food is: {}.'.format(avg) ) # format string nicely

if __name__ == "__main__":
    main()
