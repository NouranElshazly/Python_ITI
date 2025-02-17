from user.user import User
from project.Project import Project

while True:
    print("\n 1. Register \n 2. Login \n 3.Exit ")
    choice = input("Enter Your Choice : ")
    if choice=="1":
        newuser=User.register()
        
    elif choice=="2":
        user_logged_in_email =User.login()
        if user_logged_in_email:
            while True :
                print("\n 1. Create Project \n 2. View Projects \n 3.Search Project by date  \n 4.Edit Project \n 5. Delete Project \n 6.Logout ")
                projectchoice = input("Enter Your Choice : ")
                if projectchoice=="1":
                    Project.create_project(user_logged_in_email)
                elif projectchoice=="2":
                    Project.display_projects()
                elif projectchoice=="3":
                    Project.search_by_date()
                elif projectchoice=="4":
                    project_title = input("Enter your project title to edit : ")
                    Project.edit_project(project_title,user_logged_in_email)
                
                elif projectchoice=="5":
                    project_title = input("Enter your project title to delete : ")
                    Project.delete_project(project_title,user_logged_in_email)
                elif projectchoice=="6":
                    print("Exit app ")
                    break
                    

    elif choice=="3":
        print("Exit")
        break

