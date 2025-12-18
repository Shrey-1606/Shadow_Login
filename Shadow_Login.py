
import tkinter as tk
from PIL import Image,ImageTk
from Encryption_Module import * 
import ast

#----------------Some necessary variables------------------

cred_dict={}
cred_keys={}
admin_users=[]
#----------------------------------------------------------

#----------------------------------------------------------
#------------------------Login Page------------------------
#----------------------------------------------------------

def login_page():
    global username_entry
    global password_entry
    for widget in img_l.winfo_children():
        widget.destroy()
    title = tk.Label(
                        img_l, 
                        text="Welcome to Shadow_Login",
                        font=("Arial", 26, "bold"),
                        fg="white",
                        bg="#0A0F1A"
                        )
    title.place(relx=0.5, rely=0.5, anchor="center", y=-120)
    username=tk.Label(img_l,
                      text="Enter Your Username: ",
                      font=("Arial", 15),
                      bg="#0A0F1A",
                      fg="#CCCCCC")
    username.place(relx=0.5, rely=0.5, anchor="center", y=-60)
    username_entry=tk.Entry(img_l,
                      width=30,
                      font=("Arial", 15),
                      bg="#0A0F1A",
                      fg="#CCCCCC",
                      relief="flat",
                      border=0,
                      insertbackground="white")
    username_entry.place(relx=0.5, rely=0.5, anchor="center", y=-30)
    password = tk.Label(img_l,
                      text="Enter Your Password: ",
                      font=("Arial", 15),
                      bg="#0A0F1A",
                      fg="#CCCCCC")
    password.place(relx=0.5, rely=0.5, anchor="center", y=+30)
    password_entry = tk.Entry(
                        img_l,
                    width=30,
                    font=("Arial", 15),
                    bg="#0A0F1A",
                    fg="#CCCCCC",
                    relief="flat",
                    border=0,
                    insertbackground="white",
                    show="*")
    password_entry.place(relx=0.5, rely=0.5, anchor="center", y=+60)

    change_pass_btn = tk.Button(
            img_l,
            text="Change Password",
            font=("Arial", 14, "bold"),
            bg="#0B1A3A",
            fg="white",
            command=change_password_page
        )
    change_pass_btn.place(relx=0.5, rely=0.5, anchor="center", y=300)


    login_btn=tk.Button(img_l,
                        text="LOGIN",
                        font=("Arial", 16, "bold"),
                        fg="white",
                        bg="#0B1A3A",
                        activebackground="#132852",
                        activeforeground="white",
                        relief="flat",
                        padx=20,
                        pady=10,
                        command=check_cred
                        )
    login_btn.place(relx=0.5, rely=0.5, anchor="center", y=200)
    create_acc_btn=tk.Button(img_l,
                        text="Create Account",
                        font=("Arial", 12, "bold"),
                        fg="white",
                        bg="#0B1A3A",
                        activebackground="#132852",
                        activeforeground="white",
                        relief="flat",
                        padx=10,
                        pady=5,
                        command=create_acc)
    create_acc_btn.place(relx=0.5, rely=0.5, anchor="center", y=110)

def check_cred(): 
    global user_store_check
    success = False

    user_store_check = username_entry.get().strip()
    pass_store_check = password_entry.get()

  
    if user_store_check == "":
        for widget in img_l.winfo_children():
            widget.destroy()

        empty_user = tk.Label(
            img_l,
            text="Username cannot be empty",
            font=("Arial", 30, "bold"),
            fg="#FF1A1A",
            bg="#0A0F1A"
        )
        empty_user.place(relx=0.5, rely=0.5, anchor="center")

        root.after(3000, login_page)
        return

    
    if user_store_check not in cred_dict:
        for widget in img_l.winfo_children():
            widget.destroy()

        user_not_exist = tk.Label(
            img_l, 
            text="Username doesn't exist\nRedirecting to Create account page",
            font=("Arial", 30, "bold"),
            fg="white",
            bg="#0A0F1A"
        )
        user_not_exist.place(relx=0.5, rely=0.5, anchor="center")
        root.after(3000, create_acc)
        return


    for check_user in cred_dict: 
        check_pass_encyp = cred_dict[check_user]
        keys_pass = cred_keys[check_user]
        check_pass = decrypt_text(check_pass_encyp, keys_pass)

        if user_store_check == check_user and pass_store_check == check_pass: 
            success = True
            break

    if success: 
        log_success()
    else: 
        log_unsuccess()


