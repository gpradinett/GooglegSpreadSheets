import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']

credenciales = ServiceAccountCredentials.from_json_keyfile_name('gs_credentials.json')

cliente = gspread.authorize(credenciales)
"""
sheet = cliente.create('Primera')

sheet.share('gpradinett@gmail.com', perm_type='user', role='writer')
"""

sheet = cliente.open('Primera').sheet1

df = pd.read_csv('text.csv')

sheet.update([df.columns.values.tolist()] + df.values.tolist())
