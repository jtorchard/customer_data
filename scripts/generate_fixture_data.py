import datetime
import json
from itertools import chain

from faker import Faker

faker = Faker('en_GB')

NUM_OF_RECORDS = 1000
FILENAME = 'fake_fixture_data.json'


def generate_customer():
    id_counter = 1
    while True:
        yield {
            "model": "data_entry.customer",
            "pk": id_counter,
            "fields": {
                "surname": faker.last_name(),
                "given_names": faker.name(),
                "pub_date": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%m:%SZ"),
            },
        }
        id_counter += 1


def generate_licence():
    id_counter = 1
    while True:
        surname = faker.last_name()
        yield {
            "model": "data_entry.licence",
            "pk": id_counter,
            "fields": {
                "customer": id_counter,
                "surname": surname,
                "given_names": faker.name(),
                "pub_date": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%m:%SZ"),
                "date_of_birth": faker.date_of_birth().strftime("%Y-%m-%dT%H:%m:%SZ"),
                "valid_from": faker.date_of_birth().strftime("%Y-%m-%dT%H:%m:%SZ"),
                "valid_until": faker.date_of_birth().strftime("%Y-%m-%dT%H:%m:%SZ"),
                "number": f"{surname[:5]}{faker.vin()}",
                "address": faker.address(),
                "image": faker.image_url(),
            }
        }
        id_counter += 1


def generate_bank_account():
    id_counter = 1
    while True:
        yield {
            "model": "data_entry.bankaccount",
            "pk": id_counter,
            "fields": {
                "customer": id_counter,
                "pub_date": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%m:%SZ"),
                "account_number": faker.iban()[:8],
                "notes": " ".join(faker.words()),
            }
        }
        id_counter += 1


def generate_address():
    id_counter = 1
    while True:
        yield {
            "model": "data_entry.address",
            "pk": id_counter,
            "fields": {
                "customer": id_counter,
                "street1": faker.street_address(),
                "street2": faker.street_name(),
                "Town": faker.city(),
                "City": faker.city(),
                "Country": faker.country(),
                "postcode": faker.postcode(),
            }
        }
        id_counter += 1


def main():
    customer_generator = generate_customer()
    bankaccount_generator = generate_bank_account()
    licence_generator = generate_licence()
    with open(FILENAME, 'w') as f:
        json.dump(
            list(chain(
                [next(customer_generator) for _ in range(NUM_OF_RECORDS)],
                [next(bankaccount_generator) for _ in range(NUM_OF_RECORDS)],
                [next(licence_generator) for _ in range(NUM_OF_RECORDS)],
            )), f)


if __name__ == "__main__":
    main()
