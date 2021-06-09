import json

from flask import Flask, request
from Blockchain.Blockchain import Blockchain
from Model.MicrotasksInfoPackages import MicrotaskEnrollment, MicrotaskPayment

app = Flask(__name__)

blockchain = Blockchain()


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})


@app.route('/insertEnrollment', methods=['POST'])
def insert_enrollment():
    company_name = request.args.get('company_name')
    crowsourcer_name = request.args.get('crowsourcer_name')
    microtask_name = request.args.get('microtask_name')

    microtask_enrollment = MicrotaskEnrollment(company_name=company_name,
                                               crowdsourcer_name=crowsourcer_name,
                                               microtask_name=microtask_name)

    blockchain.add_new_transaction(microtask_enrollment.__dict__)
    blockchain.mine()
    return json.dumps({"success": "true"})


@app.route('/insertPayment', methods=['POST'])
def insert_payment():
    company_name = request.args.get('company_name')
    print(company_name)
    crowsourcer_name = request.args.get('crowsourcer_name')
    microtask_name = request.args.get('microtask_name')
    payment = request.args.get('payment')

    microtask_payment = MicrotaskPayment(company_name=company_name,
                                         crowdsourcer_name=crowsourcer_name,
                                         microtask_name=microtask_name,
                                         payment=payment)

    blockchain.add_new_transaction(microtask_payment.__dict__)
    blockchain.mine()
    return json.dumps({"success": "true"})


app.run(debug=True, port=5000)
