FROM python:3.11
ADD . /
RUN pip install -r requirements.txt
CMD [ "python","-u","main_multi_channel.py" ]