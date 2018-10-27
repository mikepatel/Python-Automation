# You are in charge of a display advertising program.
# Your ads are displayed on websites all over the internet.
# You have some CSV input data that counts how many times you showed an ad on each individual domain.
# Every line consists of a count and a domain name. It looks like this:
# 
# 
# Write a function that takes this input as a parameter and
# returns a data structure containing the number of hits that were recorded on each domain AND
# each domain under it.
# For example, an impression on "sports.yahoo.com" counts for "sports.yahoo.com", "yahoo.com", and "com".
# (Subdomains are added to the left of their parent domain. So "sports" and "sports.yahoo" are not valid domains.)
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
counts = ["900,google.com",
          "60,mail.yahoo.com",
          "10,mobile.sports.yahoo.com",
          "40,sports.yahoo.com",
          "300,yahoo.com",
          "10,stackoverflow.com",
          "2,en.wikipedia.org",
          "1,es.wikipedia.org"]


def domain_count(in_count):
    out_count = {}

    for item in in_count:
        count, domain = item.split(",")
        count = int(count)
        num_periods = domain.count(".")

        # check if whole domain has already been seen
        if domain not in out_count:
            out_count[domain] = count
        else:
            out_count[domain] += count

        # Look for subdomains and TLDs
        subdomain = domain
        for i in range(1, num_periods+1):
            t = subdomain
            _, subdomain = t.split(".", 1)

            # check if subdomain has already been seen
            if subdomain not in out_count:
                out_count[subdomain] = count
            else:
                out_count[subdomain] += count

    return out_count


#
out = domain_count(counts)  # return data structure containing number of hits per domain
print(out)

