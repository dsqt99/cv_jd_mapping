from flask import Flask, request, jsonify
import logging

from utils.mapping import percent_mapping

app = Flask(__name__)

@app.route('/mapping', methods=['GET', 'POST'])
def mapping():
    cv = request.args.get('cv')
    jd = request.args.get('jd')

    # phan tich cv

    res = {'cv': cv, 
           'jd': jd,
           'percent_mapping': percent_mapping(cv, jd)}

    return jsonify(res)

if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(debug=True, host='192.168.122.102', port=8002)
