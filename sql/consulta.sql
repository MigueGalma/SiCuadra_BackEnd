select idRegistros, nombre, apellido, tematica, orientacion, medidas, precio\  
from scdb.registros\
inner join scdb.codigos\
on scdb.registros.codigo = scdb.codigos.idCodigos\
order by idRegistros desc\
limit 1\