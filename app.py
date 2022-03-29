from flask import request
from database import db, app

import routes.character as character
import routes.races as races
import routes.vehicle as vehicles

if __name__ == '__main__':
    app.run(debug =True)