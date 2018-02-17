import numpy as np
import cv2
import zbar
import os.path

class BarcodeReader():


    """
        BarcodeReader(image_file<s)
    """

    scanner = zbar.Scanner()
    
    def scan(self, image_array):
        results = self.scanner.scan(image_array)
        return results

    def scanImage(self, image_file):
        image = self.getImage(image_file)
        if image is None:
            return []

        results = self.scanner.scan(image)
                    
        return results
        
    @staticmethod
    def getImage(image_file):
        return cv2.imdecode(np.fromstring(image_file, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
        
