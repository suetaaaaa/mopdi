from pydantic import BaseModel
from typing import Optional, Union

from datetime import time
from uuid import UUID



class PatientBase(BaseModel):
	fio: str
	age: str
	numberib: str
	run_dt: time
	gr1: str
	gr: str
	name: str
	col1: Optional[str]
	col2: Optional[str]
	col3: Optional[str]
	tek: str
	tekotd: str
	vr: str
	vrotd: str
	col4: Optional[str]
	refer: int
	control: int
	current: int

	class Config:
		schema_extra = {
			'example': {
				'fio': 'fio',
				'age': 'age',
				'numberib': 'numberib',
				'run_dt': '00:00:00+03:00',
				'gr1': 'gr1',
				'gr': 'gr',
				'name': 'name',
				'col1': 'NULL',
				'col2': 'NULL',
				'col3': 'NULL',
				'tek': 'tek',
				'tekotd': 'tekotd',
				'vr': 'vr',
				'vrotd': 'vrotd',
				'col4': 'NULL',
				'refer': 0,
				'control': 0,
				'current': 0
			}
		}



class PatientCreate(PatientBase):
	pass


class Patient(PatientBase):
	id: Union[int, str, UUID]

	class Config:
		orm_mode = True
