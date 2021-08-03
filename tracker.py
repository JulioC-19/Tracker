# Create an internship tracker

class Company:
    company = ''
    recruiter = ''
    headquaters = ''

    def __init__(self, company, recruiter, headquaters):
        self.company = company
        self.recruiter = recruiter
        self.headquaters = headquaters


class Position(Company):
    job_title = ''
    applied_season = ''
    location = ''
    status = ''

    def __init__(self, company, recruiter, headquaters, job_title, applied_season, location, status):
        super().__init__(company, recruiter, headquaters)
        self.job_title = job_title
        self.applied_season = applied_season
        self.location = location
        self.status = status

    def print_position(self, InternshipFile):
        print("")
        print("=============================================")
        InternshipFile.write(
            "============================================="+"\n")

        print("Company: " + self.company)
        InternshipFile.write("Company: " + self.company + "\n")

        print("Headquaters: "+self.headquaters)
        InternshipFile.write("Headquaters: " + self.headquaters+"\n")

        print("Recruiter Info: " + self.recruiter)
        InternshipFile.write("Recruiter Info: " + self.recruiter+"\n")

        print("Job posistion: " + self.job_title)
        InternshipFile.write("Job position: " + self.job_title+"\n")

        print("Application date: " + self.applied_season)
        InternshipFile.write("Application date: " + self.recruiter+"\n")

        print("Job Location: " + self.location)
        InternshipFile.write("Job Location: " + self.location+"\n")

        print("Status: " + self.status)
        InternshipFile.write("Status: " + self.status+"\n")
        print("=============================================")
        InternshipFile.write(
            "============================================="+"\n")
        print("")


InternshipFile = open("file.txt", "a")

Internship = Position("Company", "Recruiter info", "Location-State",
                      "Position title", "Month Year", "Location", "Status")
Internship.print_position(InternshipFile)
