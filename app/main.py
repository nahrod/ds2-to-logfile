from uhttp import App

app = App()

logfile = "/var/log/ds2/access.log"

@app.post('/')
def r(request):
    try:
        logline = request.body.decode("utf-8")
    except: return 500

    with open(logfile, 'a', encoding='utf-8') as f:
        f.write(logline)

    return 200

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('__main__:app')