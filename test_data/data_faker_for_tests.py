from faker import Faker


class AccountData:
    # Faker data for account test
    fake = Faker("pl_PL")
    registration_email = fake.email()
    registration_password = fake.password(12)
    login_email = fake.email()
    login_password = fake.password(12)


class BillingData:
    # Faker data for billing test
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    company = fake.company()
    street_address = fake.street_address()
    street_address_optional = fake.street_address()
    post_code = fake.postcode()
    town_city = fake.city()
    email = fake.email()
    state_county = fake.state()
    faker = Faker("Pl-pl")
    phone = faker.phone_number()