def log_success():
    for widget in img_l.winfo_children():
        widget.destroy()
    if user_store_check in admin_users: 
        
        admin_success= tk.Label(
                        img_l, 
                        text="Redirecting to Admin Page",
                        font=("Arial", 35, "bold"),
                        fg="white",
                        bg="#0A0F1A"
                        )
        admin_success.place(relx=0.5, rely=0.5, anchor="center")
        root.after(3000, admin_home)
        admin_content()
    else:
        title = tk.Label(
        img_l, 
        text="Login Successful!",
        font=("Arial", 35, "bold"),
        fg="white",
        bg="#0A0F1A"
        )
        title.place(relx=0.5, rely=0.5, anchor="center")
        logout_btn=tk.Button(img_l,
                            text="LOGOUT",
                            font=("Arial", 16, "bold"),
                            fg="white",
                            bg="#0B1A3A",
                            activebackground="#132852",
                            activeforeground="white",
                            relief="flat",
                            padx=20,
                            pady=10,
                            command=login_page)
        logout_btn.place(relx=0.5,rely=0.5,anchor="center",y=300)



def log_unsuccess(): 
    for widget in img_l.winfo_children():
        widget.destroy()
    title = tk.Label(
    img_l, 
    text="Please Check Your Password",
    font=("Arial", 25, "bold"),
    fg="#FF1A1A",
    bg="#0A0F1A"
    )
    title.place(relx=0.5, rely=0.5, anchor="center")
    root.after(3000, login_page) 

#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------


#----------------------------------------------------------
#----------------------Admin Page--------------------------
#----------------------------------------------------------
def admin_home(): 
    for widget in img_l.winfo_children():
        widget.destroy()
    title = tk.Label(
                        img_l, 
                        text="Welcome to Admin_Page",
                        font=("Arial", 26, "bold"),
                        fg="white",
                        bg="#0A0F1A"
                        )
    title.place(relx=0.5, rely=0.5, anchor="center", y=-100)
    log_disp = tk.Label(
                        img_l, 
                        text=log_data,
                        font=("Arial", 14, "bold"),
                        fg="white",
                        bg="#0A0F1A",
                        anchor="nw",
                        justify="left"
                        )
    log_disp.place(relx=0.5,rely=0.5, anchor="nw", x=-500,y=-50)
    back_login_btn=tk.Button(img_l,
                        text="< Back To Login",
                        font=("Arial", 10, "bold"),
                        fg="white",
                        bg="#0B1A3A",
                        activebackground="#132852",
                        activeforeground="white",
                        relief="flat",
                        padx=20,
                        pady=10,
                        command=login_page)
    back_login_btn.place(relx=0.5,rely=0.5,anchor="center",x=-300,y=-250)
    add_user_btn=tk.Button(img_l,
                        text="Add Admin >",
                        font=("Arial", 10, "bold"),
                        fg="white",
                        bg="#0B1A3A",
                        activebackground="#132852",
                        activeforeground="white",
                        relief="flat",
                        padx=20,
                        pady=10,
                        command=add_admin)
    add_user_btn.place(relx=0.5,rely=0.5,anchor="center",x=300,y=-250)
    del_user_btn=tk.Button(img_l,
                        text="Delete User",
                        font=("Arial", 10, "bold"),
                        fg="white",
                        bg="#0B1A3A",
                        activebackground="#132852",
                        activeforeground="white",
                        relief="flat",
                        padx=20,
                        pady=10,
                        command=del_user)
    del_user_btn.place(relx=0.5,rely=0.5,anchor="center",y=-250)

def admin_usernames():
    admin_users.clear()

    # Create file if it doesn't exist
    try:
        file = open("admin_users.txt", "r", encoding="utf-8")
    except FileNotFoundError:
        open("admin_users.txt", "w", encoding="utf-8").close()
        return

    for lines in file:
        line = lines.strip()
        if line:
            admin_users.append(line)

    admin_username_label()


def admin_username_label(): 
    global admin_username_text,admin_users
    admin_username_text="List of Admins: \n"
    admin_username_text+="\n".join(admin_users)

