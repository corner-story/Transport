from app import app
from app.model import Driver, Consigner, Good, Application
from app.extensions import db
from faker import Faker
from random import randint
import click



""" 
    生成虚拟数据
"""

@app.cli.command()
def rebuild():
    db.drop_all()
    db.create_all()



@app.cli.command()
@click.option("--users", default=20, help="create drivers")
def forge(users):
    click.echo(f"生成{users}条drivers和consigner数据:")
    f = Faker("zh_CN")

    for _ in range(int(users)):
        driver = Driver(
            username = f.name()
            ,password = "123"
            ,phone_number = f.phone_number()
            ,email = f.email()
            ,car_type = ["大货车", "小货车", "中货车"][randint(0,2)]
            ,account = f.credit_card_number()
        )
        
        consigner = Consigner(
            username = f.name()
            ,password = "123"
            ,phone_number = f.phone_number()
            ,email = f.email()
            ,address = f.address()
        )

        db.session.add(driver)
        db.session.add(consigner)
    
    db.session.commit()

    click.echo("Done...")

    
