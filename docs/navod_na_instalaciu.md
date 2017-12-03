
## N�vod na in�tal�ciu mininet-wifi
---
Pri na�om projekte, sme pou�ili predkonfigurovan� VM, na ktorej sme pod�a krokov uveden�ch ni��ie nain�talovali mininet-wifi z githubu https://github.com/intrig-unicamp/mininet-wifi 

### Pou��vate�sk� pr�ru�ka 
[Mininet-wifi dokument�cia](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xsosnak-xmoravcikm4/tree/master/docs/mininet-wifi_dokumentacia.pdf)

  
## In�tal�cia 
krok 1: $ sudo apt-get install git  
krok 2: $ git clone https://github.com/intrig-unicamp/mininet-wifi  
krok 3: $ cd mininet-wifi  
krok 4: $ sudo util/install.sh -Wnfvl 

#### install.sh vo�by:   
-W: wireless dependencies   
-n: mininet-wifi dependencies    
-f: OpenFlow   
-v: OpenvSwitch   
-l: wmediumd   

## Predkonfigurovan� VM (Virtual Machine)    
[Ubuntu 16.04 x64](https://intrig.dca.fee.unicamp.br:8840/owncloud/index.php/s/91mCANMB4LobPmQ)    
user: wifi   
pass: wifi