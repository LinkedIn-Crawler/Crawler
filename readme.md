# LinkedIn Crawler Instructions

Welcome to the LinkedIn Scraper.

## Instructions to Run the Software on a Local Computer:

- Ensure that you have a Functional Text Editor(Atom, SublimeText, etc.) on your system.
- Install chromedriver.exe  (Read all the rules on the official site before Installing)
- Install Python
- Install Selenium
- Install Parsel

### Some Other Instructions:

Wherever you see this command - 

driver = webdriver.Chrome('SAMPLE/PATH')

in the Python Files, replace 'SAMPLE/PATH' with the location of the ChromeDriver.exe on your Local System

For example,

driver = webdriver.Chrome('/home/samay/chromedriver')                 [UBUNTU]

driver = webdriver.Chrome('C:/Users/saisa/Desktop/chromedriver')      [Windows]

#### This Software requires you to provide your LinkedIn Credentials.

#### Update your LinkedIn username and password in the parameters.py file.


## This Project includes 3 functionalities:

<details>
    <summary>Search</summary>
    
    - You can run linkedin_profile_search.py on your local Computer.
    - Please Wait for a moment as the program runs.
    - Then, input the Keywords you would like to Search.
    - You can enter multiple keywords.
    - Enter the Number of Profiles You need.
    - The most relevant LinkedIn Profiles Data would be exported into a csv file(which can be renamed in parameters.py).
    - Please refer to Search_Python-Developer_Delhi.csv for sample output File. 
    - Sample Input: Keywords for Sample File: "Python Developer" "Delhi"
    - Sample Input: Number of Profiles: 17

</details>

<details>
    <summary>Connect</summary>
    
    - Similar to above Search Functionality(File name is linkedin_profile_connect.py).
    - Additional Feature: You would connect to all the people whose Profiles have been Scraped.

</details>
    
<details>
    <summary>Alumni Report Generation</summary>
    
    - You can run alumni_yearwise_linkedIn.py on your local Computer.
    - Please Wait for a moment as the program runs.
    - Then, input the Institute Name. All data relating to the The Alumni of the Institute would be Scraped.
    - Alumni Data would be exported into a csv file(which can be renamed in parameters.py).
    - Please refer to output.csv for sample output File. Input: Institute Name for Sample File: "massachusetts institute of technology" 
    - Using Microsoft Power BI, the Excel data(from output.csv) was manually Loaded to teh dashboard to create the Final Report(Alumni_Report_MIT_2000.pdf)
</details>
