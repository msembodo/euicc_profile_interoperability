import json

saipJson = '../OFR_LV_SAIP_V2.json'

with open(saipJson) as json_file:
    saipUnderTest = json.load(json_file)

# supported PEs
profileElements = ['header', 'genericFileManagement', 'pinCodes', 'pukCodes', 'akaParameter', 'cdmaParameter',
                   'securityDomain', 'rfm', 'application', 'nonStandard', 'end']
fsProfileElements = ['mf', 'cd', 'telecom', 'usim', 'opt-usim', 'isim', 'opt-isim', 'phonebook', 'gsm-access',
                     'csim', 'opt-csim']
