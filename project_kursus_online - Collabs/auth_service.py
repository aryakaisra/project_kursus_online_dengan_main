
from model.database import Session, User, ActivityLog

def login_user(username, role):
    session = Session()
    user = session.query(User).filter_by(username=username, role=role).first()
    if user:
        log = ActivityLog(username=username, action="login")
        session.add(log)
        session.commit()
        return True
    return False
