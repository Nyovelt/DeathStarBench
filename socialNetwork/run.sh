helm install social-network ~/Downloads/DeathStarBench/socialNetwork/helm-chart/socialnetwork \
  --set-string global.resources="requests: 
      cpu: "250m"
      ephemeral-storage: "1Gi"
    limits:
      cpu: "16000m"
      ephemeral-storage: "2Gi""
echo "Be sure to forward the port!"
#sleep 30
#./forward.sh
 