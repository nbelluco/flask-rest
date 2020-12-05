from flask import request, jsonify, Response
from werkzeug.exceptions import BadRequest

from src import app
from src.models import Plate
from src import db
from src.validation import validate_german_plate


@app.route('/plate', methods=['GET'])
def get_plates():
    result = []
    plates = db.session.query(Plate).all()

    for plate in plates:
        result.append({
            'plate': plate.code,
            'timestamp': plate.timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')
        })

    return jsonify(result)


@app.route('/plate', methods=['POST'])
def post_plate():
    plate_string = request.json.get('plate')

    if not plate_string:
        return BadRequest('Missing required body field: plate')

    if type(plate_string) != str:
        return BadRequest('Invalid type for body field: plate')

    if not validate_german_plate(plate_string):
        return Response('Invalid plate format', 422)

    plate = Plate(code=plate_string)
    db.session.add(plate)
    db.session.commit()

    return jsonify({
        'message': 'Plate inserted successfully'
    })
