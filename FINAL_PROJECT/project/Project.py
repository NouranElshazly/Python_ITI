from validation.validations import validate_date

#project class 
class Project :
    project_info = "Projects.txt"
    def __init__(self, Title, Details, Total_target, start_time,  end_time,user_email):
        self.Title=Title
        self.Details = Details
        self.Total_target= Total_target
        self.start_time=start_time
        self.end_time=end_time
        self.user_email= user_email #as one user can have many projects 
   
    @classmethod
    def save_project(cls,data):
        with open (cls.project_info , "w")as fp :
            for project in data :
                fp.write("|".join(project)+"\n")
    @classmethod
    def load_project(cls):
        try:
            with open(cls.project_info, 'r') as fp:
                lines = fp.readlines()
                data = [line.strip().split("|") for line in lines]  
                return data  
        except Exception :
            print("CAN NOT LOAD THIS FILE!")
    @classmethod
    def display_projects(cls):
        projects=cls.load_project()
        for i ,project in enumerate(projects):
            if len(project) >= 6:
                print(f"{i+1} . Title: {project[0]} ,Target: {project[2]} EGP, Start: {project[3]}, End: {project[4]}, User: {project[5]}")
    @classmethod
    def create_project(cls, user_email):
        """Creates a new project."""
        title = input("Enter Project Title: ")
        details = input("Enter Project Details: ")
        target = input("Enter Project Target: ")
        start_date = input("Enter Start Date (YYYY-MM-DD): ")
        while not validate_date(start_date):
            print("Invalid date format! Please enter in YYYY-MM-DD format.")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")

        end_date = input("Enter End Date (YYYY-MM-DD): ")
        while not validate_date(end_date):
            print("Invalid date format! Please enter in YYYY-MM-DD format.")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
        

        projects = cls.load_project()
        projects.append([title, details, target, start_date, end_date, user_email])
        cls.save_project(projects)

        print(f"Project '{title}' created successfully!")
    @classmethod
    def delete_project(cls,project_title,user_email):
        try:
            projects = cls.load_project()
            for project in projects:
                if project[0]== project_title and project[5]==user_email:
                    projects.remove(project)
                    cls.save_project(projects)
        except FileExistsError: 
            print(f"can not deleted unexist project {project_title}")
        else:
            print(f"Project {project_title} is deleted successfully !!")
    @classmethod
    def edit_project(cls , project_title , user_email ):
        
            projects = cls.load_project()
            if not projects:
                print(" No projects found! Make sure projects exist before editing.")
                return
            found = False
            for project in projects:
                if len(project) >= 6 and  project[0].strip().lower()== project_title.strip().lower() and  project[5]==user_email:
                    found=True
                    new_title= input("Please Enter  New Project Title  : ").strip()
                    new_details = input("Please Enter  New Project Details  : ").strip()
                    new_target = input("Please Enter  New Project Target   : ").strip()
                           # Validate and force correct date format
                    new_start_date = input("Enter New Start Date (YYYY-MM-DD): ").strip()
                    while not validate_date(new_start_date):
                        print("Invalid format! Enter date as YYYY-MM-DD.")
                        new_start_date = input("Enter New Start Date: ").strip()

                    new_end_date = input("Enter New End Date (YYYY-MM-DD): ").strip()
                    while not validate_date(new_end_date):
                        print("Invalid format! Enter date as YYYY-MM-DD.")
                        new_end_date = input("Enter New End Date: ").strip()
                    project[:5] = [new_title, new_details, new_target, new_start_date, new_end_date]
                    cls.save_project(projects)
                    print(f"Project '{project_title}' Updated successfuly !!")
                    break
            if not found:
                print(f"No project found with the title '{project_title}' for user '{user_email}'.")
    @classmethod 
    def search_by_date(cls):
        found =False
        date= input("please Enter Date (YYYY-MM-DD):  ")
        if not validate_date(date):
                print("Invalid format! Enter date as YYYY-MM-DD.")
        projects=cls.load_project()
        for project in projects:
             if  len(project) >= 6 and project[3] == date:  # Comparing start_date
                print(f"Title: {project[0]}, Target: {project[2]} EGP, Start: {project[3]}, End: {project[4]}")
                found = True

        if not found:
            print(f"No projects found with start date {date}.") 

       