def add_admin(): 
    global username_entry_add
    global password_entry_add
    for widget in img_l.winfo_children():
        widget.destroy()
    title = tk.Label(
                        img_l, 
                        text="Add Admins",
                        font=("Arial", 26, "bold"),
                        fg="white",
                        bg="#0A0F1A"
                        )
    title.place(relx=0.5, rely=0.5, anchor="center", y=-100)
    log_disp = tk.Label(
                        img_l, 
                        text=username,
                        font=("Arial", 14, "bold"),
                        fg="white",
                        bg="#0A0F1A",
                        anchor="nw",
                        justify="left"
                        )
    log_disp.place(relx=0.5,rely=0.5, anchor="nw", x=-500,y=-50)
    log_admin_disp = tk.Label(
                        img_l, 
                        text=admin_username_text,
                        font=("Arial", 14, "bold"),
                        fg="white",
                        bg="#0A0F1A",
                        anchor="nw",
                        justify="left"
                        )
    log_admin_disp.place(relx=0.5,rely=0.5, anchor="nw",x=-150,y=-50)
    username_add_admin=tk.Label(img_l,
                      text="Enter Desired Username: ",
                      font=("Arial", 15),
                      bg="#0A0F1A",
                      fg="#CCCCCC")
    username_add_admin.place(relx=0.5, rely=0.5, anchor="center",x=300, y=-60)
    username_entry_add=tk.Entry(img_l,
                      width=30,
                      font=("Arial", 15),
                      bg="#0A0F1A",
                      fg="#CCCCCC",
                      relief="flat",
                      border=0,
                      insertbackground="white")
    username_entry_add.place(relx=0.5, rely=0.5, anchor="center", x=300,y=-30)
    password_add= tk.Label(img_l,
                      text="Enter The Password: ",
                      font=("Arial", 15),
                      bg="#0A0F1A",
                      fg="#CCCCCC")
    password_add.place(relx=0.5, rely=0.5, anchor="center", x=300,y=+30)
    password_entry_add = tk.Entry(
                        img_l,
                    width=30,
                    font=("Arial", 15),
                    bg="#0A0F1A",
                    fg="#CCCCCC",
                    relief="flat",
                    border=0,
                    insertbackground="white",
                    show="*")
    password_entry_add.place(relx=0.5, rely=0.5, anchor="center",x=300, y=+60)
    add_admin_login=tk.Button(img_l,
                        text="Add Admin >",
                        font=("Arial", 10, "bold"),
                        fg="white",
                        bg="#0B1A3A",
                        activebackground="#132852",
                        activeforeground="white",
                        relief="flat",
                        padx=20,
                        pady=10,
                        command=check_cred_add)
    add_admin_login.place(relx=0.5,rely=0.5,anchor="center",x=300,y=100)
    back_admin_btn=tk.Button(img_l,
                        text="< Back To Admin Page",
                        font=("Arial", 10, "bold"),
                        fg="white",
                        bg="#0B1A3A",
                        activebackground="#132852",
                        activeforeground="white",
                        relief="flat",
                        padx=20,
                        pady=10,
                        command=admin_home)
    back_admin_btn.place(relx=0.5,rely=0.5,anchor="center",x=-300,y=-250)

