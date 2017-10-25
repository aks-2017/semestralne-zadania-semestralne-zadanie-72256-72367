# Slovensk� technick� univerzita v Bratislave
---
## AP LOAD BALANCE BASED HANDOVER IN SOFTWARE DEFINED WIFI SYSTEMS
### Marko Morav��k, Mat�� Sos�ak
---
# 1. �vod


V dne�nej dobe je pre sie�ov�ch oper�torov probl�mom zmeni� v bezdr�tov�ch syst�moch ich sie�ov� strat�giu najm� kv�li nie pr�li� flexibiln�mu hardv�ru. V�etky bezdr�tov� siete s� riaden� pod�a hlavnej normy 802.11. Tieto siete sa vyzna�uj� podporou ve�mi vysokej priepustnosti a s� ur�en� pre pripojenie ve�k�ho po�tu klientov. Tieto bezdr�tov� siete s� vysielan� pr�stupov�mi bodmi (AP), ktor� s� rozmiestnen� tak, aby pokryli v�etk�ch klientov v �o najlep�ej miere. No kv�li narastaj�cemu po�tu klientov doch�dza k pre�a�eniu t�chto zariaden� a teda n�sledne k  zn�eniu priepustnosti. Rie�en�m ich probl�mu by mohlo by� pr�ve SDN. Jedn� sa o softv�rovo definovan� siete, ktor�ch hlavn�m cie�om je oddeli� riadiacu vrstvu od sie�ovej infra�trukt�ry. �i�e v preklade pou�i� jeden centr�lny prvok, ktor� bude riadi� cel� prev�dzku a t�mto prvkom sa naz�va SDN kontrol�r. Tento kontrol�r by teda bol schopn� rozdeli� mieru z�a�e medzi viacero AP. Cie�om n�ho projektu je teda zanalyzova� v�hody a nev�hody nasadenia SDN v bezdr�tov�ch sie�ach a taktie� porovna� z�a� siete bez SDN a pri nasaden� SDN.

# 2. N�vrh rie�enia

Pre rie�enie n�ho projektu sme sa rozhodli pou�i� opera�n� syst�m Windows 10 a  simul�tor s n�zvom Mininet. V tomto simul�tore si najprv vytvor�me 3 pr�stupov� body a na ka�d� z nich pripoj�me ur�it� po�et klientov pomocou bezdr�tovej siete Wi-Fi. Potom jeden z t�chto pr�stupov�ch bodov pre�a��me tak, �e na�ho pripoj�me viacero klientov a budeme sledova�, �i n� algoritmus, ktor� je ni��ie pop�san� vyhodnot� situ�ciu spr�vne a prepne u� dlh�ie pripojen�ch klientov z pre�a�en�ho pr�stupov�ho bodu na in�. V�etky doteraz zn�me algoritmy sa zaoberaj� najm� t�m, �e sa sna�ia priradi� nov�ch klientov do AP, ktor� je najmenej vy�a�en� ale nerie�ia zmenu u� pripojen�ch klientov v pr�pade z�a�e AP, preto sme sa rozhodli sk�ma� t�to problematiku pr�ve z tohto h�adiska.

![image1](images/Topology_WS_AP.png)

*Obr.1 Sch�ma n�vrhu*

Na obr.1 je mo�n� vidie� dva pr�stupov� body (AP1 a AP2). Na AP1 s� zatia� pripojen� dvaja klienti a na AP2 je to jeden klient. Medzi t�mito dvoma pr�stupov�mi bodmi stoj� Klient LB, ktor� m� rovnako dobr� sign�l na AP1 ako aj na AP2. Ak nastane pre�a�enie pr�stupov�ho bodu AP1, tak klienta LB n� algoritmus prepoj� na AP2. Obr�zok je len ilustra�n�, preto�e na pre�a�enie je potrebn�, aby bolo na pr�stupov� bod pripojen�ch viacero klientov.





**Algoritmus vyva�ovania z�a�e medzi AP:**

