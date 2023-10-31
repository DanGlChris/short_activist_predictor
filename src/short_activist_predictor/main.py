# ---------------------------------------------------------------
# Project Name: short-activist-report
# Created by: Daglox Kankwanda
# Username: DanGlChris
# Creation Date: October 21, 2023
#
# Copyright: All rights reserved
# ---------------------------------------------------------------
print("Loading modules...")

from . import predictor


if __name__ == '__main__':
    # Create a predictor instance by hf token indentification
    predictor_ = predictor.Predictor(predictor.Predictor.Login_Token())

    # Upload the report in pdf format
    # This following function will ask you to upload a pdf to
    while(True):
        predictor_.predict_pdf()




