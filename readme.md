# LinkedIn Crawler Usage Instructions


Welcome to the LinkedIn Scraper.
Instructions to Run the Software on a Local Computer:

Ensure that you have a Functional Text Editor(Atom,SublimeText,etc.) on your System

# Install chromedriver.exe 
(Read all the rules on the official site before Installing)

# Install Python

# Install Selenium

# Install Parsel

Wherever you see this command

driver = webdriver.Chrome('SAMPLE/PATH')

in the Python Files, 

replace 'SAMPLE/PATH' with the location of the ChromeDriver.exe on your Local System

For example,


driver = webdriver.Chrome('/home/samay/chromedriver')                 [UBUNTU]

driver = webdriver.Chrome('C:/Users/saisa/Desktop/chromedriver')      [Windows]


This Software requires you to provide your LinkedIn Credentials.

# Update your LinkedIn username and password in the parameters.py file.


# This Project includes 3 functionalities:



# i) Search


    1) You can run linkedin_profile_search.py on your local Computer.
    2) Please Wait for a moment as the program runs
    3) Then, input the Keywords you would like to Search 
    4) You can enter multiple keywords.
    5) Enter the Number of Profiles You need.
    6) The most relevant LinkedIn Profiles Data would be exported into a csv file(which can be renamed in parameters.py)
    7) Please refer to Search_Python-Developer_Delhi.csv for sample output File. 
    Sample Input: Keywords for Sample File: "Python Developer" "Delhi"
    Sample Input: Number of Profiles: 17
# ii) Connect



    Similar to above Search Functionality(File name is linkedin_profile_connect.py)
    Additional Feature: You would connect to all the people whose Profiles have been Scraped
# iii) Alumni Report Generation




    1) You can run alumni_yearwise_linkedIn.py on your local Computer.
    2) Please Wait for a moment as the program runs
    3) Then, input the Institute Name. All data relating to the The Alumni of the Institute would be Scraped. 
    4) Alumni Data would be exported into a csv file(which can be renamed in parameters.py)
    5) Please refer to output.csv for sample output File.
    Input: Institute Name for Sample File: "massachusetts institute of technology" 
    6) Using Microsoft Power BI, the Excel data(from output.csv) was manually Loaded to teh dashboard to create the Final Report(Alumni_Report_MIT_2000.pdf)
