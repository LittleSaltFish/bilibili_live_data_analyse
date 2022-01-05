while :  
do
    time=$(date "+%Y-%m-%d_%H:%M:%S")
    info=$(curl https://api.live.bilibili.com/room/v1/Room/get_status_info_by_uids -H "Content-Type: application/json" -d "{\"uids\": [257958427,1958342,238329119,3766866,777536,1646746,1262638877,10330740,730732,14110780,416523954,374377,434334701,672353429,58485079,3900277,2131609593,83178096,392836434,29022551,1388514638,16573314,7774837,484322035,672328094,1871001,2920960,43222001]}")
    echo "{\"time\":\"$time\",\"data\":$info}" >> ./data/Info.json
sleep 10s
done
