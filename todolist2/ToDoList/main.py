from flask import Flask, render_template, redirect, request, make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = "sdhgfhjfndfbgwf$#%^$%sdfhgswyufwef"

tasks = []


@app.route('/')
def home_page():
    return render_template('home.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']

    tasks.append(
        {"title": title, "status": False}
    )

    return redirect('/')


@app.route('/delete_task/<task_id>', methods=['GET'])
def delete_task(task_id):
    tasks.pop(int(task_id))
    return redirect('/')


@app.route('/edit_status', methods=['post'])
def edit_status():
    task_id = int(request.form['index'])
    status = request.form['status']

    if status == 'true':
        tasks[task_id]['status'] = True
    else:
        tasks[task_id]['status'] = False
    return make_response('success')


if __name__ == '__main__':
    app.run(debug=True)