1. Kontroler dostane inform�ciu o za�a�en� od AP vo WLAN syst�me
2. Kontroler porovn� za�a�enie ka�d�ho AP s hrani�nou hodnotou
3. Za�iatok loopu
4. **IF** (za�a�enie AP &gt; Hrani�n� (threshold) hodnota)

- AP je pre�a�en�
- neprij�maj nov� stanice

5. **ELSE IF** (za�a�enie AP &lt; Hrani�n� hodnota)

- AP je m�lo pre�a�en�
- prij�maj nov� stanice

6. **IF** (stanica sa dostane do oblasti prekrytie AP sign�lov, prira� stanicu k m�lo za�a�en�mu AP)
- skontroluj susedn� AP, �i je mu mo�n� priradi� stanicu
- star�mu AP po�li spr�vu o oddelen� stanice, aby sa stanica mohla oddeli�
- prira� stanicu nov�mu AP

7. **ELSE**
- �iadne priradenie stanice sa nekon�
8. Koniec loopu

# 3.   S�visiace rie�enia

Autori v [4] sa zamerali na m�d infra�trukt�ry, kde rie�ia probl�my za�a�enie medzi AP.

### 3.1   Popis probl�mu

Na obr�zku 2(a) je mo�n� vidie� rozdelenie 7 bezdr�tov�ch stan�c, ktor� s� napojen� na AP1 a len 2 na AP2 a 3 na AP3. Tak�to rozdelenie m��e sp�sobi� stratu paketov na AP1 (zl� funkcia siete) v porovnan� s AP2 a AP3. Tak�to situ�cia dok�e by� vyrie�en� vyrovnan�m po�tu stan�c medzi v�etk�mi AP. Na obr�zku 2(b) m��eme vidie� rovnomern� rozdelenie stan�c medzi AP, po aplikovan� vhodn�ho algoritmu vyv�enie z�a�e. To vedie k zlep�eniu funkcii siete.

![image2](images/RW_stations_assignment.png)

*Obr. 2: (a) Asymetria v prira�ovan� stan�c
(b) Symetria v prira�ovan� stan�c*

### 3.2   Pridelenie bezdr�tovej stanice k AP

**3.2.1   Klasick� pr�stupy**

Postup pridelenia stanice k AP je vo v��ine syst�mov nasledovn�. WS (wireless station) preh�ad� dostupn� kan�ly ka�d�ho AP v dosahu a po��va k Beacon alebo Probe Response Frames (1-14 r�znych kan�lov). WS uklad� RSSI (Received Signal Strength Indicator � sila sign�lu) Becaonu alebo PRF a ostatn� potrebn� inform�cie, ako je ESSID, heslovanie (on/off) atd. Po skon�en� preh�ad�vania, WS zvol� AP s maxim�lnym RSSI, s t�m, �e AP sp��a aj v�etky ostatn� po�iadavky (ESSID, WEP zaheslovanie). WS sa odpoj� od AP, ak RSSI klesne pod dan� preddefinovan� hranicu. T�to proced�ra je zalo�en� na presved�en�, �e kvalita takto zvolen�ho AP je najlep�ia. Av�ak, t�to proced�ra vedie k v�sledkom, �e viacer� stanice s� pripojen� iba na p�r AP, k�m ostatn� susedn� AP zost�vaj� ne�inn�. Tak�to pre�a�enie AP vedie k poklesu v�konu. Preto je potrebn� algoritmus ktor� vezme v �vahu stav ka�d�ho AP a WS, ktor� su na neho v tom momente priraden�, za ��elom priradenia nov�ho WS k tomuto AP.

**3.2.2   Dynamick� pr�stup vyva�ovania z�a�e**

Pri dynamickom pr�stupe, pripojenie WS na dan� AP, z�le�� od po�tu u� pripojen�ch stan�c k tomuto AP a priemern� RSSI hodnota. Autori tohto rie�enia navrhli algoritmus dynamick�ho vyva�ovania z�a�e, ktor� sa zameriava na vylep�enie celkov�ho v�konu siete minim�lnym funkcion�lnym zhor�en�m AP a WS. Tento algoritmus funguje v troch �rovniach.

