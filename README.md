# Akamai DataStream 2 to Logfile

Simpel function that recieves POST requests and saves to a textfile.

## Build

```
docker build . -t ds2-to-logfile
```

## Run
```
docker run --name="ds2-to-logfile" -d --restart unless-stopped -v /var/log/ds2:/var/log/ds2 -p 127.0.0.1:18094:80/tcp ds2-to-logfile:latest
```


## Framework

https://github.com/0x67757300/uHTTP
https://0x67757300.github.io/uHTTP/

## Nginx

```
location /api/ds2 {
    auth_basic "";
    auth_basic_user_file /somelocation/htpasswd;
    proxy_set_header Host $host;
    proxy_set_header True-Client-IP $remote_addr;
    proxy_pass http://127.0.0.1:18094/;
}
```

```
htpasswd -c /somelocation/htpasswd ds2
```