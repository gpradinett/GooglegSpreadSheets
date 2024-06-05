# GooglegSpreadSheets
Este repositorio contiene un script en Python que actualiza una hoja de cálculo de Google Sheets usando datos de un archivo CSV. El script utiliza la biblioteca `gspread` para interactuar con Google Sheets y `pandas` para la manipulación de datos.

## Características

- Autenticación con la API de Google Sheets utilizando credenciales de una cuenta de servicio
- Creación de una nueva hoja de cálculo de Google Sheets (comentado en el script)
- Compartir la hoja de cálculo con una dirección de correo electrónico especificada (comentado en el script)
- Abrir una hoja de cálculo existente de Google Sheets
- Leer datos de un archivo CSV y actualizar la hoja de cálculo con estos datos

## Requisitos Previos

Antes de poder ejecutar el script, necesitas tener lo siguiente:

- Python 3.x instalado en tu sistema
- Un proyecto de Google Cloud con la API de Google Sheets y la API de Google Drive habilitadas
- Archivo JSON de credenciales de cuenta de servicio (`gs_credentials.json`)
- Las bibliotecas de Python necesarias instaladas

## Instalación

1. **Clonar el repositorio:**

    ```sh
    git clone https://github.com/tuusuario/actualizador-google-sheets.git
    cd actualizador-google-sheets
    ```

2. **Crear y activar un entorno virtual (opcional pero recomendado):**

    ```sh
    python3 -m venv venv
    source venv/bin/activate   # En Linux/macOS
    # venv\Scripts\activate    # En Windows
    ```

3. **Instalar las bibliotecas necesarias:**

    ```sh
    pip install gspread oauth2client pandas
    ```

4. **Agregar tu archivo de credenciales de cuenta de servicio:**

    Coloca tu archivo `gs_credentials.json` en el directorio raíz del repositorio.

5. **Preparar tu archivo CSV:**

    Asegúrate de tener un archivo CSV llamado `text.csv` en el directorio raíz del repositorio.

## Uso

1. **Ejecutar el script:**

    ```sh
    python3 gs_spreadsheet.py
    ```

2. **Explicación del Script:**

    - **Autenticar y autorizar:**

        ```python
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        import pandas as pd

        scope = ['https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive']

        credenciales = ServiceAccountCredentials.from_json_keyfile_name('gs_credentials.json')
        cliente = gspread.authorize(credenciales)
        ```

    - **Crear una nueva hoja de cálculo de Google Sheets y compartirla (comentado):**

        ```python
        """
        sheet = cliente.create('Primera')

        sheet.share('gpradinett@gmail.com', perm_type='user', role='writer')
        """
        ```

    - **Abrir una hoja de cálculo existente y leer datos de un archivo CSV:**

        ```python
        sheet = cliente.open('Primera').sheet1

        df = pd.read_csv('text.csv')

        sheet.update([df.columns.values.tolist()] + df.values.tolist())
        ```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contribuir

Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request.

## Contacto

Para cualquier pregunta o consulta, por favor contacta a gpradinett@gmail.com.
