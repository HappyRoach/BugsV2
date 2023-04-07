import config as setting
import psycopg2
import psycopg2.extras

class Db:
    def __init__(self):
        self.connection = psycopg2.connect(user=setting.USER,
                                           password=setting.PASSWORD,
                                           host=setting.HOST,
                                           port=setting.PORT,
                                           database=setting.DB_NAME)
        self.connection.autocommit = True
        self.cur = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def insert_user(self, FullName, Date, Pose, CurretPose, OfficalPose, Email, DataWork, Region, phone, WorkTime, spec):
        self.cur.execute(
            """INSERT INTO survey (fullname, date_time, pose, curret_pose, offical_pose, phone, email, data_work, region, work_time, spec) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
            (FullName, Date, Pose, CurretPose, OfficalPose, Email, DataWork, Region, phone, WorkTime, spec)
        )
        return True

    def delete_user(self, id):
        self.cur.execute(
            """DELETE FROM survey WHERE id=%s;""",
            (id)
        )
        return True

    def select_all_user(self):
        self.cur.execute(
            """SELECT * FROM survey"""
        )
        return self.cur.fetchall()
