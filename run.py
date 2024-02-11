from app import create_app
import os

# Load environment variables from .env file if present
from dotenv import load_dotenv
load_dotenv()

app = create_app()

if __name__ == '__main__':
    # Retrieve port and debug mode from environment variables or set to default
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False') == 'True'

    # Run the Flask app
    app.run(host='0.0.0.0', port=port, debug=debug)
