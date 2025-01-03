# this expires in one hour. Get yours at https://stackoverflow.com/a/67550427
token = 'ya29.a0ARW5m761ed24bL6VQKvXTCRVyNEwLED_DP4W3S12ezwqSZ6lLFxxZRy5KgiBwovPjJCM78KvfmVgV4hflIcE2KMCRo8PPTtUK9OCMMUDPoZMBxLF6TtyJjC_6oQreNJoCydtCvh_VoFWJCIKVDnNHVTQR9HpHfkVYs3GUYXDaCgYKAY0SARESFQHGX2Mi6txZPfzTdEMbOWBsAU3hgw0175'

import os
import re

def download(id, name):
    print('downloading', name, f'(id={id}) ...')
    os.system(rf"""curl -H "Authorization: Bearer {token}" https://www.googleapis.com/drive/v3/files/{id}?alt=media -o {name}""")

filenames = [
                'img_celeba.7z.001', 'img_celeba.7z.002', 'img_celeba.7z.003',
                'img_celeba.7z.004', 'img_celeba.7z.005', 'img_celeba.7z.006',
                'img_celeba.7z.007', 'img_celeba.7z.008', 'img_celeba.7z.009',
                'img_celeba.7z.010', 'img_celeba.7z.011', 'img_celeba.7z.012',
                'img_celeba.7z.013', 'img_celeba.7z.014'
                ]

drive_ids = [
                '0B7EVK8r0v71pQy1YUGtHeUM2dUE', '0B7EVK8r0v71peFphOHpxODd5SjQ',
                '0B7EVK8r0v71pMk5FeXRlOXcxVVU', '0B7EVK8r0v71peXc4WldxZGFUbk0',
                '0B7EVK8r0v71pMktaV1hjZUJhLWM', '0B7EVK8r0v71pbWFfbGRDOVZxOUU',
                '0B7EVK8r0v71pQlZrOENSOUhkQ3c', '0B7EVK8r0v71pLVltX2F6dzVwT0E',
                '0B7EVK8r0v71pVlg5SmtLa1ZiU0k', '0B7EVK8r0v71pa09rcFF4THRmSFU',
                '0B7EVK8r0v71pNU9BZVBEMF9KN28', '0B7EVK8r0v71pTVd3R2NpQ0FHaGM',
                '0B7EVK8r0v71paXBad2lfSzlzSlk', '0B7EVK8r0v71pcTFwT1VFZzkzZk0'
                ]

for id, name in zip(drive_ids, filenames):
   download(id, f'celebA/{name}')

download('0B7EVK8r0v71pTzJIdlJWdHczRlU', 'celebA/Anno/list_landmarks_celeba.txt')

