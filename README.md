# Microservicio de Calculo de Factorial

## Uso

### Instalacion
```bash
pip install -r requirements.txt
```

### Ejecucion
```bash
python main.py
```

### Endpoints

#### GET /numero/{numero}
Calcula el factorial de un numero y determina si es par o impar.

**Ejemplo de uso:**
```
GET http://localhost:5000/numero/5
```

**Respuesta ejemplo:**
```json
{
  "numero": 5,
  "factorial": 120,
  "tipo": "impar"
}
```

#### GET /
Endpoint de informacion del servicio.

## Analisis: Comunicacion con servicio de historial

Para implementar la comunicación con un servicio de historial externo, realizaría las siguientes modificaciones al diseño:

#### 1. Patron de Arquitectura
- **Implementar arquitectura de microservicios**: Separar claramente las responsabilidades entre el servicio de cálculo y el servicio de historial.
- **Usar comunicación asíncrona**: Para enviar eventos de calculo sin bloquear la respuesta al cliente.

#### 2. Modificaciones al Código

##### Agregar cliente HTTP para comunicación sincrónica:
Se necesitaria crear una clase que maneje las peticiones HTTP al servicio de historial. Esta clase tendria métodos para enviar los datos del calculo como numero, factorial, tipo, al endpoint del servicio externo. Tambien Deberia incluir manejo de timeouts y excepciones para casos donde el servicio no esté disponible

##### Modificar el endpoint principal:
El endpoint actual se modificaria para agregar una llamada al servicio de historial despues de calcular el factorial. Se recomienda hacerlo de forma asíncrona usando hilos por ejemplo para no bloquear la respuesta al usuario. Y si el registro en el historial falla, el servicio principal deberia continuar funcionando normalmente

## Conclusión

Para integrar un servicio de historial externo que almacene los cálculos en una base de datos, el diseño actual requeriría:

1. **Separación de responsabilidades**: Mantener el servicio de cálculo independiente del almacenamiento
2. **Cliente HTTP**: Para comunicarse con el servicio de historial
3. **Comunicación asíncrona**: Para no afectar el tiempo de respuesta al usuario
4. **Manejo de errores**: El servicio debe funcionar aunque el historial falle
5. **Configuración externa**: URLs y parámetros del servicio de historial

Con arquitectura nos permite escalar independiente de ambos servicios y mantiene la responsabilidad única de cada uno