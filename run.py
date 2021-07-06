from lineup import create_app
from lineup import db
from lineup.models import User
import sys

# Application instance
app = create_app()

# Test database initialization
app.app_context().push()
if len(sys.argv) > 1:
    if sys.argv[1] == 'drop':
        db.drop_all()
db.create_all()

if __name__ == '__main__':
    app.run(port=3000)