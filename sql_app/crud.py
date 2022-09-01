from sqlalchemy.orm import Session

from . import models, schemas



# Получение данных из таблицы mopdi_data по номеру истории болезни (поле - numberib)
def get_patient_on_numberib(db: Session, patient_numberib: str):
	return db.query(models.Patient).filter(models.Patient.numberib == patient_numberib).first()


# Получение из таблицы mopdi_data всех записей по лечащему врачу (поле - tekotd)
def get_patients_on_tekotd(db: Session, tekotd: str):
	return db.query(models.Patient).filter(models.Patient.tekotd == tekotd).all()


# Проверка наличия пациента с такой же историей болезни
def create_patient_by_numberib(db: Session, numberib: str):
	return db.query(models.Patient).filter(models.Patient.numberib == numberib).first()

# Добавление записей в таблицу mopdi_data	
def create_patient(db: Session, patient: schemas.PatientCreate):
	db_patient = models.Patient(
		fio=patient.fio,
		age=patient.age,
		numberib=patient.numberib,
		run_dt=patient.run_dt,
		gr1=patient.gr1,
		gr=patient.gr,
		name=patient.name,
		col1=patient.col1,
		col2=patient.col2,
		col3=patient.col3,
		tek=patient.tek,
		tekotd=patient.tekotd,
		vr=patient.vr,
		vrotd=patient.vrotd,
		col4=patient.col4,
		refer=patient.refer,
		control=patient.control,
		current=patient.current
		)
		
	db.add(db_patient)
	db.commit()
	db.refresh(db_patient)
	return db_patient
