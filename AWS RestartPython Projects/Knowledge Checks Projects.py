# python script to check if a student is doing well according to the number of KCs they have done


# ask user for their name
name = input("Hello there, what's your name?: ")


# add new line
print('\n')

# print user's name
print(f'Hello {name}')

# print welcome statement
print('''
      Welcome to the Azubi AWS Cloud Restart Progess Tracker
      This program tracks your progress using your KCs.
      This program expects that students complete their modules and KCs sequentially.
      Please enter the number that corresponds with the most recent module in which you completed all KCs
      
      1: Intro to computing
      2: Linux
      3: Networking
      4: Security

      If you have not completed all KCs in any module, enter "0"

      ''')


# ask user for number of KCs done
module_with_all_kc_completed = input("What is the most recent module in which you completed all KCs?: ")

# convert input to integer
module_with_all_kc_completed = int(module_with_all_kc_completed)


# add new line
print('\n')

# define function to calculate percentage
def performance(completed_module_kcs,kc):
    '''This function calculates the percentage of KCs done'''
    completed_kcs = completed_module_kcs + kc
    overall_kc = 50
    percent = round((completed_kcs / overall_kc) * 100,2)
    print(f'You have completed {percent}% of your KCs')
    if percent >= 80:
        print('Excellent job keep it up')
    elif percent >= 60:
        print("Good but not enough. Push harder!!!")
    elif percent >= 40:
        print("You're falling behind. Try to keep up!!!")
    else:
        print("You need to talk to an instructor about your performance")

# number of KCs done 
module_1 = 12
module_2 = 14
module_3= 7
module_4= 17

if module_with_all_kc_completed == 0:
    print('''
What is the last KC you completed in the Intro to Computing module.
          
1:  Introduction to Cloud Computing 
2:  Basic Computing Concepts 
3   Development Team Roles 
4:  What is Cloud Computing? 
5:  Advantages of Cloud Computing 
6:  What is Amazon Web Services? 
7:  Fundamentals of AWS Pricing 
8:  AWS Infrastructure Overview 
9:  AWS Services and Service Categories 
10: Shared Responsibility Model 
11: Introduction to Amazon S3 
12: Introduction to Amazon EC2 
          
If you have not done any KCs in the Intro to Computing module yet, enter "0"
''')
    completed_module_kcs = 0
    kc = input("Enter number that corresponds with the KC: ")
    kc = int(kc)
    performance(completed_module_kcs,kc)

elif module_with_all_kc_completed == 1:
    print('''
What is the last KC you completed in the Linux module.
          
1:  An Introduction to Linux
2:  Linux Command Line
3:  Users and Groups
4:  Editing Files
5:  Working with the File System
6:  Working with Files
7:  Managing File Permissions
8:  Working with Commands
9:  Managing Processes
10: Managing Services
11: The Bash Shell
12: Bash Shell Scripts
13: Software Management
14: Managing Log Files
          
If you have not done any KCs in the Linux module yet, enter "0"
          ''')
    completed_module_kcs = module_1
    kc = input("Enter number that corresponds with the KC: ")
    kc = int(kc)
    performance(completed_module_kcs,kc)

elif module_with_all_kc_completed == 2:
    completed_module_kcs = module_1 + module_2
    print('''
What is the last KC you completed in the Networking module.

1: Introduction to Networking
2: Networking Concepts
3: Internet Protocol
4: Amazon VPC
5: IPv4 Subnetting
6: TCP and UDP
7: Additional Networking Technologies
          
If you have not done any KCs in the Networking module yet, enter "0"''')
    kc = input("Enter number that corresponds with the KC: ")
    kc = int(kc)

    performance(completed_module_kcs,kc)

elif module_with_all_kc_completed == 3:
    print('''
What was the last KC you completed in the Security?
Enter a number that corresponds with that KC.

1: Introduction to Security
2: Security Lifecycle: Prevention
3: Network Hardening
4: Systems Hardening
5: Prevention: Data Security
6: Prevention: PKI
7: Prevention: Identity Management
8: Prevention: AWS IAM
9: Security Lifecycle: Detection
10: AWS CloudTrail
11: AWS Config
12: Security Lifecycle: Response
13: Security Lifecycle: Analysis
14: Trusted Advisor
15: Security Best Practices for Account Creation
16: AWS Security Compliance Program
17: AWS Security Resources
          
If you have not done any KCs in the Security module yet, enter "0"''')
    kc = input("Enter number that corresponds with the KC: ")
    kc = int(kc)
    completed_module_kcs = module_1 + module_2 + module_3

    performance(completed_module_kcs,kc)
    
elif module_with_all_kc_completed == 4:
    print('Way to go! Keep up the excellent work!')

    











# # try running the code
# try:
#     # convert input into integer
#     number_of_kc = int(number_of_kc)
#     # calculate percentage of KCs done
#     percentage = (number_of_kc / overall_kc) * 100
#     # run control flow
#     # check if the user has done more than 50 KCs
#     if number_of_kc > 50:
#         # print statements
#         print(f'You have done {percentage}% of your KCs.')
#         print("You have input a wrong number of KCs")
#     # check if the user has done more than 40 KCs
#     elif number_of_kc > 40:
#         # print statements
#         print(f'You have done {percentage}% of your KCs.')
#         print("Great job! You're on track!")
#     # check if the user has done more than 30 KCs
#     elif number_of_kc > 30:
#         # print statements
#         print(f'You have done {percentage}% of your KCs.')
#         print("Good job! Pick up the pace!")
#     # if all above conditions are not met
#     else:
#         # print statements
#         print(f'You have done {percentage}% of your KCs.')
#         print("You need to sit up, else you will lose the AWS exam voucher!!!")
# # check if there is an error
# except:
#     print("You did not input a number")

# # Ideas
# # use a function
# # comment to understanding of users
# # calculate according to week number and kCs per each week



# # add note to inform user that this program expects that users follow modules sequentially
# # ask user what week or module he/she is on
# # ask how many KCs the user has done for the week/module

# # ask user to input the last week's KC's they have done
# # based on the answer, display a list of KC's for the week they have not completed yet
# # ask user what the last KC they completed was
# # based on the answer calculate percentage of KCs done






