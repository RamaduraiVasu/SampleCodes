from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = r"sqlite:///......./emp.db"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Employee(Base):
    __tablename__ = "employee"

    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String)
    emp_age = Column(Integer)
    emp_gender = Column(String)
    emp_dept = Column(String)
    emp_salary = Column(Float)

    def __repr__(self):
        return f"{self.emp_id} {self.emp_name} {self.emp_dept}"

Base.metadata.create_all(engine)
new_emp = Employee(
    emp_id=3,
    emp_name="Ravi",
    emp_age=30,
    emp_gender="Male",
    emp_dept="IT",
    emp_salary=50000
)

session.add(new_emp)
session.commit()


employees = session.query(Employee).all()
print(employees)
for emp in employees:
    print(emp.emp_id, emp.emp_name, emp.emp_salary)

