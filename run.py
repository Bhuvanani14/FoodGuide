#!/usr/bin/env python
import os
from app import create_app

config_name = os.environ.get('FLASK_ENV', 'development')
app = create_app(config_name)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    debug = config_name == 'development'
    
    print(f"Starting AI Meal Planner App in {config_name} mode...")
    print(f"Running on port {port}")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
