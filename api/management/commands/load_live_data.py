from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


import csv, json, requests

class Command(BaseCommand):
    help = 'Load all the live data'

    headers = {
            'content-type': 'application/json',
            #prod
            #'Authorization':'Token dfe2687bc2ca2ed5b4da01bc49dfe3946682cb0f'
            #staging
            'Authorization':'Token fb5df470df0fa3727c49a61608996618d0954289'
    }
    #env = 'staging' 
    env = 'production'




    def handle(self, *args, **options):
        
        #self.load_users()
        self.load_projects()
        self.load_tasks()

    def _get_project_id(self, title):
        url = "http://projectservice.tangentmicroservices.com/api/v1/projects/?search={0}" . format (title)  

        r=requests.get(url, headers=self.headers)
        j = json.loads(r.content)

        if len(j) == 1:
            return j[0].get("pk")
        else:
            return None

        
    def load_tasks(self):

        with open('ProjectTasks.csv', 'rb') as csvfile:

            if self.env == 'staging':
                url = "http://staging.userservice.tangentme.com/users/"
            else:
                url = "http://projectservice.tangentmicroservices.com/api/v1/tasks/"

            task_reader = csv.reader(csvfile)
            #Name,Project (Project Phase),Project Phase,Action By,Estimated Hours to Complete,Actual Hours to Complete,Description,Due Date,Created On

            '''
            project = models.ForeignKey(Project)
            title = models.CharField('Task Name', max_length=200, blank=False, null=False)
            
            due_date = models.DateField('Due Date', blank=True, null=True)
            estimated_hours = models.DecimalField('Est. Hours', max_digits=5, decimal_places=2, default=0)
            '''

            for row in task_reader:

                project_title = row[1]
                project_id = self._get_project_id(project_title)

                if project_id is not None:
                    data = {
                        "project": project_id,
                        "title" : row[0],
                        "description" : row[0],
                        "due_date" : row[8].split(" ")[0],
                        "estimated_hours" : row[5].replace(",","") + ".00",
                    }
                    print (data)
                    response = requests.post(url, data=json.dumps(data), headers=self.headers)
                    if response.status_code == 201:
                        print ("SUCCCESS: {0}" . format (row[0]))
                    else:
                        print ("{0}: {1}" . format (response.status_code, response.content))
                    
                else:
                    print ("No project found for {0}. Ignoring task: {1}" . format (row[1], row[0]))

        
    def load_projects(self):
        with open('Projects.csv', 'rb') as csvfile:
            project_reader = csv.reader(csvfile)

            if self.env == 'staging':
                    url = "http://staging.userservice.tangentme.com/users/"
            else:
                url = "http://projectservice.tangentmicroservices.com/api/v1/projects/"

            # ['Name', 'Customer', 'Start Date', 'End Date', 'Project Leader', 'Estimated Hours', 'Completed Hours', 'Project Status', 'Status']

            for row in project_reader:
                data = {
                    "title" : row[0],
                    "description" : row[0],
                    "start_date" : row[2],
                    "end_date" : row[3],
                }
                
                response = requests.post(url, data=json.dumps(data), headers=self.headers)
                print (".")


    def load_users(self):

        with open('users.csv', 'rb') as csvfile:
            csv_reader = csv.reader(csvfile)

            for first_name, last_name, email_address, phone_number in csv_reader:

                if self.env == 'staging':
                    url = "http://staging.userservice.tangentme.com/users/"
                else:
                    url = "http://userservice.tangentmicroservices.com/users/"

                fname = filter(str.isalnum, first_name).lower()
                sname = filter(str.isalnum, last_name).lower()
                username = "{0}.{1}" . format (fname, sname)
                
                data = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email_address,
                    "username": username,
                }
                response = requests.post(url, data=json.dumps(data), headers=self.headers)

                print (".")
                




