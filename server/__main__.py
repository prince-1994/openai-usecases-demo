import uvicorn

uvicorn.run('server.app:app', port=3000, log_level='info')