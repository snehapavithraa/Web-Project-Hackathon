from flask import Flask, render_template,request, jsonify

app = Flask(__name__)


# API to create approval requests
@app.route('/api/approvals', methods=['POST'])
def create_approval():
    # Dummy logic to simulate approval creation
    approval_data = request.json
    approval_status = {'status': 'Pending', 'message': 'Approval request submitted successfully.'}

    return jsonify(approval_status)


@app.route("/")
def index():
 return render_template("index.html")

if __name__ == "__main__":
 app.run()