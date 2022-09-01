from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine



models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


# Получение данных из таблицы mopdi_data по номеру истории болезни (поле - numberib)
@app.get('/patients/{patient_numberib}', response_model=schemas.Patient)
def read_patient_on_numberib(patient_numberib: str, db: Session = Depends(get_db)):
	db_patient = crud.get_patient_on_numberib(db, patient_numberib=patient_numberib)

	if db_patient is None:
		raise HTTPException(status_code=404, detail="Patient not found")

	return db_patient


# Получение из таблицы mopdi_data всех записей по лечащему врачу (поле - tekotd)
@app.get('/patients/tekotd/{tekotd}', response_model=list[schemas.Patient])
def read_patients_on_tekotd(tekotd: str, db: Session = Depends(get_db)):
	tekotd_patients = crud.get_patients_on_tekotd(db, tekotd=tekotd)

	if not tekotd_patients:
		raise HTTPException(status_code=404, detail='Tekotd patients not found')

	return tekotd_patients


# Обновление данных таблицы (полей refer - референсная граница, control - граница контроля,
# vr - врач) по выбранному номеру истории болезни (поле - numberib)
@app.put('/patients/update_patient/{patient_numberib}', response_model=schemas.Patient)
def update_patient_rcv(patient_numberib: str, refer: int, control: int, vr: str, db: Session = Depends(get_db)):
	db_patient = crud.get_patient_on_numberib(db, patient_numberib=patient_numberib)

	if db_patient is None:
		raise HTTPException(status_code=404, detail="Patient not found")

	setattr(db_patient, 'refer', refer)
	setattr(db_patient, 'control', control)
	setattr(db_patient, 'vr', vr)
	db.commit()

	return db_patient


# Проверка наличия пациента с такой же историей болезни и добавление записей в таблицу mopdi_data
@app.post('/patients/create', response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
	db_patient = crud.create_patient_by_numberib(db, numberib=patient.numberib)

	if db_patient:
		raise HTTPException(status_code=400, detail='Such number ib already registered')

	return crud.create_patient(db=db, patient=patient)
