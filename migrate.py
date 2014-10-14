
from pymongo import MongoClient
import getpass

def migrate(USER, PASS):
    client = MongoClient('kahana.mongohq.com:10014')
    db=client.rumi_development
    db.authenticate(USER, PASS)
    project_id = [24,26,27,28,29]
    data_store_id = [639,767,673,791,675]

    for i in range(len(project_id)):

        cu=db.data_sets.find( {'__project_id__': project_id[i], '__data_store_id__': data_store_id[i]} )
        keys=cu[0].keys()
        l=[]
        l.append(keys)
        for j in cu:
            row = []
            for key, value in j.iteritems():
                row.append(value)
            l.append(row)

        for r in l:
            print r
        print "------------"

if __name__ == '__main__':
    USER = raw_input("Enter the username: ")
    PASS = getpass.getpass('Password:')
    migrate(USER,PASS)
    



