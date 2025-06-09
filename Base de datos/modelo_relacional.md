# 📊 Modelo Relacional - Sistema de Automatización de Hogar Inteligente
*Basado en el Diagrama Entidad-Relación versión 2*

## 🎯 Objetivo
Implementar un modelo de base de datos normalizado hasta 3FN que soporte la gestión de usuarios, dispositivos y automatizaciones del hogar inteligente, siguiendo el diseño establecido en el diagrama E-R.

## 📋 Tablas del Sistema

### USUARIO
| Campo | Tipo | Restricciones |
|-------|------|---------------|
| Nombre_Usuario (PK) | VARCHAR(15) | PRIMARY KEY, LENGTH(8-15) |
| Contraseña_Usuario | VARCHAR(15) | NOT NULL, LENGTH(8-15) |

### DISPOSITIVO
| Campo | Tipo | Restricciones |
|-------|------|---------------|
| Id_Dispositivo (PK) | INT | AUTO_INCREMENT, PRIMARY KEY |
| Nombre_Dispositivo | VARCHAR(50) | NOT NULL |
| Estado | VARCHAR(20) | NOT NULL |
| Tipo | VARCHAR(20) | NOT NULL |
| Nombre_Usuario (FK) | VARCHAR(15) | REFERENCES USUARIO |

### AUTOMATIZACION
| Campo | Tipo | Restricciones |
|-------|------|---------------|
| Id_Automatizacion (PK) | INT | AUTO_INCREMENT, PRIMARY KEY |
| Nombre_Usuario (FK) | VARCHAR(15) | REFERENCES USUARIO |
| Id_Dispositivo (FK) | INT | REFERENCES DISPOSITIVO |
| Condicion_Inicio | VARCHAR(100) | NOT NULL |
| Condicion_Corte | VARCHAR(100) | NOT NULL |

## ✅ Formas Normales Aplicadas:

### Primera Forma Normal (1FN)
- ✅ **Eliminados atributos multivaluados**: No hay campos que contengan múltiples valores
- ✅ **Cada campo contiene valores atómicos**: Todos los campos son indivisibles  
- ✅ **Filas únicas**: Cada tabla tiene clave primaria que garantiza unicidad

### Segunda Forma Normal (2FN)
- ✅ **Cumple 1FN**: Se aplican todas las reglas de 1FN
- ✅ **Sin dependencias parciales**: Todos los atributos no clave dependen completamente de la clave primaria
- ✅ **Claves primarias identifican únicamente**: USUARIO usa Nombre_Usuario como clave natural

### Tercera Forma Normal (3FN)
- ✅ **Cumple 2FN**: Se aplican todas las reglas de 2FN
- ⚠️ **Dependencias transitivas**: Los campos Estado y Tipo en DISPOSITIVO pueden normalizarse en el futuro
- ✅ **Diseño simple y funcional**: Mantiene la estructura del diagrama E-R original

## 🔗 Relaciones del Sistema

1. **USUARIO → DISPOSITIVO** (1:M) - *Relación "Gestiona"*
   - Un usuario puede gestionar múltiples dispositivos
   - Cada dispositivo pertenece a un único usuario
   - **Clave foránea**: Nombre_Usuario en DISPOSITIVO

2. **USUARIO + DISPOSITIVO → AUTOMATIZACION** (N:M) - *Relación "Configura"*
   - Un usuario puede configurar múltiples automatizaciones
   - Un dispositivo puede tener múltiples automatizaciones
   - Cada automatización involucra un usuario y un dispositivo
   - **Claves foráneas**: Nombre_Usuario e Id_Dispositivo en AUTOMATIZACION

## 🔧 Consideraciones del Diseño

### Decisiones basadas en el Diagrama E-R:
- **Nombre_Usuario como clave primaria**: Siguiendo el diseño original del diagrama
- **Campos Estado y Tipo directos**: Mantenidos como atributos simples según el E-R
- **Relación N:M Usuario-Automatización**: Respeta la cardinalidad del diagrama original
- **Condiciones como texto**: Flexibilidad para diferentes tipos de condiciones

### Ventajas del diseño actual:
- ✅ **Simplicidad**: Fácil de entender e implementar
- ✅ **Flexibilidad**: Las condiciones pueden ser cualquier texto
- ✅ **Consistencia**: Sigue exactamente el diagrama E-R establecido

## 📊 Integridad Referencial
Todas las relaciones están garantizadas mediante:
- **Claves primarias (PK)**: Identificadores únicos por tabla
- **Claves foráneas (FK)**: Referencias entre tablas siguiendo el diagrama E-R
- **Restricciones CHECK**: Validaciones de longitud para usuarios (8-15 caracteres)
- **Restricciones UNIQUE**: Prevención de duplicados en nombres de usuario

## 🔧 Scripts SQL
Ver carpeta `scripts_sql/` para implementación actualizada:
- `crear_tablas.sql`: Creación de tablas según diagrama E-R
- `insertar_datos.sql`: Datos de ejemplo y referencia
- `consultas.sql`: Consultas útiles del sistema

## 📋 Correspondencia con Diagrama E-R
Este modelo relacional sigue **exactamente** la estructura del diagrama E-R versión 2:
- ✅ **Entidades**: Usuario, Dispositivo, Automatización
- ✅ **Atributos**: Todos los mostrados en el diagrama
- ✅ **Claves primarias**: Marcadas en rojo en el diagrama
- ✅ **Claves foráneas**: Marcadas en verde en el diagrama  
- ✅ **Relaciones**: "Gestiona" (1:M) y "Configura" (N:M)
- ✅ **Cardinalidades**: Respetadas según el diseño original