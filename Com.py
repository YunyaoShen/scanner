# -*- encoding=utf-8 -*-
import serial
import time
# import WriteLog


class COM:
  def __init__(self, port, baud):
    self.port = port
    self.baud = int(baud)
    self.open_com = None
    # self.log = WriteLog.WriteLog('ITC_LOG.LOG')
    self.get_data_flag = True
    self.real_time_data = ''


  def get_real_time_data(self):
    return self.real_time_data

  def clear_real_time_data(self):
    self.real_time_data = ''


  def set_get_data_flag(self, get_data_flag):
    self.get_data_flag = get_data_flag

  def open(self):
    try:
      self.open_com = serial.Serial(self.port, self.baud,parity=serial.PARITY_NONE, stopbits=1, bytesize=8)
    except Exception as e:
      print('Open com fail:{}/{}'.format(self.port, self.baud))
      print('Exception:{}'.format(e))

  def close(self):
    if self.open_com is not None and self.open_com.isOpen:
      self.open_com.close()

  def send_data(self, data):
    if self.open_com is None:
      self.open()
    success_bytes = self.open_com.write(data)
    success_data = self.get_data()
    return success_data

  def get_data(self, over_time=30):
    all_data = ''
    if self.open_com is None:
      self.open()
    start_time = time.time()
    while True:
      end_time = time.time()
      if end_time - start_time < over_time and self.get_data_flag:
        # data = self.open_com.read(self.open_com.inWaiting())
        data = self.open_com.read(8) # read 1 size
        data = str(data)
        if data != '':
          # print('Get data is:{}'.format(data))
          all_data = all_data + data
          self.real_time_data = all_data
          break
      else:
        self.set_get_data_flag(True)
        break
    return all_data



if __name__ == '__main__':
  pass
  com = COM("COM3", 9600)
  com.open()
  data = bytearray([0x55, 0x01, 0x01, 0x04, 0x19, 0x00, 0x00, 0x8B])
  print(com.send_data(data))
  # com.get_data()
  com.close()
