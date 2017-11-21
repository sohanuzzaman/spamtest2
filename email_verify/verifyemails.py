import os
import requests
import json

inputfile = "{}/email_verify/raw_leads.txt".format(os.getcwd())
outputfile = "{}/email_verify/pure_leads.txt".format(os.getcwd())

# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()

# Read a file and convert each line to set items
def file_to_set(file_name):
    leads = set()
    with open(file_name, 'rt') as f:
        for line in f:
            leads.add(line.replace('\n', ''))
    return leads


# Iterate through a set, each item will be a line in a file
def set_to_file(leads, file_name):
    with open(file_name,"w") as f:
        for l in leads:
            f.write(l+"\n")


def validate_email(email):
    response = requests.get("https://trumail.io/json/{}".format(email))
    response = json.loads(response.text)
    if (
        response["disposable"] == False
        and response["deliverable"] == True
        and response["hostExists"] == True
    ):
        return True
    else:
        return False



def email_verify(leads):
    pure_leads = set()
    for l in leads:
        status = validate_email(l)
        if status == True:
            pure_leads.add(l)
            print ("{} is a good lead".format(l))
        else:
            print("{} is a bad lead".format(l))
    return pure_leads

leads = file_to_set(inputfile)
delete_file_contents(outputfile)
pure_leads = email_verify(leads)
set_to_file(pure_leads, outputfile)