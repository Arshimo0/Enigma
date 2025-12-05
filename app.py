from flask import Flask, render_template, request
from logic import CipherLogic

app = Flask(__name__)
cipher = CipherLogic()

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    original_text = ""
    key = ""
    error = None

    if request.method == 'POST':
        # Get data from the HTML form
        original_text = request.form.get('text', '')
        key = request.form.get('key', '')

        if 'reset' in request.form:
            # If reset button was clicked, clear everything
            return render_template('index.html', result="", original_text="", key="")

        # Process the logic
        result = cipher.process_text(original_text, key)
        
        if result is None:
            error = "Invalid Key! Please enter a number."

    return render_template('index.html', result=result, original_text=original_text, key=key, error=error)

if __name__ == '__main__':
    # Debug mode allows you to see changes without restarting
    app.run(debug=True, host='0.0.0.0', port=5000)