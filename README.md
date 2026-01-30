Introduction: 


-Shadow_Login is a Python-based GUI authentication system built using Tkinter, featuring secure encrypted credential storage, role-based access control (Admin/User), and a fully interactive interface.
-This project demonstrates how traditional login systems can be enhanced with custom encryption, file-based secure storage, and admin-level management, all wrapped in a modern GUI.


Intial Page: 


<img width="1260" height="740" alt="image" src="https://github.com/user-attachments/assets/22b60f44-dab3-4b6a-8415-5eed5224e5b9" />


Features: 
-Offline Authentication (Condition: File access is blocked for the user) 
-Easily integrable program
-Ability to create account
-Admin accounts which can create new admins and delete existing users (except admins)
-Ability to change password


Requirements: 
-TKinter
-Pillow


Login Page: 

The program starts with the login page itself. You have the options to create account, change your existing account's password, or to just simply login. Admin logins are automatically detected as admin usernames are stored in a separate file. 


<img width="1260" height="740" alt="image" src="https://github.com/user-attachments/assets/22b60f44-dab3-4b6a-8415-5eed5224e5b9" />


Create Account Page: 

Account creation is quite easy with a few conditions being in the password which are listed quite promptly and failing to do so will force you to recreate the password again. 


<img width="1271" height="741" alt="image" src="https://github.com/user-attachments/assets/cd6e255d-6555-4bd9-9630-e2cd2a5e0eb2" />


Change Password Page: 

Change password is fairly simple system in this program. You need to know your old password in order to change it. Admins can fetch encrypted passwords and decrypt it by the module provided specifically to them, fail in doing so will result in losing the user. 


<img width="1275" height="747" alt="image" src="https://github.com/user-attachments/assets/a4c15eea-52a1-4bfb-9ec9-7f9472816f84" />


Admin Page: 

Admin Page is used in case of count of users, seeing the username existing on the system, usernames corresponding to their encrypted passwords, adding more admins and deleting users in case of security breach


<img width="1277" height="745" alt="image" src="https://github.com/user-attachments/assets/757d1d90-66a4-4e4b-a30a-634710114fdc" />


Adding Admins: 

Adding admins is fairly a simple task, this process writes the username of the new admin in the admin file allowing the new admin to access the admin page upon login


<img width="1274" height="746" alt="image" src="https://github.com/user-attachments/assets/79dd7b83-7c8e-4d5d-aec9-3e520cb6f30e" />


Deleting User: 

Deleting user becomes a necessity in case of security breach. Hence this system allows admin to delete a malicious user as per requirement 


<img width="1267" height="738" alt="image" src="https://github.com/user-attachments/assets/1375c4ad-8e78-41b1-bbde-513de3e23625" />



Key Limitations in this Project: 
-As whole system being offline, if the user gains the ability to access files, all passwords can be decrypted. 
-Usage of encryption-decryption is a very risky method.
-Not-so-good looking UI due to Tkinter's limitations.


Future Goals: 
-Usage of hashing for storage of passwords.
-Shifting of password and encryption keys file to a secured cloud storage.
-Making the project hybrid i.e. can be used for offline programs and as well as for online websites as well.
-UI Tweaks














