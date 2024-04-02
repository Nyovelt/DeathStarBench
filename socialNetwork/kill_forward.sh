ps aux | grep deployment/jaeger | grep -v grep | awk {'print $2'} | xargs kill
ps aux | grep deployment/media-frontend | grep -v grep | awk {'print $2'} | xargs kill
ps aux | grep deployment/nginx-thrift | grep -v grep | awk {'print $2'} | xargs kill
ps aux | grep deployment/frontend | grep -v grep | awk {'print $2'} | xargs kill # online boutique
ps aux | grep deployment/nginx-web-server | grep -v grep | awk {'print $2'} | xargs kill # media service
