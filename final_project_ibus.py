#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 21:47:00 2017

@author: popo
"""

from gurobipy import*

## global variable
NUM_SCAPE = 28
trip_landscape = ' '
trip_time = 0
trip_fee = 0


if __name__ == '__main__':

    ## requirement
    ### GUI
    trip_landscape = '奇美博物館'
    trip_time = 600
    trip_fee = 500


    # Model
    m = Model('lanscape arranage')

    # Add parameters
    landscape, popularity, ticket, stay_time, traffic_time = multidict({
          '奇美博物館': ['1052', '200', '80', '0'],             #1
          '安平樹屋': ['813', '50', '20', '0'],
          '安平古堡': ['494', '50', '30', '0'],
          '林百貨': ['559', '0', '60', '0'],
          '赤坎樓': ['761', '50', '40', '0'],
          '億載金城': ['92', '50', '20', '0'],
          '國立成功大學': ['149', '0', '60', '0'],
          '孔子廟': ['485', '0', '30', '0'],
          '祀典孔廟': ['485', '0', '30', '0'],
          '大天后宮': ['83', '0', '20', '0'],						#10
          '國立台灣文學館': ['203', '0', '30', '0'],
          '烏山頭水庫': ['101', '200', '40', '0'],
          '關子嶺溫泉': ['153', '0', '80', '0'],
          '神農街': ['485', '0', '40', '0'],
          '夕遊出張所': ['85', '0', '20', '0'],
          '度小月擔仔麵': ['400', '100', '40', '0'],
          '文章牛肉麵': ['113', '100', '60', '0'],
          '富盛號餐廳': ['110', '30', '40', '0'],
          '矮仔成蝦仁飯': ['103', '50', '20', '0'],
          '裕成水果店': ['67', '50', '30', '0'],				#20
          '六千牛肉湯': ['63', '100', '60', '0'],
          '邱家小卷米粉': ['63', '80', '60', '0'],
          '阿江炒鱔魚意麪': ['61', '70', '20', '0'],
          '金德春捲': ['66', '40', '15', '0'],
          '王氏魚皮': ['34', '60', '40', '0'],
          '阿松割包': ['49', '70', '10', '0'],
          '勝利早點': ['42', '60', '40', '0'],	
          '懷舊小棧': ['9', '50', '20', '0'],   					#28  
      })


    # update
    m.update()

    # Add Decision variable
    x = {}
    for i in range(NUM_SCAPE):
    	x[i] = m.addVar(lb=0, ub=1, vtype=GRB.INTEGER, name=landscape[i])
    
    # Add Objective and Constraints
    ## Objective
    m.setObjective(quicksum(popularity[landscape[i]]*x[i] for i in range(NUM_SCAPE)), GRB.MAXIMIZE)                        
      
    ## constraint
    ### 旅行時間
    m.addConstr(quicksum(x[i]*stay_time[i]<=trip_time for i in range(NUM_SCAPE)), "Trip Time")

    ### 旅費
    m.addConstr(quicksum(x[i]*tick[i]<=trip_fee for i in range(NUM_SCAPE)), "Trip Fee")

    ###


    ###
    m.optimize()

    for v in m.getVars():
        print('%s'% name[v.varName])
        print('%s %g' % (v.varName,v.x))
        print('Obj: %g' % m.objVal)

    for v in m.getVars():
        if(v.x == 1):
            print('%s %s %i %s' % (v.varName, name[v.varName], day[v.varName], order[v.varName]))

