
## Návod na inštaláciu mininet-wifi
---
Pri našom projekte, sme použili predkonfigurovanú VM, na ktorej sme pod¾a krokov uvedených nižšie nainštalovali mininet-wifi z githubu https://github.com/intrig-unicamp/mininet-wifi 

### Používate¾ská príruèka 
[Mininet-wifi dokumentácia](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xsosnak-xmoravcikm4/tree/master/docs/mininet-wifi_dokumentacia.pdf)

  
## Inštalácia 
krok 1: $ sudo apt-get install git  
krok 2: $ git clone https://github.com/intrig-unicamp/mininet-wifi  
krok 3: $ cd mininet-wifi  
krok 4: $ sudo util/install.sh -Wnfvl 

#### install.sh vo¾by:   
-W: wireless dependencies   
-n: mininet-wifi dependencies    
-f: OpenFlow   
-v: OpenvSwitch   
-l: wmediumd   

## Predkonfigurovaná VM (Virtual Machine)    
[Ubuntu 16.04 x64](https://intrig.dca.fee.unicamp.br:8840/owncloud/index.php/s/91mCANMB4LobPmQ)    
user: wifi   
pass: wifi