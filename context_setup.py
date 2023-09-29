from app import app, db  # Replace 'your_app' with the actual name of your Flask app

def perform_tasks_in_context():
    # Create an application context
    app_ctx = app.app_context()
    app_ctx.push()

    # Perform Flask-related tasks within the context
    with app.app_context():
        db.create_all()  # Example: Perform database tasks

    # Pop the context to clean up
    app_ctx.pop()

if __name__ == '__main__':
    perform_tasks_in_context()
