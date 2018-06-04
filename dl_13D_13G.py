import requests
import os

# all_forms = set()

# with open('idx',encoding='latin1') as f:
#     for n,x in enumerate(f):
#         if '.txt' in x:
#             all_forms.add(x.split('|')[2])
#         if n % 1000000 == 0:
#             print(n)
# print(all_forms)

# all_form = {'PX14A6G', 'SC TO-T/A', 'SC TO-T', '11-KT', '25', '1-SA/A', 'UPLOAD', 'TH', 'S-3D/A', 'NT 10-D/A', '253G4', '8-K15D5/A', '8-A12G/A', 'SF-1', 'S-20/A', 'DOS/A', 'N-14MEF', 'G-405N/A', 'NT 10-K', 'S-2', 'DEF-OC', 'N-23C3A/A', 'N-6/A', 'SC 13D/A', 'N-4 EL/A', '39-310B', '40-33/A', 'G-FIN', 'U-13-60', 'F-4', '8-A12B/A', '1-E', 'EFFECT', 'SC 14D1/A', 'WDL-REQ', 'NRSRO-UPD', '40-6C/A', '8-B12G/A', 'ADVW', 'SDR/A', 'SC 13E4/A', 'ABS-15G/A', '34-12H', 'S-3/A', '15-12G/A', 'N-14AE', '424B2', '10KSB/A', 'U-12-IB/A', 'N-23C-1', 'CERT', 'CFPORTAL', 'SC 13E3', 'G-FIN/A', 'FOCUSN/A', 'ADV-H-T', 'N-Q/A', 'SB-2', '497H2', '40FR12B', '35-APP', 'ADV-H-C', 'N-3', '253G1', 'D/A', 'UNDER/A', '25-NSE', '13F-E', 'CB', 'QRTLYRPT', '11-K', '4/A', 'SB-1MEF', 'ADVCO', '40-6B/A', '10-K405', '15F-12B/A', '485B24E', 'TTW/A', '1-A/A', 'AFDB/A', '40-RPT', 'QUALIF', 'CT ORDER', 'N-5/A', 'F-80', 'CERTPAC', '40-8F-A/A', 'NT N-MFP', 'N-23C3C/A', 'U-9C-3', 'S-8 POS', '10-QT', '2-AF', '1-U', 'NT-NSAR', 'F-3/A', '485APOS', 'S-4 POS', 'TA-2', 'CFPORTAL/A', '5/A', 'NO ACT', 'NSAR-U/A', 'ADB', 'N-6', 'F-2', '40FR12G/A', 'SC 13E3/A', '10-12G/A', 'N-27D-1', 'N-8A', '10QSB', '13FCONP', 'N-CR', 'U-12-IA/A', 'DFAN14A', 'SC 14D9/A', 'SEC STAFF LETTER', 'SC 14F1/A', 'MSD/A', '1/A', 'N-1/A', 'F-4 POS', 'C', 'CERTBATS', 'DEF 14C', 'N-3 EL/A', 'APP WD/A', 'N-14/A', 'DRSLTR', 'POS462C', 'S-1', 'U-33-S', 'N-CR/A', '40-8F-M/A', 'SE', '40-APP/A', 'MSD', 'N-1A EL', '485A24F', 'F-6', 'N-18F1/A', 'N-3/A', '1-A-W', 'S-4EF/A', '24F-2NT/A', 'S-6', 'N-23C3B/A', 'SC14D9C', 'F-X', '40-8F-B/A', 'F-9EF', 'CERTPBS', 'PRES14A', '40-202A', 'PREC14C', '305B2/A', 'C-W', 'NTN 10Q', 'X-17A-5/A', '24F-2NT', 'U-3A3-1', 'F-3', '10QSB/A', 'SB-2MEF', 'F-10EF', 'NT N-MFP1', '8A12BT', '13F-NT', 'APP WDG', 'N-1A', 'X-17A-5', '8-K', 'PRRN14A', '19B-4', 'SC 13E1/A', '8-K15D5', 'N-18F1', '10-K', 'N-54A', 'CERTCSE', '40-206A/A', 'N-6F', 'T-3', '486BPOS', 'S-8', 'N-2MEF', '253G3', '485BXT', 'BDCO', 'DOSLTR', '40-17GCS', 'ID-NEWCIK', '40-17F1', 'POS AM', '20-F/A', 'F-3D', 'TACO', 'SP 15D2/A', '40-24B2/A', '497K', 'SDR', '1', '1-E AD', 'NRSRO-CE', '10-12B/A', '497AD', 'ADV/A', 'CERTNYS', 'DEF13E3', '6B ORDR', 'F-80/A', 'F-X/A', 'SC 13E1', 'EBRD/A', '485BPOS', 'OIP ORDR', 'DEFR14C', 'N-1A/A', 'N-8B-2', '40-8F-2', 'N-23C3A', 'F-8 POS', 'N-8F ORDR', 'F-4/A', 'U-12-IA', 'S-B', 'ADN-MTL', 'S-B/A', '10-Q', 'F-1MEF', 'DEFM14A', 'QRTLYRPT/A', 'U-13E-1', 'TTW', '10SB12B', 'NSAR-B/A', 'MSDW', 'D', 'TA-1/A', 'F-3ASR', 'DEFA14C', 'SC TO-I/A', '40-203A/A', '10-KT', '26', 'SC14D1F/A', 'N-CSRS', '35-APP/A', '40-8B25', '20FR12B/A', '10KSB40/A', '40-17F1/A', 'N-8B-2/A', 'C-AR', 'F-6EF', '40-205E', 'F-3MEF', 'SF-3/A', 'N-MFP1', 'CERTAMX', 'SC 14D1', 'NSAR-BT/A', 'F-10', '40-33', '13F-HR/A', '424B7', 'FOCUSN', 'F-7/A', 'N-CSR', '6-K', 'F-6/A', 'POS AMI', 'SC13E4F/A', 'NSAR-U', 'F-1', 'S-3D', '40FR12G', 'DEFC14A', 'BW-2', 'N-1', '8-K12G3', '20FR12G', '8-M', 'F-2/A', 'C-AR/A', 'NSAR-AT', '486B24E', '40-6C', '40-17G', '39-304D', 'SF-3', 'N-2', 'S-3ASR', '497K2', 'NT 15D2/A', 'PREC14A', '10-K405/A', '15F-15D/A', 'SC 14F1', '8-K/A', '11-KT/A', 'APP NTC', '24F-1', 'U5A/A', 'IRANNOTICE', '18-K/A', 'PRE13E3', '10-12B', 'NRSRO-CE/A', '40-17G/A', 'ARS/A', '497K1', '40-8F-M', 'N-4/A', '10-KSB', '40-203A', 'N-MFP1/A', 'OIP NTC', '424A', 'S-BMEF', '8F-2 ORDR', '40-OIP/A', 'U5S', '10-KSB/A', 'TA-2/A', 'N-14AE/A', '487', '485A24E', 'N-Q', '24F-2EL/A', 'F-N', 'N-23C-1/A', 'NT-NCSR/A', '1-A-W/A', '1-K/A', 'G-405/A', 'N-30D', '10-Q/A', '13F-E/A', 'DEFS14A', '10-12G', 'C-TR', '8-A12B', 'NT 10-Q', '1-A POS', 'ANNLRPT/A', 'DRS', 'PRER14A', 'SC TO-C', 'POS 8C', 'CERTBSE', 'UNDER', '305B2', 'REG-NR', 'DOS', '424H/A', 'N14AE24', 'U-6B-2', '10-C/A', 'ANNLRPT', '486APOS', '24F-2EL', 'N-23C3B', 'NSAR-B', 'DRS/A', '6B NTC', 'SC 14N', 'F-9/A', 'SC14D9F', '10-QT/A', 'N14EL24/A', '3', 'N-5', '485BXTF', 'PRE 14C', 'U5S/A', 'ADV-NR', 'PREA14A', 'PREM14C', '15-15D/A', 'FWP', 'CORRESP', '10-D/A', '2-A', 'APP ORDR', 'PRES14C', '424B1', 'DEF 14A', '40-8F-L', 'SB-2/A', 'N-MFP', 'N-30B-2', 'N-8F/A', '10-D', '1-A', '497J', 'S-2MEF', '8-K12B/A', 'NT-NSAR/A', 'N-30D/A', '8-K12G3/A', '485B24F', 'S-3MEF', '424B3', '425', 'POS EX', 'MA-W', 'SC14D9F/A', '2-A/A', 'C/A-W', 'MA-I', 'RW WD', 'PX14A6N', '2-E/A', 'SD/A', '424B4', '10-KT/A', '12G3-2B', 'IFC', '13F-HR', 'S-1/A', '486A24E', 'F-9', 'N-2/A', 'F-7', 'NTN 10D', 'U-57', 'PRE13E3/A', '35-CERT/A', '10SB12B/A', 'NTN 10K', '8A12BT/A', 'U5B', 'REGDEX/A', '1-Z/A', 'CB/A', 'NT 20-F', 'F-3DPOS', 'NT 15D2', 'N-6F/A', 'SF-1/A', 'PREA14C', 'N-8F', '10-C', 'S-6/A', 'SB-1', 'SP 15D2', 'S-4/A', 'ARS', 'N-CSRS/A', 'AW', 'REGDEX', 'S-6EL24/A', 'N-8A/A', 'N-1A EL/A', '10KSB40', '10-QSB/A', '8A12BEF', 'F-N/A', 'NSAR-A', 'DEFC14C', 'NT 10-Q/A', '40-8F-A', '1-E/A', 'SC TO-I', 'SC 13G/A', '40-8F-2/A', 'STOP ORDER', 'U-13-60/A', 'DSTRBRPT/A', 'NTFNCSR', 'F-10/A', '40-F', '5', 'REG-NR/A', '15F-15D', '20FR12B', 'S-4', 'U-3A-2/A', 'REVOKED', '40-205E/A', 'G-405', 'G-405N', 'N-14 8C/A', 'N-14', '40-24B2', 'DEFS14C', '15-12B', 'N-54C/A', 'PRER14C', 'ABS-15G', 'SC 13D', '1-Z', 'U-7D/A', 'MSDCO', '15-15D', 'TA-W', '10KSB', '10SB12G', 'TA-1', 'N-54A/A', 'PREN14A', 'C-AR-W', 'N14EL24', '40-6B', '1-SA', 'CERTNAS', 'NSAR-A/A', 'DFRN14A', 'IADB', '8-B12B', 'PREM14A', 'AW WD', 'ABS-EE/A', '10SB12G/A', 'MA-A', '8-B12G', 'MA-I/A', 'NTN15D2', 'N-PX/A', '20-F', 'MA', 'N-4 EL', '12G32BR', 'C/A', '8-A12G', '6-K/A', '10-QSB', 'EBRD', 'SL', 'N-8F NTC', '10KT405', 'F-10POS', 'U-1', 'SC 14D9', 'BW-3', 'DEFN14A', '18-K', 'SC 13G', 'SC 13E4', 'S-20', 'NT 10-K/A', '4', 'S-1MEF', '25/A', 'SD', 'DEFR14A', 'NTN 20F', 'APP WD', 'NT N-MFP2', '40-202A/A', 'NT 11-K', '13F-NT/A', '144', 'N-14 8C', 'POSASR', 'SC13E4F', 'S-4EF', '8-K12B', '2-E', 'G-FINW', 'DEFA14A', 'U-9C-3/A', 'U-33-S/A', 'NT-NCSR', '8-B12B/A', 'N14AE24/A', 'ADV-E', 'NT 20-F/A', 'U5B/A', 'CFPORTAL-W', 'MA/A', '40FR12B/A', '15F-12B', '1-K', '15F-12G/A', '497K3A', 'S-11', 'NTFNSAR', 'DSTRBRPT', 'F-8', '18-12B', 'U-3A-2', 'N-8B-4', '40-17F2/A', '40-APP', 'NSAR-BT', 'N-54C', 'F-8/A', 'SUPPL', 'U-7D', 'N-3 EL', '40-F/A', 'SC 14N/A', 'NTN 11K', '15F-12G', 'S-6EL24', 'SB-1/A', '20FR12G/A', 'CERTARCA', '424H', '19B-4E', '40-17F2', '9-M', '40-8FC/A', 'N-MFP2', 'ABS-EE', 'U-6B-2/A', 'F-4MEF', 'DEFM14C', 'F-6 POS', 'F-80POS', 'C-U', 'S-11MEF', 'N-MFP/A', '13FCONP/A', 'S-11/A', 'SC14D1F', 'N-PX', '40-206A', 'S-3', 'S-3DPOS', 'NSAR-AT/A', 'N-23C3C', '40-8FC', 'F-1/A', '40-8F-B', '1-U/A', 'T-3/A', '253G2', 'DEF13E3/A', 'U-57/A', 'S-4MEF', 'POS AMC', 'S-8/A', '25-NSE/A', 'C-U-W', 'RW', '10-K/A', 'U5A', 'NT 11-K/A', '8F-2 NTC', '39-304D/A', '424B8', 'DEL AM', 'U-12-IB', 'AFDB', '15-12G', '15-12B/A', 'U-1/A', '11-K/A', '1-Z-W', 'N-23C-2/A', 'F-7 POS', 'PRE 14A', 'N-CSR/A', '144/A', '3/A', 'S-2/A', 'N-4', 'F-9 POS', 'N-MFP2/A', 'NT 10-D', '424B5', '24F-2TM', '10KT405/A', '497', 'N-23C-2', '40-8F-L/A', '40-OIP', '35-CERT', '497K3B', 'POS462B'}

_13 = ['SC 13D/A', 'SC 13D', 'SC 13G', 'SC 13G/A']

with open('idx',encoding='latin1') as f:
    for n,x in enumerate(f):
        if '.txt' in x:
            elem = x.split('|')
            if elem[2] in _13:
                form = elem[2].split(' ')[1].replace('/','')
                if os.path.isfile(f'./13D/{elem[0]}_{elem[3]}_{form}.txt'):
                    continue
                print(f'Downloading {elem[0]}_{elem[3]}.txt')
                with open(f'./13D/{elem[0]}_{elem[3]}_{form}.txt','w',encoding="utf-8") as f:
                    f.write(requests.get(f'https://www.sec.gov/Archives/{elem[-1]}').content.decode('utf-8','ignore'))            
