
# 
# Your previous JavaScript content is preserved below:
# 
# You are in charge of a display advertising program. Your ads are displayed on websites all over the internet. You have some CSV input data that counts how many times you showed an ad on each individual domain. Every line consists of a count and a domain name. It looks like this:
# 
# 
# Write a function that takes this input as a parameter and returns a data structure containing the number of hits that were recorded on each domain AND each domain under it. For example, an impression on "sports.yahoo.com" counts for "sports.yahoo.com", "yahoo.com", and "com". (Subdomains are added to the left of their parent domain. So "sports" and "sports.yahoo" are not valid domains.)
# 
# Sample output (in any order):
# 1320    com
#  900    google.com
#  410    yahoo.com
#   60    mail.yahoo.com
#   10    mobile.sports.yahoo.com
#   50    sports.yahoo.com
#   10    stackoverflow.com
#    3    org
#    3    wikipedia.org
#    2    en.wikipedia.org
#    1    es.wikipedia.org
# 
counts = [ "900,google.com",
      "60,mail.yahoo.com",
      "10,mobile.sports.yahoo.com",
      "40,sports.yahoo.com",
      "300,yahoo.com",
      "10,stackoverflow.com",
      "2,en.wikipedia.org",
      "1,es.wikipedia.org" ]

#temp = counts[1].split(".")
#print(temp)
#temp2 = counts[1].split(",")
#print(temp2)

def domainCount(counts):
    # for each item in count split on ","
    # first part will be count -> converted from string to int
    # second part will be domain -> move R to L to create subdomains
    # period count -> subdomains
    # has this subdomain been seen before? -> running totals
    # add the count to each subdomain
    prev_subdomains = []
    # hits structure with key domain
    dict_domain = {} # dictionary structure should be returned
    
    for i in range(len(counts)):
        hit, domain = counts[i].split(",")
        hit = int(hit)
        #print(type(hit))
        print(hit)
        #print(domain)
        
        _, subdomains = domain.rsplit(".", 1)
        #print(subdomains)
        if not domain in prev_subdomains:
            prev_subdomains.append(domain)
        
        #for s in subdomains:
        if not subdomains in prev_subdomains:
            prev_subdomains.append(subdomains)
            
        
                
                    
        #if not subdomains in prev_subdomains:
        #    prev_subdomains.append(subdomains)
            
    print(prev_subdomains)
            
    return dict_domain
        

#domainCount(counts)  # temp call
out = domainCount(counts)  # return data structure containing number of hits per domain

