from sqlalchemy import Column, Integer, Text, Time
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from .database import Base

import uuid



class Patient(Base):
	__tablename__ = 'mopdi_data'

	fio = Column(Text, index=True)
	age = Column(Text, index=True)
	numberib = Column(Text, index=True)
	id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid1, index=True)
	run_dt = Column(Time(timezone=True), server_default=func.current_time(), index=True)
	gr1 = Column(Text, index=True)
	gr = Column(Text, index=True)
	name = Column(Text, index=True)
	col1 = Column(Text, index=True, nullable=True)
	col2 = Column(Text, index=True, nullable=True)
	col3 = Column(Text, index=True, nullable=True)
	tek = Column(Text, index=True)
	tekotd = Column(Text, index=True)
	vr = Column(Text, index=True)
	vrotd = Column(Text, index=True)
	col4 = Column(Text, index=True, nullable=True)
	refer = Column(Integer, index=True)
	control = Column(Integer, index=True)
	current = Column(Integer, index=True)
