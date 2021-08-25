from vlcconnect import create_app

app = create_app()

def main() -> None:
    """Main Entry point for the Flask Application"""

    app.run(debug=True)

if __name__ == "__main__":
    main()
