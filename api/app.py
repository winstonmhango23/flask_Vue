import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS


students = [
    {
        'id': uuid.uuid4().hex,
        'firstname': 'Winston',
        'lastname': 'Mhango',
		'gender': 'male',
		'age': 34,
        'paid': True
    },
    {
        'id': uuid.uuid4().hex,
        'firstname': 'Laston',
        'lastname': 'Mwamande',
		'gender': 'male',
		'age': 35,
        'paid': False
    },
	{
        'id': uuid.uuid4().hex,
        'firstname': 'Adams',
        'lastname': 'Kampote',
		'gender': 'male',
		'age': 45,
        'paid': True
    },
	{
        'id': uuid.uuid4().hex,
        'firstname': 'Madalitso',
        'lastname': 'Kafotokoza',
		'gender': 'Female',
		'age': 17,
        'paid': False
    },
]

# instantiate the app
app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#  defining a delete resource method
def deleteStudent(student_id):
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            return True
    return False

# route for all the resources
@app.route('/students', methods=['GET', 'POST'])
def all_students():
    response_object = {'status': 'success'}

	# if method is POST, create a single resource
    if request.method == 'POST':
        post_data = request.get_json()
        students.append({
            'id': uuid.uuid4().hex,
            'firstname': post_data.get('firstname'),
            'lastname': post_data.get('lastname'),
			'gender': post_data.get('gender'),
			'age': post_data.get('age'),
            'paid': post_data.get('paid')
        })
        response_object['message'] = 'student added!'
	
	# if method is not POST(if it is GET),the response object should return a list of students
    else:
        response_object['students'] = students
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()