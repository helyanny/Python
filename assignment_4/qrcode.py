from helper import *
import txtdata

class QRCode :
    """ docstring """
    def __init__(self, file_path, last_update_date = "00/00/0000", owner = "Default Owner" , error_correction = 0.0) :
        self.last_update_date = convert_date(last_update_date)
        self.owner = owner
        code_data = txtdata.get_data(file_path)
        self.data = txtdata.TxtData(code_data)
        self.error_correction = error_correction
        
    def __str__(self) :
        last_update_year = self.last_update_date["Year"]
        return "The QR code was created by " + self.owner + " and last updated in " + last_update_year + "." \
                        + "\nThe details regarding the QR code file are as follows:" + "\nThis TxtData object has " \
                        + str(self.data.rows) + " rows and " + str(self.data.cols) + " columns."

    def equals(self, another_qrcode) :
        return (another_qrcode.data.__eqself.data) and (another_qrcode.error_correction == self.error_correction)
    
    def is_corrupted(self, precise_qrcode) :
        return TxtData.approximately_equals(self, precise_qrcode.data, self.error_correction)
    
        
        