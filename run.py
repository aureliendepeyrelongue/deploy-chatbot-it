from app import app

if __name__ == "__main__":
    # app.run(debug=True, use_debugger=True, use_reloader=True)
    app.run(host='0.0.0.0', port=5000)
