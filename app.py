from flask import Flask, jsonify, request

app = Flask(__name__)

databaza = [
    {
        "id": 1,
        "name": "Adrian",
        "surename": "červenka",
        "nickname": "Rašpľa"
    },
    {
        "id": 2,
        "name": "MartiMarko",
        "surename": "Mihaloivička",
        "nickname": "Mirha"
    },
]

@app.route("/")
def home():
    return jsonify({"message": "Dummy Flask API is running!"})


@app.route("/api")
def get_data():
    return jsonify(databaza)


if __name__ == "__main__":
    app.run(debug=True)
    @app.route('/api')
    def api():
        return jsonify(databaza)
    
    @app.route('/api/student/<int:student_id>')
    def find_student(student_id):
        for student in databaza["students"]:
            if student["id"] == student_id:
                return jsonify(student)
        return jsonify({"error": "Student not found"}), 404
