import os
import sys
import datetime
import json
#from connection import identity

#data_path = identity.path

json_input = '{"params": {"unit": 4}, "weights": {"brutto": 200, "netto": 200, "tare": 0, "peak": 200, "valley": 0, "weight1": 45, "weight2": 56, "weight3": 34, "weight4": 65, "weight5": 0, "weight6": 0, "weight7": 0,"weight8": 0, "weightA": 0, "weightB": 0} }'

data = json.loads(json_input)


def initDevice():
    device_array = data['device']
    device_id = param_array.id
    return {'id': str(device_id)}


def readParams():
    param_array = data['params']
    weight_unit = param_array.unit
    weight_unit_data = ['', 'lb', 'g', 't', 'kg', 'ft']
    weight_unit_name = weight_unit_dic[weight_unit]
    # instrument.serial.close()
    return {'weight': str(weight_unit_name)}


def readWeights():
    weight_array = data["weights"]
    brutto = float(weight_array.brutto)
    netto = float(weight_array.netto)
    tare = float(weight_array.tare) if weight_array.tare else brutto-netto
    peak = float(weight_array.peak)
    valley = float(weight_array.valley)
    weight1 = float(weight_array.weight1)
    weight2 = float(weight_array.weight2)
    weight3 = float(weight_array.weight3)
    weight4 = float(weight_array.weight4)
    weight5 = float(weight_array.weight5)
    weight6 = float(weight_array.weight6)
    weight7 = float(weight_array.weight7)
    weight8 = float(weight_array.weight8)
    weightA = float(weight_array.weightA)
    weightB = float(weight_array.weightB)
    return {'brutto': brutto, 'netto': netto, 'tare': tare, 'peak': peak, 'weight1': weight1, 'weight2': weight2, 'weight3': weight3, 'weight4': weight4}
