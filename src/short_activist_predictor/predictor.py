from . import predictor_init
from . import Filter
from . import sys

import numpy as np
import os
import pdfplumber

#from google.colab import drive, files
from tkinter.filedialog import askopenfilename
from builtins import staticmethod
from pwinput import pwinput

class Predictor:
    A_ = "Status First Day Low"
    B_ = "Status First Day Close"
    C_ = "Status First Week"
    D_ = "Status First Week Close"
    E_ = "Status First Month Max"
    F_ = "Status First Month Closed"
    global Data_, data7

    def __init__(self, token: str):

        # Configuration system
        os.environ["HF_HUB_DISABLE_CACHE"] = "1"

        self.predictor_in: predictor_init.Predictor_init = predictor_init.Predictor_init(token_=token) # generate new predictor module
        self.predictor_in.load_all_models()
        self.predictor_in.load_data()
        self.predictor_in.upload_data()

        Data_ = self.predictor_in.Data_
        data6_save = self.predictor_in.Data_save
        data6_save['Text'] = data6_save['Text'].map(lambda x: x.split(" "))
        data7 = data6_save

    def predict_pdf(self):
        text = Filter.tokenizer_text(self.Upload_pdf())
        self.predict(text)

    # This function try to match two list.
    # Create a list contain elements of data and data_low that have value as success prediction
    # Value is the prediction success state
    '''def analyze(self, Data_check = Data_, data=data7, status="Status First Day Low", value=1):
        Data__low = Data_check[["Activist", "Symbol", status]]
        Data__low["Activist"] = Data__low["Activist"].map(
            lambda x: " ".join([re.sub(r'[&),_(\']', " ", i) for i in x.split(" ")]))  # Process Activist's Name
        Data__low["Activist"] = Data__low["Activist"].map(lambda x: x.lower())
        Data__low = Data__low[Data__low[status] == value]

        # data_low are data for prediction value = 1
        # intersection between activist on campaigns file and all short activist reports
        data4_ = data.copy()
        list_ = []
        for a in list(Data__low["Activist"].values):
            if a in list(data4_["Research firm"].values):  # select activist that are on the two lists
                list_.append(a)

        data4_ = data4_[data4_["Research firm"].isin(list_)]
        Data__low = Data__low[Data__low["Activist"].isin(list_)]

        # Check compatibility of Target or Symbol (Some report from campaigns don't have same target to our dataset of report)
        list_1 = []
        for i, a in enumerate(list(Data__low["Symbol"].values)):
            if a in list(data4_["Target"].values):
                list_1.append(a)

        data4_ = data4_[data4_["Target"].isin(list_1)]
        Data__low = Data__low[Data__low["Symbol"].isin(list_1)]

        final_list = []
        for name, target in zip(list(Data__low["Activist"]), list(Data__low["Symbol"])):
            final_list.append((name, target))

        data4_ = data4_[data4_[['Research firm', 'Target']].apply(tuple, axis=1).isin(final_list)]

        return [data4_, Data__low]'''

    # This function try to match two list.
    # Create a list contain elements of data and data_low that have value as success prediction
    # Value is the prediction success state
    '''def analyze2(self, Data_check=Data_, data=data7, status="Status First Day Low"):
        Data__low = Data_check[["Activist", "Symbol", status]]  # Select only element of campaingns in status's value
        Data__low["Activist"] = Data__low["Activist"].map(
            lambda x: " ".join([re.sub(r'[&),_(\']', " ", i) for i in x.split(" ")]))  # Process Activist's Name
        Data__low["Activist"] = Data__low["Activist"].map(lambda x: x.lower())

        # intersection between activist on compaigns file and all short activist report
        data4_ = data.copy()
        list_ = []
        for a in list(Data__low["Activist"].values):
            if a in list(data4_["Research firm"].values):  # select activist that are on the two lists
                list_.append(a)

        data4_ = data4_[data4_["Research firm"].isin(list_)]
        Data__low = Data__low[Data__low["Activist"].isin(list_)]

        # Check compatibility of Target or Symbol (Some report from compaigns don't have same target to our dataset of report)
        list_1 = []
        for i, a in enumerate(list(Data__low["Symbol"].values)):
            if a in list(data4_["Target"].values):
                list_1.append(a)

        data4_ = data4_[data4_["Target"].isin(list_1)]
        Data__low = Data__low[Data__low["Symbol"].isin(list_1)]
        Create by Da glox k an kw anda

        final_list = []
        for name, target in zip(list(Data__low["Activist"]), list(Data__low["Symbol"])):
            final_list.append((name, target))

        data4_ = data4_[data4_[['Research firm', 'Target']].apply(tuple, axis=1).isin(final_list)]

        return [data4_, Data__low]'''

    # this function return topic probability
    # topic_model refer to the BERTtopic model
    def __get_element_prob(self, topic_model, topic_model_B, text__, status='succeed'):
        proba_, proba_B = 0, 0
        if status == "succeed":
            topics_, prob_ = topic_model.find_topics(text__, top_n=5)
            proba_ = max(prob_)
            # print("A----->", proba_)
            return proba_

        elif status == "failed":
            topics_B_, prob_B_ = topic_model_B.find_topics(text__, top_n=5)  # top_n refer to number of topic to choose for research'
            proba_B = max(prob_B_)
            # print("B----->", proba_B)
            return proba_B

    def predict(self, text):
        print("\n----Start prediction----")

        # first day
        succeed_first_day = self.__get_element_prob(self.predictor_in.topic_model_Data_first_day_predicted_succeed,
                                             self.predictor_in.topic_model_Data_first_day_predicted_failed, text)
        failed_first_day = self.__get_element_prob(self.predictor_in.topic_model_Data_first_day_predicted_succeed,
                                            self.predictor_in.topic_model_Data_first_day_predicted_failed, text, status='failed')
        self.__result(succeed_first_day, failed_first_day, 'the first day')

        # first day closed
        succeed_first_day_closed = self.__get_element_prob(self.predictor_in.topic_model_Data_first_day_predicted_constant_succeed,
                                                    self.predictor_in.topic_model_Data_first_day_predicted_constant_failed, text)
        failed_first_day_closed = self.__get_element_prob(self.predictor_in.topic_model_Data_first_day_predicted_constant_succeed,
                                                   self.predictor_in.topic_model_Data_first_day_predicted_constant_failed, text,
                                                   status='failed')
        self.__result(succeed_first_day_closed, failed_first_day_closed, 'the end of the first day')

        # first week
        succeed_week = self.__get_element_prob(self.predictor_in.topic_model_Data_first_week_predicted_succeed,
                                        self.predictor_in.topic_model_Data_first_week_predicted_failed, text)
        failed_week = self.__get_element_prob(self.predictor_in.topic_model_Data_first_week_predicted_succeed,
                                       self.predictor_in.topic_model_Data_first_week_predicted_failed, text, status='failed')
        self.__result(succeed_week, failed_week, 'the week')

        # first week closed
        succeed_week_closed = self.__get_element_prob(self.predictor_in.topic_model_Data_first_week_predicted_constant_succeed,
                                               self.predictor_in.topic_model_Data_first_week_predicted_constant_failed, text)
        failed_week_closed = self.__get_element_prob(self.predictor_in.topic_model_Data_first_week_predicted_constant_succeed,
                                              self.predictor_in.topic_model_Data_first_week_predicted_constant_failed, text,
                                              status='failed')
        self.__result(succeed_week_closed, failed_week_closed, 'the end of the week')

        # first month
        succeed_month = self.__get_element_prob(self.predictor_in.topic_model_Data_first_month_predicted_succeed,
                                         self.predictor_in.topic_model_Data_first_month_predicted_failed, text)
        failed_month = self.__get_element_prob(self.predictor_in.topic_model_Data_first_month_predicted_succeed,
                                        self.predictor_in.topic_model_Data_first_month_predicted_failed, text, status='failed')
        self.__result(succeed_month, failed_month, 'the month')

        # first month closed
        succeed_month_closed = self.__get_element_prob(self.predictor_in.topic_model_Data_first_month_predicted_constant_succeed,
                                                self.predictor_in.topic_model_Data_first_month_predicted_constant_failed, text)
        failed_month_closed = self.__get_element_prob(self.predictor_in.topic_model_Data_first_month_predicted_constant_succeed,
                                               self.predictor_in.topic_model_Data_first_month_predicted_constant_failed, text,
                                               status='failed')
        self.__result(succeed_month_closed, failed_month_closed, 'the end of the month')

        print("----End----")
    def predict_advanced(self, text):
        # on day of month
        succeed_day_of_month = self.__get_element_prob(self.predictor_in.topic_model_Data_first_day_to_month_predicted_constant_succeed,
                                                self.predictor_in.topic_model_Data_first_day_to_month_predicted_constant_failed, text)
        failed_day_of_month = self.__get_element_prob(self.predictor_in.topic_model_Data_first_day_to_month_predicted_constant_succeed,
                                               self.predictor_in.topic_model_Data_first_day_to_month_predicted_constant_failed, text,
                                               status='failed')
        self.__result(succeed_day_of_month, failed_day_of_month, 'one day of the month')

        # first month
        succeed_day_on_week = self.__get_element_prob(self.predictor_in.topic_model_Data_first_day_to_week_predicted_constant_succeed,
                                               self.predictor_in.topic_model_Data_first_day_to_week_predicted_constant_failed, text)
        failed_day_on_week = self.__get_element_prob(self.predictor_in.topic_model_Data_first_day_to_week_predicted_constant_succeed,
                                              self.predictor_in.topic_model_Data_first_day_to_week_predicted_constant_failed, text,
                                              status='failed')
        self.__result(succeed_day_on_week, failed_day_on_week, 'one day on the week')

        # first month closed
        succeed_3_next_week = self.__get_element_prob(self.predictor_in.topic_model_Data_first_week_to_month_predicted_constant_succeed,
                                               self.predictor_in.topic_model_Data_first_week_to_month_predicted_constant_failed, text)
        failed_3_next_week = self.__get_element_prob(self.predictor_in.topic_model_Data_first_week_to_month_predicted_constant_succeed,
                                              self.predictor_in.topic_model_Data_first_week_to_month_predicted_constant_failed, text,
                                              status='failed')
        self.__result(succeed_3_next_week, failed_3_next_week, 'the 3 next weeks')

    def __result(self, succeed, failed, period='that period'):
        print(f"Probability of success during {period} ----->", succeed)
        print(f"Probability of failure during {period} ----->", failed)
        print("This report indicates a probability of",
              ("success" if succeed >= failed and succeed >= 0.9 else "failure"),
              f"during {period}\n")

    def __upload_file(self):
        try:
            print("\nUpload a report here (PDF): ")
            file_path = askopenfilename(filetypes=[('PDF Files', '*.pdf')])
            if file_path is not None:
                return file_path

        except FileNotFoundError:
            print("Cancel uploading report")
            sys.exit()


    def __pdf_to_text(self, file_path):
        with pdfplumber.open(file_path) as pdf:
            title = file_path.split("/")
            title = title[len(title)-1]
            size = pdf.stream.tell()
            print(f'User uploaded file "{title}" with length {size} bytes')
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
        return text

    # Use the functions
    def Upload_pdf(self):
        pdf_file_path = self.__upload_file()
        text = self.__pdf_to_text(pdf_file_path)
        return text

    ## Here I check if there are failed element in our succeed list
    def __best_performance(self, test_succeed, test_failed):
        succeed, failed = 0, 0
        for elem1, elem2 in zip(test_succeed, test_failed):
            if (elem1 >= elem2):
                succeed += 1
            else:
                failed += 1
        return succeed / len(test_succeed)  # 0 to 1

    def __get_performance(self, test_succeed, test_failed):
        print("performance : ", self.__best_performance(test_succeed, test_failed))
        print("mean succeed:", self.__minimal_stat_(test_succeed))
        print("mean failed:", self.__minimal_stat_(test_failed))

    def __minimal_stat_(element):
        arr = np.array(element)
        mean = np.mean(arr)
        std_dev = np.std(arr)

        return mean, std_dev

    @staticmethod
    def Login_Token():
        _token = pwinput("Enter your hugging face token here : ", "*")
        return _token