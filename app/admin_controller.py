
from flask import render_template, request

from app import app, service

from flask import jsonify

@app.route("/admin-app")
def admin_test():
    user_id = 1
    return render_template("pages/admin/admin_app.html")

@app.route("/admin-data")
def admin_data():
    user_id = 1
    solutions = service.get_solutions_for_admin_app()
    return jsonify(solutions)

@app.route("/admin-data/solution",methods=["PUT"])
def admin_insert_solution():
    if request.method == 'PUT':
        if request.headers['Content-Type'] == 'application/json':
            solution_id = request.json['solution_id']
            approved = request.json['approved']
            service.update_solution_for_admin_app(solution_id,approved)
           
    return "success"