
from model.database import Session, ActivityLog

def tampilkan_login_siswa():
    session = Session()
    logs = session.query(ActivityLog).all()
    siswa_logs = list(filter(lambda x: x.username.startswith("siswa"), logs))
    ringkas = list(map(lambda x: f"{x.username} -> {x.action} @ {x.timestamp}", siswa_logs))

    for r in ringkas:
        print(r)
