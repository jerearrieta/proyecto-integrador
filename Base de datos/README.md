### 🗃️ Base de Datos

Para el sistema SmartHome se identificaron tres entidades principales necesarias para representar la información de manera estructurada: `Usuario`, `Dispositivo` y `Automatización`.

- **Usuario:** contiene los datos personales del usuario, como `nombre`, `apellido`, `email` y `contraseña`. El atributo `email` se considera una clave candidata, ya que debe ser único. Cada usuario puede tener varios dispositivos y automatizaciones asociadas.

- **Dispositivo:** representa cada equipo inteligente dentro del hogar, como luces, cámaras o termostatos. Incluye atributos como `nombre`, `tipo`, `estado` e `id_usuario` (clave foránea que lo vincula al usuario propietario). El campo `estado` puede ser un valor booleano (encendido/apagado) o un valor específico según el tipo de dispositivo.

- **Automatización:** permite definir reglas automáticas configuradas por los usuarios. Se compone de `descripcion`, `condicion`, `accion` e `id_usuario`. Por ejemplo, una condición podría ser “si son las 7:00 am” y la acción asociada “encender cafetera”.

Se definieron relaciones **uno a muchos (1:N)** entre `Usuario` y `Dispositivo`, y también entre `Usuario` y `Automatización`, ya que un mismo usuario puede tener múltiples elementos asociados en cada entidad.

El modelo fue diseñado pensando en una futura implementación sobre un sistema gestor de bases de datos relacional. Además, se elaboró un diagrama E-R que representa gráficamente la estructura de las entidades y sus relaciones, el cual se puede consultar en la carpeta de documentación del repositorio.
