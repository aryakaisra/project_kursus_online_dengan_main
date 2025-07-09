from controller.main_controller import login_controller
from controller.activity_filter import tampilkan_login_siswa
from model.database import Session, User

def isi_data_awal():
    session = Session()
    if session.query(User).count() == 0:
        session.add_all([
            User(username="admin1", role="Admin"),
            User(username="instruktur_andi", role="Instruktur"),
            User(username="siswa_budi", role="Siswa"),
            User(username="siswa_citra", role="Siswa")
        ])
        session.commit()

def main():
    isi_data_awal()
    print("Selamat datang di Aplikasi Kursus Online")
    username = input("Masukkan username: ")
    role = input("Masukkan role (Admin/Instruktur/Siswa): ")
    login_controller(username, role)
    opsi = input("Tampilkan aktivitas login siswa? (y/n): ")
    if opsi.lower() == 'y':
        tampilkan_login_siswa()

if __name__ == "__main__":
    main()
