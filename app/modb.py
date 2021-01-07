import minimalmodbus

instrument = minimalmodbus.Instrument('COM4 ', 2, close_port_after_each_call=True)
instrument.serial.baudrate = 38400

def readParams():
        weight_unit = instrument.read_register(1119)
        weight_unit_dic = ['','lb', 'g', 't', 'kg','ft']
        weight_unit_name = weight_unit_dic[weight_unit]
        #instrument.serial.close()
        return {'weight': str(weight_unit_name)}

def readWeights():
        brutto = instrument.read_register(2, 3)
        netto = instrument.read_register(4, 3)
        tare = round(brutto - netto, 3)
        peak = instrument.read_register(6, 3)
        weight1 = instrument.read_register(51, 3)
        weight2 = instrument.read_register(53, 3)
        weight3 = instrument.read_register(55, 3)
        weight4 = instrument.read_register(57, 3)
        #instrument.serial.close()
        return {'brutto': brutto, 'netto': netto, 'tare': tare, 'peak': peak, 'weight1': weight1, 'weight2': weight2, 'weight3': weight3, 'weight4': weight4}