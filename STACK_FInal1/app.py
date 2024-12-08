from flask import Flask, render_template, request, redirect, url_for
from stack_list import Stack

app = Flask(__name__)
stacklist = Stack()  

@app.route('/stackslists')
def show_stackslists():
    
    return render_template('stackslists.html', stacklist=stacklist.print_stack())

@app.route('/', methods=['POST'])
def update():
    
    operation = request.form['operation']
    data = request.form.get('data', None)

    if operation == "is_empty":
        result = stacklist.is_empty()
        return render_template('stackslists.html', stacklist=stacklist.print_stack(), result=result)
    elif operation == "push" and data:
        stacklist.push(data)
    elif operation == "pop":
        stacklist.pop()
    elif operation == "peek":
        result = stacklist.peek()
        return render_template('stackslists.html', stacklist=stacklist.print_stack(), result=result)

    
    return redirect(url_for('show_stackslists'))

if __name__ == '__main__':
    app.run(debug=True)