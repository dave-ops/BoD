# how to generate a CSR
```
sudo apt update
sudo apt install openssl
openssl genrsa -out korg.com.key 2048
openssl req -text -noout -verify -in korg.com.csr
openssl req -new -key korg.com.key -out korg.com.csr


namecheap
```
openssl req -new -newkey rsa:2048 -nodes -keyout korg.cc.key -out korg.cc.csr
openssl req -text -noout -verify -in korg.cc.csr

Domains to Validate
korg.cc Primary Domain

Host
_3F25ED85710673798D72B079D8937E2E.korg.cc

Target
5767EB6F18A20F77F5A352D0F287DEAD.7D6040069393FD475A19AD1615756EB8.67cba987124ac.comodoca.com