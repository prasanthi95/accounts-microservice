from flask import Flask
from flask_talisman import Talisman
from service.common import log_handlers

app = Flask(__name__)

# Task 22: Configure Talisman security headers
talisman = Talisman(app)

# Rest of your configuration...
log_handlers.init_logging(app, "gunicorn.error")
app.logger.info("Service initialized")
