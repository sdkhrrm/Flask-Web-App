from website import create_app

app = create_app()

if __name__ == '__main__':
    # debug=True means every time code changes website reloads
    app.run(debug=True) 