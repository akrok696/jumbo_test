# Automation_testing_with_selenium

This is a framework that will make your life easier in the field of automation testing. The goal of this framework is to making automation testing as easier as python that any one can learn and start using easily. 


#### Below are few useful features of this framework
- Modular Design.
- Easy to understand

#### Prerequisite
- High learning sprit towards automation
- Basic knowledge in python

## Quick Start
- ##### Clone Framework
    <pre>
    git clone https://github.com/akrok696/jumbo_test.git</pre>
- ##### Copy the jumbo_test folder to your project location and open command prompt from there.
    

- ##### Install required Python Packages
    <pre>
    pip install -r requirements.txt</pre>
- ##### Run the test
    <pre>
    python3 main.py</pre>
- ##### Work on project
    Congratulations! framework is ready you can add new testcases now.

## Repo Structure
- jumbo
    - tests 
    - tools
    - main.py

## Web UI Testing:
**Driver**
- As selenium supports different drivers for different browsers, for our project we will use chromium web driver.


**Consts**
- Locator is the unique identifier for any element using which we can find the element. 
- Consts can be formed: 
    1) By x-path, 
    2) By css, 
    3) By id, 
    4) By attribute,
    5) By name

- Let's take a example of a submit button whose xpath is //button[@type='submit 
- The const for the submit button will be:
    SUBMIT_BUTTON = "//button[@type='submit']"
 
 
**Tests**
- Contains test cases 
- All the functionality and UI test cases should be created inside this folder

 
**main.py**
- main.py is the entry point for tests execution. From adding the setup and teardown to every test case to import external plugins or modules we can configure these easily.


### How to work with this framework
Suppose you want to test the Jumbo welcome page.

#### **Step-1**
As we want to test jumbo web page let's create test with name starts with test_FILENAME.py inside tests folder. 


#### **Step-2**
Add name of the test_FILENAME.py to __init__.py


#### **Step-3**
Now we are ready to write the test script.


#### Step-4 - Running the script
We can run the complete testing by using the below command
<pre>
python3 main.py or you can start them directly from IDE 
</pre>

Awesome we have done this. Similarly you can follow step 2,3,4 to write and running automation for every web site.