def del_user(): 
    global username_entry_del
    global password_entry_del
    for widget in img_l.winfo_children():
        widget.destroy()
    title = tk.Label(
                        img_l, 
                        text="Delete Users",
                        font=("Arial", 26, "bold"),
                        fg="white",
                        bg="#0A0F1A"
                        )
    title.place(relx=0.5, rely=0.5, anchor="center", y=-100)
    log_disp = tk.Label(
                        img_l, 
                        text=username,
                        font=("Arial", 14, "bold"),
                        fg="white",
                        bg="#0A0F1A",
                        anchor="nw",
                        justify="left"
                        )
    log_disp.place(relx=0.5,rely=0.5, anchor="nw", x=-500,y=-50)
    username_del_lbl=tk.Label(img_l,
                      text="Enter Desired Username to delete: ",
                      font=("Arial", 15),
                      bg="#0A0F1A",
                      fg="#CCCCCC")
    username_del_lbl.place(relx=0.5, rely=0.5, anchor="center",x=300, y=-60)
    username_entry_del=tk.Entry(img_l,
                      width=30,
                      font=("Arial", 15),
                      bg="#0A0F1A",
                      fg="#CCCCCC",
                      relief="flat",
                      border=0,
                      insertbackground="white")
    username_entry_del.place(relx=0.5, rely=0.5, anchor="center", x=300,y=-30)
    password_del_lbl= tk.Label(img_l,
                      text="Enter The Password: ",
                      font=("Arial", 15),
                      bg="#0A0F1A",
                      fg="#CCCCCC")
    password_del_lbl.place(relx=0.5, rely=0.5, anchor="center", x=300,y=+30)
    password_entry_del = tk.Entry(
                        img_l,
                    width=30,
                    font=("Arial", 15),
                    bg="#0A0F1A",
                    fg="#CCCCCC",
                    relief="flat",
                    border=0,
                    insertbackground="white",
                    show="*")
    password_entry_del.place(relx=0.5, rely=0.5, anchor="center",x=300, y=+60)
    del_user_login=tk.Button(img_l,
                        text="Delete User",
                        font=("Arial", 10, "bold"),
                        fg="white",
                        bg="#0B1A3A",
                        activebackground="#132852",
                        activeforeground="white",
                        relief="flat",
                        padx=20,
                        pady=10,
                        command=delete_user)
    del_user_login.place(relx=0.5,rely=0.5,anchor="center",x=300,y=100)
    back_admin_btn=tk.Button(img_l,
                        text="< Back To Admin Page",
                        font=("Arial", 10, "bold"),
                        fg="white",
                        bg="#0B1A3A",
                        activebackground="#132852",
                        activeforeground="white",
                        relief="flat",
                        padx=20,
                        pady=10,
                        command=admin_home)
    back_admin_btn.place(relx=0.5,rely=0.5,anchor="center",x=-300,y=-250)

def admin_content(): 
    global log_data
    file=open("cred_store.txt","r",encoding="utf-8")
    file.readline()
    log_data=""
    for lines in file: 
        log_data+=f"{lines}\n"

def check_cred_add(): 
    user_store_check = username_entry_add.get()
    pass_store_check = password_entry_add.get()
    success=False
    flag=0
    if user_store_check not in cred_dict: 
        flag=1
        if user_store_check == "" : 
            add_admin()
        else:
            for widget in img_l.winfo_children():
                widget.destroy()
            user_not_exist = tk.Label(
            img_l, 
            text="Username doesn't exist",
            font=("Arial", 30, "bold"),
            fg="white",
            bg="#0A0F1A"
            )
            user_not_exist.place(relx=0.5, rely=0.5, anchor="center")
            root.after(3000, admin_home)
    elif user_store_check in admin_users: 
            for widget in img_l.winfo_children():
                widget.destroy()
            admin_exists = tk.Label(
                                    img_l, 
                                    text="Admin Already Added",
                                    font=("Arial", 30, "bold"),
                                    fg="white",
                                    bg="#0A0F1A"
                                    )
            admin_exists.place(relx=0.5, rely=0.5, anchor="center")
            root.after(3000, admin_home)
            return None
    else:
        for check_user in cred_dict: 
            check_pass_encyp=cred_dict[check_user]
            keys_pass=cred_keys[check_user]
            check_pass=decrypt_text(check_pass_encyp,keys_pass)
            if str(user_store_check)==check_user and str(pass_store_check)==check_pass: 
                success=True
                break
    if success and flag ==0: 
        cred_admin = open("admin_users.txt","a",encoding="utf-8")
        cred_admin.seek(0,2)
        cred_admin.write("\n"+f"{user_store_check}")
        cred_admin.close()
        admin_usernames()
        for widget in img_l.winfo_children():
            widget.destroy()

        admin_success= tk.Label(
                            img_l, 
                            text="Added an Admin",
                            font=("Arial", 35, "bold"),
                            fg="white",
                            bg="#0A0F1A"
                            )  
        admin_success.place(relx=0.5, rely=0.5, anchor="center")
        root.after(3000,admin_home)  
    elif not success and flag==0 : 
        log_unsuccess()

