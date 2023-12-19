FROM python
WORKDIR /test_project/
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD python -m pytest -s --alluredir=test_results/ /test_project/tests/