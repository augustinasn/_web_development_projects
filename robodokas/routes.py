from flask import jsonify, request, send_file
from robodokas import app
from robodokas.helpers import send_mail
from robodokas.doc_generators import generate_vmi_eds

import os


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return 'Welcome!'

@app.route('/VmiEds', methods=['GET', 'POST'])
def vmi_eds():
    req = request.get_json()

    params = {'user': req['user'],
              'date': req['date'],
              'loc': req['loc'],
              'taxPayerName': req['taxPayerName'],
              'taxPayerCode': req['taxPayerCode'],
              'taxPayerRepName': req['taxPayerRepName'],
              'taxPayerRepBasis': req['taxPayerRepBasis']
              }

    filename = generate_vmi_eds(params)
    
    send_mail(params['user'],
              filename)

    return 'Success!'

@app.route('/download/<string:filename>', methods=['GET', 'POST'])
def download(filename):
    filepath = os.path.join(os.getcwd(),
                            'robodokas',
                            'src',
                            'output',
                            filename)
    
    return send_file(filepath, as_attachment=True)


