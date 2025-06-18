from flask import Flask, render_template, request, flash, send_from_directory
import main
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    show_download = False
    if request.method == 'POST':
        try:
            mode = request.form.get('mode')
            if mode == '1':
                t = float(request.form.get('t'))
                r = float(request.form.get('r'))
                z = float(request.form.get('z'))
                result = main.predict_temp(t, r, z)
            elif mode == '2':
                times_str = request.form.get('times')
                times = main.parse_numbers(times_str)
                main.plot_temperature_distribution(main.model, times)
                result = "Temperature distribution plot can be downloaded using the hyperlink below"
                show_download = True
            else:
                error = "Invalid mode selected."
        except Exception as e:
            error = f"Error: {e}"
    return render_template('index.html', result=result, error=error, show_download=show_download)

@app.route('/download-image')
def download_image():
    directory = os.path.join(os.getcwd(), 'pinn_results')
    filename = 'temperature_distribution.png'
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)