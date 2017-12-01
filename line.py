#!/usr/bin/python
"""
Setting the position of Nodes (only for Stations and Access Points) and providing mobility.

"""

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelAP
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def topology():

    "Create a network."
    net = Mininet( controller=Controller, link=TCLink, accessPoint=OVSKernelAP )

    print "*** Creating nodes"

    ap1 = net.addAccessPoint( 'ap1', ssid= 'new-ssid1', mode= 'g', channel= '1', position='30,40,0', range='35' )
    ap2 = net.addAccessPoint( 'ap2', ssid= 'new-ssid2', mode= 'g', channel= '6', position='80,40,0', range='35' )

    sta1 = net.addStation( 'sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8', range='3', )
    sta2 = net.addStation( 'sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8', position='40,58,0', range='3' )
    sta3 = net.addStation( 'sta3', mac='00:00:00:00:00:04', ip='10.0.0.4/8', position='25,60,0', range='3' )
    sta4 = net.addStation( 'sta4', mac='00:00:00:00:00:05', ip='10.0.0.5/8', position='70,40,0', range='3' )
    sta5 = net.addStation( 'sta5', mac='00:00:00:00:00:06', ip='10.0.0.6/8', position='25,20,0', range='3' )
    sta6 = net.addStation( 'sta6', mac='00:00:00:00:00:07', ip='10.0.0.7/8', position='20,40,0', range='3' )
    c1 = net.addController( 'c1', controller=Controller)



    net.propagationModel("logDistancePropagationLossModel", exp=5)
	


    #print "*** Configuring wifi nodes"
    net.configureWifiNodes()

    print "*** Associating and Creating links"
    net.addLink(ap1, ap2)

    net.plotGraph(max_x=120, max_y=120)

    net.associationControl('llf')

    net.seed(1)

    #net.startMobility(AC='llf', time=0)
    #net.mobility(sta1, 'start', time=1, position='0,50,0')
    #net.mobility(sta1, 'stop', time=49, position='100,50,0')
    #net.stopMobility(time=50)
	
    net.startMobility(time=0, model='RandomWayPoint', max_x=120, max_y=80, min_v=1, max_v=1.2, AC='llf')
    #net.startMobility(time=0, model='RandomDirection', max_x=140, max_y=140, min_v=0.7, max_v=0.9, AC='llf')
    #net.startMobility(time=0, model='RandomWalk', max_x=140, max_y=140, min_v=0.7, max_v=0.9, AC='llf')


    print "*** Starting network"
    net.build()
    c1.start()
    ap1.start( [c1] )
    ap2.start( [c1] )


    print "*** Running CLI"
    CLI( net )


    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'debug' )
    topology()
