from pydantic import BaseModel
from typing import Union
from datetime import datetime


class CursosResponseModel(BaseModel):
    curso_id:              int
    nombre:                str
    descripcion:           str
    horario:               str
    docente_id:            int

class DocenteResponseModel(BaseModel):
    docente_id:            int
    nombre:                str
    especialidad:          str

class EstudianteResponseModel(BaseModel):
    usuario_id:         int
    nombre:             str
    email:              str
    tipo_documento:     str
    numero_documento:   int
    fecha_nacimiento:   datetime

# class LocationResponseModel(BaseModel):
#     ciudad:                     Union[str, None]
#     pais:                       str

