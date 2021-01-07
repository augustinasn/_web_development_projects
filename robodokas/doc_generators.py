from mailmerge import MailMerge
from datetime import date
from datetime import datetime
import os

def generate_vmi_eds(params):
    template = os.path.join('robodokas',
                            'src',
                            'templates',
                            'VmiEds_MM.docx')

    document = MailMerge(template)

    document.merge(Date=params['date'],
                   Location=params['loc'],
                   TaxPayerName=params['taxPayerName'],
                   TaxPayerCode=params['taxPayerCode'],
                   TaxPayerRepName=params['taxPayerRepName'],
                   TaxPayerRepBasis=params['taxPayerRepBasis'])

    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = f'vmieds_{timestamp}.docx'
    filepath = os.path.join('robodokas',
                            'src',
                            'output',
                            filename)
    
    document.write(filepath)

    return filename