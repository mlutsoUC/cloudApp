#import minimalmodbus

#instrument = minimalmodbus.Instrument('COM4 ', 2, close_port_after_each_call=True)
#instrument.serial.baudrate = 38400


def readParams():
    weight_unit = 4
    weight_unit_dic = ['', 'lb', 'g', 't', 'kg', 'ft']
    weight_unit_name = weight_unit_dic[weight_unit]
    # instrument.serial.close()
    return {'weight': str(weight_unit_name)}


def readWeights():
    brutto = 1024.256
    netto = 512.128
    tare = round(brutto - netto, 3)
    peak = 4069
    weight1 = 512.256
    weight2 = 256.128
    weight3 = 128.064
    weight4 = 64.32
    # instrument.serial.close()
    return {'brutto': brutto, 'netto': netto, 'tare': tare, 'peak': peak, 'weight1': weight1, 'weight2': weight2, 'weight3': weight3, 'weight4': weight4}
