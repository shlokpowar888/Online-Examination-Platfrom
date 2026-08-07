import os
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('auth/login.html')

@app.route('/auth/login.html')
def login():
    return render_template('auth/login.html')

@app.route('/auth/register.html')
def register():
    return render_template('auth/register.html')

@app.route('/student/dashboard.html')
def student_dashboard():
    return render_template('student/dashboard.html')

@app.route('/student/exams/available.html')
def student_exams_available():
    return render_template('student/exams/available.html')

@app.route('/student/results/list.html')
def student_results():
    return render_template('student/results/list.html')

@app.route('/student/results/detail.html')
def student_result_detail():
    return render_template('student/results/detail.html')

@app.route('/faculty/dashboard.html')
def faculty_dashboard():
    return render_template('faculty/dashboard.html')

@app.route('/exams/create.html')
def exams_create():
    return render_template('exams/create.html')

@app.route('/evaluation/evaluate.html')
def evaluation_evaluate():
    return render_template('evaluation/evaluate.html')

@app.route('/admin/dashboard.html')
def admin_dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/roles/permissions.html')
def admin_permissions():
    return render_template('admin/roles/permissions.html')

@app.route('/reports/exam_report.html')
def reports_exam():
    return render_template('reports/exam_report.html')

@app.route('/exam_runtime/lobby.html')
def exam_lobby():
    return render_template('exam_runtime/lobby.html')

@app.route('/exam_runtime/exam.html')
def live_exam():
    return render_template('exam_runtime/exam.html')

@app.route('/exam_runtime/submitted.html')
def exam_submitted():
    return render_template('exam_runtime/submitted.html')

@app.route('/admin/users/list.html')
def admin_users():
    return render_template('admin/users/list.html')

@app.route('/admin/system/metrics.html')
def admin_metrics():
    return render_template('admin/system/metrics.html')

@app.route('/questions/list.html')
def questions_list():
    return render_template('questions/list.html')

@app.route('/questions/create.html')
def questions_create():
    return render_template('questions/create.html')

@app.route('/exams/list.html')
def exams_list():
    return render_template('exams/list.html')

@app.route('/evaluation/pending.html')
def evaluation_pending():
    return render_template('evaluation/pending.html')

@app.route('/subjects/list.html')
def subjects_list():
    return render_template('subjects/list.html')

@app.route('/notifications/center.html')
def notifications_center():
    return render_template('notifications/center.html')

if __name__ == '__main__':
    print("\n============================================================")
    print("Online Examination Platform - Frontend Development Server")
    print("============================================================")
    print("Running locally at: http://127.0.0.1:5000\n")
    app.run(debug=True, port=5000)
