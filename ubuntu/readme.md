# ubuntu
set up server

## quick commands
pwd             | print current path 
apply updates   | apt-get update && apt-get upgrade -y
reboot          | reboot
delete dir      | rm -rf node_modules
ubuntu version  | lsb_release -a
go home         | cd ~
delete files    | rm -f "*jjj*"
rename/move     | mv  a.txt n.txt

## npm install gets ⠦Killed
this is due to insufficient memory, triggering the Out of Memory (OOM) killer,

**add additional swap space for npm installs**
```
free -h
sudo fallocate -l 2G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile
```


## nginx
installed?    | nginx -v

### install
```
sudo apt install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
```

## install node
```
sudo apt update
sudo apt install unzip
curl -o- https://fnm.vercel.app/install | bash
fnm install 22
node -v
npm install -g npm@latest
npm -v
```

## install nextjs app
```
sudo apt update
sudo apt install nodejs npm
node -v
npm -v
```

## deploy nextjs to nginx
```
sudo mkdir -p /var/www/html/korg-cc
sudo chown $USER:$USER /var/www/html/korg-cc

client -> server
scp -r /home/vm-reverse-proxy-admin/repos/code.orb user@server-ip:/var/www/code-orb

local -> local
cp -r /home/root/repos/code-orb /var/www/html/code-orb
```

## upload certs
```
scp korg_cc.zip root@159.223.149.1:/root/
unzip korg_cc.zip -d /root/certs/korg_cc
mv *.crt /etc/nginx/ssl/
mv *.key /etc/nginx/ssl/private/
mv *.ca-bundle /etc/nginx/ssl/chain.pem
openssl pkcs7 -print_certs -in /etc/nginx/ssl/korg_cc.p7b -out /etc/nginx/ssl/tmp/korg_cc_from_p7b.pem
cat /etc/nginx/ssl/korg_cc.crt /etc/nginx/ssl/chain.pem/korg_cc.ca-bundle > /etc/nginx/ssl/korg_cc_fullchain.pem
openssl req -new -newkey rsa:2048 -nodes -keyout /etc/nginx/ssl/private/korg_cc.key -out /etc/nginx/ssl/korg_cc.csr
```
/etc/nginx/sites-available/default
```
server {
    listen 443 ssl;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /etc/ssl/certs/fullchain.pem;  # or just domain.crt if no chain
    ssl_certificate_key /etc/ssl/private/domain.key;

    # Optional: If .ca-bundle is separate and not in fullchain.pem
    ssl_trusted_certificate /etc/ssl/certs/domain.ca-bundle;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;

    root /var/www/html;
    index index.html;
}
```
```
nginx -t
systemctl reload nginx
openssl s_client -connect 159.223.149.1:443
```

## install mongodb
```
sudo apt-get install gnupg curl
curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
   --dearmor
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
ps --no-headers -o comm 1
sudo systemctl start mongod
sudo systemctl daemon-reload
sudo systemctl status mongod
sudo systemctl enable mongod
```

### stop mongo
```
sudo systemctl stop mongod
sudo systemctl restart mongod
```

### use
```
mongosh
```

## install git
```
sudo apt install git-all
ls ~/.ssh
ssh-keygen -t rsa -b 4096 -C "david@codeforge.cc"
digitalocean
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub
```

## install python
```
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
apt search python3. | grep -i python3 | sort -V
```

## get ip
```
curl -s https://ipinfo.io/ip
```
