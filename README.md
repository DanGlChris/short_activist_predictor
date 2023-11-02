Short activist predictor
===================
## Note

This Python package provides a machine learning model for predicting the likelihood of success for short activist reports targeting public companies.

### Installation

You can install the package using pip:

```bash
pip install short_activist_predictor
```
### Usage

The package provides a `Predictor` module with function `predict_pdf()` that takes in a path to the PDF file of the short report and the target company name. It loads and analyzes the report text using NLP. The Predictor then outputs probability scores between 0-1 predicting the chance of a successful outcome from the report release over 3 time periods - within 1 days, 1 week, and 1 month.

Here's an example of how to use the `Predictor.predict_pdf()` function:

``` python    
from short_activist_predictor.predictor import Predictor

# Create a predictor instance by hf token indentification
predictor_ = Predictor(Predictor.Login_Token())

# Upload the report in pdf format
# This following function will ask you to upload a pdf to
while(True):
  predictor_.predict_pdf()
```    

To request access, please email danglchis.manage@gmail.com with your name, institution affiliation, and details on your proposed use case. We will evaluate requests and provide access to those with legitimate needs aligned with the intended uses of this model

### Requirements

To use this package, you need to have Python 3.10 or higher installed on your system. You also need to have the following packages installed:

   - Bertopic
   - Transformers
   - Huggingface_hub
   - NLTK

### License

This package is licensed under the GNU General Public License v3.0. See the LICENSE file for more information.

### Contact

If you have any questions or suggestions, feel free to contact Daglox Kankwanda at @danglchris.

