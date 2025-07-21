user=None

def update_logged_status(email):
    global user
    user=email

def check_log_status():
    if user is not None:
        return True

    return False



