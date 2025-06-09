### 🗃️ Base de Datos

El diseño de base de datos para el sistema parte de un enfoque relacional basado en el **Diagrama Entidad-Relación versión 2**, que contempla tres entidades principales: `Usuario`, `Dispositivo` y `Automatización`. El modelo sigue las especificaciones exactas del diagrama E-R establecido.

#### 📦 Entidades Principales:

- **Usuario:** contiene los datos personales del usuario. Utiliza `Nombre_Usuario` como clave primaria y `Contraseña_Usuario`, ambos con validaciones de longitud (8-15 caracteres).

- **Dispositivo:** representa los dispositivos del hogar inteligente. Incluye `Id_Dispositivo` (clave primaria), `Nombre_Dispositivo`, `Estado`, `Tipo` y referencia al `Nombre_Usuario` propietario.

- **Automatización:** permite definir reglas automáticas en el sistema. Posee `Id_Automatizacion` (clave primaria), `Condicion_Inicio`, `Condicion_Corte` y está vinculada tanto al `Usuario` como al `Dispositivo` (relación N:M).

#### 🔗 Relaciones Principales:

- **Usuario → Dispositivo** (1:M) - *Relación "Gestiona"*: 
  - Un usuario puede gestionar múltiples dispositivos
  - Cada dispositivo pertenece a un único usuario
  - Implementada mediante `Nombre_Usuario` (FK) en tabla DISPOSITIVO

- **Usuario + Dispositivo → Automatización** (N:M) - *Relación "Configura"*:
  - Un usuario puede configurar múltiples automatizaciones
  - Un dispositivo puede tener múltiples automatizaciones  
  - Cada automatización involucra un usuario específico y un dispositivo específico
  - Implementada mediante `Nombre_Usuario` e `Id_Dispositivo` (FK) en tabla AUTOMATIZACION

#### ✅ Formas Normales Aplicadas:

- **1FN**: Eliminados atributos multivaluados
- **2FN**: Sin dependencias parciales
- **3FN**: Eliminadas dependencias transitivas

#### 📋 Estructura del Modelo:

**Tabla USUARIO:**
- `Nombre_Usuario` (PK) - Clave primaria alfanumérica (8-15 caracteres)
- `Contraseña_Usuario` - Campo obligatorio (8-15 caracteres)

**Tabla DISPOSITIVO:**
- `Id_Dispositivo` (PK) - Identificador único autoincremental
- `Nombre_Dispositivo` - Nombre descriptivo del dispositivo
- `Estado` - Estado actual (ENCENDIDO, APAGADO, MANTENIMIENTO, AHORRO_DE_ENERGIA)
- `Tipo` - Tipo de dispositivo (luz, camara, puerta, ciclo, etc.)
- `Nombre_Usuario` (FK) - Referencia al propietario

**Tabla AUTOMATIZACION:**
- `Id_Automatizacion` (PK) - Identificador único autoincremental
- `Nombre_Usuario` (FK) - Referencia al usuario configurador
- `Id_Dispositivo` (FK) - Referencia al dispositivo automatizado
- `Condicion_Inicio` - Condición textual para activar la automatización
- `Condicion_Corte` - Condición textual para desactivar la automatización

#### 🔧 Implementación:

Ver [Modelo Relacional Completo](modelo_relacional.md) para análisis detallado de normalización.

![Diagrama del Modelo Relacional](image.png)