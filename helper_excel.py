import gspread
from oauth2client.service_account import ServiceAccountCredentials

def open_travel_file():
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
  client = gspread.authorize(creds)

  bamboo = client.open('AIS DATA').worksheet('Bamboo Take 2')
  ais = client.open('AIS DATA').worksheet('AIS Data - Wed, 06 Nov 2019 19:35:45 GMT')
  ais_names_list = ais.col_values(2)
  bamboo_first_name = bamboo.col_values(2)
  bamboo_last_name = bamboo.col_values(1)
  # pseudocode: for name in bamboo doc that == name in ais doc, change value of placed to "Yes" else "No"
  yeses = []
  nos = []

  for num in range(1,194):
    for name in ais_names_list:
      if f'{bamboo.row_values(num)[0]} {bamboo.row_values(num)[1]}'== name:
        yeses.append({num: "Yes"})
        continue
    else:
      nos.append({num: "No"})
    continue
  print(yeses)

  yeses= [{bamboo.find(val).row: 'Yes'} for index,val in enumerate(bamboo_last_name)
    if (name.upper() == f'{bamboo_first_name[index].upper()} {bamboo_last_name[index].upper()}'\
      for name in ais_names_list
      )]

  print("All done")

# def read_from_json_data():