- �rove� automatickej vo�by kan�lu pre AP - zameriava sa na �o najlep�ie rozdelenie AP do dostupn�ch kan�lov
- �rove� rozhodovania o pripojen� stanice k AP - ur�uje sp�sob, ak�m si WS vyberie AP, ku ktor�mu sa prirad�.
- �rove� pozorovania odkazov - ur�uje, kedy WS opust� dan� AP a kedy sa vykon� roamingov� funkcia.

**�rove� automatick�ho v�beru kan�lu pre AP**

Na za�iatku f�zy ka�d�ho AP, je AP informovan� o existencii in�ch AP v jeho okol�, pou�it�m komunika�n�ho protokolu IEEE, navrhnut�ho pre servis roamingov�ch slu�ieb. Jedn� sa o Inter Access Point Protocol (IAPP), ktor� pren�a v�etky potrebn� inform�cie, �o dokazuje, �e AP slu�ba m� rovnak� LAN. V tom istom �ase, akt�vne AP preh�ad� kan�ly, aby zistil ktor� AP s� susedmi. Okrem toho je informovan� o opera�n�ch kan�loch susedn�ho AP. Tieto inform�cie pou��va na to, aby za�ali pou��va� ako opera�n� kan�l ten, v ktorom je ru�enie od susedn�ho AP �o najni��ie. To vedie k najlep�ej kvalite komunik�cie s WS. T�to �rove� algoritmu vyv�enia za�a�enia je sk�r inicializa�nou �rov�ou, kde s� podmienky oper�cie siete normalizovan�. Je to potrebn� �rove�, preto�e v��ina sie�ov�ch administr�torov ignoruje z�kladn� aspekty bezdr�tov�ch siet�. Doteraz neexistuje �iadny AP s �rov�ou automatick�ho v�beru kan�la pre AP kv�li �a�kostiam pri implement�cii. �o sa t�ka po�iato�n�ho opera�n�ho kan�la, je zvolen� ako 1 alebo 6 alebo 11 (pre USA s 1 a� 14 kan�lmi), ako je to zn�zornen� na obr�zku 2. Rovnak� vzdialenos� medzi t�mito kan�lmi (1, 6, 11 ...) poskytuje minim�lnu interferenciu medzi susediacimi AP.

![image3](images/RW_AP_channels.png)

*Obr. 3: Po�iato�n� automatick� v�ber kan�lu pre AP v p�sme 14 kan�lov*

**�rove� rozhodovania o pripojen� stanice k AP**

![image4](images/RW_AP_WS_association.png)

*Obr. 4: Postup na �rovni rozhodovania o pripojen�*

Ni - po�et stan�c priraden�ch k AP
Si - RSSI hodnota Probe Requestu na AP
Mi - Priemern� RSSI hodnota pre skupinu stan�c priraden�ch k AP

# 4. Zdroje

[1] D.Gong and Y.Yang, &quot;AP association in 802.11 n wlans with heterogeneous clients,&quot; in INFOCOM, 2012 Proceedings IEEE, 2012, pp. 1440-1448

[2] A. Balachandran, P. Bahl, and G. M. Voelker, &quot;Hot-spot congestion relief in public-area wireless networks,&quot; in Mobile Computing Systems and Applications.

[3] S-T.Sheu and C-C.Wu, &quot;Dynamic Load Balance Algorithm (DLBA) for IEEE 802.11 Wireless LAN,&quot; Tamkang Journal of Science and Engineering, vol. 1, pp. 45-52, 1999.

[4] I.Papanikos and M.Logothetis, &quot;A Study on Dynamic Load Balance for IEEE 802.11b Wireless LAN,&quot; in 8th International Conference on Advances in Communication and Control (COMCON), 2001.