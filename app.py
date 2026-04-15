import sqlite3

conn = sqlite3.connect("trabajo1.db")

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS cursos(
        id INTEGER PRIMARY KEY,
        descripcion TEXT NOT NULL,
        horas INTERGER NOT NULL
        
    )
    """
)
conn.execute(
    """
CREATE TABLE  IF NOT EXISTS estudiantes (
    id INTERGER PRYMARY KEY,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL
)
"""
)
conn.execute(
   """
   CREATE TABLE IF NOT EXISTS inscripciones(
    id INTEGER PRIMARY KEY,
    fecha TEXT NOT NULL,
    curso_id INTEGER NOT NULL,
    estudiante_id INTEGER NOT NULL, -- Agregada la coma aquí
    FOREIGN KEY (curso_id) REFERENCES cursos(id),
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id)
 )
"""
)
conn.execute(
   """
    INSERT INTO inscripciones (fecha,estudiante_id,curso_id)
    VALUES
    ('2026-04-14',1,1)
    """
)
conn.commit()
#conn.execute(
   #"""
    #INSERT INTO cursos (descripcion,horas)
    #VALUES ('Python de 0 a experto',40)
    #"""
    #)

#Conn.execute(
    #"""
    #INSERT INTO estudiantes (nombre, apellidos, fecha_nacimiento)
    #VALUES
    #('Vania', 'Yana', '2005-09-27')
    #"""
#)
#conn.commit()

print("\nCURSOS")
cursor = conn.execute("SELECT * FROM cursos")
for row in cursor:
    print(row)
print("\nESTUDIANTES")
cursor = conn.execute("SELECT * FROM estudiantes")
for fila in cursor:
    print(fila)

print("\nINSCRIPCIONES")
cursor = conn.execute("SELECT * FROM inscripciones")
for fila in cursor:
    print(fila)