def check_cred_del(): 
    user_store_check = username_entry_del.get()
    pass_store_check = password_entry_del.get()
    success=False
    flag=0
    if user_store_check not in cred_dict: 
        flag=1
        if user_store_check == "" : 
            add_admin()
        else:
            for widget in img_l.winfo_children():
                widget.destroy()
            user_not_exist = tk.Label(
            img_l, 
            text="Username doesn't exist",
            font=("Arial", 30, "bold"),
            fg="white",
            bg="#0A0F1A"
            )
            user_not_exist.place(relx=0.5, rely=0.5, anchor="center")
            root.after(3000, admin_home)
    elif user_store_check in admin_users: 
            for check_user in cred_dict: 
                check_pass_encyp=cred_dict[check_user]
                keys_pass=cred_keys[check_user]
                check_pass=decrypt_text(check_pass_encyp,keys_pass)
                if str(user_store_check)==check_user and str(pass_store_check)==check_pass: 
                    success=True
    if success and flag==0: 
        cred_admin = open("admin_users.txt","a",encoding="utf-8")
        cred_admin.seek(0,2)
        cred_admin.write("\n"+f"{user_store_check}")
        cred_admin.close()
        
        for widget in img_l.winfo_children():
            widget.destroy()
        admin_success= tk.Label(
                            img_l, 
                            text="Added an Admin",
                            font=("Arial", 35, "bold"),
                            fg="white",
                            bg="#0A0F1A"
                            )  
        admin_success.place(relx=0.5, rely=0.5, anchor="center")
        root.after(3000,admin_home)  
    elif not success and flag==0: 
        log_unsuccess()

