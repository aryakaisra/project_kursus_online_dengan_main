
from service.auth_service import login_user

def login_controller(username, role):
    if login_user(username, role):
        print(f"{username} berhasil login sebagai {role}")
    else:
        print("Login gagal.")
