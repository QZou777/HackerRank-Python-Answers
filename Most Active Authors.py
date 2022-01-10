import requests

def getUsernames(threshold):
    # define a list to hold usernames
    usernames = [] 
    # initiate a value for total page to be 1, which will be corrected after requesting information through API
    total_page = 1
    current_page = 1 
    
    # request information for all pages
    while current_page <=total_page:
        responce = requests.get("https://jsonmock.hackerrank.com/api/article_users/search?page={}".format(current_page), verify=False)
        page_info = responce.json()
        
        # update the total page information when read in the information from 1st page:
        if current_page ==1:
            total_page = page_info['total_pages']
                
        # Get information from users
        for i in range(len(page_info['data'])):
            # check if user submission count is above the threshold or not 
            if page_info['data'][i]['submission_count'] > threshold:
                usernames.append(page_info['data'][i]['username'])
        # update the current page
        current_page +=1
        
    print(*usernames, sep='\n')

getUsernames(10)