files = \
'''
README.txt,https://drive.google.com/file/d/0B4qLcYyJmiz0U2hZTEJfaEZSMFE/view?usp=drivesdk&resourcekey=0-cTCk9DqGXv86m499IyAEqw
image_list.txt,https://drive.google.com/file/d/0B4qLcYyJmiz0U25vdEVIU3NvNFk/view?usp=drivesdk&resourcekey=0-teLq3ccDXh4RL614An52_w
deltas29000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0U1pnMEI4WXN1S3M/view?usp=drivesdk&resourcekey=0-hM1CnIL4UvrRZySkFmrp5Q
deltas28000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0U1BhWlFGRXc1aHc/view?usp=drivesdk&resourcekey=0-k12ILfo-2hO3KdvQSZe3AA
deltas27000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0U1BRYl9tSWFWVGM/view?usp=drivesdk&resourcekey=0-rrCwEAXwTVYeMfEMRyGTlw
deltas26000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0U0tBanQ4cHNBUWc/view?usp=drivesdk&resourcekey=0-T15J0a7E9raLXqfcpuGzag
deltas25000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0U0lYX1J1Tk5vMjQ/view?usp=drivesdk&resourcekey=0-ca1L9JTjzelvP0CiWlNSrw
deltas24000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0U0YwQmluMmJuX2M/view?usp=drivesdk&resourcekey=0-i2R8kFevTHii0H7RtTldEA
deltas23000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0U05ZNG14X3ZjYW8/view?usp=drivesdk&resourcekey=0-Sw2SpqsuSDjzcguK_OhLsg
deltas22000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TzZySG9IWlZaeGc/view?usp=drivesdk&resourcekey=0-R5JPFUSa7vr_V7vzoxqJ3g
deltas21000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TzBBNE8xbFhaSlU/view?usp=drivesdk&resourcekey=0-EK_78DdZukWVPHhTKh1_cg
deltas20000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TnJQSS1vZS1JYUE/view?usp=drivesdk&resourcekey=0-Du_y4GKxkZRG5LfpKfuB0A
deltas19000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TnBtdW83OXRfdG8/view?usp=drivesdk&resourcekey=0-gU9LdyDpqmUnOdsZSEmtvA
deltas18000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TmhIUGlVeE5pWjg/view?usp=drivesdk&resourcekey=0-s3rzknF1346ftHmDKJKX4A
deltas17000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TmZqZXN3UWFkUm8/view?usp=drivesdk&resourcekey=0-HOKxoz4SvO2MoFnkMikCog
deltas16000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TmVkVGJmWEtVbFk/view?usp=drivesdk&resourcekey=0-IeuT8X5zA2PJ38uKJrhI4Q
deltas15000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TmRZTmZyenViSjg/view?usp=drivesdk&resourcekey=0-MqadwU3o_OZVGoZpeGssQg
deltas14000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0Tm5MSUp3ZTZ0aTg/view?usp=drivesdk&resourcekey=0-HDxTe-TxEbWLFD8tsscKxA
deltas13000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TlpJU1pleF9zbnM/view?usp=drivesdk&resourcekey=0-MY-DM5zqa0iT5yCIazcNkw
deltas12000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0Tlhvdl9zYlV4UUE/view?usp=drivesdk&resourcekey=0-Hf0Hu2gU66jHwnkMDcV8Lw
deltas11000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TlNyLUtOTzk3QjQ/view?usp=drivesdk&resourcekey=0-juhz2JJQuZ3S0a9dH7n2vg
deltas10000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TlBCNFU3QkctNkk/view?usp=drivesdk&resourcekey=0-nHcFo2CwLwHwRq83T2fpkg
deltas09000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0Tl9wNEU2WWRqcE0/view?usp=drivesdk&resourcekey=0-s5gyrDmxVFROyPEP1nzgaA
deltas08000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0Tksyd21vRmVqamc/view?usp=drivesdk&resourcekey=0-IBdA46rzRaNBIgSS53c8mw
deltas07000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TjdaV2ZsQU94MnM/view?usp=drivesdk&resourcekey=0-wESGuSKFoQQhZJQ3nD_1Zg
deltas06000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TjVkYkF4dTJRNUk/view?usp=drivesdk&resourcekey=0-CXikVqes2G9wQiY_C0bNRg
deltas05000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TjRzeWlhLVJIYk0/view?usp=drivesdk&resourcekey=0-Nys8Ac9QTxWrD1uC7S_w5w
deltas04000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TjRxVkZ1NGxHTXc/view?usp=drivesdk&resourcekey=0-UL5e7pJZ9VlyhFmihLAmtg
deltas03000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TjRWUXVvM3hZZE0/view?usp=drivesdk&resourcekey=0-RV-S_TvQvSCGu7HRItZN6g
deltas02000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TjNRV2dUamd0bEU/view?usp=drivesdk&resourcekey=0-itFlUMogBNKgygH_VBq18w
deltas01000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TjAwOTRBVmRKRzQ/view?usp=drivesdk&resourcekey=0-02MbrO33N-bBt-LqhtRM7Q
deltas00000.zip,https://drive.google.com/file/d/0B4qLcYyJmiz0TXdaTExNcW03ejA/view?usp=drivesdk&resourcekey=0-qtjFcg-E6mw63vh-UBO9Iw
LICENSE.txt,https://drive.google.com/file/d/1y5k_G-3t-cjW01QMxXNfhcp95FCpts79/view?usp=drivesdk
'''

for file in files.split('\n'):
    id = re.search(r'/d/(.*?)/', file)
    if not id:
        print('bad file:', file)
        continue
    id = id.group(1)
    name = file.split(',')[0]
    download(id, f'celebA-HQ/{name}')

download('0B4qLcYyJmiz0U25vdEVIU3NvNFk', 'celebA-HQ/image_list.txt')