def delete_user():
    global cred_dict, cred_keys, admin_users

    user_store_check = username_entry_del.get()
    pass_store_check = password_entry_del.get()
    success = False

    # User existence check
    if user_store_check not in cred_dict:
        for widget in img_l.winfo_children():
            widget.destroy()
        lbl = tk.Label(
            img_l,
            text="Username doesn't exist",
            font=("Arial", 30, "bold"),
            fg="white",
            bg="#0A0F1A"
        )
        lbl.place(relx=0.5, rely=0.5, anchor="center")
        root.after(3000, admin_home)
        return

    # Admin protection
    if user_store_check in admin_users:
        for widget in img_l.winfo_children():
            widget.destroy()
        lbl = tk.Label(
            img_l,
            text="Admin accounts cannot be deleted",
            font=("Arial", 30, "bold"),
            fg="#FF1A1A",
            bg="#0A0F1A"
        )
        lbl.place(relx=0.5, rely=0.5, anchor="center")
        root.after(3000, admin_home)
        return

    # Password verification
    check_pass_encyp = cred_dict[user_store_check]
    keys_pass = cred_keys[user_store_check]
    check_pass = decrypt_text(check_pass_encyp, keys_pass)

    if str(pass_store_check) == str(check_pass):
        success = True

    if not success:
        log_unsuccess()
        return

    # Remove user from cred_store.txt
    with open("cred_store.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open("cred_store.txt", "w", encoding="utf-8") as f:
        for line in lines:
            if not line.startswith(user_store_check + "⟡"):
                f.write(line)

    # Remove user from cred_keys.txt
    with open("cred_keys.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open("cred_keys.txt", "w", encoding="utf-8") as f:
        for line in lines:
            if not line.startswith(user_store_check + "⟡"):
                f.write(line)

    # Refresh dictionaries
    store_dict()

    # Success screen
    for widget in img_l.winfo_children():
        widget.destroy()

    lbl = tk.Label(
        img_l,
        text="User Deleted Successfully",
        font=("Arial", 35, "bold"),
        fg="white",
        bg="#0A0F1A"
    )
    lbl.place(relx=0.5, rely=0.5, anchor="center")

    root.after(3000, admin_home)


    
#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------


#----------------------------------------------------------
#---------------------Storage Units------------------------
#----------------------------------------------------------

def store_secret():
    cred_key = open("cred_keys.txt","a",encoding="utf-8")
    cred_key.seek(0,2)
    cred_key.write("\n"+f"{user_store}⟡{sec_key}")

def store_cred(): 
    cred = open("cred_store.txt","a",encoding="utf-8")
    cred.seek(0,2)
    cred.write("\n"+f"{user_store}⟡{encrypted}")

def get_cred():
    global user_store, encrypted, sec_key

    user_store = username_entry_create.get()
    raw_pass = password_entry_create.get()

    encrypted, sec_key = encrypt_text(raw_pass)

    store_cred()
    store_secret()
    store_dict()

    # 🔥 AUTO MAKE FIRST USER ADMIN
    make_admin_if_first_user(user_store)


def store_dict(): 
    global username
    cred_dict.clear()
    cred_keys.clear()

    with open("cred_store.txt","r",encoding="utf-8") as check_file:
        check_file.readline()
        for line in check_file:
            line = line.strip()
            if "⟡" not in line:
                continue
            x = line.split("⟡")
            cred_dict[x[0]] = x[1]

    with open("cred_keys.txt","r",encoding="utf-8") as check_keys:
        check_keys.readline()
        for secrets in check_keys:
            secrets = secrets.strip()
            if "⟡" not in secrets:
                continue
            x_1 = secrets.split("⟡")
            cred_keys[x_1[0]] = ast.literal_eval(x_1[1])

    username = "List of Usernames: \n"
    for usernames in cred_dict:
        username += f"{usernames}\n"


#DEL USER

#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------


#----------------------------------------------------------
#----------------------Account Creation--------------------
#----------------------------------------------------------

def create_acc():
    global username_entry_create
    global password_entry_create
    global password_entry_create_2

    for widget in img_l.winfo_children():
        widget.destroy()

    title = tk.Label(
                        img_l, 
                        text="Create Account",
                        font=("Arial", 26, "bold"),
                        fg="white",
                        bg="#0A0F1A"
                        )
    title.place(relx=0.5, rely=0.5, anchor="center", y=-120)
    username=tk.Label(img_l,
                      text="Enter Your Username: ",
                      font=("Arial", 15),
                      bg="#0A0F1A",
                      fg="#CCCCCC")
    username.place(relx=0.5, rely=0.5, anchor="center", y=-60)
    username_entry_create=tk.Entry(img_l,
                      width=30,
                      font=("Arial", 15),
                      bg="#0A0F1A",
                      fg="#CCCCCC",
                      relief="flat",
                      border=0,
                      insertbackground="white")
    username_entry_create.place(relx=0.5, rely=0.5, anchor="center", y=-30)
    password = tk.Label(img_l,
                      text="Enter Your Password: ",
                      font=("Arial", 15),
                      bg="#0A0F1A",
                      fg="#CCCCCC")
    password.place(relx=0.5, rely=0.5, anchor="center", y=+30)
    password_entry_create = tk.Entry(
                        img_l,
                    width=30,
                    font=("Arial", 15),
                    bg="#0A0F1A",
                    fg="#CCCCCC",
                    relief="flat",
                    border=0,
                    insertbackground="white",
                    show="*")
    password_entry_create.place(relx=0.5, rely=0.5, anchor="center", y=+60)
    password_2= tk.Label(img_l,
                      text="Confirm Your Password: ",
                      font=("Arial", 15),
                      bg="#0A0F1A",
                      fg="#CCCCCC")
    password_2.place(relx=0.5, rely=0.5, anchor="center", y=+100)
    password_entry_create_2 = tk.Entry(
                        img_l,
                    width=30,
                    font=("Arial", 15),
                    bg="#0A0F1A",
                    fg="#CCCCCC",
                    relief="flat",
                    border=0,
                    insertbackground="white",
                    show="*")
    password_entry_create_2.place(relx=0.5, rely=0.5, anchor="center", y=+130)
    create_btn=tk.Button(img_l,
                        text="CREATE",
                        font=("Arial", 16, "bold"),
                        fg="white",
                        bg="#0B1A3A",
                        activebackground="#132852",
                        activeforeground="white",
                        relief="flat",
                        padx=20,
                        pady=10,
                        command=username_exists)
    create_btn.place(relx=0.5,rely=0.5,anchor="center",y=300)
    back_login_btn=tk.Button(img_l,
                        text="< Back To Login",
                        font=("Arial", 10, "bold"),
                        fg="white",
                        bg="#0B1A3A",
                        activebackground="#132852",
                        activeforeground="white",
                        relief="flat",
                        padx=20,
                        pady=10,
                        command=login_page)
    back_login_btn.place(relx=0.5,rely=0.5,anchor="center",x=-300,y=-250)
    password_type= tk.Label(img_l,
                      text="-Password must have a character from a-z\n-Password must have an uppercase letter\n-Password must contain a number\n-Password must have a special character among these !@#$*|,.\n-Use of any other character than mentioned is prohibited",
                      anchor="w",
                      justify="left",
                      font=("Arial", 13),
                      bg="#0A0F1A",
                      fg="#A17DFB")
    password_type.place(relx=0.5, rely=0.5,anchor="center", y=+200)

def username_exists():
    if username_entry_create.get() in cred_dict: 
        for widget in img_l.winfo_children():
            widget.destroy()
        title = tk.Label(
        img_l, 
        text="Username Already Exists\nRedirecting to Login",
        font=("Arial", 25, "bold"),
        fg="#FF1A1A",
        bg="#0A0F1A"
        )
        title.place(relx=0.5, rely=0.5, anchor="center")
        root.after(3000, login_page)
    else:
        check_confirm()

def check_confirm(): 
    if password_entry_create.get()==password_entry_create_2.get(): 
        password_strength()
    else: 
        pass_no_match()

def password_strength(): 
    global count 
    sp_ch=set("!@#$*|,.")
    number=set("0123456789")
    flag1=0
    flag2=0
    flag3=0
    flag4=0
    blackflag=0

    for char in password_entry_create.get(): 
        char=str(char)
        if char.islower(): 
            flag1=1
        elif char.isupper(): 
            flag2=1
        elif char in number: 
            flag3=1
        elif char in sp_ch: 
            flag4=1
        else: 
            blackflag=1
    if blackflag==1: 
        invalid_ch()
    else: 
        count = flag1+flag2+flag3+flag4
        if count <4: 
            pw_label()
        else: 
            get_cred()
            strength_pass()

def pass_no_match(): 
    for widget in img_l.winfo_children():
        widget.destroy()
    pass_no = tk.Label(
    img_l, 
    text="Account Creation Unsuccessful\nPasswords don't match",
    font=("Arial", 30, "bold"),
    fg="#FF1A1A",
    bg="#0A0F1A"
    )
    pass_no.place(relx=0.5, rely=0.5, anchor="center")
    root.after(3000, create_acc)

def strength_pass(): 
        for widget in img_l.winfo_children():
            widget.destroy()

        title = tk.Label(
        img_l, 
        text="Account Created Successfully!",
        font=("Arial", 30, "bold"),
        fg="white",
        bg="#0A0F1A"
        )
        title.place(relx=0.5, rely=0.5, anchor="center")
        root.after(3000, login_page)

def pw_label(): 
    for widget in img_l.winfo_children():
        widget.destroy()
    if count == 1: 
        title = tk.Label(
        img_l, 
        text="Password is very weak\nFollow instructions given for Password",
        font=("Arial", 25, "bold"),
        fg="white",
        bg="#0A0F1A"
        )
        title.place(relx=0.5, rely=0.5, anchor="center")
        root.after(3000, create_acc)
    elif count == 2: 
        title = tk.Label(
        img_l, 
        text="Password is weak\nFollow instructions given for Password",
        font=("Arial", 25, "bold"),
        fg="white",
        bg="#0A0F1A"
        )
        title.place(relx=0.5, rely=0.5, anchor="center")
        root.after(3000, create_acc)
    elif count == 3: 
        title = tk.Label(
        img_l, 
        text="Password is of medium strength\nFollow instructions given for Password",
        font=("Arial", 25, "bold"),
        fg="white",
        bg="#0A0F1A"
        )
        title.place(relx=0.5, rely=0.5, anchor="center")
        root.after(3000, create_acc)
   
def invalid_ch(): 
    for widget in img_l.winfo_children():
        widget.destroy()
    invalid = tk.Label(
    img_l, 
    text="Account Creation Unsuccessful\nInvalid Characters in Password",
    font=("Arial", 30, "bold"),
    fg="#FF1A1A",
    bg="#0A0F1A"
    )
    invalid.place(relx=0.5, rely=0.5, anchor="center")
    root.after(3000, create_acc) 


def make_admin_if_first_user(username):
    if len(admin_users) == 0:
        with open("admin_users.txt", "a", encoding="utf-8") as f:
            f.write(username + "\n")
        admin_usernames()

def change_password_page():
    global old_pass_entry, new_pass_entry, new_pass_entry_2,username_123
    username_123=username_entry.get()
    for widget in img_l.winfo_children():
        widget.destroy()

    title = tk.Label(
        img_l,
        text="Change Password",
        font=("Arial", 26, "bold"),
        fg="white",
        bg="#0A0F1A"
    )
    title.place(relx=0.5, rely=0.5, anchor="center", y=-120)

    # Old password
    tk.Label(
        img_l,
        text="Enter Old Password:",
        font=("Arial", 15),
        bg="#0A0F1A",
        fg="#CCCCCC"
    ).place(relx=0.5, rely=0.5, anchor="center", y=-60)

    old_pass_entry = tk.Entry(
        img_l,
        width=30,
        font=("Arial", 15),
        bg="#0A0F1A",
        fg="#CCCCCC",
        relief="flat",
        border=0,
        insertbackground="white",
        show="*"
    )
    old_pass_entry.place(relx=0.5, rely=0.5, anchor="center", y=-30)

    # New password
    tk.Label(
        img_l,
        text="Enter New Password:",
        font=("Arial", 15),
        bg="#0A0F1A",
        fg="#CCCCCC"
    ).place(relx=0.5, rely=0.5, anchor="center", y=20)

    new_pass_entry = tk.Entry(
        img_l,
        width=30,
        font=("Arial", 15),
        bg="#0A0F1A",
        fg="#CCCCCC",
        relief="flat",
        border=0,
        insertbackground="white",
        show="*"
    )
    new_pass_entry.place(relx=0.5, rely=0.5, anchor="center", y=50)

    # Confirm password
    tk.Label(
        img_l,
        text="Confirm New Password:",
        font=("Arial", 15),
        bg="#0A0F1A",
        fg="#CCCCCC"
    ).place(relx=0.5, rely=0.5, anchor="center", y=100)

    new_pass_entry_2 = tk.Entry(
        img_l,
        width=30,
        font=("Arial", 15),
        bg="#0A0F1A",
        fg="#CCCCCC",
        relief="flat",
        border=0,
        insertbackground="white",
        show="*"
    )
    new_pass_entry_2.place(relx=0.5, rely=0.5, anchor="center", y=130)

    # Update button
    tk.Button(
        img_l,
        text="UPDATE PASSWORD",
        font=("Arial", 16, "bold"),
        fg="white",
        bg="#0B1A3A",
        activebackground="#132852",
        activeforeground="white",
        relief="flat",
        padx=20,
        pady=10,
        command=update_password
    ).place(relx=0.5, rely=0.5, anchor="center", y=200)

    # Back button
    tk.Button(
        img_l,
        text="< Back",
        font=("Arial", 10, "bold"),
        fg="white",
        bg="#0B1A3A",
        activebackground="#132852",
        activeforeground="white",
        relief="flat",
        padx=20,
        pady=10,
        command=login_page
    ).place(relx=0.5, rely=0.5, anchor="center", y=260)


def update_password():
    username = username_123
    old_pass = old_pass_entry.get()
    new_pass = new_pass_entry.get()
    confirm_pass = new_pass_entry_2.get()

    # Check old password
    enc_pass = cred_dict.get(username)
    key = cred_keys.get(username)
    real_pass = decrypt_text(enc_pass, key)

    if old_pass != real_pass:
        log_unsuccess()
        return

    if new_pass != confirm_pass:
        pass_no_match()
        return

    # Encrypt new password
    new_enc, new_key = encrypt_text(new_pass)

    # Update cred_store.txt
    with open("cred_store.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open("cred_store.txt", "w", encoding="utf-8") as f:
        for line in lines:
            if line.startswith(username + "⟡"):
                f.write(username + "⟡" + new_enc + "\n")
            else:
                f.write(line)

    # Update cred_keys.txt
    with open("cred_keys.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open("cred_keys.txt", "w", encoding="utf-8") as f:
        for line in lines:
            if line.startswith(username + "⟡"):
                f.write(username + "⟡" + str(new_key) + "\n")
            else:
                f.write(line)

    store_dict()

    for widget in img_l.winfo_children():
        widget.destroy()

    tk.Label(
        img_l,
        text="Password Updated Successfully",
        font=("Arial", 30, "bold"),
        fg="white",
        bg="#0A0F1A"
    ).place(relx=0.5, rely=0.5, anchor="center")

    root.after(3000, login_page)



#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------


#----------------------------------------------------------
#------Window Specification and Initiation of Program------
#----------------------------------------------------------
root = tk.Tk()
root.title("Shadow_Login")
root.minsize(1280,720)
root.geometry("1280x720+320+180")
img = Image.open("project_jack.jpg")
img = img.resize((1280,720),Image.LANCZOS)
usable_img=ImageTk.PhotoImage(img)
img_l=tk.Label(root,image=usable_img)
img_l.pack(fill="both", expand=True)
store_dict()
admin_usernames()
login_page()
root.mainloop()

#----------------------------------------------------------
#--------------------End of Program------------------------
#----------------------------------------------------------
