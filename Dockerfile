##Version: 1.0
##MANTAINER: Stephanie Andreon Ramos

FROM ubuntu:18.04
RUN cd /; mkdir hough-ellipse
WORKDIR /hough-ellipse/
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y dpkg tar sudo gcc g++ wget cmake debianutils python3 libfftw3-3 build-essential

RUN apt install -y python3-pip
RUN pip3 install virtualenv | echo 2

RUN apt install -y python3-tk


RUN virtualenv -p /usr/bin/python3 venv
RUN source venv/bin/activate
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install opencv-python

COPY teste-hough-ellipse-transform.py /hough-ellipse/
COPY vidro2.tif /hough-ellipse/
