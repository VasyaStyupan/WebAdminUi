FROM users/driver/chromedriver
FROM python
WORKDIR ./app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . .
CMD pytest -s -v /app/tests/main_screen/LDEF_T*.py
