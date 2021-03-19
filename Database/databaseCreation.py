from cassandra.auth import PlainTextAuthProvider
import config as cfg
from cassandra.query import BatchStatement, SimpleStatement
from prettytable import PrettyTable
import time
import ssl
import cassandra
from cassandra.cluster import Cluster
from cassandra.policies import *
from ssl import PROTOCOL_TLSv1_2, SSLContext, CERT_NONE
from requests.utils import DEFAULT_CA_BUNDLE_PATH

def PrintTable(rows):
    t=[]
    for r in rows:
        print(r)

#<authenticateAndConnect>
ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.verify_mode = CERT_NONE
auth_provider = PlainTextAuthProvider(username=cfg.config['username'], password=cfg.config['password'])
cluster = Cluster([cfg.config['contactPoint']], port = cfg.config['port'], auth_provider=auth_provider,ssl_context=ssl_context)
session = cluster.connect()
#</authenticateAndConnect>

#<createKeyspace>
print ("\nCreating Keyspace")
session.execute('CREATE KEYSPACE IF NOT EXISTS miniproj WITH replication = {\'class\': \'NetworkTopologyStrategy\', \'datacenter\' : \'1\' }')
#</createKeyspace>

#<createTable>
print ("\nCreating Table")
session.execute('CREATE TABLE IF NOT EXISTS miniproj.students (student_id int PRIMARY KEY, student_name text, password text, year text)')
#</createTable>

#<insertData>
session.execute("INSERT INTO  miniproj.students  (student_id, student_name , password, year) VALUES (%s,%s,%s,%s)", [1,'Lybkov','password', 'First'])
session.execute("INSERT INTO  miniproj.students  (student_id, student_name , password, year) VALUES (%s,%s,%s,%s)", [2,'Doniv','abcd1234', 'Second'])
session.execute("INSERT INTO  miniproj.students  (student_id, student_name , password, year) VALUES (%s,%s,%s,%s)", [3,'Keviv','hello@123', 'Final'])
session.execute("INSERT INTO  miniproj.students  (student_id, student_name , password, year) VALUES (%s,%s,%s,%s)", [4,'Ehtevs','qmul@789', 'First'])
session.execute("INSERT INTO  miniproj.students  (student_id, student_name , password, year) VALUES (%s,%s,%s,%s)", [5,'Dnivog','hello@456', 'Final'])
session.execute("INSERT INTO  miniproj.students  (student_id, student_name , password, year) VALUES (%s,%s,%s,%s)", [6,'Ateegk','qmul@197!', 'Second'])
session.execute("INSERT INTO  miniproj.students  (student_id, student_name , password, year) VALUES (%s,%s,%s,%s)", [7,'KannabbuS','password@123', 'Second'])
#</insertData>

print ("\nCreating Table")
session.execute('CREATE TABLE IF NOT EXISTS miniproj.teachers (teacher_id int PRIMARY KEY, teacher_name text, password text, subject_id int)')
#</createTable>

#<insertData>
session.execute("INSERT INTO  miniproj.teachers  (teacher_id, teacher_name , password, subject_id) VALUES (%s,%s,%s,%s)", [100,'Lybkov','teacher@123',1000])
session.execute("INSERT INTO  miniproj.teachers  (teacher_id, teacher_name , password, subject_id) VALUES (%s,%s,%s,%s)", [101,'Doniv','newteacher@123',1001])
session.execute("INSERT INTO  miniproj.teachers  (teacher_id, teacher_name , password, subject_id) VALUES (%s,%s,%s,%s)", [102,'Keviv','oldteacher@123',1002])
#</insertData>
print ("\nCreating Table")
session.execute('CREATE TABLE IF NOT EXISTS miniproj.subjects (subject_id int PRIMARY KEY, subject_name text, year text, time text)')
#</createTable>

#<insertData>
session.execute("INSERT INTO  miniproj.subjects  (subject_id, subject_name , year, time) VALUES (%s,%s,%s,%s)", [1000,'Maths','First', '10 AM'])
session.execute("INSERT INTO  miniproj.subjects  (subject_id, subject_name , year, time) VALUES (%s,%s,%s,%s)", [1001,'Science','Second', '11 AM'])
session.execute("INSERT INTO  miniproj.subjects  (subject_id, subject_name , year, time) VALUES (%s,%s,%s,%s)", [1002,'History','Final', '12 PM'])


print ("\nCreating Table")
session.execute('CREATE TABLE IF NOT EXISTS miniproj.admins (admin_id int PRIMARY KEY, admin_name text, password text)')
#</createTable>

#<insertData>
session.execute("INSERT INTO  miniproj.admins  (admin_id, admin_name , password) VALUES (%s,%s,%s)", [10000,'Admin','admin@123'])
#</insertData>

#<queryAllItems>
print ("\nSelecting All")
rows = session.execute('SELECT * FROM miniproj.students')
PrintTable(rows)
#</queryAllItems>


#<queryAllItems>
print ("\nSelecting All")
rows = session.execute('SELECT * FROM miniproj.subjects')
PrintTable(rows)
#</queryAllItems>


#<queryAllItems>
print ("\nSelecting All")
rows = session.execute('SELECT * FROM miniproj.teachers')
PrintTable(rows)
#</queryAllItems>


#<queryAllItems>
print ("\nSelecting All")
rows = session.execute('SELECT * FROM miniproj.admins')
PrintTable(rows)
#</queryAllItems>

#<queryByID>
print ("\nSelecting Id=1")
rows = session.execute('SELECT * FROM miniproj.students where student_id=1')
PrintTable(rows)
#</queryByID>

cluster.shutdown()
