FROM python:3.13.1-alpine3.21
LABEL authors="jorchard"

#RUN addgroup --gid 1001 --system app && \
#    adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group app

#RUN addgroup -S app && adduser --no-create-home --shell /bin/false --disabled-password -S app -G app
#USER app

WORKDIR /usr/app/web
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./entrypoint.sh ./
RUN sed -i 's/\r$//g' /usr/app/web/entrypoint.sh
RUN chmod +x /usr/app/web/entrypoint.sh

COPY . .
EXPOSE 8000

#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#ENTRYPOINT ["gunicorn", "customer_data.wsgi:application", "--bind", "0.0.0.0:8000"]
ENTRYPOINT ["/usr/app/web/entrypoint.sh"]
