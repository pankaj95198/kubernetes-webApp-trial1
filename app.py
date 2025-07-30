from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello App</title>
    <script>
        window.onload = function() {
            let name = prompt("Enter your name:");
            if(name) {
                document.getElementById("greet").innerText = "Hello " + name + "!";
            }
        }
    </script>
</head>
<body>
    <h1 id="greet">Welcome!</h1>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
